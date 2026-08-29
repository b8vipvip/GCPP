# GCPP Core 0.1

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。BCP 14 规范关键词及协议标识符保持英文原样。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror. BCP 14 normative keywords and protocol identifiers remain in English.

## 简体中文

状态：**Working Draft（工作草案）**  
预期轨道：公开、与具体实现无关的来源标准。

### 1. 范围

GCPP 为可验证数字内容来源定义可互操作语义，标准化四个长期问题：

1. **Identity（身份）** — 哪个 Actor 作出了来源声明？
2. **Provenance（来源/演化）** — 哪些生成或转换事件产生了当前 Subject？
3. **Integrity（完整性/关联性）** — 当前 Subject 与这些事件绑定的内容之间是什么关系？
4. **Evidence（证据）** — 哪些可验证 Artifact 支持身份、事件、完整性和历史声明？

GCPP 不定义事实真伪、合法性、质量、作者政策、版权归属、内容审核结果，也不判断未验证内容是否由人类创作。

关键词 **MUST**、**MUST NOT**、**REQUIRED**、**SHALL**、**SHALL NOT**、**SHOULD**、**SHOULD NOT**、**RECOMMENDED**、**NOT RECOMMENDED**、**MAY** 和 **OPTIONAL** 仅在全部大写出现时，按 BCP 14 解释。

### 2. 架构不变量

符合 GCPP Core 的实现 MUST 保持以下不变量：

- `VERIFIED` provenance MUST NOT 被展示为事实为真的证明。
- `UNVERIFIED` provenance MUST NOT 被展示为内容由人类创作、虚假、违法、恶意或低质量的证明。
- Watermark 或可恢复 Locator MUST NOT 单独认证 Actor 或 Generation Event。
- Public provenance MUST NOT 强制要求用户账号 ID、IP 地址、设备 ID、邮箱、手机号或 Raw Prompt。
- Core verification MUST NOT 依赖一个全球特权在线验证服务。
- GCPP Core MUST 与任何单一存储系统、传输协议、身份系统、Hash Function、Signature Algorithm、Watermark Algorithm、Evidence Ledger、AI Architecture、Provider、Platform、Government 或 Jurisdiction 保持独立。
- Partial 和 Transformed provenance MUST 是一等状态；实现 MUST NOT 把所有结果压缩成 AI/non-AI 二元值。
- Policy Decision MUST 保持在 GCPP 密码学验证结果之外。

### 3. 分层模型

GCPP 分为五个逻辑层：

1. **Identity** — Actor、Identifier、Verification Method、Key History。
2. **Provenance** — Event 及其 Parent Relationship。
3. **Evidence** — Signature、Watermark、Transparency Proof、Timestamp、Attestation 以及未来 Proof Type。
4. **Verification** — 对可用 Claim 和 Evidence 的确定性评估。
5. **Presentation** — 从 Verification Vector 派生的人类可读标签。

数据库、区块链、Transparency Log、P2P Store、HTTP Endpoint、本地文件或云系统等物理基础设施均位于 GCPP Core 之外。

### 4. Actor

`Actor` 是作出来源声明的实体，例如 AI Provider、Organization、Human Author、Editing Application、Camera、Autonomous Agent 或 Hardware Device。

Actor 通过抽象 Identifier 标识：

```text
ActorIdentifier {
  method
  identifier
}
```

GCPP Core 不强制 DID、X.509、Domain Key、Raw Public Key 或任何未来身份方法。身份方法独立注册并版本化。

Verifier MUST 区分“对 Identifier 的密码学控制”与“现实法律实体或品牌身份声明”。

### 5. Provenance Event

`ProvenanceEvent` 表示一次被声明的内容状态转换。Event Type 来自 Registry，可包括生成、人工编辑、AI 重写、翻译、摘要、组合、渲染、转码、发布、采集或未来转换。

Event 构成 Directed Acyclic Graph（DAG）。MUST 支持多个 Parent。

每个 Event 都拥有 opaque event identifier。AI Generation Event SHOULD 使用高熵且不从用户信息推导的 `GenerationID`。

