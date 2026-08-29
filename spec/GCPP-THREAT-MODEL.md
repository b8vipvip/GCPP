# GCPP 威胁模型 0.1 / GCPP Threat Model 0.1

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。协议状态码及 BCP 14 关键词保持英文原样。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror. Protocol state codes and BCP 14 keywords remain in English.

## 简体中文

状态：**Working Draft（工作草案）**

本威胁模型定义 GCPP 计划检测、抵抗或准确表达的攻击，同时明确协议无法保证的内容。

### 1. 安全目标

GCPP 的目标是提高以下攻击的难度：

- 伪造来源声明，使其看起来像由另一个 Actor 签名；
- 把真实 Locator 或 Identifier 移植到无关内容，并让它错误认证整个 Subject；
- 在存在独立 Historical Evidence 时，无痕重写已认证的 Provenance History；
- 当 Robust Carrier 仍然存活时，仅通过普通格式转换就删除全部 Provenance；
- 把 Partial Provenance 混淆成 Whole-Document Provenance；
- 把 Provider 的 Model Declaration 混淆成独立证明的 Model Execution；
- 把缺少 Provenance 错误解释为内容虚假或人类创作的证明。

### 2. 非目标

GCPP 不保证：

- 内容事实正确；
- 检测所有 AI 生成内容；
- 在任意重写、翻译、重新生成、人工重新表达或破坏性编辑后仍保留 Provenance；
- 阻止 Provider 故意对其内部模型执行作出虚假 Signed Claim；
- 对自然人作法律归属；
- 对已经公开的内容继续保密；
- 执行平台政策或国家政策。

### 3. 对手类别

#### 3.1 Content Editor

可以 Copy、Paste、Normalize、Reformat、Delete、Insert、Reorder、Paraphrase、Translate 或部分重写内容。

#### 3.2 Provenance Stripper

故意删除 Metadata、Sidecar、Hidden Unicode、Custom Clipboard MIME Type、Manifest 或已知 Watermark Carrier。

#### 3.3 Locator Transplanter

把有效 RID、Watermark Pattern、Manifest Reference 或 Provenance Fragment 复制到无关内容。

#### 3.4 Signature Forger

在不拥有签名 Key 的情况下，尝试创建看起来由 Provider/Actor 签名的 Record。

#### 3.5 Watermark Learner

反复查询 Provider 以推断 Watermark Behavior，然后尝试 Scrub 或 Spoof。

#### 3.6 Malicious or Compromised Provider

控制合法 Signing Key，可以签署误导性 Model Declaration 或省略 Transparency Publication。

#### 3.7 Key Thief

获得合法 Actor Signing Key，并在 Revocation 或 Compromise 被识别前签署欺诈 Record。

#### 3.8 History Rewriter

在发布后尝试删除或替换早期 Provenance Record/Checkpoint。

#### 3.9 Resolver Attacker

控制用于获取 Candidate Provenance Record 的 Server、Cache、CDN、P2P Node 或 Index。

#### 3.10 Policy Manipulator

利用有效协议输出作出协议不支持的推断，例如 `UNVERIFIED = FAKE` 或 `VERIFIED = TRUE`。

### 4. Core 防御

#### Signature Forgery

防御：使用可替换、已注册的 Signature Scheme 进行 Cryptographic Record Signature，并定义明确的 Key Lifecycle Semantics。

预期结果：Signature Invalid，不进行可信归属。

#### Locator Transplant

防御：Locator 仅用于 Discovery；归属还要求 Signed Record Verification 和 Content Binding/Coverage。

预期结果：`LOCATOR_RECOVERED`，但 Integrity Failed/Insufficient，不认证来源。

#### Partial-Copy Inflation

防御：Partial Coverage 是一等状态，MUST NOT 外推至整个当前 Subject。

预期结果：在支持的情况下输出带 Authenticated Coverage 的 `PARTIAL_PROVENANCE`。

#### Metadata Stripping

防御：多个独立 Carrier MAY 共存。Text Profile 可以在 Metadata、Sidecar、Clipboard Payload 之外加入 Robust In-Band Locator。

预期结果：Provenance 可以从 Attached Proof 平滑降级到 Locator Recovery，而不是二元失败。

#### Arbitrary Rewrite

一般情况下无法保证防御。如果所有承载 Provenance 的信息都被删除，GCPP 报告 `UNVERIFIED`。

#### Resolver Tampering

防御：获取到的 Record 不因 Transport 而可信；Signature 和 Evidence 在本地验证。

预期结果：恶意 Resolver 可以拒绝服务，但不能创建合法 Provider Signature。

#### Historical Rewriting

防御：可选的 Append-Only Evidence、Transparency Log、Witness System、Timestamp、Blockchain 或未来 Evidence System。

预期结果：History Assurance 作为独立维度报告；缺少 History Evidence 不自动使有效 Signature 失效。

