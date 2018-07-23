
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

## <p align="center">Attention is all you need

### <p align="center"> 摘要

目前序列转换模型都是完全基于R/CNN且都包含一个编码和一个解码部分。表现最好的模型也是通过attention机制将编码解码相连。我们提出一个新的简易网络结构Transformer，只基于attention机制完全摒弃了R/CNN结构。该模型在两个机器翻译任务上都表现出了高可平行性运算，明显缩短训练时长。模型在 2014 WMT 英德翻译任务中达到了28.4 BLEU分数，超过现有的最佳模型包括集成模型 2 BLEU。在 2014 WMT英法翻译任务中，我们的模型在单个模型中达到 state-of-the-art 分值 41.8 BLEU，训练使用8个GPU，时长3.5天。该模型具有良好的泛化能力，能够成功的应用在庞大以及受限的训练数据中。

### 1 介绍
尤其是LSTM、GRU等RNN网络已经确定在语言模型和机器翻译等序列模型和转换任务中达到state-of-the-art的表现。目前，许多努力仍在推动循环语言模型与编码-解码的架构的界限。  
循环模型通常是根据输入输出序列的符号位置进行因子计算的。该模型根据前一个隐形状态$h_1$以及输入的位置$t$作为当前隐性状态$h$计算的输入以此在计算时对其位置与步骤。该固有序列特性阻碍了并行训练，这对于长序列输入非常重要，因为内存大小限制了批处理数据。目前研究已经通过分解技巧和条件计算在计算效率方面有了重要提升，且后者还提高了模型性能。但是，顺序计算的基本约束依然存在。  
在许多任务中，attention机制已经成为序列模型和转换模型中不可或缺的部分，它可以建模依赖关系而不考虑输入输出序列中的距离。大多数情况，attention机制都和循环网络一起使用。  
在Transformer中，模型架构避免避免循环结构且完全依赖于attention机制来构建输入输出的全局依赖关系。Transformer允许更多的并行化并且经过8片P100 GPU 至少训练12小时可以在翻译任务上达到新的state-of-the-art

### 2 背景

减少顺序计算的目标也是形成可扩展神经GPU、ByteNet和ConvS2S的基础，这些模型都使用了卷积神经网络作为基础模块为所有的输入输出位置并行计算隐性特征。在这些模型中，关联任意两个输入输出位置的信号所需的操作次数会随着位置之间的距离而增加，ConvS2S是线性增加，ByteNet是对数增加的。这使得学习远距离位置的依赖变得更加困难。在Transformer中，这种操作数会减少到一个固定常数次，尽管平均化attention权重位置会降低效果但是使用Multi-Head attention会将其抵消。  
Self-attention(有时也称之为 intra-attention)是关联单个序列的不同位置以计算出序列的特征的attention机制，已经在包括阅读理解、摘要总结、文本蕴含和学习任务无关的句子表征任务中成功使用。  
端到端的记忆网络是基于循环attention机制而非序列对齐循环网络，其已经在简单的语言问答模型和语言建模任务中表现良好。  
据我们所知，Transformer是第一个仅依赖于self-attention机制来计算输入输出的表征而非使用序列对齐的循环神经网络或者卷积神经网络。在一下章节中，将描述Transformer、self-attention并讨论其优点。  

### 3 模型结构

![Transformer](images/Transformer.png)

> 大多数序列转换模型都有编码-解码结构.
编码器映射一个用符号表示的输入序列
$(x_1,{\ldots},x_n)$ 到一个连续的表示$z= (z_1,{\ldots},z_n)$。 根据z，解码器生成符号的一个输出序列$(y_1,...,y_m)$ ，一次一个元素。 在每一步中，模型都是自回归的，当生成下一个时，消耗先前生成的符号作为额外输入。
Transformer遵循这种整体架构，编码器和解码器都使用`self-attention堆叠`和`point-wise`、全连接的层,分别显示在上图左右。

#### 3.1 编码与解码堆叠 

