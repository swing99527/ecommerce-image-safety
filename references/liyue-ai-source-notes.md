# @liyue_ai Source Notes — Prompt Patterns for Ecommerce Image Work

更新：2026-09-21

本文件不是 X 原文存档。目标是：
1. 找到原作者可验证来源；
2. 提取可迁移的 Prompt 工程模式；
3. 映射到 content-agent 的电商生图 Skill。

## Source A — 女性人像安全写法

Original X:
https://x.com/liyue_ai/status/2056947629548843481

可迁移模式：
- 不围绕单个“敏感词”做机械替换；
- 把重点从身体部位 / 挑逗动作迁移到：
  - 明确成年人
  - 整体体态
  - 服装结构
  - 自然姿态
  - 镜头构图
  - 光线
  - 商业 / 编辑审美
- 对电商的等价抽象：从 body-first 改为 product-first。

在本 Skill 中映射为：
`prompts/safety-rewriter.md`。

## Source B — GPT Image 2 安全审核机制讨论

Original X:
https://x.com/liyue_ai/status/2057714329416581302

使用方式：
- 仅作为第三方工程假设 / 经验线索；
- 不把作者关于内部分类器的推断当作官方事实；
- 真实生产规则必须回到 OpenAI Usage Policies / Images API / Moderation 官方文档。

对本 Skill 的启发：
- 风险是“整组视觉语义”的组合，而非词表；
- 同一文字输入可能因为最终画面不同而出现不同 output moderation 结果；
- 因此失败处理必须区分 input / output，并禁止无限随机重试。

## Source C — 城市宣传海报

Original X:
https://x.com/liyue_ai/status/2045332620352119274

可迁移模式：
- 先定义一个强视觉隐喻；
- 用明确的构图路径组织视线（例如 S 型流线）；
- 用真实地标 / 产品资产做 reality anchor；
- 同时预留大面积负空间；
- 最后定义文字区域、比例和画面完成度。

电商映射：
品牌海报不要“元素堆满”，而要：
`hero product + one visual metaphor + one compositional path + brand anchors + whitespace + copy region`。

## Source D — 品牌 KV 母版

Indexed source:
https://x.com/liyue_ai/status/2066173641898008721

X 正文在部分抓取环境不可读；该 status id 可由公开提示词索引交叉确认。

可迁移模式：
- 输入品牌名 / 主推产品 / 广告语 / 目标人群 / 画幅 / KV 类型 / 平台；
- 先识别品牌行业与视觉资产，再组织产品叙事；
- 不是普通产品图，而是 concept key visual。

生产化改造：
- 不允许模型仅凭记忆“自动认定”当前品牌资产或产品参数；
- 先由事实层提供 verified brand facts / supplied brand assets；
- Prompt Builder 只消费 verified facts；
- 避免虚构官方 slogan、产品规格或代言关系。

## Source E — 电商定制图实践

Original X:
https://x.com/liyue_ai/status/2064665423258239439

作者公开说明其女性写真导演 Skill 包含电商穿戴 / 试衣能力，也指出“模特穿戴商品”与“完整电商套图 / 海报系统”是不同层级。

可迁移模式：
- 电商模特图：product fidelity first；
- 电商套图：需要额外的 KV / layout / copy / platform 层；
- 不应让一个人像 Prompt 同时承担全部电商设计职责。

## Source F — 原作者开源 Skill

Repository:
`liyue-aigc/female-portrait-director`

License: MIT
Pinned commit:
`8cddecd6786d187688e8e89a1f606540186a962f`

重点文件：
- `skill/routes/commercial/ecommerce-tryon.md`
- `skill/tools/safety-rewrite.md`
- `skill/tools/failure-diagnosis.md`
- `skill/core/director-gate.md`
- `skill/core/parameter-lock.md`
- `skill/core/reference-image-lock.md`

### 提取的可复用工程原则

#### 1. 参数锁定优先
用户明确指定的 SKU / 颜色 / 版型 / 材质 / 场景 / 画幅必须锁定。
Agent 只能补全缺失字段，不能偷偷换目标。

#### 2. 电商优先级
安全
> 上传商品
> 品类
> 颜色
> 版型
> 材质
> 图案 / 结构 / 装饰
> 完整度
> 展示范围
> 模特
> 姿态
> 场景
> 平台
> 审美。

#### 3. 模特是商品展示载体
普通写真可以人物审美优先；
电商试衣必须商品还原优先。

#### 4. Director Mode
Prompt 不应机械拼字段，而应组成一个可拍摄瞬间：
- time slice
- one small event
- action chain
- gaze target
- 2–3 selective environment details
- camera
- lighting

#### 5. 敏感服装不自动切“性感写真”
贴身 / 吊带 / 泳装 / 内衣出现时仍由 ecommerce route 主导。
人物气质只是 secondary styling；商品展示是 primary objective。

#### 6. 真人 / 商品参考图先锁
对身份 / 商品核心视觉先形成 protected-feature lock，再做风格扩展。

## 原作者近期公开 Prompt 结构观察

在其 X 公开样例中，经常使用结构化字段：

- 摄影风格
- 写真 / 业务方向
- 场景方向
- 服装方向
- 气质标签
- 五官方向 / 五官细节
- 发型方向 / 发型细节
- 身形方向
- 线条强调
- 镜头方向
- 姿态动作
- 光线氛围
- 滤镜效果
- 画幅比例
- 补充要求

本 Skill 不直接复制这些具体成人写真 Prompt，而把字段抽象为：
`commercial objective → subject → product → pose → camera → scene → lighting → fidelity → constraints → output`。

## 版权与使用边界

- X 帖：仅保存 source id 与独立总结，不整篇复制。
- 原作者 GitHub：MIT，可改造；保留 NOTICE / attribution。
- 本 Skill 的政策结论不由 X 帖决定，官方政策优先。
