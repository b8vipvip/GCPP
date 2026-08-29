# GCPP 数据模型 0.1 / GCPP Data Model 0.1

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。协议结构名、字段名和 BCP 14 关键词保持英文原样。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror. Protocol structure names, field names, and BCP 14 keywords remain in English.

## 简体中文

状态：**Working Draft（工作草案）**

本文件定义 GCPP Core 使用的抽象数据模型，并有意不规定 JSON、CBOR、protobuf、ASN.1、区块链存储、HTTP 传输或任何其他物理表示。

### 1. 基础设计规则

所有协议对象 MUST 显式版本化，或通过版本化 Profile 解释。

用于 Event 和 Generation 的 Identifier SHOULD 是 opaque 且高熵的。它们 MUST NOT 编码用户账号、IP 地址、设备标识、地理位置或 Raw Prompt。

Algorithm Identifier、Identity Method、Evidence Scheme、Normalization Profile、Event Type 和 Carrier Type 使用由 Registry 管理的符号值或数值。

### 2. ActorIdentifier

```text
ActorIdentifier {
  method: RegistryID
  identifier: BytesOrString
}
```

`method` 定义如何解释 `identifier`，以及如何解析 Verification Material。Core 不要求 Online Resolution。

### 3. Event

```text
Event {
  id: OpaqueID
  type: RegistryID
  time?: TimeClaim
}
```

在得到提供更强时间保证的 Evidence Scheme 支持之前，`time` 仅是 Claim。

Generation Event SHOULD 使用 Generation-specific Opaque Identifier。其他 Transformation Event MAY 使用等价 Opaque Event Identifier。

### 4. Subject

```text
Subject {
  media_type: MediaType
  bindings: [ContentBinding, ...]
}
```

若一个经过认证的 Provenance Claim 要绑定到具体内容，Subject MUST 至少包含一个 Content Binding。

### 5. ContentBinding

```text
ContentBinding {
  binding_type: RegistryID
  algorithm: RegistryID
  normalization_profile: RegistryID
  value: Bytes
  parameters?: Map
}
```

`binding_type` 示例包括 Exact Digest、Normalized-Text Digest、Segment Commitment Set、Content-Defined Chunk Tree，或未来 Robust Integrity Construction。

同一 Subject MAY 对不同表示同时携带多个 Binding。

### 6. ModelClaim

```text
ModelClaim {
  public_model_id: String
  model_family?: String
  model_commitment?: Commitment
  extensions?: [Extension, ...]
}
```

`public_model_id` 是 Provider 的公开声明。`model_commitment` 可以在不泄露信息的情况下，对 Internal Model Build 或 Routing Information 作 Commitment。

仅存在 `ModelClaim` MUST NOT 被解释为 Execution Proof。

### 7. ParentReference

```text
ParentReference {
  event_id?: OpaqueID
  record_commitment?: Commitment
  relation_type: RegistryID
  subject_selector?: Selector
}
```

Record MAY 有零个或多个 Parent。实现 MUST 支持 Multiple Parent，以表示 Composition 和 Multi-source Transformation。

### 8. CarrierDescriptor

```text
CarrierDescriptor {
  carrier_type: RegistryID
  scheme: RegistryID
  locator?: BytesOrString
  parameters?: Map
}
```

Carrier 描述 Record 或 Recovery Locator 如何随内容一起存在或如何从内容恢复。Carrier Validity 不等于 Provenance Validity。

### 9. RecoveryLocator

```text
RecoveryLocator {
  scheme: RegistryID
  value: Bytes
  confidence?: Number
  fragments?: [Bytes, ...]
}
```

Recovery Locator 是 Discovery Material。它 MAY 解析到零个、一个或多个候选 Record。Verifier MUST 对候选 Record 进行独立认证。

### 10. Evidence

```text
Evidence {
  evidence_type: RegistryID
  scheme: RegistryID
  subject: EvidenceSubject
  proof: BytesOrStructuredValue
  parameters?: Map
}
```

`subject` 必须精确标识 Proof 覆盖的对象。Evidence Type 的注册 Scheme Specification MUST 定义 Canonical Verification Rules。

### 11. Extension

