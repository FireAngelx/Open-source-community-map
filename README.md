# 基于多维特征描绘的开源社区图谱

该GitHub仓库的主要目的在于——**创新杯相关学习资料汇总，项目各个部分的上传保存以及备份**，issue里可以存放其待解决的问题

## Repo Intro
- 仓库地址：https://github.com/Zhoues/Open-source-community-map
- 仓库是当前状态是**开源公有的**，之后正式开展项目的搭建之后会**转换成私有仓库**，仅对课程成员开放。
- 本仓库的文件结构如下：
  - `Learning materials`   存放我们当前**可以学习的资料**，里面会有具体的分类，每一个人有相应的板块负责
  - `Difficultis and Goals`    **以md的形式**记录我们当前的**困难点**，可以选择合适的机会咨询他人,以及记录我们**当前计划之后需要完成的目标 **
  - `project`   存放**我们项目的主体**，里面有具体的分类，之后会逐步更新

## About
- 该项目的**issue可以存放待解决的问题**，之后可以**统一记录至Difficultis中**
- 关于关注：如果你想随时获取 repo 的更新提醒，**可以打开 watch 功能**。
- 关于其他问题：如果你有其他问题想单独找我，可以直接微信联系。

## How to Contact us

| 姓名   | 身份 | github昵称 | 邮箱              |
| ------ | ---- | ---------- | ----------------- |
| 周恩申 | 组员 | Zhoues     | 2868470542@qq.com |
| 李思睿 | 组员 |            |                   |
| 闫思桥 | 组员 |            |                   |
| 李毅骁 | 组员 |            |                   |
| 侯博   | 组员 |            |                   |

## 项目介绍

### 项目的创新点

我们的项目重点在于针对开源社区（如Gitee）的某一个具体的开源项目（如华为鸿蒙系统）中参与开发的人员进行**描绘用户画像**，以及对参与其中的人员进行**个性化的推荐**。对于一个具体的开源项目，当某一个开发人员**遇到困难**或者需要对项目的某一个部分**进行改进**而需要提交Issue或者Pull-request解决问题的时候，开源社区进行的**个性化推荐**是按照传统的两种度量角度进行推荐，分别是根据**开源项目贡献度**，以及**关联项目的技术相关度**进行推荐。我们则另外考虑了开发人员以及贡献人员的**社交关联度**，充分利用**开源社区建立的社交关系进行相关的推荐**。其次对于**描绘用户画像**方面，传统的算法往往描绘的画像（或者是标注Tag）是**固定数量**的，不具有灵活性，而对于活跃以及不太活跃的用户其画像（或者是标注Tag）的数量应该不一致，我们希望可以为其**提供恰当数量的标注**，有利于开源社区的管理。

### 项目的难点

首先是**如何获取数据**，传统的获取网页数据的方式有很多种，爬虫是我们最常接触的，但是对于较大的或者是官方的网站（比如Gitee），其反爬机制以及涉及到法律层面的违规使我们不得不去再次思考如何获取数据。**API接口是一个好的选择**，但是如何学习API的使用是我们的一个难点。其次是**数据的可视化**，采用API获取数据完毕之后，我们需要以一种**清晰直观的方式实现我们的算法结果**，我们是利用网页还是小程序，如果采用网页，前端如何实现也是我们需要解决的一个难点。