#### Watermark Spoofing

防御：Watermark 和 RID 不认证 Identity。强归属来自 Signed Record + Content Binding。

#### Provider False Declaration

防御：普通 Provider Signature 证明 Provider 作出了声明，而不是证明其内部执行声明一定真实。更强 Model Assurance 需要可选 Attestation 或 Verifiable-Execution Evidence。

预期结果：`MODEL_DECLARED`，而不是 `MODEL_EXECUTION_PROVEN`。

#### Key Compromise

防御：Identity Profile 必须支持 Key Rotation、Revocation/Compromise Status 和 Historical Key Validation。Correction 应尽量使用 Append-Only 方式。

### 5. 隐私威胁

#### Cross-Generation User Tracking

稳定的 per-user 或 per-device Provenance Identifier 可能变成 Tracking Primitive。因此 GCPP Identifier MUST NOT 强制嵌入 User Identity，并且 SHOULD 在不同 Generation Event 之间不可关联。

#### Prompt Guessing

公开低熵 Prompt 的 Deterministic Hash 可能通过 Dictionary Attack 泄露信息。因此 Public Prompt Binding 不是必需项；需要时应使用 Randomized Commitment。

#### Permanent Public Personal Data

Append-Only 或 Blockchain Evidence 可能让误公开的个人数据很难甚至无法删除。Profile SHOULD Anchor Commitment，而不是 Raw User Data 或 Raw Content。

### 6. 可用性威胁

不假设任何 Online Resolver、Provider Endpoint、Log 或 Chain 永久存在。因此 GCPP 支持 Self-Contained Proof Bundle、Sidecar、Cached Record、Independent Mirror 和 Multiple Evidence System。

Availability Failure MUST 与 Cryptographic Invalidity 分开表达。

### 7. Algorithm Agility 威胁

Hash、Signature、Identity、Watermark 和 Evidence Algorithm 都可能过时。Registry 和 Profile MUST 支持 Deprecation 和 Migration，而不改变 Core Provenance Semantics。

Historical Verification Software SHOULD 保留长期验证所需的 Algorithm Identifier 和 Verification Material。

### 8. 内容类型限制

极短文本、Deterministic Code、Formula、JSON、Fixed-Format Output 和 Low-Entropy Generation 可能没有足够自由度进行 Robust In-Band Watermark，而不损害正确性。

Profile MUST 允许声明 Locator Capacity 很低或为零，并 fallback 到 Attached/Sidecar Proof。

### 9. 防止语义过度推断

协议的 Presentation Vocabulary 本身属于安全模型。即使密码学正确，把 `UNVERIFIED` 展示为 `FAKE`，或把 `VERIFIED` 展示为 `TRUE`，也会产生 Policy-Level Spoofing Vulnerability。

Conformance Testing SHOULD 除密码学向量外，也覆盖 UI/API 语义误用测试。

### 10. 残余风险

GCPP 提高 Provenance Forgery 成本，并显式呈现 Evidence Quality。它不能让信息不可摧毁，不能仅从密码学证明现实真相，也不能强迫不参与协议的软件或本地开源模型输出 Provenance。

目标结果是渐进式 Assurance：Exact、Derivative、Partial、Locator-Only 或 Unverified，而不是不可能实现的“通用永久追踪”。

---

# English

Status: **Working Draft**

This threat model defines the attacks GCPP intends to detect, resist, or represent accurately. It also states what the protocol cannot guarantee.

## 1. Security goals

GCPP aims to make it difficult to:

- forge a provenance claim as if signed by another actor;
- transplant a real locator or identifier into unrelated content and have it authenticate the whole subject;
- silently rewrite authenticated provenance history when independent historical evidence exists;
- erase all provenance through ordinary format conversion when a robust carrier survives;
- confuse partial provenance with whole-document provenance;
- confuse provider model declarations with independently proven model execution;
- turn absence of provenance into proof of falsity or human authorship.

## 2. Non-goals

GCPP does not guarantee:

- factual correctness of content;
- universal detection of all AI-generated content;
- survival of provenance after arbitrary rewriting, translation, re-generation, manual re-expression, or destructive editing;
- prevention of a provider intentionally making a false signed claim about its own internal model execution;
- legal attribution to a natural person;
- secrecy of content that is already public;
- enforcement of platform or national policy.

## 3. Adversary classes

### 3.1 Content editor

Can copy, paste, normalize, reformat, delete, insert, reorder, paraphrase, translate, or partially rewrite content.

### 3.2 Provenance stripper

Intentionally removes metadata, sidecars, hidden Unicode, custom clipboard MIME types, manifests, or known watermark carriers.

### 3.3 Locator transplanter

Copies a valid RID, watermark pattern, manifest reference, or provenance fragment into unrelated content.

### 3.4 Signature forger

Attempts to create a record that appears signed by a provider or actor without possession of its signing key.