```text
Extension {
  id: RegistryID
  critical: Boolean
  value: StructuredValue
}
```

未知 non-critical Extension 在 Core Claim Evaluation 中被忽略，但必须被报告。未知 critical Extension 应使受影响 Claim 变为 `UNSUPPORTED`，而不是 `INVALID`，除非 Enclosing Profile 另有规定。

### 12. ProvenanceRecord

```text
ProvenanceRecord {
  version: Version
  event: Event
  actor: ActorIdentifier
  subject: Subject
  model_claim?: ModelClaim
  parents: [ParentReference, ...]
  carriers: [CarrierDescriptor, ...]
  evidence: [Evidence, ...]
  extensions: [Extension, ...]
}
```

Record 是逻辑 Claim Set。Deployment Profile 定义 Canonical Serialization 与 Signature Envelope。

### 13. SignedProvenance

```text
SignedProvenance {
  record: ProvenanceRecord
  signer: ActorIdentifier
  signature_scheme: RegistryID
  signature: Bytes
  signature_parameters?: Map
}
```

Signature Input MUST 是完整 Record 的 Profile-defined Canonical Encoding，加上任何要求的 Domain-Separation Context。

Profile MUST 无歧义地定义 Algorithm Substitution 和 Key-Identifier Behavior。

### 14. VerificationVector

```text
VerificationVector {
  actor_authentication
  record_signature
  model_assurance
  exact_integrity
  partial_integrity
  authenticated_coverage?
  locator_state
  lineage_state
  historical_evidence
  unsupported_critical_features[]
  diagnostics[]
}
```

每个字段独立评估。Presentation Label 从该结构派生；它们不是存放在 Record 中的权威“真相”。

### 15. Canonicalization 边界

Canonicalization 是安全关键部分。GCPP Core 有意将 Canonical Encoding 和 Media Normalization 留给 Profile，但每个 Profile MUST 精确定义，使两个符合规范的实现对相同 Logical Value 生成完全相同的 Signature Input 和 Content-Binding Input。

### 16. Media Normalization

Normalization Profile SHOULD 针对具体 Representation。文本 Profile 可以定义 Unicode Normalization、Line Ending、Whitespace Rule、Control Character Treatment 和 Markup Extraction。Binary Media 可以使用 Identity（Raw Bytes）或显式定义的 Canonical Representation。

Normalization MUST NOT 静默删除语义相关信息，除非 Profile 明确规定这一权衡。

### 17. 演进

新字段通常应通过 Registered Extension 或 Profile Update 引入。Core Object 的语义只有在 Major Protocol Revision 时才应改变。

---

# English

Status: **Working Draft**

This document defines the abstract data model used by GCPP Core. It deliberately does not prescribe JSON, CBOR, protobuf, ASN.1, blockchain storage, HTTP transport, or any other physical representation.

## 1. Primitive design rules

All protocol objects MUST be explicitly versioned or interpreted through a versioned profile.

Identifiers used for events and generations SHOULD be opaque and high entropy. They MUST NOT encode a user's account, IP address, device identifier, geographic location, or raw prompt.

Algorithm identifiers, identity methods, evidence schemes, normalization profiles, event types, and carrier types are registry-controlled symbolic or numeric values.

## 2. ActorIdentifier

```text
ActorIdentifier {
  method: RegistryID
  identifier: BytesOrString
}
```

The `method` defines how `identifier` is interpreted and how verification material is resolved. Core does not require online resolution.

## 3. Event

```text
Event {
  id: OpaqueID
  type: RegistryID
  time?: TimeClaim
}
```

`time` is a claim until supported by an evidence scheme that provides stronger temporal assurance.

A generation event SHOULD use a generation-specific opaque identifier. Other transformation events MAY use equivalent opaque event identifiers.

## 4. Subject

```text
Subject {
  media_type: MediaType
  bindings: [ContentBinding, ...]
}
```

A subject MUST contain at least one content binding for an authenticated provenance claim to bind to concrete content.

## 5. ContentBinding

```text
ContentBinding {
  binding_type: RegistryID
  algorithm: RegistryID
  normalization_profile: RegistryID
  value: Bytes
  parameters?: Map
}
```

