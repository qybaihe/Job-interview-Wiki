# Job Interview Wiki

一个面向中文求职场景的结构化面试资料仓库。

## 仓库目标
- 按 **公司 / 事业群 / 部门** 组织面试资料
- 用 **Markdown** 存题库
- 用 **JSON** 存结构化面试经验
- 将题目、题目感悟、整场面试感悟分开沉淀

---

## 目录结构（树状）

```text
companies/
  字节跳动/
    抖音电商/
      商业化技术/
        question-bank.md
        interview-experiences/
          README.md
          sample.json

  腾讯/
    微信事业群/
      基础平台/
        question-bank.md
        interview-experiences/
          README.md
          sample.json

  阿里巴巴/
    淘天集团/
      技术平台/
        question-bank.md
        interview-experiences/
          README.md
          sample.json
```

要求：
- **第一层只有公司名称**
- 点击进入公司后，再看到该公司的各个事业群
- 进入事业群后，再细分到部门
- 部门下题库与面经并列

---

## 数据设计

### 题库
- 文件：`question-bank.md`
- 作用：沉淀高频题、算法题、项目题、系统设计题、反问题

### 面试经验
- 目录：`interview-experiences/`
- 格式：JSON
- 一场面试一份 JSON

每份 JSON 重点保存：
- 题目
- 题目对应感悟
- 最终整场面试的感悟

示例见：
- `docs/json-schema.example.json`

---

## 当前已初始化公司
- 字节跳动
- 腾讯
- 阿里巴巴
- 美团
- 拼多多
- 快手
- 京东
- 百度

---

## 文档
- `PLAN.md`：项目查找计划
- `SOURCES.md`：来源口径与清洗规则
- `FIRST_BATCH.md`：第一批优先抓取清单

---

## 当前策略
先建立正确结构，再做高质量样本，再逐步扩张。
