# Moderation / Generation Failure Handler

## 输入

- error_code
- HTTP status
- moderation_stage: input | output | unknown | null
- moderation_categories
- risk_analysis
- rewrite_count
- retry_count
- moderation_mode
- previous_prompt_hash

## 输出动作

- retry_same
- rewrite_once
- product_only
- human_review
- block
- ops_fail

## 规则

### Safety block
如果 error_code = moderation_blocked：

- identical prompt retry = 0；
- moderation_mode 不得因为 block 从 auto 改成 low；
- hard policy flag → block；
- age / rights unresolved → human_review；
- legitimate ecommerce ambiguity 且 rewrite_count=0 → rewrite_once；
- rewrite_count>=1 → product_only / human_review / block，按业务目标选择；
- output stage block 不代表 prompt 一定违规，仍禁止随机原样重试。

### User / request error
请求参数、图片格式、尺寸等错误：
- 修正具体请求后再发；
- 不原样重试。

### 429
- rate limit：遵循 Retry-After，否则 exponential backoff + jitter；
- quota / spend limit：不重试，ops_fail。

### 5xx / overloaded
- 有限次 backoff；
- 建议 max_transient_retries <= 3。

### Auth / permission
- 401 / 403 → ops_fail，不重试。

## 安全不变量

max_semantic_rewrite_attempts = 1
max_identical_prompt_retries_after_safety_block = 0
allow_auto_to_low_after_block = false
allow_random_retry_until_pass = false
