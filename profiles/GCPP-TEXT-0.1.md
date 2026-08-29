# GCPP 文本 Profile 0.1 / GCPP Text Profile 0.1

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。BCP 14 规范关键词和协议标识符保持英文原样。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror. BCP 14 normative keywords and protocol identifiers remain in English.

## 简体中文

状态：**Experimental Working Draft（实验性工作草案）**  
Profile 目标：在保持模型吞吐和文本质量的同时，实现纯文本的稳健来源恢复。

### 1. 目的

纯文本是一种困难的来源载体，因为复制/粘贴通常会删除文档 metadata 和 sidecar 状态。本 Profile 定义一种分层 Carrier 策略，使 metadata 丢失时来源能力可以平滑降级，而不是立即完全失效。

本 Profile 不声称能够通用检测所有 AI 内容，也不承诺经过任意重写后水印仍然存在。

### 2. 性能不变量

面向生产、符合规范的文本来源 Carrier SHOULD NOT 要求：

- 额外一次 LLM inference pass；
- 第二次模型调用；
- 为语义重排生成多个完整句子候选；
- 每句话调用 embedding 模型；
- 逐 token 网络请求；
- 逐 token ledger/blockchain 操作；
- 逐 token zero-knowledge proof 生成。

推荐的 in-band 路径是轻量级 sampling/logit transformation，不应实质改变主模型 forward pass。

如果某种水印方案在特定输出上无法满足 Provider 的正确性或延迟要求，本 Profile 允许不嵌入 in-band Carrier，但必须明确声明相应 capability state。

### 3. 分层 Carrier 模型

在可用时，文本来源 SHOULD 同时使用多个独立 Carrier：

1. **Attached proof** — 与内容一起打包的完整签名来源对象。
2. **Structured clipboard carrier** — 供支持协议的应用使用。
3. **Document/HTML metadata** — 用于富格式。
4. **Robust in-band locator** — 通过生成选择编码的短 locator。
5. **Auxiliary Unicode carrier** — 仅作为可选辅助通道。

任何单一 Carrier 都不要求在所有环境中强制存在。

### 4. GID 与 RID 分离

完整 `GenerationID` 是权威事件标识符，不要求能够完整装入可见文本。

in-band 文本水印承载紧凑的 `RecoveryLocator`（RID）或其片段，用于发现候选 Signed Record。

RID 属性：

- 可以短于 GID，或与 GID 独立；
- 可以使用错误纠正和交织；
- 可以解析到多个候选；
- 不足以单独进行认证；
- 本身不要求全球唯一。

这避免了不现实的主张，例如要求四个字符的回答在不影响可见内容的情况下携带完整密码学身份并具有强编辑鲁棒性。

### 5. Locator Watermark 抽象

注册的文本 Locator 方案定义：

```text
TextLocatorScheme {
  scheme_id
  version
  payload_capacity
  synchronization_method
  error_correction_method
  detector_parameters
  generation_constraints
}
```

方案 MAY 工作于 token sampling、lexical choice、punctuation choice 或未来高效的 in-band 机制，但 Core 不规定具体算法。

### 6. 质量与正确性

当嵌入会实质损害正确性、安全、确定性格式、代码执行、数学输出、结构化数据有效性或 Provider 定义的生成质量时，Text Locator 方案 MUST 允许生成器 abstain（不嵌入）。

Record SHOULD 传达类似以下 capacity state：

- `NONE`
- `PROVIDER_ONLY`
- `PARTIAL_LOCATOR`
- `FULL_LOCATOR`
- `REDUNDANT_LOCATOR`
- `UNAVAILABLE_LOW_ENTROPY`

这些状态描述 Carrier 容量，而不是 provenance validity。

### 7. 低熵输出

通常需要 fallback 的例子包括：

- 极短回答；
- 不允许改写的精确引用；
- 源代码；
- 严格 Schema 的 JSON/XML；
- 公式；
- deterministic 或 temperature-zero 输出；
- 要求精确措辞的固定法律/医疗文本；
- 有效 token 极少的 constrained decoding。

对于这些输出，即使没有嵌入稳健的 in-band Locator，Attached Proof、Clipboard Proof 或 Sidecar Proof 仍可提供完整来源。

