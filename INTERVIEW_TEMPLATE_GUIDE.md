# INTERVIEW_TEMPLATE_GUIDE.md

## 目标

统一 `Job-interview-Wiki` 中结构化面经 JSON 的模板口径，避免：
- sample.json 过于简陋，无法指导高质量产出
- 不同 worker 写出的候选 JSON 字段漂移
- “真实原帖 / 聚合整理 / 样板占位”混在一起说不清

---

## 推荐字段

```json
{
  "company": "公司名",
  "business_group": "业务线/事业群",
  "department": "部门/岗位方向",
  "role": "具体岗位名",
  "source": {
    "type": "public-interview-post | public-aggregated | manual-curated-with-public-tech-basis",
    "url": "主来源",
    "urls": ["可选，多来源列表"],
    "note": "来源说明",
    "verification_status": "verified-single-post | mixed-public-aggregated | public-tech-basis-enriched-not-single-interview-post"
  },
  "interview_rounds": 3,
  "questions": [
    {
      "round": "一面",
      "question": "题目原文或尽量贴近原文的表达",
      "insight": "候选人的复盘/这题的考察点"
    }
  ],
  "final_insight": "整场面试的总结"
}
```

---

## 字段解释

### `company`
正式中文公司名，例如：
- 字节跳动
- 腾讯
- 阿里巴巴
- 美团

### `business_group`
第二层目录口径，对应业务线 / 事业群 / 大业务板块。

### `department`
第三层目录口径，对应部门、技术方向或岗位归属团队。

### `role`
尽量写具体岗位名，而不是笼统写“技术岗”。
例如：
- 后台开发工程师
- 服务端开发
- 推荐算法工程师
- 客户端开发工程师

### `source.type`
建议只用以下三类：
- `public-interview-post`：真实公开单篇面经原帖
- `public-aggregated`：多个公开来源保守聚合
- `manual-curated-with-public-tech-basis`：样板/技术基底整理，不冒充真实单帖

### `source.verification_status`
用于明确证据强度：
- `verified-single-post`
- `mixed-public-aggregated`
- `public-tech-basis-enriched-not-single-interview-post`

### `questions[].round`
建议显式写轮次：
- 一面
- 二面
- 三面
- HR面
- 主管面

如果原始来源没有清晰轮次，也可以写：
- 未明确轮次

---

## 什么时候能写成“真实面经 JSON”

必须至少满足以下之一：
1. 能定位到公开单篇面经原帖
2. 能从公开来源中清楚辨认出同一场面试的轮次和题目顺序

如果做不到，就不要强行伪装成“已逐字核实原帖”，而应：
- 标成 `public-aggregated`
- 或先做 question-bank 候选

---

## 什么时候只应该做题库候选

以下情况更适合补题库，不适合直接写正式 JSON：
- 只有搜索摘要，没有原文细节
- 只有零散评论区题目
- 岗位/业务线无法确认
- 同一方向只有题目集合，没有单场面试上下文

---

## 样板文件的定位

样板文件只用于：
- 建目录
- 演示结构
- 辅助后续真实内容替换

样板文件不应：
- 计入真实面经产能
- 在 README 里和正式 JSON 混淆
- 被写成像“已经核实的真实原帖”

---

## 推荐做法

1. 先找真实公开原帖
2. 再写结构化 JSON
3. 再从 JSON 抽 question-bank
4. 没有原帖时，优先做保守聚合候选，不要硬装真实单帖

---

## 结论

今后仓库中的 JSON 模板，以 `docs/json-schema.example.json` 为最小结构参考；
字段口径、证据强度、样板使用边界，以本文件为准。
