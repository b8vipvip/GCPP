# GCPP 验证语义 0.1 / GCPP Verification Semantics 0.1

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。协议状态码及 BCP 14 关键词保持英文原样。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror. Protocol state codes and BCP 14 keywords remain in English.

## 简体中文

状态：**Working Draft（工作草案）**

本文件定义符合 GCPP 的 Verifier 如何解释 Claim 与 Evidence，并有意保持 Policy-Neutral。

### 1. Verification 是 Vector，不是单一 Verdict

Verifier MUST 先计算彼此独立的验证维度，再派生人类可读标签。单一 Boolean 结果不足以满足 GCPP 一致性要求。

最小维度：

```text
actor_authentication
record_signature
model_assurance
exact_integrity
partial_integrity
authenticated_coverage
locator_state
lineage_state
historical_evidence
unsupported_critical_features
```

### 2. 通用状态词汇

除非某个 Registered Profile 定义更具体的词汇，维度 SHOULD 使用：

- `VALID`
- `INVALID`
- `UNVERIFIED`
- `UNSUPPORTED`
- `NOT_PRESENT`
- `PARTIAL`

Model Assurance 使用：

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

Locator State 使用：

- `LOCATOR_NOT_PRESENT`
- `LOCATOR_DETECTED`
- `LOCATOR_PARTIAL`
- `LOCATOR_RECOVERED`
- `LOCATOR_AMBIGUOUS`

### 3. 验证顺序

Verifier SHOULD 按以下逻辑顺序执行：

1. Parse Record，并拒绝结构上畸形的 Mandatory Field；
2. 评估未知 Critical Extension；
3. Resolve/Load Actor Verification Material；
4. 验证 Provenance Record Signature；
5. 将 Actor Identity Evidence 与 Signature Validity 分开评估；
6. 针对 Presented Subject 评估 Exact Content Binding；
7. 在可用时评估 Partial/Segment Binding；
8. 评估 Parent Reference 和 Provenance DAG Consistency；
9. 仅把 Watermark/Locator Recovery 作为 Discovery Evidence；
10. 评估 Timestamp、Transparency Inclusion、Witness 或 Anchor 等 Historical Evidence；
11. 评估可选 Execution/Attestation Evidence；
12. 输出 `VerificationVector`；
13. 派生 Presentation Label，但不改变底层 Vector。

### 4. Signature 语义

有效 Record Signature 证明：相关 Signing Key 的持有者签署了 Canonical Record。它本身不证明：

- Legal Identity；
- Factual Truth；
- Model Execution Correctness；
- User Identity；
- Historical Timestamp；
- Current-Content Identity。

这些需要独立 Evidence Dimension。

### 5. Identity 语义

`actor_authentication = VALID` 表示 Verifier 选定的 Identity Method 和 Local Trust Policy 支持该 Actor Binding。

Verifier MUST 暴露 Identity Method，并 SHOULD 暴露 Trust Basis。它 MUST NOT 在 Evidence 不足时，把 Provider-controlled Key 静默提升为更强的现实世界身份声明。

### 6. Exact Integrity

`exact_integrity = VALID` 表示至少一个由 Profile 指定的 Exact Content Binding，在规定的 Normalization Profile 下与 Presented Content 匹配。

`exact_integrity = INVALID` 表示 Presented Content 与该 Binding 不完全匹配。它不会使历史 Record 上的有效 Signature 失效，也不会抹掉 Partial Provenance。

### 7. Partial Integrity 与 Coverage

当存在 Segment/Chunk Evidence 时，Verifier SHOULD 根据 Profile 定义的 Denominator 计算 Authenticated Coverage。

Coverage MUST 只标识能够绑定到 Authenticated Provenance 的内容。MUST NOT 从一小块存活 Fragment 外推到整个 Document。

如果当前 Document 只有 5% 被认证为某次 Source Generation，Verifier MUST NOT 将整个 Document 标记为该 Source 的原始输出。

### 8. Locator 语义

Watermark 或 Locator 可以帮助恢复 Candidate RID 或 Record Reference。以下规则为规范性要求：

> 恢复到 Locator 永远不足以单独完成 Actor 或 Generation Attribution。

归属至少要求有效 Signed Record，以及在相关 Profile 下足够的 Content Relationship。

移植到无关内容的 Locator SHOULD 产生 `LOCATOR_RECOVERED` 加 Failed/Insufficient Content Binding，而不是 Verified Attribution。

### 9. Historical Evidence

Historical Evidence 与 Signature Validity 独立评估。

例如：

- Signed Transparency Checkpoint；
- Inclusion/Consistency Proof；
- Timestamp Proof；
- Witness Quorum；
- Blockchain/Distributed-Ledger Anchor；
- Hardware Append-Only Log。

