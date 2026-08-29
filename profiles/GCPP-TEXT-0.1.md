# GCPP Text Profile 0.2 / GCPP 纯文本耐久来源 Profile 0.2

> 状态 / Status: **Experimental Working Draft**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 定位

GCPP-TEXT 0.2 不定义新的通用 Manifest。其目标是为 **C2PA Durable Content Credentials / Soft Binding** 提供一个生成式纯文本专用、低开销、可恢复的 `RecoveryLocator (RID)` Profile，并补充文本 normalization、partial attribution 与低熵降级语义。

C2PA 已支持非结构化文本、Soft Binding、Invisible Watermark、Fingerprint 与 Manifest Repository；GCPP-TEXT 的差异不在“支持文本”，而在于：

- 把完整 Generation 身份与短 RID 分离；
- RID 只负责发现候选 Manifest/Record；
- 为 ECC、同步、冗余和局部恢复留出容量；
- 尽量让 locator 信号存在于正常可见文本生成选择中，而不是只依赖文件 metadata 或 Unicode 隐藏字符；
- locator 恢复后仍必须验证 C2PA Claim Signature 与内容绑定。

## 2. 性能不变量

Baseline **SHOULD NOT** 要求：

- 额外 LLM inference pass；
- 第二模型调用；
- 多个完整候选句的语义 reranking；
- 每句 embedding 调用；
- per-token 网络请求；
- per-token ledger/blockchain 操作；
- per-token ZK proof。

推荐热路径：

```text
model forward
   ↓
logits
   ↓
lightweight locator processor
   ↓
sampling
   ↓
token
```

## 3. GID/RID

- `GenerationID (GID)`：权威生成事件身份；
- `RecoveryLocator (RID)`：短、可冗余、可碰撞的发现值。

RID **MUST NOT** 被解释为 Provider authentication。

推荐映射：

```text
RID
 ↓
C2PA soft-binding identifier / compatible resolver key
 ↓
Manifest Repository
 ↓
C2PA Manifest + GCPP assertions
```

## 4. 多通道 Carrier

按可用性组合：

1. C2PA embedded/external Manifest；
2. structured clipboard carrier；
3. document/HTML metadata；
4. robust in-band RID locator；
5. auxiliary Unicode carrier。

Unicode Variation Selector 或 zero-width 类机制可作为辅助，但 **MUST NOT** 是 durable claim 的唯一依据。

## 5. 低熵降级

非常短的文本、代码、JSON/XML、公式、精确引文、固定法律文本、temperature≈0 等场景必须允许：

```text
capacity.none
capacity.provider-only
capacity.partial-locator
capacity.full-locator
capacity.redundant-locator
capacity.low-entropy-unavailable
```

不能为了嵌水印破坏正确性。

## 6. 恢复与认证

Verifier：

```text
attached C2PA proof?
   ├─ yes → validate
   └─ no
        ↓
robust locator detection
        ↓
RID candidate(s)
        ↓
manifest resolution
        ↓
C2PA signature validation
        ↓
hard/soft binding validation
        ↓
GCPP partial coverage / model assurance
```

高 watermark confidence 不能覆盖无效签名或 content mismatch。

## 7. Anti-transplant

把真实 RID 移植到无关文本中时，Verifier 应得到 locator evidence，但不得把无关内容归属给原 Provider。结果应类似：

```text
locator = RECOVERED
signature = VALID (for historical manifest)
content_relationship = INSUFFICIENT
presentation = LOCATOR_ONLY / PARTIAL
```

## 8. 与中国 GB 45438 的关系

中国 `AIGC` 文件元数据可作为独立 regulatory carrier。GCPP-TEXT 不把 `ContentProducer/ProduceID` 当成 C2PA Claim Signature，也不把 C2PA 签名当成中国法规显式标识的替代。

二者可以同时存在。

## 9. Benchmark 要求

候选 scheme 必须测量：

- throughput/latency；
- quality regression；
- false positive / false negative；
- 多语言；
- deletion/insertion/substitution；
- copy/paste/normalization；
- paraphrase/translation degradation；
- spoofing/transplant；
- detector-key compromise；
- ECC/synchronization recovery。

---

# English

GCPP-TEXT 0.2 is a generative plain-text profile for **C2PA Durable Content Credentials / Soft Binding**, not a new manifest format. It separates authoritative `GenerationID` from compact `RecoveryLocator`, preserves low-overhead generation constraints, supports graceful abstention for short/low-entropy outputs, and requires C2PA signature/content-binding validation after locator recovery.

The baseline must not require extra LLM passes, large full-sentence semantic reranking, per-token network/ledger calls, or per-token ZK proofs. Unicode hidden carriers are auxiliary only. A recovered RID is discovery evidence, never actor authentication.
