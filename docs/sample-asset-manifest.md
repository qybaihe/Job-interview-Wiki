# 样板 / 示例资产治理清单

## 统计口径
- `companies/**/interview-experiences/` 下 JSON 总数：**132**
- 其中样板 / 示例 JSON：**34**
  - `sample.json`：8 份
  - 文件名含“样板”：26 份

## 存在 `sample.json` 的目录
1. `companies/快手/电商事业部/服务端研发/interview-experiences/`
2. `companies/美团/到店事业群/后端技术/interview-experiences/`
3. `companies/百度/智能云/基础架构/interview-experiences/`
4. `companies/腾讯/微信事业群/基础平台/interview-experiences/`
5. `companies/京东/零售技术/后端研发/interview-experiences/`
6. `companies/拼多多/主站业务/服务端/interview-experiences/`
7. `companies/阿里巴巴/淘天集团/技术平台/interview-experiences/`
8. `companies/字节跳动/抖音电商/商业化技术/interview-experiences/`

## 重复模板资产
### 完全重复的 `sample.json`
上述 8 份 `sample.json` 内容完全一致，可视为同一模板的多点复制。

### 重名“首批样板”文件
以下 3 份文件名重复，且命名不带明确公司/方向信息：
- `companies/腾讯/微信事业群/基础平台/interview-experiences/2026-首批样板-后端开发.json`
- `companies/阿里巴巴/淘天集团/技术平台/interview-experiences/2026-首批样板-后端开发.json`
- `companies/字节跳动/抖音电商/商业化技术/interview-experiences/2026-首批样板-后端开发.json`

## 治理建议
1. 为 README / progress_state / 后续脚本建立统一排除规则：
   - `sample.json`
   - 文件名含“样板”
2. 建议将 `sample.json` 迁移为仓库级单一模板，或至少显式标记为“模板，不计入真实面经统计”。
3. 将 `2026-首批样板-后端开发.json` 重命名为带公司与方向前缀的模板名，避免 basename 冲突。
4. 若不立刻迁移模板，至少应维护一份显式 manifest，避免未来再次统计失真。