### 8. 错误纠正与同步

稳健 Locator 方案 SHOULD 针对 deletion、insertion、substitution 设计，而不仅是 bit flip。

注册方案可以使用：

- block error-correcting codes；
- interleaving；
- rateless/fountain-style coding；
- synchronization strings；
- edit-distance codes；
- 重复的独立 Locator 片段；
- 未来编码结构。

具体结构由 Profile 注册并可替换。

### 9. 恢复流程

Verifier 处理纯文本时 SHOULD：

1. 检查存在的 Attached/Clipboard/Metadata Carrier；
2. 仅按 detector scheme 允许的规则进行规范化；
3. 尝试注册的稳健 Locator 检测；
4. 恢复零个或多个 RID 候选，并给出置信度/诊断；
5. 从任意可用来源解析候选 Signed Provenance Record；
6. 验证 Record Signature；
7. 将当前文本与 Exact/Partial Content Binding 比较；
8. 只归属得到有效 Binding 支持的内容。

高 Watermark Confidence 不能覆盖无效 Signature 或 Content Mismatch。

### 10. Copy/Paste 行为

支持协议的软件 MAY 将来源信息放入自定义剪贴板 representation，例如：

```text
application/gcpp-provenance+cbor
```

并与普通的 `text/plain`、`text/html` representation 同时提供。

理解 GCPP Clipboard Profile 的接收应用可以保留完整 Signed Proof。不支持协议的应用可以丢弃结构化 representation 而只保留可见文本；如果存在 in-band Locator，则它作为 fallback。

以上 media type 目前只是 provisional，在获得正式注册之前 MUST NOT 表示为已经注册的 IANA media type。

### 11. Unicode 辅助 Carrier

Zero-width character、variation selector、特殊空格或等效 Unicode 机制 MAY 作为辅助 Carrier。

它们 MUST NOT 成为稳健性声明背后的唯一机制，因为 Normalizer 和 Sanitizer 可以在不改变可见文本的情况下删除它们。

实现 MUST NOT 将辅助 Unicode Carrier 的删除自动解释为恶意剥离的证明。

### 12. 文本规范化

Text Integrity 与 Watermark Detection 使用不同的 normalization concern。

`TEXT-PLAIN` Integrity Profile SHOULD 至少定义：

- Unicode normalization form；
- line-ending normalization；
- trailing spaces 处理；
- BOM/control character 处理；
- 是否保留或删除视觉不可见字符；
- 与语言无关的编码要求。

Normalization Rule MUST 明确且版本化。

### 13. Exact 与 Partial Text Binding

Provider SHOULD 创建精确的 normalized-text binding，并 MAY 创建 Segment/Chunk Commitment 用于部分归属。

Segment Boundary SHOULD 能抵抗前部一次插入导致的灾难性整体偏移。可以注册 content-defined、paragraph-aware、sentence-aware 或未来更稳健的 segmentation profile。

Coverage Calculation MUST 使用定义明确的 denominator，并且 MUST NOT 推断未匹配文本也属于来源 Generation。

### 14. 编辑结果

示例行为：

- 格式/字体变化：Attached 或 Normalized Binding 可能仍有效；
- 普通跨软件复制：Robust Locator 可能存活；
- 少量词语修改：Locator/ECC 可能存活，Exact Digest 失败；
- 删除段落：Partial Binding 可认证保留下来的 Segment；
- 插入无关文本：只归属匹配 Segment；
- 中度改写：取决于具体 Scheme，Core 不保证；
- 翻译/回译：预期恢复能力下降；
- 完整重写/重新生成：Provenance 可能无法恢复。

最后一种状态报告为 `UNVERIFIED`，而不是 `HUMAN`。

### 15. Anti-Transplant 规则

移植到无关文本中的 RID 或可检测 Watermark MUST NOT 认证该无关文本。

Verifier 必须要求有效 Signed Record 和足够的 Content Relationship。移植 Locator 应产生 `LOCATOR_ONLY` 或表示 Locator/Content 不一致的诊断，而不是通过归属认证。

### 16. Scheme 评估

