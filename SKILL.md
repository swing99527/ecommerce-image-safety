# Ecommerce Image Safety Skill

把自由文本的电商生图需求，转换成可审计、商品优先、政策感知的图片生成计划。

## North Star

不要优化“怎么过审核”，而要优化：

**如何把合法的电商视觉意图表达成准确、可控、可审计的商业视觉规范。**

## 触发条件

当任务涉及以下任一情况时使用本 Skill：

- 电商商品图、PDP、详情页、主图、社媒种草图、广告 KV；
- 模特穿搭、试衣、泳装、内衣、运动服、美妆、珠宝、3C、食品、家居；
- 真人参考图、模特授权、品牌资产、Logo / 包装；
- GPT Image 生成前风险判断；
- moderation block / output block / 生成失败后的安全路由；
- 生成后的商品保真、人物安全、广告真实性、平台发布审核。

## 非目标

本 Skill 不是审核绕过器。禁止：

- 用同义词、编码、拆分请求伪装被禁止的意图；
- 对 moderation_blocked 原样重复生成“撞通过”；
- 因为被拦截而自动把 moderation 从 auto 改成 low；
- 把未成年人或年龄未知人物默认为成年人；
- 虚构肖像授权、品牌授权、医疗证据或代言关系；
- 把被禁止的意图包装成“商业摄影”“电商用途”继续执行。

## 决策枚举

- allow：意图合法且信息充分，可进入 Prompt Builder。
- rewrite：业务目标合法，但表达高歧义；仅做一次 safety-preserving rewrite。
- review：年龄、授权、声明、品牌权利或平台规则存在实质不确定性。
- product_only：保留合法商品目标，但不使用真人/人体展示；切到平铺、衣架、包装或非人体人台。
- block：硬性政策风险或明确规避安全机制。

## 内部 Risk Tier

- R0：纯商品 / 静物 / 包装 / 鞋包配饰。
- R1：普通成年模特商业图片。
- R2：潜在敏感但可能合法：成年泳装、内衣、睡衣；普通儿童服装；医疗/护肤声明类。
- R3：年龄、肖像授权、品牌授权、代言真实性等关键条件未确认。
- R4：硬性禁止或明确 safety evasion。

R0-R4 是本仓库工程分级，不是 OpenAI 官方分级。

## 完整工作流

Structured Intake
→ Risk Analyzer
→ Deterministic Policy Gate
→ Age / Rights Gate
→ Safety-Preserving Rewriter（仅 decision=rewrite）
→ Ecommerce Prompt Builder
→ GPT Image
→ Moderation Failure Handler
→ Output Image Reviewer
→ Platform Publish Reviewer
→ Audit Log / Publish

## 强制不变量

1. 未成年人性化 / 剥削 / CSAM → block。
2. 年龄未知 + 泳装 / 内衣 / 高身体强调 → review，不自动猜成年。
3. 真人商业拟真使用：授权不足时不得生成“本人真实代言”；可在不改变业务目标时切 generic non-identifiable model。
4. 非自愿亲密内容 → block。
5. 欺诈、冒充、虚构代言 → block。
6. 本电商 Skill 不处理政治竞选 / 游说 / 选举说服素材 → block。
7. 明确要求绕过安全机制 → block。
8. moderation_blocked 后：identical retry = 0。
9. moderation_blocked 后：auto → low 自动切换 = 禁止。
10. semantic safe rewrite 最多 1 次。
11. 网络、429、瞬时 5xx 才允许有限 backoff retry；安全拦截不属于基础设施重试。

## 调用顺序

1. 读取 `prompts/risk-analyzer.md`。
2. 用 `schemas/risk-analysis.schema.json` 验证输出。
3. 套用本文件与 `references/policy-mapping.md` 的 deterministic gates。
4. decision=rewrite 时，仅运行一次 `prompts/safety-rewriter.md`。
5. 读取 `prompts/prompt-builder.md` 生成商品优先 Prompt。
6. API 失败时运行 `prompts/failure-handler.md`。
7. 返回图片后运行 `prompts/output-reviewer.md`。
8. 发布前运行 `prompts/platform-reviewer.md`。
9. 记录 trace 与最终决策。

## 生产默认值

- GPT Image moderation：`auto`。
- semantic rewrite：max 1。
- identical retry after moderation block：0。
- transient retry：指数退避 + jitter，有限次数。
- R2：必须后审；建议人工抽检。
- R3：暂停生成，补元数据 / 人工审。
- R4：直接 block。

## 必须记录的审计字段

`trace_id, sku, product_category, channel, raw_intent_hash, prompt_version,
policy_version, model_version, risk_tier, risk_flags, age_class,
likeness_consent, moderation_mode, rewrite_count, openai_request_id,
openai_error_code, moderation_stage, moderation_categories,
output_asset_hash, output_review, platform_review, final_decision`

## 来源优先级

OpenAI 官方政策 / API 文档
> 企业自己的更严格规则
> 原作者 @liyue_ai 的开源 Skill 方法
> X / 社区工程经验

第三方经验不能覆盖官方政策。
