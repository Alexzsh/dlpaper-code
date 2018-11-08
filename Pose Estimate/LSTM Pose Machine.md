# LSTM Pose Machine

| English word | meaning                 |
| ------------ | ----------------------- |
| joint        | 关键点                  |
| occlude      | v. 闭塞的；堵塞；咬合的 |
|              |                         |
|              |                         |
|              |                         |
|              |                         |
|              |                         |

- CPM ERROR

  - 检测对称关键点
  - 检测闭塞状关键点或大幅度动作时的关键点
  - 检测物体快速移动物体的关键点

  ![image-20181108154053332](https://ws3.sinaimg.cn/large/006tNbRwly1fx0p4lax5mj31420zenpd.jpg)

- 本文是在CPM的基础上做了一些改进，克服了CPM用于视频pose estimation时计算代价昂贵及帧之间缺乏几何连续性的缺点。阅读论文前需要先理解CPM。

## LPM结构

![image-20181108154845778](https://ws1.sinaimg.cn/large/006tNbRwly1fx0pcq6uyoj31cc0n4tx3.jpg)

