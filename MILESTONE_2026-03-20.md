# Milestone · 2026-03-20

## 这次阶段性整合做了什么

这不是单点更新，而是一轮围绕 `Job-interview-Wiki` 自动推进能力、仓库治理能力、模板规范和正式内容沉淀的集中升级。

---

## 一、自动推进能力升级

### 1. 修复 cron 空转问题
之前的问题：
- cron 虽然在跑，但经常只检查目录结构或读文件后结束
- 有时只改 `progress_state.json` 就返回成功
- 结果看起来“完成了”，实际上没有真实内容产出，也没有 commit / push

本轮已完成：
- 收紧 cron 规则
- 强制要求每轮必须有真实产出，或明确失败
- 禁止“只读目录 / 只改状态文件 / 假完成”

### 2. 建立并行 orchestrator 模式
将原先偏单线程推进，升级为：
- 1 个 orchestrator
- 多个 worker 并行搜索 / 整理候选
- orchestrator 统一收口、审阅、合并、commit、push

好处：
- 能并行探索多个板块
- 避免多个子线程直接写同一仓库导致 git 冲突
- 让搜索与正式落库解耦

### 3. 明确 worker 状态汇报
新增要求：
每轮必须汇报每个 worker 的状态，状态固定为：
- success
- partial
- timeout
- no-source
- blocked
- skipped

这使得后续可以更清楚地判断：
- 哪个板块长期有产出
- 哪个板块总是找不到可信来源
- 哪个板块是性能瓶颈

---

## 二、长期任务池与固定板块分工建立

### 4. 建立长期 backlog
新增 / 强化：
- `TODO_DEEPENING_BACKLOG.md`

作用：
- 把仓库后续工作拆为从零建设、薄覆盖补厚、强方向深挖、资产治理、长期扩展池
- 保证 cron 不会在吃完第一批方向后立刻枯竭

### 5. 建立 8 个固定 worker boards
新增：
- `TODO_WORKER_BOARDS.md`

作用：
- 把 8 个 worker 固定为 8 个板块负责人，而不是每轮临时抢任务
- 板块包括：
  - 字节
  - 阿里 / 蚂蚁
  - 腾讯
  - 美团 / 京东
  - 百度 / 华为
  - 拼多多 / 快手 / 小红书
  - 扩展公司
  - 资产治理

意义：
- 降低重复搜索
- 提升汇报可解释性
- 方便后续做板块级效果评估

---

## 三、模板与仓库规范升级

### 6. 修复 README 并补强仓库介绍
README 从“统计错误 + 尾部损坏/乱码风险”修到：
- 首页说明完整可读
- 当前覆盖范围更清楚
- 统计口径更明确
- 仓库目标、结构、内容类型、阶段状态都有清晰描述

### 7. 升级结构化面经 JSON 模板
新增 / 修订：
- `docs/json-schema.example.json`
- `INTERVIEW_TEMPLATE_GUIDE.md`

统一了：
- source.type 的分类
- verification_status 的口径
- round 字段
- 真实单帖 / 聚合整理 / 样板占位的边界

这一步很关键，因为它直接决定后续自动产出的质量上限。

---

## 四、正式内容沉淀

### 8. 已沉淀进正式仓库的内容
在这轮自动推进与治理过程中，已经正式落库并推送了多类内容，包括但不限于：

#### 真实面经 JSON
- 字节跳动 / 飞书 / 后端平台
- 拼多多 / Temu / 服务端
- 百度 / 文心大模型 / 推理平台
- 以及后续多轮 parallel batch add verified content 所带来的新增内容

#### 正式题库补强
- 华为 / 云计算BU / 后端研发
- 蚂蚁集团 / 支付宝 / 后端开发
- 哔哩哔哩 / 推荐算法
- 滴滴 / 出行平台 / 后端开发
- 网易 / 云音乐 / 后端开发
- 小米 / AIoT平台 / 后端研发（新增正式题库）

#### 资产治理
- README 统计修正
- 模板规范文档
- worker boards 与长期 backlog

---

## 五、浏览器搜索能力打通

### 9. 验证 OpenClaw 浏览器能力可用
已确认：
- OpenClaw browser 能启动
- 可检测到本机 Google Chrome
- 可打开百度页面
- 可等待页面加载
- 可查看 tabs
- 可抓取 snapshot 页面内容

这意味着：
- 当 `web_search` / `web_fetch` 限额受限时
- 后续可以考虑让 worker 退化到“浏览器直接搜索”策略

这一步目前属于**能力验证完成**，尚未完全接入到 cron 的正式自动化流程。

---

## 六、当前项目状态判断

截至这次整合，`Job-interview-Wiki` 已经从“能自动跑一点内容”的状态，升级到：

### 已具备
- 自动推进
- 并行探索
- 模板规范
- 板块分工
- 候选到正式内容的沉淀机制
- 基础浏览器搜索能力

### 仍待继续
- 把浏览器搜索正式接入 worker fallback 逻辑
- 清理样板文件与 `sample.json` 口径
- 修复 / 重建 `controller/progress_state.json` 的可信状态基线
- 提升 README / 统计与真实文件树的一致性自动化程度
- 对 partial JSON 候选做更严格的人工升级筛选

---

## 七、为什么这次整合值得单独记一次提交

因为这次不是普通的“补几份题库 / 修几行 README”，而是：

1. **修了自动推进机制本身**
2. **建了可持续 backlog 和固定 worker 分工**
3. **统一了 JSON 模板与证据强度口径**
4. **沉淀了一批正式内容**
5. **打通了浏览器搜索能力验证**

这几件事加起来，实质上把仓库从“内容驱动”推进到了“机制 + 内容双轮驱动”。

---

## 建议的提交信息

如果要为这次整合单独打一条有价值的提交，建议信息写成：

```bash
docs(jobwiki): add milestone summary for automation, templates, and content pipeline
```

如果更偏项目治理，也可以用：

```bash
chore(jobwiki): record 2026-03-20 milestone across automation, worker boards, and templates
```
