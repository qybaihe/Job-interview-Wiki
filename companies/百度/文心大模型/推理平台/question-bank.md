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

## 推理引擎深度专项（vLLM / TensorRT-LLM / KV Cache，社招高频追问）

> 来源：知乎「大模型面试整理(二)—模型推理相关问题」、GitHub LLMs_interview_notes / llm_interview_note 仓库、CSDN「大模型推理百倍加速之KV cache篇」「LLM推理的Attention计算和KV Cache优化」、80aj.com「大模型面试100问03：推理与部署篇」、百度FastDeploy开源文档

### KV Cache 原理与优化（8题）
- KV Cache 的核心原理是什么？为什么自回归生成中每一步只需要计算新 token 的 Q，而 K/V 可以复用之前的缓存？
- 单个 token 的 KV Cache 占用多少显存？给出计算公式（2 × hidden_dim × num_layers × dtype_bytes），以 13B 模型 FP16 为例算一下。
- KV Cache 的显存占用和哪些因素相关？batch size、序列长度、模型层数、hidden_dim 分别如何影响？
- KV Cache 量化有哪些方案？FP8 / INT8 量化对推理精度的影响如何？vLLM 和 TensorRT-LLM 分别怎么支持 KV Cache 量化？
- 长上下文场景下 KV Cache 显存爆炸怎么办？窗口注意力（Sliding Window Attention）、稀疏注意力、KV Cache 驱逐策略（H2O / StreamingLLM）各自的思路？
- KV Cache 复用在哪些场景有价值？多轮对话前缀复用、System Prompt 复用、P-Tuning 前缀复用分别怎么实现？
- Prefix Caching 的原理？如何判断两个请求可以共享 KV Cache 前缀？vLLM 的 automatic prefix caching 机制？
- MQA（Multi-Query Attention）和 GQA（Grouped-Query Attention）如何减少 KV Cache 的显存占用？Llama 2 用的是哪种？

### PagedAttention 与显存管理（6题）
- PagedAttention 解决了什么问题？传统 KV Cache 预分配方式的显存浪费有多严重（论文指出有效利用率可低至 20%）？
- PagedAttention 的核心设计思想？为什么借鉴操作系统虚拟内存的分页机制？逻辑块和物理块的映射关系？
- PagedAttention 如何处理动态序列长度？新 token 生成时如何按需分配物理块？请求结束后如何回收？
- vLLM 的 Block Manager 是怎么工作的？block size 的选择对性能有什么影响？
- PagedAttention 支持 copy-on-write 吗？在 beam search 场景下如何高效共享 KV Cache 块？
- vAttention 等后续工作对 PagedAttention 做了哪些改进？连续虚拟内存 vs 分页的 trade-off？

### Continuous Batching 与调度（5题）
- Continuous Batching（又叫 in-flight batching）和 Static Batching 的核心区别？为什么 Static Batching 在 LLM 场景下效率低？
- Continuous Batching 如何处理 Early-finished Requests？新请求如何动态插入正在运行的 batch？
- Prefill 阶段和 Decode 阶段的计算特性有什么不同（compute-bound vs memory-bound）？为什么需要分离调度（Disaggregated Prefill）？
- 当显存不足以容纳所有活跃请求的 KV Cache 时，vLLM 的抢占策略是什么？swap 到 CPU 内存 vs 重计算的 trade-off？
- 请求优先级调度怎么做？FCFS / SJF / 优先级队列在推理场景下各自的适用性？

### 推理加速技术综合（7题）
- FlashAttention 的核心优化思路？什么是 IO-aware？tiling 技术如何减少 HBM 访问次数？FlashAttention-2 相比 v1 改进了什么？
- FlashDecoding 和 FlashAttention 的区别？为什么 decode 阶段需要单独优化（batch_size × num_heads 维度并行）？
- Speculative Decoding（投机采样）的原理？draft model 和 target model 如何配合？为什么能保证生成结果和原模型完全一致（rejection sampling）？
- 模型量化方法对比：PTQ（GPTQ / AWQ / SmoothQuant）vs QAT 的区别？INT8 vs INT4 vs FP8 各自适合什么场景？W4A16 vs W8A8 是什么意思？
- 算子融合（Kernel Fusion）在推理优化中的作用？哪些算子通常会被融合（如 QKV projection、LayerNorm + Linear）？
- Tensor Parallelism / Pipeline Parallelism / Sequence Parallelism 在推理场景下分别怎么用？TP 和 PP 对延迟和吞吐的影响？
- MoE（Mixture of Experts）模型的推理有什么特殊挑战？Expert Parallelism 怎么做？All-to-All 通信开销怎么优化？

### 推理框架对比与选型（5题）
- vLLM、TensorRT-LLM、SGLang、LMDeploy 各自的核心特点和适用场景？
- vLLM 的架构？Scheduler + Worker + Block Manager 的协作流程？
- TensorRT-LLM 相比 vLLM 的优势和劣势？为什么 TensorRT-LLM 在 NVIDIA GPU 上通常有更好的单卡性能？
- 百度 FastDeploy 的定位？如何实现模型压缩、推理和服务的协同优化？ERNIE-4.5-300B 在 FastDeploy 上的性能数据？
- 如何评估一个推理框架的性能？TTFT / TPOT / throughput / GPU utilization 分别怎么测？benchmark 工具有哪些？

### 追问链路（社招深度追问）
- 「KV Cache → PagedAttention → Continuous Batching → 调度策略」：从单请求优化到多请求并发优化的完整链路，每一步解决什么问题？
- 「量化 → FlashAttention → Speculative Decoding → 分布式并行」：从模型压缩到计算优化到解码加速到多卡扩展，如何组合使用？
- 「百度昆仑芯 vs NVIDIA GPU」：国产芯片在推理场景的适配挑战？软件栈（编译器/算子库/推理框架）的差异？FastDeploy 如何做跨硬件适配？
- 「从零设计一个大模型推理服务」：请求接入层（限流/鉴权/路由）→ 调度层（Continuous Batching/优先级/抢占）→ 推理引擎层（KV Cache管理/算子优化/多卡并行）→ 输出层（流式返回/token callback），每层的关键设计决策？

## 系统设计题
- 设计一个大模型推理服务平台（请求网关/推理引擎/GPU资源池/监控）
- 设计一个短链接服务
- 设计一个分布式缓存系统
