# 题库｜腾讯 / 云与智慧产业事业群（CSIG） / 基础架构 / 后端开发

## 岗位方向
- 腾讯云后台开发、基础架构研发
- 技术栈偏好：Go（主力）、C++、Java
- 核心考察：Go语言深度、云原生技术栈（K8s/etcd/Docker）、MySQL底层、分布式系统、Linux系统编程

## Go语言基础

1. Goroutine和OS线程的区别？Goroutine的初始栈大小？如何动态增长？
2. GMP调度模型中G、M、P分别是什么？P的数量由什么决定？
3. Go的work stealing机制是什么？什么时候触发hand off？
4. Go的GC机制？三色标记法的流程？写屏障的作用？
5. Go 1.8+的混合写屏障和之前的插入写屏障有什么区别？
6. GOGC环境变量的作用？如何调优GC？
7. Go的channel底层结构？有缓冲和无缓冲channel的区别？
8. 向已关闭的channel发送数据会怎样？从已关闭的channel读取呢？
9. Go的context包的用途？WithCancel、WithTimeout、WithValue的使用场景？
10. Go的defer执行顺序？for循环中的defer有什么问题？
11. Go的select语句可以用于什么？多个case同时就绪时如何选择？
12. Go的interface底层结构（iface和eface）？nil interface和nil pointer的区别？
13. Go struct能不能比较？什么情况下不能比较？
14. Go的map是并发安全的吗？sync.Map的实现原理？
15. Go的slice扩容策略？append操作什么时候会触发扩容？

> 来源：牛客腾讯云社招Golang面经、CSDN腾讯CSIG后台开发面经、知乎2024届秋招Golang面经

## 云原生技术栈（CSIG特色）

### Kubernetes
16. K8s的核心组件有哪些？各自的职责？
17. 一个Pod从创建到运行的完整流程？涉及哪些组件？
18. K8s的Scheduler调度策略？预选（Predicates）和优选（Priorities）的区别？
19. Pod之间如何通信？同Node和跨Node的通信方式？
20. Service的三种类型（ClusterIP/NodePort/LoadBalancer）？kube-proxy的三种模式？
21. Deployment的滚动更新策略？maxSurge和maxUnavailable的含义？
22. K8s的健康检查机制？livenessProbe和readinessProbe的区别？
23. K8s的资源限制（requests和limits）？QoS等级（Guaranteed/Burstable/BestEffort）？
24. K8s的HPA（Horizontal Pod Autoscaler）原理？基于什么指标扩缩容？
25. K8s的ConfigMap和Secret的区别？如何热更新配置？

### etcd
26. etcd是什么？为什么K8s选择etcd作为数据存储？
27. Raft共识算法的三种角色？Leader选举流程？
28. Raft如何处理网络分区（脑裂）？
29. etcd的MVCC实现？revision的概念？
30. etcd的watch机制原理？如何保证事件不丢失？
31. etcd的租约（Lease）机制？用于什么场景？

### Docker/容器
32. Docker容器和虚拟机的区别？各自的优劣？
33. Linux Namespace有哪些类型？各自隔离什么资源？
34. Cgroups的作用？如何限制容器的CPU和内存？
35. Docker的分层存储（UnionFS/OverlayFS）原理？
36. Docker镜像的构建优化？如何减小镜像体积？
37. 容器网络模式有哪些？bridge/host/none/overlay的区别？

> 来源：CSDN腾讯CSIG-腾讯云-后台开发面经（已offer）、牛客腾讯云社招Golang面经、腾讯云开发者社区K8s面试题汇总

## MySQL

38. InnoDB和MyISAM的区别？为什么InnoDB是默认引擎？
39. B+树索引的结构？为什么比B树更适合数据库？
40. 聚簇索引和非聚簇索引的区别？什么是回表？如何避免？
41. 联合索引的最左前缀原则？索引下推（ICP）是什么？
42. 索引失效的常见场景？（函数计算、隐式类型转换、LIKE %开头、OR条件等）
43. MySQL的事务隔离级别？InnoDB默认是哪个？各级别解决什么问题？
44. MVCC的实现原理？ReadView的结构？RC和RR下ReadView的区别？
45. InnoDB的锁类型？行锁、间隙锁、临键锁分别解决什么问题？
46. 死锁的产生条件？MySQL如何检测和处理死锁？
47. MySQL主从复制的原理？binlog的三种格式（statement/row/mixed）？
48. 慢查询如何排查？EXPLAIN的关键字段含义？

