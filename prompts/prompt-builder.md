# Ecommerce Image Prompt Builder

## 目标

把已通过 Risk / Rights / Age Gate 的结构化 brief，转换成商品优先、可执行的 GPT Image Prompt。

## 标准结构

### 1. PURPOSE
- catalog / PDP / main image / campaign / social commerce / detail
- SKU / product name
- intended platform

### 2. SUBJECT
- product only / mannequin / synthetic adult / verified real adult
- 敏感成年品类需要明确成年
- 真人授权字段只作为系统元数据，不在画面里“声明授权”

### 3. PRODUCT
写清：
- color
- material
- cut
- silhouette
- seams
- trim / hardware
- pattern
- label / packaging
- supplied-reference fidelity

### 4. POSE / ACTION
只选择能帮助商品展示的简单动作。

### 5. CAMERA
优先：
- eye-level
- front / neutral three-quarter
- full-body / waist-up / product detail
- 明确主体占比与留白

### 6. SCENE
场景必须支持产品叙事，不能抢 SKU。

### 7. LIGHTING
- 电商主图：均匀、低色差
- lifestyle：自然光 / 柔光，但保持商品真实色
- 材质特写：保留纹理、高光与暗部层次

### 8. PRODUCT FIDELITY
必须明确哪些东西不能改变：
- geometry
- color relationships
- print / pattern
- logo / label placement
- strap / neckline / sleeve / waistline / hem
- packaging text when reference is supplied

### 9. BRAND / TEXT
- 只有在拥有 / 已授权的品牌资产上使用指定 logo。
- 不要“自动发明”官方广告语、代言关系或产品参数。
- 对需要事实的品牌 / 产品信息，先由外部事实检索层提供 verified facts。

### 10. NON-TARGET ELEMENTS
只写和业务风险相关的排除项，例如：
- no unrelated logos
- no extra text
- no redesign of supplied SKU
- no body-part-focused framing when not product-required

### 11. OUTPUT
- aspect ratio
- size
- quality
- number of variants

## 模板

Create a [shot_type] ecommerce image for [SKU].

Commercial objective:
[what the customer must understand about the product]

Subject:
[product-only / clearly adult synthetic model / verified adult reference subject]

Product fidelity:
Preserve [color, geometry, cut, material, pattern, seams, trim, logo/label placement] from the supplied product reference.

Pose / action:
[natural product-serving action]

Camera:
[framing, angle, subject scale, negative space]

Scene:
[clean relevant environment]

Lighting:
[lighting that preserves material and color]

Brand / text constraints:
[authorized brand assets and exact supplied copy only]

Do not:
[only concrete non-target elements]

Output:
[ratio / size / quality].