Text Locator Scheme 在被推荐进入 Internet Deployment Profile 之前，SHOULD 评估：

- output-quality regression；
- latency and throughput overhead；
- cross-language behavior；
- short-text capacity；
- low-entropy failure behavior；
- false positive rate；
- false negative rate；
- deletion/insertion/substitution robustness；
- paraphrase/translation robustness；
- spoofing and watermark-stealing resistance；
- detector-key compromise consequences。

Benchmark MUST 将 Recovery Performance 与 Cryptographic Attribution Performance 分开。

### 17. 未来演进

如果未来语义方法达到足够低的成本，可以注册新的 Semantic Method；但昂贵的大量多候选语义重排明确不属于 GCPP Text Profile 的 baseline。

---

# English

Status: **Experimental Working Draft**  
Profile goal: robust provenance recovery for plain text while preserving model throughput and text quality.

## 1. Purpose

Plain text is a difficult provenance medium because copy/paste commonly strips document metadata and sidecar state. This profile defines a layered carrier strategy that can degrade gracefully when metadata is lost.

This profile does not claim universal AI detection and does not promise watermark survival after arbitrary rewriting.

## 2. Performance invariant

A production-conforming text provenance carrier SHOULD NOT require:

- an additional LLM inference pass;
- a second model call;
- generation of multiple full sentence candidates for semantic reranking;
- embedding-model calls on every sentence;
- per-token network requests;
- per-token ledger/blockchain operations;
- per-token zero-knowledge proof generation.

The preferred in-band path is a lightweight sampling/logit transformation that does not materially alter the main model forward pass.

If a watermarking scheme cannot meet the provider's correctness or latency requirements for a given output, the profile permits the in-band carrier to be absent and requires the capability state to say so explicitly.

## 3. Layered carrier model

Text provenance SHOULD use multiple independent carriers when available:

1. **Attached proof** — full signed provenance object bundled with content.
2. **Structured clipboard carrier** — for supporting applications.
3. **Document/HTML metadata** — for rich formats.
4. **Robust in-band locator** — a short locator encoded through generation choices.
5. **Auxiliary Unicode carrier** — optional convenience channel only.

No single carrier is mandatory in every environment.

## 4. GID and RID separation

The full `GenerationID` is the authoritative event identifier. It is not required to fit inside the visible text.

The in-band text watermark carries a compact `RecoveryLocator` (RID) or fragments that can be used to discover candidate signed records.

RID properties:

- shorter than or independent from the GID;
- may be error-corrected and interleaved;
- may resolve to multiple candidates;
- not sufficient for authentication;
- not required to be globally unique on its own.

This avoids unrealistic claims that a four-character answer can invisibly carry a full cryptographic identity with strong edit robustness.

## 5. Locator watermark abstraction

A registered text-locator scheme defines:

```text
TextLocatorScheme {
  scheme_id
  version
  payload_capacity
  synchronization_method
  error_correction_method
  detector_parameters
  generation_constraints
}
```

The scheme MAY operate on token sampling, lexical choices, punctuation choices, or future efficient in-band mechanisms, but Core does not prescribe one algorithm.

## 6. Quality and correctness

A text-locator scheme MUST allow the generator to abstain from embedding when constraints would materially harm correctness, safety, deterministic formatting, code execution, mathematical output, structured data validity, or provider-defined generation quality.

The record SHOULD communicate a capacity state such as:

- `NONE`
- `PROVIDER_ONLY`
- `PARTIAL_LOCATOR`
- `FULL_LOCATOR`
- `REDUNDANT_LOCATOR`
- `UNAVAILABLE_LOW_ENTROPY`

These states describe carrier capacity, not provenance validity.

## 7. Low-entropy outputs

Examples that often require fallback behavior:

- very short answers;
- exact quotations where transformation is not permitted;
- source code;
- JSON/XML with strict schemas;
- formulas;
- deterministic or temperature-zero output;
- fixed legal/medical text requiring exact wording;
- constrained decoding with very few valid tokens.

For such outputs, attached proof, clipboard proof, or sidecar proof can provide full provenance even when no robust in-band locator is embedded.

## 8. Error correction and synchronization

