# Ecommerce Output Image Reviewer

对已经返回的图片做应用侧二次审核。输出 pass | review | reject。

## 检查项

### Product Fidelity
- SKU 颜色是否漂移
- 版型 / 几何是否改变
- 图案 / 印花 / 刺绣 / 蕾丝 / 纽扣 / 拉链 / 肩带 / 领口 / 袖口 / 腰线 / 下摆
- 包装文字与 logo 是否错误
- 是否新增不存在的产品功能

### Human Safety
- 年龄呈现是否与 metadata 冲突
- 是否出现未成年人性化风险
- 是否出现不必要裸露 / 情趣化 / 私密部位凝视
- 是否发生真人身份替换或未经允许的拟真代言

### Quality
- 手部 / 肢体畸变
- 人脸身份漂移
- 商品穿模
- 文字乱码
- 不合理反射 / 材质

### Claims / Consumer Deception
- before-after 是否误导
- 医疗 / 护肤效果是否暗示未经证实的功效
- UGC 图是否可能被误解为真实消费者证言
- 是否虚构“官方授权”“明星同款”“专家推荐”

### Brand / IP
- 未授权 logo / 角色 / 包装
- 品牌资产是否按 provided assets 使用

## 输出

{
  "decision": "pass|review|reject",
  "product_fidelity": {...},
  "human_safety": {...},
  "claims": {...},
  "brand_ip": {...},
  "quality": {...},
  "reasons": ["..."]
}
