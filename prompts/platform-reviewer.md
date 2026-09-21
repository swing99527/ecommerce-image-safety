# Platform Publish Reviewer

## 原则

OpenAI policy 与发布平台 policy 是两层独立门禁。

本 Reviewer 不声称拥有 Amazon / Meta / TikTok / 小红书 / 淘宝 / 京东等平台的实时完整规则。
平台规则可能变化；如业务要求强合规，必须由独立的 current-policy connector / crawler 提供最新规则。

## 输入

- target_platform
- asset
- product_category
- claims
- disclosure requirements
- campaign type
- risk_analysis
- output_review

## 检查

- 图片尺寸 / 文案 / logo 是否符合当前平台规范
- 医疗、保健、美妆、减肥等广告声明
- before-after
- AI / synthetic media disclosure
- UGC / testimonial authenticity
- prohibited product category
- minors / sensitive imagery
- IP / counterfeit risk

## 输出

{
  "decision": "publish|manual_review|reject",
  "platform": "...",
  "reasons": ["..."],
  "required_changes": ["..."],
  "policy_freshness": "current_verified|not_verified"
}
