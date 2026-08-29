# GCPP 一致性测试向量 / GCPP Conformance Test Vectors

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。协议状态码、字段名和 BCP 14 关键词保持英文原样。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror. Protocol state codes, field names, and BCP 14 keywords remain in English.

## 简体中文

状态：**Initial test plan（初始测试计划）**

本目录定义互操作测试案例，未来每个 GCPP Verifier 都应能够一致地评估这些案例。在第一套 Internet Deployment Profile 确定 Canonical Encoding 与 Baseline Algorithm 后，将加入具体序列化 Fixture。

### 1. 目的

Test Vector 是标准契约的一部分，用于防止两个实现对同一 Provenance Record 得出不同解释。

Vector MUST 包含负向和歧义场景，而不仅是有效原始内容。

### 2. 必需 Core 案例

#### TV-CORE-001 — Valid Original

输入：

- 结构有效的 Signed Record；
- 在选定 Test Policy 下可信的 Actor Verification Material；
- Exact Subject Binding 匹配；
- 没有未知 Critical Extension。

预期 Presentation Label：`VERIFIED_ORIGINAL`。

预期 Vector 重点：

```text
record_signature = VALID
actor_authentication = VALID
exact_integrity = VALID
```

#### TV-CORE-002 — 单字节或单字符修改

历史 Record 的 Signature 仍有效，但当前 Exact Content Binding 失败。

预期：MUST NOT 为 `VERIFIED_ORIGINAL`。

如果没有 Partial Binding，即使历史 Record 真实有效，对当前内容的归属仍不足。

#### TV-CORE-003 — 带 Parent 的有效 Derivative

Signed Child Record 引用有效 Parent，并绑定当前 Subject。

预期：当 Transformation Relationship 验证成功时为 `VERIFIED_DERIVATIVE`。

#### TV-CORE-004 — Partial Copy

只有选定 Source Segment 出现在更大的当前 Document 中。

预期：`PARTIAL_PROVENANCE`；Authenticated Coverage 不得包含 Unmatched Text。

#### TV-CORE-005 — Forged Signature

Record Syntax 与 Content Binding 看似合理，但 Signature 无效。

预期：

```text
record_signature = INVALID
```

不得进行 Verified Actor Attribution。

#### TV-CORE-006 — 恢复 RID，但内容无关

Generation A 的有效 RID/Watermark Locator 被插入无关内容 B。

预期：

```text
locator_state = LOCATOR_RECOVERED
exact_integrity != VALID
```

Presentation MUST NOT 把 B 全部归属为 A。预期 Label 为 `LOCATOR_ONLY` 或等价的 insufficient-attribution state。

#### TV-CORE-007 — Ambiguous RID

RID 解析到多个 Signed Record。

预期：

```text
locator_state = LOCATOR_AMBIGUOUS
```

Content Binding 可以进一步消歧。若 Binding 不足，则不得进行 Generation Attribution。

#### TV-CORE-008 — 未知 Non-Critical Extension

预期：Core Verification 继续；Extension 被报告为 unsupported。

#### TV-CORE-009 — 未知 Critical Extension

预期：受影响 Claim 为 `UNSUPPORTED`；内容不得被标记为 Fake。

#### TV-CORE-010 — Provider Signature 有效，但没有 History Evidence

预期：

```text
record_signature = VALID
historical_evidence = NOT_PRESENT
```

Verifier 不得混淆这两个维度。

#### TV-CORE-011 — 无效 Transparency/Anchor Evidence

Provider Signature 和 Content Binding 有效，但可选 Historical Proof 无效。

预期：Provenance Authentication 与 Historical Assurance 分开报告。

#### TV-CORE-012 — 当前 Key 已 Revoked/Compromised，但 Historical Key 当时有效

Generation 发生在 Key Compromise 前，且 Profile 提供 Historical Key Validity Evidence。

预期：Historical Verification 按 Key-Lifecycle Profile 处理，而不是自动判定所有旧 Record 无效。

#### TV-CORE-013 — Provenance Graph 中出现 Cycle

预期：Lineage Invalid / Diagnostic Cycle Detected。各个独立 Signed Record 可以继续保留自身 Signature State。

#### TV-CORE-014 — Missing Parent

Child Signature 有效，但一个 Parent Record 不可获得。

预期：输出 Availability/Missing-Lineage Diagnostic，而不是 Forged-Content 结论。

#### TV-CORE-015 — 仅有 Provider Model Declaration

有效 Provider Signature 声明 Model `M`，但没有 Execution Attestation。

预期：

```text
model_assurance = MODEL_DECLARED
```

MUST NOT 升级为 `MODEL_EXECUTION_PROVEN`。

### 3. Text Profile 案例