一个 Record 可以有有效 Provider Signature，但没有 Historical Evidence。此时 Verifier MUST 报告这种区别，而不是让整个 Provenance Record 失败。

### 10. Lineage

Verifier MUST 支持 Multiple Parent，并检测 Provenance DAG 中明显的 Cycle。

Child Event 不会追溯性改变 Parent Record 的有效性。Missing Parent MAY 降低 Lineage Assurance，但 MUST NOT 自动让独立有效的 Signed Child Record 失效。

### 11. 派生 Presentation Label

以下标签 RECOMMENDED 用于可互操作 UI。

#### VERIFIED_ORIGINAL

最低条件：

- Record Signature Valid；
- Actor Authentication 在选定 Trust Policy 下 Valid；
- Exact Content Binding Valid；
- 没有影响该 Claim 的 Unresolved Critical Feature。

Historical Evidence 与 Model Assurance SHOULD 分别展示，不会被该标签隐式提升。

#### VERIFIED_DERIVATIVE

适用于：

- 存在有效 Signed Provenance Path；
- 当前内容不是 Source Event 的 Exact Match；
- 当前 Subject 存在 Verified Derivation Relationship 或显著的 Authenticated Partial Relationship。

#### PARTIAL_PROVENANCE

仅部分当前内容能够密码学或结构性绑定到一个或多个有效 Provenance Record 时使用。

在有意义时，UI SHOULD 显示 Authenticated Coverage。

#### LOCATOR_ONLY

当 Recovery Carrier/Watermark 指示存在 Provenance Material，但 Authentication 或 Content Binding 不足/不可用时使用。

#### UNVERIFIED

当 GCPP 无法建立足够 Provenance 时使用。

规范解释：

```text
UNVERIFIED != HUMAN
UNVERIFIED != FAKE
UNVERIFIED != ILLEGAL
UNVERIFIED != LOW_QUALITY
```

### 12. Truth Separation

任何 GCPP Label 都不表示内容事实正确。UI 和 API MUST 将 Provenance State 与 Fact-Checking、Moderation、Copyright、Plagiarism、Academic Integrity 或 Legal Status System 分离。

规范解释：

```text
VERIFIED != TRUE
```

### 13. Local Policy

不同 Application MAY 对 Actor Identity、可接受 Algorithm、Evidence Age 或 Required Historical Assurance 应用不同 Trust Policy。Raw Verification Vector SHOULD 保持可用，以避免 Local Policy 冒充 Protocol Fact。

### 14. Diagnostics

Verifier SHOULD 为以下失败提供 Machine-Readable Diagnostic：

- malformed record；
- unsupported critical extension；
- invalid signature；
- unresolved actor key；
- exact content mismatch；
- insufficient partial coverage；
- ambiguous locator；
- broken lineage reference；
- stale/revoked verification key；
- historical evidence unavailable；
- evidence proof invalid。

Diagnostic MUST 避免仅因 Provenance Verification 失败就宣称内容为 Fake。

---

# English

Status: **Working Draft**

This document defines how conforming verifiers interpret GCPP claims and evidence. It is intentionally policy-neutral.

## 1. Verification is a vector, not a verdict

A verifier MUST compute independent dimensions before deriving a human-readable label. A single boolean result is insufficient for GCPP conformance.

Minimum dimensions:

```text
actor_authentication
record_signature
model_assurance
exact_integrity
partial_integrity
authenticated_coverage
locator_state
lineage_state
historical_evidence
unsupported_critical_features
```

## 2. Common state vocabulary

Unless a registered profile defines a more specific vocabulary, dimensions SHOULD use:

- `VALID`
- `INVALID`
- `UNVERIFIED`
- `UNSUPPORTED`
- `NOT_PRESENT`
- `PARTIAL`

Model assurance uses:

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

Locator state uses:

- `LOCATOR_NOT_PRESENT`
- `LOCATOR_DETECTED`
- `LOCATOR_PARTIAL`
- `LOCATOR_RECOVERED`
- `LOCATOR_AMBIGUOUS`

## 3. Verification order

A verifier SHOULD follow this logical order:

1. Parse the record and reject structurally malformed mandatory fields.
2. Evaluate unknown critical extensions.
3. Resolve or load actor verification material.
4. Verify the provenance-record signature.
5. Evaluate actor identity evidence separately from signature validity.
6. Evaluate exact content bindings against the presented subject.
7. Evaluate partial or segment bindings when available.
8. Evaluate parent references and provenance DAG consistency.
9. Evaluate watermark/locator recovery as discovery evidence only.
10. Evaluate historical evidence such as timestamps, transparency inclusion, witnesses, or anchors.
11. Evaluate optional execution/attestation evidence.
12. Emit a `VerificationVector`.
13. Derive a presentation label without changing the underlying vector.

