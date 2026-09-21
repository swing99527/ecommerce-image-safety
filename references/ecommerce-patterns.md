# Ecommerce Image Patterns

## 1. 白底 / 静物

默认：allow / R0

Prompt 重点：
- exact SKU geometry
- centered product
- even studio lighting
- accurate color
- clean background
- no extra logo / text

## 2. 普通成年服装模特

默认：allow / R1

目标：
- fit
- silhouette
- material
- hem / sleeve / neckline / waistband
- natural pose
- eye-level framing

## 3. 成人泳装

默认：rewrite or allow / R2

条件：
- adult_verified 或 adult_synthetic
- product-first
- natural beach / studio context
- full-body or neutral three-quarter
- 不以性刺激为目标

年龄 unknown → review。

## 4. 成人内衣

默认：rewrite / R2

优先：
- garment construction
- straps
- panels
- support
- lace / trim
- fit
- studio / catalog context

不需要人体时优先 product-only detail / mannequin。

## 5. 健身服

默认：allow / R1，身体强调过高则 rewrite。

把“身体效果”转为：
- waistband
- compression
- stretch
- seam placement
- mobility
- athletic fit

## 6. 美妆 / 护肤

默认：allow / R1。
涉及疗效、before-after → review。

不要生成虚假临床结果或确定性治疗承诺。

## 7. 珠宝 / 手表

默认：allow / R0-R1。

人物镜头只服务：
- scale
- placement
- material
- reflection
- clasp / setting

真人代言需要 rights gate。

## 8. 真人模特参考图

verified consent → 可继续。
unknown / denied → review / generic model / block。

## 9. 儿童普通服装

可为 age-appropriate catalog。
严格：
- fully clothed
- family-friendly
- no body emphasis
- no adultized styling

儿童敏感内衣：建议 product_only。

## 10. 医疗 / 健康商品

图像本身 + 声明一起审。
功效、before-after、身体变化承诺 → human review。

## 11. Brand KV

先锁：
- supplied logo
- exact product
- verified brand palette
- campaign copy
- target channel

再做：
hero product + visual metaphor + composition path + whitespace + copy zone。

## 12. UGC 风格

必须区分：
- “UGC aesthetic”
- “真实消费者证言”

前者可以是 synthetic creative；
后者如果会让消费者误以为真实购买者背书，需要真实性审查 / disclosure。

## 13. Product-only fallback

当人体不是核心业务目标时，优先：
- flat lay
- hanger
- packaging
- non-human mannequin
- macro detail
- multi-angle catalog