#### TV-TEXT-001 — Rich Copy 保留 Full Proof

Clipboard 同时包含 Plain Text 和 Structured GCPP Provenance Carrier。预期不依赖 Watermark 即可完成 Full Proof Resolution。

#### TV-TEXT-002 — Plain-Text Copy 删除 Metadata

只保留 Visible Text。Recover Robust Locator 后，通过 Signed Record + Content Binding 完成认证。

#### TV-TEXT-003 — Unicode Auxiliary Carrier 被删除

Visible Text 和 Robust Locator 仍存在。预期：Auxiliary Carrier 丢失不等于恶意篡改。

#### TV-TEXT-004 — 少量 Substitution

Exact Normalized-Text Digest 失败；注册的 Locator Scheme 恢复 RID；Segment Evidence 标识存活内容。

预期 Label 取决于 Authenticated Coverage，通常为 `VERIFIED_DERIVATIVE` 或 `PARTIAL_PROVENANCE`。

#### TV-TEXT-005 — 删除段落

存活 Segment 通过认证；被删除材料不存在。

预期：Coverage 仅按照 Profile-defined Denominator 对当前可认证材料计算。

#### TV-TEXT-006 — 插入无关内容

原始 AI 文本作为大 Document 的一部分继续存在。

预期：Inserted Content 保持 Unaunthenticated；不得进行 Whole-Document Attribution。

#### TV-TEXT-007 — Low-Entropy Code Output

Record 声明 `capacity.low-entropy-unavailable`；Attached Proof 有效。

预期：即使没有 In-Band Locator，Provenance 仍可为 `VERIFIED_ORIGINAL`。

#### TV-TEXT-008 — Very Short Text

没有完整 RID 容量，也没有 Metadata/Attached Proof。

预期：根据选定 Profile 为 `UNVERIFIED` 或粗粒度 Carrier State；MUST NOT 推断 Human Authorship。

#### TV-TEXT-009 — Full Paraphrase/Re-Generation

没有足够 Carrier 或 Content Binding 存活。

预期：`UNVERIFIED`。

### 4. 隐私案例

#### TV-PRIV-001 — Generation Identifier Inspection

GID 不得编码 Account ID、IP Address、Device ID 或 Geographic Location。

#### TV-PRIV-002 — Raw Prompt Absent

Baseline Public Record 不包含 Raw Prompt。

#### TV-PRIV-003 — Randomized Input Commitment

Enterprise Profile 使用 Randomized Commitment 绑定输入；Public Record 不披露输入。

### 5. Presentation Semantic 案例

Conformance Test SHOULD 除密码学外检查 API/UI Label。

禁止的语义映射包括：

```text
UNVERIFIED -> "human-written"
UNVERIFIED -> "fake"
VERIFIED -> "true"
LOCATOR_RECOVERED -> "generated by provider X"
```

除非存在 GCPP-VERIFY 要求的额外 Evidence。

### 6. 未来 Fixture 格式

当第一套 Canonical Serialization Profile 确定后，每个 Machine-Readable Vector 应包含：

```text
id
profile
input_content
records
evidence
trust_policy
expected_verification_vector
expected_label
notes
```

Fixture 应保持 deterministic，并可跨语言使用。

---

# English

Status: **Initial test plan**

This directory defines interoperability cases that every GCPP verifier should eventually be able to evaluate consistently. Concrete serialized fixtures will be added after the first Internet deployment profile fixes canonical encoding and baseline algorithms.

## 1. Purpose

Test vectors are part of the standards contract. They prevent two implementations from interpreting the same provenance record differently.

Vectors MUST include negative and ambiguous cases, not only valid originals.

## 2. Required Core cases

### TV-CORE-001 — valid original

Inputs:

- structurally valid signed record;
- trusted actor verification material under the chosen test policy;
- exact subject binding matches;
- no unknown critical extension.

Expected presentation label: `VERIFIED_ORIGINAL`.

Expected vector highlights:

```text
record_signature = VALID
actor_authentication = VALID
exact_integrity = VALID
```

### TV-CORE-002 — one-byte or one-character modification

Record signature remains valid over the historical record, but current exact content binding fails.

Expected: MUST NOT be `VERIFIED_ORIGINAL`.

If no partial binding exists, current-content attribution is insufficient even though the historical record is authentic.

### TV-CORE-003 — valid derivative with parent

A signed child record refers to a valid parent and binds to the current subject.

Expected: `VERIFIED_DERIVATIVE` when the transformation relationship validates.

### TV-CORE-004 — partial copy

Only selected source segments appear in a larger current document.

Expected: `PARTIAL_PROVENANCE`; authenticated coverage must not include unmatched text.

### TV-CORE-005 — forged signature

Record syntax and content binding appear plausible but signature is invalid.

Expected:

