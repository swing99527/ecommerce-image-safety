# Policy Mapping

更新检查日期：2026-09-21

## 官方来源优先

1. OpenAI Usage Policies
   https://openai.com/policies/usage-policies/
2. GPT-Image-2 model
   https://developers.openai.com/api/docs/models/gpt-image-2
3. Image generation guide
   https://developers.openai.com/api/docs/guides/image-generation
4. Create Image API reference
   https://developers.openai.com/api/reference/resources/images/methods/generate/
5. Image prompting guide
   https://developers.openai.com/api/docs/guides/image-prompting
6. Moderation API
   https://developers.openai.com/api/docs/guides/moderation
7. Safety best practices
   https://developers.openai.com/api/docs/guides/safety-best-practices
8. Under-18 API guidance
   https://developers.openai.com/api/docs/guides/safety-checks/under-18-api-guidance
9. CSAM guidance
   https://developers.openai.com/api/docs/guides/csam-guidance
10. ChatGPT Images 2.0 deployment safety
    https://deploymentsafety.openai.com/chatgpt-images-2-0

## 工程解释

- Images safety 是多层机制，不能简化成词表。
- Direct Images API 的 moderation 参数包括 auto / low（以当前官方 API 为准）。
- low 表示 less restrictive filtering，不是关闭政策审核。
- moderation_blocked 应与网络 / 服务器错误区分。
- 如 API 返回 moderation_stage / coarse categories，应记录并用于 routing；不要把它反推成内部 classifier 完整逻辑。
- 独立 Moderation API 可作为应用侧 pre/post signal，但不是 Usage Policy 的完整替代品。
- OpenAI 安全系统会持续变化；模型 snapshot 不意味着 safety stack 永久固定。

## 本 Skill 的额外企业规则

企业规则可以比平台更严格，例如：
- 儿童贴身商品默认 product-only；
- 未验证真人商业用途默认 review；
- R2 一律 post-review；
- 任何 moderation block 都不自动切 low。

这些是本项目工程规则，不应描述为 OpenAI 官方要求。