A robust locator scheme SHOULD be designed for deletion, insertion, and substitution rather than only bit flips.

Registered schemes may use:

- block error-correcting codes;
- interleaving;
- rateless/fountain-style coding;
- synchronization strings;
- edit-distance codes;
- repeated independent locator fragments;
- future coding constructions.

The exact construction is profile-registered and replaceable.

## 9. Recovery

A verifier processing plain text SHOULD:

1. inspect attached/clipboard/metadata carriers if present;
2. normalize only as allowed by the detector scheme;
3. attempt registered robust locator detection;
4. recover zero or more RID candidates plus confidence/diagnostics;
5. resolve candidate signed provenance records from any available source;
6. verify record signatures;
7. compare the current text against exact and partial content bindings;
8. attribute only content supported by valid bindings.

A high watermark confidence cannot override an invalid signature or content mismatch.

## 10. Copy/paste behavior

Supporting software MAY place provenance in a custom clipboard representation such as:

```text
application/gcpp-provenance+cbor
```

alongside ordinary representations such as `text/plain` and `text/html`.

A receiving application that understands the GCPP clipboard profile can preserve the full signed proof. A non-supporting application can drop the structured representation while leaving visible text intact; the in-band locator remains the fallback when present.

The media type above is provisional and MUST NOT be represented as an officially registered IANA type until such registration exists.

## 11. Unicode auxiliary carrier

Zero-width characters, variation selectors, special spaces, or equivalent Unicode mechanisms MAY be used as an auxiliary carrier.

They MUST NOT be the only mechanism behind a robustness claim because normalizers and sanitizers can remove them without changing visible text.

An implementation MUST NOT treat deletion of the auxiliary Unicode carrier as proof of malicious stripping.

## 12. Text normalization

Text integrity and watermark detection use separate normalization concerns.

A `TEXT-PLAIN` integrity profile SHOULD define at least:

- Unicode normalization form;
- line-ending normalization;
- treatment of trailing spaces;
- treatment of BOM/control characters;
- whether visually invisible characters are preserved or removed;
- language-independent encoding requirements.

Normalization rules MUST be explicit and versioned.

## 13. Exact and partial text binding

A provider SHOULD create an exact normalized-text binding and MAY create segment/chunk commitments for partial attribution.

Segment boundaries SHOULD resist catastrophic shift after one early insertion. Content-defined, paragraph-aware, sentence-aware, or future robust segmentation profiles can be registered.

Coverage calculations MUST use a defined denominator and MUST NOT infer that unmatched text belongs to the source generation.

## 14. Edit outcomes

Illustrative behavior:

- formatting/font change: attached or normalized binding may remain valid;
- ordinary cross-software copy: robust locator may survive;
- small word edits: locator/ECC may survive, exact digest fails;
- deleted paragraphs: partial binding may authenticate surviving segments;
- inserted unrelated text: only matched segments are attributed;
- moderate paraphrase: scheme-dependent; no Core guarantee;
- translation/back-translation: expected recovery degradation;
- full rewrite/re-generation: provenance may become unrecoverable.

The last state is reported as `UNVERIFIED`, not `HUMAN`.

## 15. Anti-transplant rule

A RID or detectable watermark transplanted into unrelated text MUST NOT authenticate the unrelated text.

The verifier must require a valid signed record and sufficient content relationship. A transplanted locator should produce `LOCATOR_ONLY` or a diagnostic indicating locator/content inconsistency.

## 16. Scheme evaluation

Before a text-locator scheme is recommended for an Internet deployment profile, it SHOULD be evaluated for:

- output-quality regression;
- latency and throughput overhead;
- cross-language behavior;
- short-text capacity;
- low-entropy failure behavior;
- false positive rate;
- false negative rate;
- deletion/insertion/substitution robustness;
- paraphrase/translation robustness;
- spoofing and watermark-stealing resistance;
- detector-key compromise consequences.

Benchmarks MUST distinguish recovery performance from cryptographic attribution performance.

## 17. Future evolution

Semantic methods may be registered later if they become sufficiently low-cost, but expensive multi-candidate semantic reranking is intentionally not part of the baseline GCPP Text Profile.