### 3.5 Watermark learner

Queries a provider repeatedly to infer watermark behavior, then attempts to scrub or spoof it.

### 3.6 Malicious or compromised provider

Controls legitimate signing keys and can sign misleading model declarations or omit transparency publication.

### 3.7 Key thief

Obtains a legitimate actor signing key and signs fraudulent records until revocation or compromise is recognized.

### 3.8 History rewriter

Attempts to delete or replace earlier provenance records or checkpoints after publication.

### 3.9 Resolver attacker

Controls a server, cache, CDN, P2P node, or index used to retrieve candidate provenance records.

### 3.10 Policy manipulator

Uses valid protocol outputs to make unsupported claims such as `UNVERIFIED = FAKE` or `VERIFIED = TRUE`.

## 4. Core defenses

### Signature forgery

Defense: cryptographic record signatures with replaceable registered schemes and explicit key lifecycle semantics.

Expected result: invalid signature, not trusted attribution.

### Locator transplant

Defense: locator is discovery-only; attribution additionally requires signed record verification plus content binding/coverage.

Expected result: `LOCATOR_RECOVERED` with failed or insufficient integrity, not verified origin.

### Partial-copy inflation

Defense: partial coverage is first-class and MUST NOT be extrapolated to the entire current subject.

Expected result: `PARTIAL_PROVENANCE` with measured authenticated coverage where supported.

### Metadata stripping

Defense: multiple independent carriers MAY coexist. Text profiles can include a robust in-band locator in addition to metadata, sidecars, or clipboard payloads.

Expected result: provenance can degrade gracefully from attached proof to locator recovery instead of binary failure.

### Arbitrary rewrite

Defense: none can be guaranteed in the general case. If all information carrying provenance is removed, GCPP reports `UNVERIFIED`.

### Resolver tampering

Defense: retrieved records are not trusted based on transport. Signatures and evidence are verified locally.

Expected result: a malicious resolver can deny availability but cannot create valid provider signatures.

### Historical rewriting

Defense: optional append-only evidence, transparency logs, witness systems, timestamps, blockchains, or future evidence systems.

Expected result: history assurance is reported as a distinct dimension; lack of history evidence does not invalidate an otherwise valid signature.

### Watermark spoofing

Defense: watermarks and RIDs do not authenticate identity. Strong attribution comes from signed records and content binding.

### Provider false declaration

Defense: a normal provider signature proves the provider made the declaration, not that the declaration about internal execution is true. Stronger model assurance requires optional attestation or verifiable-execution evidence.

Expected result: `MODEL_DECLARED`, not `MODEL_EXECUTION_PROVEN`.

### Key compromise

Defense: identity profiles must support key rotation, revocation/compromise status, and historical key validation. Corrections should be append-only where possible.

## 5. Privacy threats

### Cross-generation user tracking

A stable per-user or per-device provenance identifier could become a tracking primitive. GCPP identifiers therefore MUST NOT require embedded user identity and SHOULD be unlinkable across generation events.

### Prompt guessing

Publishing deterministic hashes of low-entropy prompts can leak information through dictionary attacks. Public prompt bindings are therefore not required and should use randomized commitments when needed.

### Permanent public personal data

Append-only or blockchain evidence can make accidental personal-data publication difficult or impossible to remove. Profiles SHOULD anchor commitments rather than raw user data or raw content.

## 6. Availability threats

No online resolver, provider endpoint, log, or chain is assumed immortal. GCPP therefore supports self-contained proof bundles, sidecars, cached records, independent mirrors, and multiple evidence systems.

Availability failure MUST be represented separately from cryptographic invalidity.

## 7. Algorithm agility threats

Hash, signature, identity, watermark, and evidence algorithms can become obsolete. Registries and profiles MUST support deprecation and migration without changing Core provenance semantics.

Historical verification software SHOULD preserve algorithm identifiers and verification material needed for long-term validation.

## 8. Content-specific limits

Very short text, deterministic code, formulas, JSON, fixed-format outputs, and low-entropy generation may not have enough freedom for robust in-band watermarking without harming correctness.

Profiles MUST be allowed to declare low or zero locator capacity and fall back to attached/sidecar proof.

## 9. Safety against semantic overclaim

The protocol's presentation vocabulary is part of the security model. Implementations that turn `UNVERIFIED` into `FAKE`, or `VERIFIED` into `TRUE`, create a policy-level spoofing vulnerability even when cryptography is correct.

Conformance testing SHOULD include UI/API semantic misuse tests in addition to cryptographic vectors.

## 10. Residual risk

GCPP raises the cost of provenance forgery and makes evidence quality explicit. It cannot make information indestructible, cannot prove reality from cryptography alone, and cannot force non-participating software or local open-source models to emit provenance.

The intended outcome is graceful assurance: exact, derivative, partial, locator-only, or unverified — not an impossible promise of universal permanent tracking.