```text
record_signature = INVALID
```

No verified actor attribution.

### TV-CORE-006 — recovered RID, unrelated content

A valid RID/watermark locator from generation A is inserted into unrelated content B.

Expected:

```text
locator_state = LOCATOR_RECOVERED
exact_integrity != VALID
```

Presentation MUST NOT attribute all of B to A. Expected label is `LOCATOR_ONLY` or an equivalent insufficient-attribution state.

### TV-CORE-007 — ambiguous RID

RID resolves to multiple signed records.

Expected:

```text
locator_state = LOCATOR_AMBIGUOUS
```

Content bindings may disambiguate. Without sufficient binding, no generation attribution.

### TV-CORE-008 — unknown non-critical extension

Expected: Core verification continues; extension is reported unsupported.

### TV-CORE-009 — unknown critical extension

Expected: affected claim is `UNSUPPORTED`; content is not labeled fake.

### TV-CORE-010 — provider signature valid, no history evidence

Expected:

```text
record_signature = VALID
historical_evidence = NOT_PRESENT
```

The verifier must not conflate these dimensions.

### TV-CORE-011 — invalid transparency/anchor evidence

Provider signature and content binding valid, optional historical proof invalid.

Expected: provenance authentication and historical assurance reported separately.

### TV-CORE-012 — revoked/compromised current key, valid historical key

The generation predates key compromise and the profile provides historical key validity evidence.

Expected: historical verification follows the key-lifecycle profile rather than treating every old record as automatically invalid.

### TV-CORE-013 — cycle in provenance graph

Expected: lineage invalid/diagnostic cycle detected. Individual independently signed records can retain their own signature states.

### TV-CORE-014 — missing parent

Child signature valid but one parent record unavailable.

Expected: availability/missing-lineage diagnostic rather than forged-content conclusion.

### TV-CORE-015 — provider model declaration only

Valid provider signature claims model `M` but no execution attestation exists.

Expected:

```text
model_assurance = MODEL_DECLARED
```

MUST NOT become `MODEL_EXECUTION_PROVEN`.

## 3. Text-profile cases

### TV-TEXT-001 — rich copy preserves full proof

Clipboard includes plain text plus structured GCPP provenance carrier. Expected full proof resolution without watermark dependence.

### TV-TEXT-002 — plain-text copy strips metadata

Only visible text survives. Robust locator is recovered and then authenticated through signed record plus content binding.

### TV-TEXT-003 — Unicode auxiliary carrier stripped

Visible text and robust locator remain. Expected: auxiliary carrier loss does not imply malicious tampering.

### TV-TEXT-004 — small substitutions

Exact normalized-text digest fails; registered locator scheme recovers RID; segment evidence identifies surviving content.

Expected label depends on authenticated coverage, normally `VERIFIED_DERIVATIVE` or `PARTIAL_PROVENANCE`.

### TV-TEXT-005 — paragraph deletion

Surviving segments authenticate; deleted material is absent.

Expected: coverage calculated only over current authenticated material according to the profile-defined denominator.

### TV-TEXT-006 — unrelated insertion

Original AI text remains as one portion of a larger document.

Expected: inserted content remains unauthenticated; no whole-document attribution.

### TV-TEXT-007 — low-entropy code output

Record declares `capacity.low-entropy-unavailable`; attached proof is valid.

Expected: provenance can still be `VERIFIED_ORIGINAL` without an in-band locator.

### TV-TEXT-008 — very short text

No full RID capacity. Metadata/attached proof absent.

Expected: `UNVERIFIED` or coarse carrier state according to the selected profile; MUST NOT infer human authorship.

### TV-TEXT-009 — full paraphrase/re-generation

No sufficient carrier or content binding survives.

Expected: `UNVERIFIED`.

## 4. Privacy cases

### TV-PRIV-001 — generation identifier inspection

GID must not encode account ID, IP address, device ID, or geographic location.

### TV-PRIV-002 — raw prompt absent

Baseline public record contains no raw prompt.

### TV-PRIV-003 — randomized input commitment

Enterprise profile binds an input using randomized commitment; public record does not disclose the input.

## 5. Presentation-semantic cases

Conformance tests SHOULD check API/UI labels in addition to cryptography.

Forbidden semantic mappings include:

```text
UNVERIFIED -> "human-written"
UNVERIFIED -> "fake"
VERIFIED -> "true"
LOCATOR_RECOVERED -> "generated by provider X"
```

without the additional evidence required by GCPP-VERIFY.

## 6. Future fixture format

Once the first canonical serialization profile is selected, each machine-readable vector should contain:

```text
id
profile
input_content
records
evidence
trust_policy
expected_verification_vector
expected_label
notes
```

Fixtures should be deterministic and usable across languages.