## 4. Signature semantics

A valid record signature establishes that the holder of the relevant signing key signed the canonical record. It does not, by itself, establish:

- legal identity;
- factual truth;
- model execution correctness;
- user identity;
- historical timestamp;
- current-content identity.

Those require separate evidence dimensions.

## 5. Identity semantics

`actor_authentication = VALID` means the verifier's selected identity method and local trust policy support the actor binding.

A verifier MUST expose the identity method and SHOULD expose the basis of trust. It MUST NOT silently turn a provider-controlled key into a stronger real-world identity claim than the available evidence supports.

## 6. Exact integrity

`exact_integrity = VALID` means at least one profile-designated exact content binding matches the presented content under the specified normalization profile.

`exact_integrity = INVALID` means the presented content does not exactly match that binding. It does not invalidate a valid signature over the historical record and does not erase partial provenance.

## 7. Partial integrity and coverage

When segment/chunk evidence exists, a verifier SHOULD calculate authenticated coverage over a profile-defined denominator.

Coverage MUST identify only material that can be bound to authenticated provenance. It MUST NOT extrapolate from a small surviving fragment to the entire document.

If only 5% of a current document is authenticated to a source generation, the verifier MUST NOT label the whole document as an original output of that source.

## 8. Locator semantics

A watermark or locator can help recover a candidate RID or record reference. The following rule is normative:

> A recovered locator is never sufficient for actor or generation attribution.

Attribution requires at least a valid signed record and a sufficient content relationship under the relevant profile.

A locator transplanted into unrelated content SHOULD result in `LOCATOR_RECOVERED` plus failed/insufficient content binding, not a verified attribution.

## 9. Historical evidence

Historical evidence is evaluated independently from signature validity.

Examples:

- signed transparency checkpoint;
- inclusion/consistency proof;
- timestamp proof;
- witness quorum;
- blockchain or distributed-ledger anchor;
- hardware append-only log.

A record can have a valid provider signature and no historical evidence. In that case the verifier MUST report that distinction rather than failing the entire provenance record.

## 10. Lineage

A verifier MUST support multiple parents and detect obvious cycles in the provenance DAG.

A child event does not retroactively alter the validity of a parent record. Missing parents MAY reduce lineage assurance but MUST NOT automatically invalidate an otherwise valid signed child record.

## 11. Derived presentation labels

The following labels are RECOMMENDED for interoperable user interfaces.

### VERIFIED_ORIGINAL

Minimum conditions:

- record signature valid;
- actor authentication valid under the selected trust policy;
- exact content binding valid;
- no unresolved critical feature affects the claim.

Historical evidence and model assurance SHOULD be shown separately and are not implicitly upgraded by this label.

### VERIFIED_DERIVATIVE

Use when:

- a valid signed provenance path exists;
- the current content is not an exact match to the original source event;
- the current subject has a verified derivation relationship or substantial authenticated partial relationship.

### PARTIAL_PROVENANCE

Use when only part of the current content can be cryptographically or structurally bound to one or more valid provenance records.

The UI SHOULD show authenticated coverage when meaningful.

### LOCATOR_ONLY

Use when a recovery carrier or watermark indicates provenance material but authentication or content binding is insufficient or unavailable.

### UNVERIFIED

Use when GCPP cannot establish sufficient provenance.

Normative interpretation:

```text
UNVERIFIED != HUMAN
UNVERIFIED != FAKE
UNVERIFIED != ILLEGAL
UNVERIFIED != LOW_QUALITY
```

## 12. Truth separation

No GCPP label means that content is factually correct. UIs and APIs MUST keep provenance state separate from fact-checking, moderation, copyright, plagiarism, academic-integrity, or legal-status systems.

Normative interpretation:

```text
VERIFIED != TRUE
```

## 13. Local policy

Different applications MAY apply different trust policies to actor identity, acceptable algorithms, evidence age, or required historical assurance. The raw verification vector SHOULD remain available so that local policy does not masquerade as protocol fact.

## 14. Diagnostics

A verifier SHOULD provide machine-readable diagnostics for failures such as:

- malformed record;
- unsupported critical extension;
- invalid signature;
- unresolved actor key;
- exact content mismatch;
- insufficient partial coverage;
- ambiguous locator;
- broken lineage reference;
- stale/revoked verification key;
- historical evidence unavailable;
- evidence proof invalid.

Diagnostics MUST avoid declaring content fake solely because provenance verification failed.