### 6. Generation Identity 与 Recovery Locator

`GenerationID` 标识一次被声明的生成事件。

`RecoveryLocator`（RID）是紧凑的 Discovery Value，MAY 被嵌入文本水印等 Robust Carrier。RID：

- MUST NOT 被视为认证；
- MAY 短于 GenerationID；
- MAY 是部分值或存在碰撞；
- MAY 解析到多个候选 Record；
- 在做归属判断前 MUST 继续执行 Signature 和 Content-Binding Verification。

这一分离避免短文本或低熵内容被迫承载完整密码学身份。

### 7. Provenance Record

GCPP 抽象记录包含：

```text
ProvenanceRecord {
  version
  event {
    id
    type
    time?
  }
  actor {
    identifier
  }
  subject {
    media_type
    bindings[]
  }
  model_claim?
  parents[]
  carriers[]
  evidence[]
  extensions[]
}
```

Serialization 由 Deployment Profile 定义，而不是 Core。Signature 对 Profile 定义的 Record Canonical Encoding 计算。

### 8. Model Claim

Model Claim 是声明，不自动等于 Model Execution Proof。

```text
ModelClaim {
  public_model_id
  model_family?
  model_commitment?
}
```

Verification MUST 至少区分：

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

Provider Signature 可以建立 `MODEL_DECLARED`。更强状态需要额外注册 Evidence，例如 Hardware Attestation 或 Verifiable Execution Proof。

### 9. Content Binding

Record MUST 能够绑定内容，但不能永久写死某一个 Hash Function 或表示形式。

```text
ContentBinding {
  binding_type
  algorithm
  normalization_profile
  value
}
```

Subject MAY 同时携带多个 Binding，例如 Raw Bytes、Normalized Visible Text、Structured Document Form 或 Chunk/Segment Commitment。

Exact Integrity 与 Partial Integrity 是不同概念。Full-Content Digest Mismatch MUST NOT 单独抹掉其他仍然有效的 Partial Provenance。

### 10. Evidence

Evidence 可扩展：

```text
Evidence {
  evidence_type
  scheme
  subject
  proof
  parameters?
}
```

Evidence Type 可以包括 Digital Signature、Watermark Recovery、Transparency Inclusion、Timestamp、Witness Proof、Blockchain Anchor、Hardware Attestation、Verifiable Credential、Execution Proof 或未来 Scheme。

GCPP Core 不偏好区块链或任何其他 Evidence Substrate。

### 11. Carrier

Carrier 用于传输 Provenance 或 Locator，例如 Embedded Manifest、Sidecar File、Custom Clipboard Format、Document Metadata、Robust Watermark、External Reference 或未来机制。

Carrier MUST NOT 与它承载的 Proof 混淆。即使 Record 通过不可信 Transport 获得，只要 Signature 和 Binding 有效，仍然可以完成验证。

### 12. Extension

Record MUST 支持 Extension。Extension 分为 critical 和 non-critical。

- 未知 non-critical Extension 在 Core Verification 中 MUST 被安全忽略，同时报告 unsupported。
- 未知 critical Extension MUST 使受影响 Claim 被报告为 unsupported，而不是 fake。

### 13. 隐私

Public GCPP Record SHOULD 最小化可关联信息。Generation Identifier SHOULD 在不同用户和 Session 之间不可关联。Raw Prompt 和 User Account Identifier 不属于公共来源必需信息，Core MUST NOT 强制要求它们。

如果企业或审计场景必须绑定输入，Profile SHOULD 使用 salted/randomized commitment 和 selective disclosure，而不是公开 Raw Prompt 或稳定 User Identifier。

### 14. 历史与修正

GCPP 倾向 append-only correction，而不是 silent history rewriting。Revocation、Key Compromise、Supersession 或 Corrected Claim SHOULD 通过额外 Record/Evidence 表达，并保留原始 Record。

### 15. Verification Output

Core Verification 产生结构化 Vector，而不是一个 Boolean。至少报告：

