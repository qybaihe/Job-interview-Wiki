# 快手｜商业化｜后端研发｜题库

## 岗位方向
- 后端开发（Java为主）
- 商业化技术 / 广告投放 / 广告引擎
- 信息流广告 / 搜索广告 / 电商广告后端

## 来源
- https://www.nowcoder.com/discuss/486354378278957056
- https://blog.csdn.net/qq_33945246/article/details/140814062
- https://blog.csdn.net/weixin_32146783/article/details/114779356
- https://www.nowcoder.com/discuss/507961220322861056
- https://www.nowcoder.com/discuss/353158997379325952
- https://zhuanlan.zhihu.com/p/106910633

---

## 网络（高频）
- HTTP头常见字段有哪些？各自作用？
- HTTP/1.1、HTTP/2.0、HTTP/3.0的核心区别？
- QUIC协议的特点？为什么基于UDP？0-RTT怎么实现？
- TCP三次握手的过程？为什么不是两次或四次？
- 四次挥手的过程？为什么不是三次？TIME_WAIT的作用？
- TCP和UDP的区别？分别适合什么场景？
- TCP拥塞控制的四个阶段？
- HTTPS握手过程？中间人攻击怎么防？

## MySQL（高频）
- MySQL索引的底层数据结构？B+树为什么比B树适合数据库？
- B+树为什么范围查询快？
- 聚簇索引和非聚簇索引的区别？什么是回表？怎么避免回表？
- MVCC的实现原理？ReadView的生成时机在RC和RR下有什么区别？
- 当前读和快照读的区别？各自加什么锁？
- 事务隔离级别有哪些？可重复读怎么解决幻读？
- MySQL事务ACID分别靠什么机制保证？
- 索引失效的常见场景？EXPLAIN怎么看执行计划？
- 分库分表后分页查询怎么处理？

## Redis（高频）
- Redis过期键的删除策略？惰性删除和定期删除的区别？
- Redis内存淘汰策略有哪些？allkeys-lru和volatile-lru的区别？
- Redis能实现ACID吗？Redis事务和MySQL事务的本质区别？
- Redis哨兵机制的原理？故障转移的过程？
- Redis集群模式下数据怎么分布？哈希槽的设计？
- Redis分布式锁怎么实现？SET NX EX + Lua释放的完整流程？
- Redlock方案的原理？为什么需要多数节点？
- Redisson看门狗机制是什么？自动续期怎么实现？
- 布隆过滤器的原理？误判率怎么计算？适合什么场景？
- 缓存穿透、缓存击穿、缓存雪崩的区别和解决方案？

## Java 基础与并发（高频）
- HashMap JDK7和JDK8的实现差异？为什么JDK7并发扩容会死循环？
- ConcurrentHashMap JDK7分段锁 vs JDK8 CAS+synchronized？
- HashMap什么时候转红黑树？为什么阈值是8？
- CAS原理？ABA问题怎么解决？AtomicStampedReference的设计？
- synchronized锁升级过程？偏向锁→轻量级锁→重量级锁？
- ThreadLocal的实现原理？为什么会内存泄漏？怎么解决？
- Spring IOC容器的初始化过程？Bean的生命周期？
- Spring AOP的实现原理？JDK动态代理和CGLIB的区别？
- Spring事务传播行为？自调用事务失效的原因？
- volatile保证了什么？为什么不能保证原子性？

## JVM（中频）
- G1垃圾收集器的工作原理？Region的划分？Mixed GC的触发条件？
- G1和CMS的区别？各自适合什么场景？
- JVM内存模型？堆、栈、方法区的区别？
- Young GC和Full GC频繁时怎么排查？
- 线上OOM怎么排查？常用工具（jmap/jstack/MAT/Arthas）？

## 分布式与中间件（中频）
- 分布式锁的实现方式对比？Redis vs ZooKeeper vs MySQL？
- 多系统调用时如何保证数据一致性？
- 本地消息表+MQ最终一致性方案的设计？
- Kafka和RocketMQ的区别？各自适合什么场景？
- 负载均衡算法有哪些？一致性哈希的原理和虚拟节点的作用？
- Raft协议的核心？Leader选举和日志复制的过程？

## 广告系统专项（商业化方向）
- 广告投放系统的核心链路？请求→召回→粗排→精排→竞价→计费→曝光？
- GSP和VCG竞价机制的区别？
- 广告预算平滑消耗怎么设计？
- CTR/CVR预估在后端怎么对接？特征服务怎么设计？
- 广告反作弊的常见手段？
- 广告实时计费系统怎么保证准确性和高可用？
- 广告投放对延迟的要求？P99<100ms怎么优化？

## 手撕代码（真实面经原题）
- 打家劫舍（动态规划）
- 子数组之和（前缀和/哈希表）
- 区间合并问题
- 两个线程交替打印奇偶数
- 三个线程交替打印1、2、3
- 手写LRU缓存
- 二分查找及其变体

## Java 基础补充（25春招真题）
- Int和Integer的区别？Integer缓存池范围？自动装箱/拆箱的性能影响？
- ==和equals()的区别？String的equals()实现？
- equals()和hashCode()为什么需要同时重写？违反契约会导致什么问题？
- Int a = 1000, Integer b = 1000; a == b 的结果？Integer与int比较时的拆箱规则？
- Object中wait()和notify()的作用？为什么必须在synchronized块中调用？
- Thread.sleep()和Object.wait()的区别？各自对锁的影响？
- 深拷贝和浅拷贝的区别？Java中实现深拷贝的方式（序列化/递归clone/JSON）？

## 设计模式补充（25春招真题）
- 手写双检锁（DCL）单例模式，为什么要用volatile？
- new对象的三步（分配内存→初始化→引用赋值）和指令重排序的关系？

## SQL 实操（25春招真题）
- GROUP BY聚合查询：查找学生名字和成绩总和
- LIKE模糊匹配 + MAX聚合：查找张姓学生的名字和最高成绩
- SQL执行顺序：FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

## 手撕代码补充（25春招真题）
- 一次遍历翻转链表从m到n的结点（LeetCode 92，头插法）

## 系统设计题
- 设计一个广告投放系统的核心链路
- 设计一个实时竞价（RTB）系统
- 设计一个预算控制系统（预算平滑消耗、超投防控）
