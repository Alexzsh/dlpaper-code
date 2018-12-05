# Convolution Pose Machines

| English words | 翻译 |
| ------------- | ---- |
| belief map    |      |



CPMs 由全卷积网络序列化组成，并重复输出每个关节点的 2D 置信图. 每一个stage，采用图像特征和上一 stage 输出的2D置信图作为输入.

置信图为后面的阶段提供了每个关节点位置的空间不确定性(spatial uncertainty)的非参数编码，使得 CPM 可以学习到丰富的与图像相关的关节点间关系的空间模型.

以 CPM 的某个特定 stage 为例： 关节点置信图的空间信息，为后续 stage 提供了很无歧义的线索信息. 因此，CPM 的每个 stage 都可以输出越来越精细的关节点置信图，如 Figure 1.

![image-20181108161400708](https://ws4.sinaimg.cn/large/006tNbRwly1fx0q302ujcj30al066ack.jpg)

为了捕捉关节点间 long-range 的相互关系，CPMs 中每个 stage 的网络设计的启发点是：**同时在图像和置信图上得到大的接受野(large receptive field)**.



## Pose machines

$T_p \in Z$ 表示关节点$p$的像素位置，$Z$是图片内所有的关节点位置$(u,v)$集合

人体姿态估计的目标就是预测图片中P个人体关节点的位置$Y=(Y_1,...Y_P)$

Pose Machine 由 多类别分类器序列化组成，如下图所示，$g_t(\cdot)$分类器预测每一层中各关节点的位置

![image-20181108185056233](https://ws1.sinaimg.cn/large/006tNbRwly1fx0um9zhxrj314y06cq9t.jpg) 



在每个stage $t \in \{1,...,T\} $ 中，分类器$g_t$ 基于$z$区域抽取的图像特征$X_z$以及邻近的分类器的输出预测每个关节点的`belief map`（将作为后续stage的输入）。当stage=1时置信图根据以下公式计算:
$$
g_1(X_z)\rightarrow\{b_1^p(Y_p=z)_{p\in\{0...P\}}
$$
其中，$b_1^p(Y_p=z)$是由$g_1$ 分类器对区域$z$在第一阶段中的第$p^{th}$ 关节点的预测得分。也就是说，对于大小为$w,h$ 的图片来说，我们在每个区域$z=(u,v)^T$计算p 关节点的置信图，也可以表示为如下公式：
$$
b_t^p[u,v]=b_t^p(Y_p=z)
$$
方便起见，我们使用置信图的集合来表示左右关节点$b_t\in \R^{w*h*(P+1)}$ `P+1为P个关节点+1个背景` 

​	在之后的阶段中，分类器考虑$(1)$式内容以及上下文环境中的分类器的输出，公式如下：
$$
g_t(X_z',\psi_t(z,b_{t-1}))\rightarrow\{b_t^p(Y_p=z)\}_{p\in\{0...P+1\}}
$$
其中，$\psi_{t>1}(\cdot)$ 一个将置信图$b_{t-1}$  映射到上下文特征的函数。`文章中并没有详细展开这个函数` 



**算法主要流程**

- 在每一个阶段计算每个关节点的置信图
- 对于每个关节点计算时需要累加所有阶段的置信图得到总置信图
- 根据每个关节点的总置信图找到最大的点即该关节点的位置

以半身模型为例，有九个关节点，分成四个阶段，网络结构图如下：

![image-20181108195552389](https://ws4.sinaimg.cn/large/006tNbRwly1fx0whu0yy1j311u102anr.jpg)

其中

- ori image为原始input彩色图像
- center image为提前构建的高斯函数模板，用于将置信图归拢到图像中心
- score* 即为每个部分的置信图
- img $(w,h)=(368,368)$

**第一个阶段**：通过一个基本的卷积直接预测每个关节点的值，根据上文介绍，共得到10个关节点的值，其中有一个为背景

**第二个阶段**：将原始图像做卷积后得到的纹理特征与前一阶段得到的个关节点的空间特征以及中心归拢后的结果串联起来作为输入，通过卷积得到该阶段的值

**第三个阶段**:  输入不再是原图，而是第二个阶段中间特征图，同样也是卷积后和前一阶段的结果以及中心归拢后的结果串联起来作为输入，通过卷积得到该阶段的值

**第四个阶段(后续阶段)**：和第三阶段完全一样。在设计复杂网络例如对于全身模型时，只需要调整关节点数量，并重复第三阶段即可

## Experience

| 数据集                                                | 类别       | 关节点数 | 训练/测试样本数 |
| ----------------------------------------------------- | ---------- | -------- | --------------- |
| [FLIC](http://bensapp.github.io/flic-dataset.html)    | 半身，影视 | 9        | 3987/1016       |
| [LSP](http://www.comp.leeds.ac.uk/mat4saj/lspet.html) | 全身，体育 | 14       | 11000/1000      |
| [MPII](http://human-pose.mpi-inf.mpg.de/)             | 全身，日常 | 14       | 28000/          |

在这三个数据及上，PCK(Percentage Keypoints Metric)指标均超过已有文献。下图示出一例。

![image-20181108201918398](https://ws2.sinaimg.cn/large/006tNbRwly1fx0x6861e8j31980go7pb.jpg)

## ERROR AND TRICK

#### 梯度消失

这是较深的网络都会遇到的问题，文章中通过采用中层监督的方式来加强反向传播，中层监督的groundtruth来源于对groundtruth中的location point做高斯分布产生。而Loss的形式是简单的每个像素的平方loss。

![image-20181108202021809](https://ws2.sinaimg.cn/large/006tNbRwly1fx0x7bseiuj316g0mw1kx.jpg)

- 黑色表示有中层监督的梯度分布，黑色在每层基本分布都较为均匀，能够正常更新
- 红色表示无中层监督的梯度分布，可以看到红色在后几层分布比较均匀而到前几层就完全没有办法传递到

#### 数据增强

基本的随机旋转、缩放、镜像等，值得一提的是本文也使用了不同尺度的图像，1、4、8、12等尺度图像作为进一步的扩充