- actor authentication state；
- record signature state；
- model assurance state；
- exact integrity state；
- 可用时的 partial integrity/coverage state；
- locator/watermark state；
- lineage state；
- historical evidence state；
- unsupported critical features。

`VERIFIED_ORIGINAL`、`VERIFIED_DERIVATIVE`、`PARTIAL_PROVENANCE`、`LOCATOR_ONLY` 和 `UNVERIFIED` 等 Presentation Label 根据 GCPP-VERIFY 从该 Vector 派生。

### 16. 协议独立性

任何符合 GCPP Core 的规范都不得把某个具名区块链、Provider Registry、Centralized Resolver、Watermark Algorithm 或 Model Architecture 作为永久协议依赖。

可替换机制属于 Registry 和 Profile。只有当 provenance 本身的语义必须改变时，才应修改 Core Semantics。

---

# English

Status: **Working Draft**  
Intended track: public, implementation-agnostic provenance standard.

## 1. Scope

GCPP defines interoperable semantics for verifiable digital-content provenance. It standardizes four durable questions:

1. **Identity** — which actor made a provenance claim?
2. **Provenance** — which generation or transformation events produced the current subject?
3. **Integrity** — how does the current subject relate to the content bound by those events?
4. **Evidence** — which verifiable artifacts support the identity, event, integrity, and history claims?

GCPP does not define factual truth, legality, quality, authorship policy, copyright ownership, moderation outcomes, or whether unverified content is human-created.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described by BCP 14 when, and only when, they appear in all capitals.

## 2. Architectural invariants

A conforming GCPP Core implementation MUST preserve these invariants:

- `VERIFIED` provenance MUST NOT be presented as factual truth.
- `UNVERIFIED` provenance MUST NOT be presented as proof that content is human, fake, illegal, malicious, or low quality.
- A watermark or recoverable locator MUST NOT by itself authenticate an actor or generation event.
- Public provenance MUST NOT require a user account identifier, IP address, device identifier, email address, phone number, or raw prompt.
- Core verification MUST NOT require one globally privileged online verification service.
- GCPP Core MUST remain independent of any single storage system, transport protocol, identity system, hash function, signature algorithm, watermark algorithm, evidence ledger, AI architecture, provider, platform, government, or jurisdiction.
- Partial and transformed provenance MUST be first-class states; implementations MUST NOT collapse every result to an AI/non-AI boolean.
- Policy decisions MUST remain outside the GCPP cryptographic verification result.

## 3. Layer model

GCPP separates five logical layers:

1. **Identity** — actors, identifiers, verification methods, key history.
2. **Provenance** — events and their parent relationships.
3. **Evidence** — signatures, watermarks, transparency proofs, timestamps, attestations, and future proof types.
4. **Verification** — deterministic evaluation of the available claims and evidence.
5. **Presentation** — human-readable labels derived from the verification vector.

Physical infrastructure such as databases, blockchains, transparency logs, P2P stores, HTTP endpoints, local files, or cloud systems is outside GCPP Core.

## 4. Actor

An `Actor` is an entity that makes a provenance claim. Examples include an AI provider, organization, human author, editing application, camera, autonomous agent, or hardware device.

An actor is identified by an abstract identifier:

```text
ActorIdentifier {
  method
  identifier
}
```

GCPP Core does not mandate DID, X.509, domain keys, raw public keys, or any future identity method. Identity methods are registered and versioned independently.

A verifier MUST distinguish cryptographic control of an identifier from claims about a real-world legal or brand identity.

## 5. Provenance event

A `ProvenanceEvent` represents one asserted content-state transition. Event types are registry values and can include generation, human edit, AI rewrite, translation, summarization, composition, rendering, transcoding, publication, capture, or future transformations.

Events form a directed acyclic graph (DAG). Multiple parents MUST be supported.

Each event has an opaque event identifier. AI generation events SHOULD use a high-entropy, non-user-derived `GenerationID`.

## 6. Generation identity and recovery locator

A `GenerationID` identifies one asserted generation event.

