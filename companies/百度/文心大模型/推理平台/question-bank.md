# 百度｜文心大模型｜推理平台｜题库

## 岗位方向
- 后端开发（Java/Go/C++）
- 推理平台 / 模型服务化 / 推理引擎
- 大模型部署 / GPU资源调度 / 高性能计算

## 来源
- https://www.nowcoder.com/discuss/392829046223241216
- https://blog.csdn.net/weixin_44427286/article/details/119358356
- https://www.nowcoder.com/enterprise/139/interview
- https://www.glassdoor.com/Interview/Baidu-Software-Engineer-Interview-Questions-EI_IE35325.0,5_KO6,23.htm
- https://www.nowcoder.com/creation/subject/feba655c853c4295b44fe0e647827d9c

---

## 操作系统（高频）
- 进程和线程的区别？协程和线程的区别？
- 进程间通信方式有哪些？各自适合什么场景？
- 进程的状态有哪些？线程的状态有哪些？
- 虚拟内存的原理？页表和TLB的作用？
- 内存分页和分段机制？各自的优缺点？
- 死锁的四个必要条件？如何预防和解决死锁？
- Linux常用命令？怎么查看进程占用的CPU和内存？
- select/poll/epoll的区别？epoll为什么高效？

## 网络（高频）
- TCP三次握手的过程？中间涉及哪些协议？
- TCP四次挥手？TIME_WAIT的作用和持续时间？
- TCP和UDP的区别？各自适合什么场景？
- HTTP/1.1和HTTP/2.0的区别？多路复用怎么实现？
- HTTPS的握手过程？证书验证的流程？
- DNS解析的完整过程？递归查询和迭代查询的区别？

## MySQL（高频）
- MySQL索引的底层数据结构？B+树 vs B树 vs 跳表？
- 聚簇索引和非聚簇索引的区别？什么是回表？覆盖索引？
- MVCC的实现原理？undo log版本链和ReadView？
- 事务隔离级别？可重复读怎么解决幻读？
- MySQL事务ACID分别靠什么机制保证？
- 慢查询怎么排查？EXPLAIN各字段的含义？
- 分库分表的方案？水平拆分和垂直拆分的区别？
- MySQL主从复制的原理？binlog的三种格式？

## Redis（高频）
- Redis有哪些数据结构？各自的底层实现和适用场景？
- 给你一个key怎么知道用的哪种数据结构？OBJECT ENCODING命令？
- Redis缓存和MySQL的一致性怎么保证？Cache Aside Pattern？
- 二次缓存（本地缓存+Redis）怎么设计？
- Redis持久化方式？RDB和AOF的区别？混合持久化？
- Redis集群模式？哈希槽的分配？节点扩缩容怎么做？
- Redis大key问题怎么排查和治理？

## Java 基础与并发（高频）
- HashMap底层实现？put的完整流程？扩容机制？
- ConcurrentHashMap的实现？JDK7 vs JDK8？
- Java GC机制？GC Roots有哪些？可达性分析？
- G1和CMS的区别？各自适合什么场景？
- 线程池核心参数？拒绝策略？线程池大小怎么设置？
- synchronized和ReentrantLock的区别？
- volatile的作用？happens-before规则？
- Java内存模型（JMM）？主内存和工作内存？

## 分布式与中间件（中频）
- 消息队列的使用场景？如何保证消息不丢失？如何保证顺序性？
- 微服务架构下服务发现怎么做？注册中心挂了怎么办？
- 分布式事务的解决方案？2PC/3PC/TCC/Saga/本地消息表？
- 负载均衡算法有哪些？一致性哈希的原理？
- 限流算法？令牌桶和漏桶的区别？

## 云原生与容器化（推理平台方向高频）
- Docker和虚拟机的区别？Docker的核心技术（namespace/cgroup/unionfs）？
- K8s核心概念？Pod/Deployment/Service/Ingress？
- K8s的调度策略？GPU资源怎么调度（nvidia-device-plugin）？
- HPA弹性伸缩的原理？自定义指标伸缩怎么做？
- 容器镜像的分层机制？怎么优化镜像大小？

## 大模型推理专项（推理平台方向）
- 大模型推理的核心性能指标？TTFT/TPOT/吞吐量/GPU利用率？
- KV Cache的原理？为什么能加速自回归生成？
- Continuous Batching vs Static Batching的区别？
- PagedAttention（vLLM）的设计思想？解决了什么问题？
- 模型量化的方法？INT8/INT4/GPTQ/AWQ的区别？
- Tensor Parallelism和Pipeline Parallelism的区别？
- 投机采样（Speculative Decoding）的原理？
- FlashAttention的优化思路？IO-aware的含义？
- 模型服务化的架构设计？请求网关→队列→推理引擎→结果返回？
- 多模型管理和版本切换怎么做？灰度发布？
- 百度FastDeploy推理部署套件了解吗？
- 百度昆仑芯片和NVIDIA GPU在推理场景的对比？

## 手撕代码（真实面经原题）
- 二叉树最大深度（递归+非递归）
- LRU缓存实现（HashMap+双向链表）
- 买卖股票的最佳时机
- 环形链表判断
- 手写快排
- 子集（回溯法）
- 短链接系统设计（哈希+base62编码）

## 大模型工程实操（实习面真题）
- 优化Prompt的经验？Few-shot示例选择、CoT引导、指令格式优化、温度/top-p调参？
- Prompt在生产环境中的工程化管理？版本控制、A/B测试、效果评估？
- 大模型微调SFT的优化方法？数据质量/LoRA/QLoRA/学习率调度/混合精度？
- SFT vs RLHF的优劣对比？DPO等替代方案？
- 参数高效微调（PEFT）方法对比？LoRA/QLoRA/Adapter/Prefix-Tuning？

## 分布式协议深度（实习面真题）
- Raft协议的三大核心？Leader选举/日志复制/安全性保证？
- Raft网络分区时任期号膨胀问题？Pre-Vote机制的原理？
- Check Quorum机制？Leader如何检测自己是否仍被多数节点认可？
- Raft vs Paxos的区别？为什么Raft更易工程实现？

## 计算机网络补充（实习面真题）
- 计算机网络五层模型？各层的核心协议和设备？
- TCP/IP分别属于哪一层？TCP/IP协议族的含义？
- ARP协议的工作层次？ARP欺骗的原理和防范？

## 系统设计题
- 设计一个大模型推理服务平台（请求网关/推理引擎/GPU资源池/监控）
- 设计一个短链接服务
- 设计一个分布式缓存系统