> 来源：CSDN腾讯CSIG后台开发面经、知乎csig腾讯云暑期实习面经

## Redis

49. Redis的五种基本数据类型及底层实现？
50. ZSet的底层为什么用跳表而不是红黑树？
51. Redis的持久化方式？RDB和AOF的区别？AOF重写流程？
52. Redis的过期策略？惰性删除和定期删除？内存淘汰策略有哪些？
53. Redis的主从复制流程？全量同步和增量同步？
54. Redis Sentinel和Cluster的区别？各自解决什么问题？
55. Redis如何实现分布式锁？Redlock算法的原理和争议？

> 来源：知乎csig腾讯云暑期实习面经、CSDN腾讯后端面试题汇总

## 分布式系统

56. CAP定理？为什么不能同时满足三者？实际系统如何取舍？
57. 一致性哈希的原理和使用场景？虚拟节点解决什么问题？
58. 分布式事务的解决方案？2PC、3PC、TCC、Saga各自的优缺点？
59. 消息队列如何保证消息不丢失？（生产者确认、Broker持久化、消费者手动ACK）
60. 消息队列如何保证消息不重复消费？（幂等性设计）
61. 微服务中的服务发现机制？客户端发现和服务端发现的区别？
62. 熔断、限流、降级的区别？Sentinel/Hystrix的实现原理？

> 来源：牛客腾讯云社招Golang面经、CSDN腾讯后台面经大全

## 计算机网络

63. TCP三次握手和四次挥手的流程？为什么握手三次挥手四次？
64. TCP的拥塞控制算法？慢启动、拥塞避免、快重传、快恢复？
65. HTTP/1.1、HTTP/2、HTTP/3的主要区别？
66. HTTPS的握手流程？证书验证过程？
67. TCP和UDP的区别？什么场景用UDP？
68. select、poll、epoll的区别？epoll的LT和ET模式？

> 来源：CSDN腾讯CSIG后台开发面经、牛客腾讯后台面经大全

## Linux系统

69. 进程和线程的区别？Linux下如何创建进程和线程？
70. 进程间通信方式有哪些？各自的优缺点？
71. Linux的文件系统？inode的概念？软链接和硬链接的区别？
72. Linux常用排查命令？（top/htop/vmstat/iostat/netstat/ss/tcpdump/strace/perf）
73. 如何排查CPU使用率过高？如何排查内存泄漏？

> 来源：牛客腾讯云社招Golang面经、CSDN腾讯后端面试题

## 算法手撕题

74. LRU Cache实现（哈希表+双向链表）
75. 二叉搜索树中第K小的元素
76. 链表倒数第N个节点
77. Top K问题（堆/快速选择）
78. 岛屿数量（BFS/DFS）
79. 合并K个有序链表
80. 最长回文子串

> 来源：CSDN腾讯CSIG后台开发面经、牛客腾讯后台面经

## 系统设计题

1. 设计一个分布式配置中心（类似etcd/Apollo）
2. 设计一个容器编排调度系统的核心模块
3. 设计一个高可用的API网关
4. 设计一个分布式日志收集系统

## 反问方向

- CSIG基础架构团队当前的技术重点？云原生方向的规划？
- 团队的技术栈以Go为主吗？有没有Rust等新语言的尝试？
- 新人入职后的培养路径？

## 备注
- 来源：CSDN腾讯CSIG-腾讯云-后台开发面经（已offer）、知乎csig腾讯云暑期实习面经、CSDN腾讯CSIG暑期后端实习面经（已offer）、牛客腾讯云社招Golang面经、腾讯云开发者社区K8s面试题汇总
- CSIG后端面试特点：Go语言是核心（即使简历写Java也会问Go）、云原生技术栈是区分度最高的考点、项目深挖占比大
- 面试风格：喜欢DFS深挖底层原理，一个知识点会追问到候选人答不上来为止