> - 编码器： 编码器由N = 6 个完全相同的层堆叠而成。每一层都有两个子层。 第一层是一个`multi-head self-attention`机制，第二层是一个简单的全连接的前馈网络。 我们对每个子层再采用一个残差连接 ，后接层归一化。  
也就是说，每个子层的输出是`LayerNorm(x + Sublayer(x))`，其中`Sublayer(x)` 是由子层本身实现的函数。 为了方便这些残差连接，模型中的所有子层以及词0嵌入层的维度都为$d_{model} = 512$。
- 解码器： 解码器同样由N = 6 个完全相同的层堆叠而成。 除了每个编码器层中的两个子层之外，解码器还插入第三个子层，对编码栈的输出执行`multi-head attention`。  
与编码器类似，我们在每个子层再采用残差连接，然后进行层归一化。 我们还修改解码器中的`self-attention`子层，以防止影响到后面的位置。 这种`mask multi-head self-attention`将输出的词嵌入偏移一个位置，确保对位置的预测$i$只能依赖小于$i$ 的已知输出。

#### 3.2 Attention
> Attention函数可以描述为将`query`和一组`key-value`对映射到输出，其中`query`、`key`、`value`和输出都是向量。 输出为`value`的加权和，其中分配给每个`value`的权重通过`query`与相应`key`的兼容函数来计算。

##### 3.2.1 缩放版的点积attention

+ 我们将我们特殊的attention称为`缩放点积attention`。 输入由`query`、$d_k$ 维的`key`和$d_v$ 维的`value`组成。 我们计算`query`和所有`key`的点积并除以 $\sqrt{d_{k}}$，然后应用`softmax`函数以获得值的权重。
+ 在实践中，我们同时计算一组`query`的attention函数，并将它们组合成一个矩阵Q。 `key`和`value`也一起打包成矩阵 K 和 V 。 我们计算输出矩阵为$$Attention(Q,K,V) = softmax(\frac {{QK}^T} {\sqrt{d_k}})V$$
+ 两个最常用的attention函数是加法attention和点积attention。除了缩放因子 $\frac{1}{\sqrt{d_{k}}}$ 之外，点积attention与我们的算法相同。 加法attention使用具有单个隐藏层的前馈网络计算兼容性函数。 虽然两者在理论上的复杂性相似，但在实践中点积attention使用高度优化的矩阵乘法代码，其速度更快、更节省空间
+ 当$d_k$的值比较小的时候，这两个机制的性能相差相近，当$d_k$比较大时，加法attention比不带缩放的点积attention性能好。 我们怀疑，对于很大的dk值，点积大幅度增长，将softmax函数推向具有极小梯度的区域4。 为了抵消这种影响，我们缩小点积 $\frac{1}{\sqrt{d_{k}}} $倍。

##### 3.2.2 Multi-Head Attention

+ 我们发现，在执行`Attention`函数时，将`query`,`key`,`value`通过学习到的线性变换h次得到的$d_k$,$d_k$,$d_v$维将比$d_{model}$维效果更好。且针对每种变换并行执行Attention函数得到$d_v$维的输出值，在将其连接并再次变换产生最终结果。
+ `multi-head attention`允许模型考虑不同位置的不同特征子空间的信息，如果只有一个Attention head ，做平均化时会削弱结果。
\begin{align}
MultiHead(Q,K,V) =& Concat(head_1,{\ldots},head_h)W^O \\ where head_i =& Attention(QW^Q_i,KW_i^K,VW^V_i)
\end{align}
其中,$W^Q_i\in R^{d_{model}*d_k}$,$W^K_i\in R^{d_{model}*d_k}$,$W^V_i\in R^{d_{model}*d_v}$,$W^O\in R^{hd_v*d_{model}}$  
本文中我们并行计算八层Attention。每一层使用的参数$d_k=d_v=d_{model}/h=64$。由于每层大小减小，总计算成本与具体全部纬度的单层Attention相似

##### 3.2.3 Attention在模型中的应用
> Transformer通过三种方式使用`multi-head attention`

> + 在编码解码层中，`queries`来自于前一层的解码层，且`keys` 和`values`来自于前一层编码层的输出。这模仿在Seq2Seq模型中典型的编码-解码Attention机制
+ 编码器包含`self-attention`层。该层中`keys，values,queries`都来自于同一个地方，在这里是前一层编码器。编码器的每一个位置都能关注上一层编码器的所有位置。
+ 同样的，解码器的`self-attention`层的每一个位置都能关注上一层解码器的所有位置。我们需要阻止解码器中左向信息流来保持自回归性。我们通过屏蔽softmax输入中所有不合法的值(设置为-$\infty$)来实现缩放点积Attention。

#### 3.3 