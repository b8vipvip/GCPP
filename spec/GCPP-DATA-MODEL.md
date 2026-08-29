# GCPP Data Model 0.2 / GCPP 数据模型 0.2

> 状态 / Status: **Working Draft**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 设计原则

GCPP 0.2 不再把自身抽象对象默认实现成另一套独立 Manifest。抽象对象用于定义生成式语义；C2PA-based Internet Profile 应将这些对象映射为 C2PA Manifest/Assertion/Ingredient/Soft Binding 等现有结构。

## 2. GenerationEvent

```text
GenerationEvent {
  generation_id: OpaqueID
  actor: ActorIdentifier
  time?: TimeClaim
  model_claim?: ModelClaim
  parent_events[]
  extensions[]
}
```

`generation_id` SHOULD 高熵、不可从用户身份推导。

## 3. RecoveryLocator

```text
RecoveryLocator {
  scheme: RegistryID
  value: Bytes
  confidence?: Number
  fragments?: [Bytes, ...]
}
```

RID 是 discovery material，不是 authentication。C2PA Profile 中可映射到 soft-binding identifier 或 Manifest Repository lookup key。

## 4. PartialAttribution

```text
PartialAttribution {
  source_event
  subject_selector
  authenticated_coverage
  denominator_profile
  binding_evidence[]
}
```

它只描述当前资产中被证据支持的部分，不得把 unmatched material 归属给来源。

## 5. ModelClaim

```text
ModelClaim {
  public_model_id
  model_family?
  model_commitment?
  evidence[]
}
```

存在 `ModelClaim` 只表示声明。真正 assurance level 由 Verifier 根据证据计算。

## 6. ModelLineageClaim

```text
ModelLineageClaim {
  subject_model
  relation_type
  source_model_or_dataset?
  dataset_commitment?
  training_run_commitment?
  evidence[]
  disclosure_policy?
  extensions[]
}
```

常见 `relation_type`：

```text
trained-on
fine-tuned-from
teacher-distilled-from
synthetic-data-generated-by
reasoning-traces-generated-by
preference-optimized-from
unknown-influence
```

## 7. RegulatoryLabelEvidence

```text
RegulatoryLabelEvidence {
  jurisdiction_profile
  label_type
  provider_identifier?
  content_identifier?
  raw_or_normalized_fields?
  validation_state
}
```

例如中国 GB 45438 Adapter 可解析 `AIGC.Label`、`ContentProducer`、`ProduceID` 等字段，但这些字段不自动成为 C2PA Claim Signature。

## 8. EvidenceReference

```text
EvidenceReference {
  evidence_type
  scheme
  subject
  proof_or_reference
  assurance_scope
}
```

`assurance_scope` 必须明确证据针对：

```text
asset-origin
content-integrity
actor-identity
historical-existence
model-execution
model-lineage
regulatory-label
```

## 9. C2PA Mapping

C2PA-based Profile SHOULD 优先映射：

```text
GenerationEvent        -> C2PA assertion / action extension
Actor signature        -> C2PA Claim Signature
Exact content binding  -> C2PA Hard Binding
RecoveryLocator        -> C2PA Soft Binding identifier
Transformation parents -> C2PA Ingredients / relationships
Model claims           -> AI/ML-related assertion/profile
Model lineage          -> model credential / ingredient / GCPP assertion
```

GCPP 自身不要求独立序列化这些对象，除非某个非 C2PA Profile 明确需要。

## 10. VerificationVector

```text
VerificationVector {
  output_provenance
  actor_authentication
  record_signature
  exact_integrity
  partial_integrity
  authenticated_coverage?
  locator_state
  asset_lineage_state
  model_assurance
  model_lineage_assurance
  historical_evidence
  regulatory_label_state
  unsupported_critical_features[]
  diagnostics[]
}
```

## 11. 版本演进

新增算法、Carrier、身份、监管体系或 C2PA 版本适配通常应通过 Registry/Profile/Adapter 实现，不应轻易修改这些抽象语义。

---

# English

GCPP Data Model 0.2 defines abstract generative semantics rather than a competing manifest container. A C2PA-based Internet Profile should map generation events, actor signatures, hard/soft bindings, ingredients, model claims, and model-lineage assertions onto existing C2PA structures wherever possible.

The model adds first-class objects for `RecoveryLocator`, `PartialAttribution`, `ModelClaim`, `ModelLineageClaim`, and jurisdiction-specific `RegulatoryLabelEvidence`. Every evidence reference should state its assurance scope so asset provenance, actor identity, model execution, model lineage, and regulatory labeling are not conflated.