A `RecoveryLocator` (RID) is a compact discovery value that MAY be embedded in a robust carrier such as a text watermark. The RID:

- MUST NOT be treated as authentication;
- MAY be shorter than the GenerationID;
- MAY be partial or collision-prone;
- MAY resolve to multiple candidate records;
- MUST be followed by signature and content-binding verification before attribution.

This separation prevents short or low-entropy content from being forced to carry a complete cryptographic identity.

## 7. Provenance record

The abstract GCPP record contains:

```text
ProvenanceRecord {
  version
  event {
    id
    type
    time?
  }
  actor {
    identifier
  }
  subject {
    media_type
    bindings[]
  }
  model_claim?
  parents[]
  carriers[]
  evidence[]
  extensions[]
}
```

Serialization is defined by deployment profiles, not by Core. A signature is computed over a profile-defined canonical encoding of the record.

## 8. Model claim

A model claim is an assertion, not automatically a proof of model execution.

```text
ModelClaim {
  public_model_id
  model_family?
  model_commitment?
}
```

Verification MUST distinguish at least:

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

A provider signature can establish `MODEL_DECLARED`. Stronger states require additional registered evidence such as hardware attestation or verifiable execution proof.

## 9. Content binding

A record MUST be able to bind to content without hard-coding a single hash function or representation.

```text
ContentBinding {
  binding_type
  algorithm
  normalization_profile
  value
}
```

A subject MAY carry multiple bindings, for example raw bytes, normalized visible text, structured document form, or chunk/segment commitments.

Exact and partial integrity are distinct concepts. Full-content digest mismatch MUST NOT by itself erase otherwise valid partial provenance.

## 10. Evidence

Evidence is extensible:

```text
Evidence {
  evidence_type
  scheme
  subject
  proof
  parameters?
}
```

Evidence types can include digital signatures, watermark recovery, transparency inclusion, timestamps, witness proofs, blockchain anchors, hardware attestation, verifiable credentials, execution proofs, or future schemes.

GCPP Core does not privilege blockchain or any other evidence substrate.

## 11. Carriers

A carrier transports provenance or a locator. Examples include embedded manifests, sidecar files, custom clipboard formats, document metadata, robust watermarks, external references, and future mechanisms.

A carrier MUST NOT be confused with the proof it transports. A record obtained through an untrusted transport can still verify if its signatures and bindings are valid.

## 12. Extensions

Records MUST support extensions. Extensions are either critical or non-critical.

- Unknown non-critical extensions MUST be safely ignored for Core verification while being reported as unsupported.
- Unknown critical extensions MUST cause the affected claim to be reported as unsupported, not fake.

## 13. Privacy

Public GCPP records SHOULD minimize correlatable information. Generation identifiers SHOULD be unlinkable across users and sessions. Raw prompts and user-account identifiers are out of scope for public provenance and MUST NOT be required by Core.

If an input must be bound for enterprise or audit use, profiles SHOULD use salted or randomized commitments and selective disclosure rather than publishing raw prompts or stable user identifiers.

## 14. History and correction

GCPP favors append-only correction over silent history rewriting. Revocation, key compromise, supersession, or corrected claims SHOULD be represented by additional records or evidence that preserve the original record.

## 15. Verification output

Core verification produces a structured vector rather than one boolean. At minimum it reports:

- actor authentication state;
- record signature state;
- model assurance state;
- exact integrity state;
- partial integrity/coverage state when available;
- locator/watermark state;
- lineage state;
- historical evidence state;
- unsupported critical features.

Presentation labels such as `VERIFIED_ORIGINAL`, `VERIFIED_DERIVATIVE`, `PARTIAL_PROVENANCE`, `LOCATOR_ONLY`, and `UNVERIFIED` are derived from that vector according to GCPP-VERIFY.

## 16. Protocol independence

No conforming GCPP Core specification may require one named blockchain, one named provider registry, one centralized resolver, one watermark algorithm, or one model architecture as a permanent protocol dependency.

Replaceable mechanisms belong in registries and profiles. Core semantics change only when the meaning of provenance itself must change.