Examples of `binding_type` include exact digest, normalized-text digest, segment commitment set, content-defined chunk tree, or a future robust integrity construction.

The same subject MAY carry multiple bindings over different representations.

## 6. ModelClaim

```text
ModelClaim {
  public_model_id: String
  model_family?: String
  model_commitment?: Commitment
  extensions?: [Extension, ...]
}
```

`public_model_id` is the provider's public declaration. `model_commitment` can commit to internal model build or routing information without revealing it.

Presence of `ModelClaim` alone MUST NOT be interpreted as execution proof.

## 7. ParentReference

```text
ParentReference {
  event_id?: OpaqueID
  record_commitment?: Commitment
  relation_type: RegistryID
  subject_selector?: Selector
}
```

A record MAY have zero or more parents. Implementations MUST support multiple parents so composition and multi-source transformations can be represented.

## 8. CarrierDescriptor

```text
CarrierDescriptor {
  carrier_type: RegistryID
  scheme: RegistryID
  locator?: BytesOrString
  parameters?: Map
}
```

A carrier identifies how the record or a recovery locator can accompany or be recovered from content. Carrier validity is not equivalent to provenance validity.

## 9. RecoveryLocator

```text
RecoveryLocator {
  scheme: RegistryID
  value: Bytes
  confidence?: Number
  fragments?: [Bytes, ...]
}
```

A recovery locator is discovery material. It MAY resolve to zero, one, or many candidate records. A verifier MUST authenticate candidate records separately.

## 10. Evidence

```text
Evidence {
  evidence_type: RegistryID
  scheme: RegistryID
  subject: EvidenceSubject
  proof: BytesOrStructuredValue
  parameters?: Map
}
```

`subject` identifies exactly what the proof covers. Evidence types MUST specify canonical verification rules in their registered scheme specifications.

## 11. Extension

```text
Extension {
  id: RegistryID
  critical: Boolean
  value: StructuredValue
}
```

Unknown non-critical extensions are ignored for Core claim evaluation but reported. Unknown critical extensions cause the affected claim to be `UNSUPPORTED` rather than `INVALID` unless the enclosing profile states otherwise.

## 12. ProvenanceRecord

```text
ProvenanceRecord {
  version: Version
  event: Event
  actor: ActorIdentifier
  subject: Subject
  model_claim?: ModelClaim
  parents: [ParentReference, ...]
  carriers: [CarrierDescriptor, ...]
  evidence: [Evidence, ...]
  extensions: [Extension, ...]
}
```

Records are logical claim sets. A deployment profile defines canonical serialization and signature envelopes.

## 13. SignedProvenance

```text
SignedProvenance {
  record: ProvenanceRecord
  signer: ActorIdentifier
  signature_scheme: RegistryID
  signature: Bytes
  signature_parameters?: Map
}
```

The signature input MUST be the profile-defined canonical encoding of the complete record plus any required domain-separation context.

Profiles MUST define algorithm substitution and key-identifier behavior unambiguously.

## 14. VerificationVector

```text
VerificationVector {
  actor_authentication
  record_signature
  model_assurance
  exact_integrity
  partial_integrity
  authenticated_coverage?
  locator_state
  lineage_state
  historical_evidence
  unsupported_critical_features[]
  diagnostics[]
}
```

Each field is independently evaluated. Presentation labels are derived from this structure; they are not stored as authoritative truth in the record.

## 15. Canonicalization boundary

Canonicalization is security-critical. GCPP Core deliberately keeps canonical encodings and media normalization in profiles, but every profile MUST define them precisely enough that two conforming implementations generate identical signature inputs and content-binding inputs for the same logical value.

## 16. Media normalization

Normalization profiles SHOULD be representation-specific. For text, profiles can define Unicode normalization, line-ending handling, whitespace rules, control-character treatment, and markup extraction. For binary media, normalization can be identity (raw bytes) or an explicitly defined canonical representation.

Normalization MUST NOT silently erase semantically relevant information unless the profile explicitly defines that tradeoff.

## 17. Evolution

New fields should normally be introduced as registered extensions or profile updates. Core object meaning should change only with a major protocol revision.
