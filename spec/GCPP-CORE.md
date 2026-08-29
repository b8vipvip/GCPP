# GCPP Core 0.2 / GCPP 核心规范 0.2

> 状态 / Status: **Working Draft**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. Scope / 范围

GCPP 0.2 将自己定位为**生成式内容专用的 provenance profile/extension 语义层**，而不是重新定义一套与 C2PA 平行的通用 Content Credentials 容器。

GCPP 标准化四个长期问题：

1. **Identity** — 谁作出了来源或训练血缘声明？
2. **Provenance** — 哪些生成、转换、训练或蒸馏事件产生了当前内容或模型？
3. **Integrity** — 当前对象与声明绑定对象还保持怎样的可验证关系？
4. **Evidence** — 什么证据支持这些声明？

同时把两个来源域明确分离：

```text
OUTPUT_PROVENANCE
MODEL_LINEAGE
```

前者处理具体内容资产；后者处理模型训练、蒸馏、synthetic-data 与祖先模型关系。

## 2. 与 C2PA 的关系

GCPP **SHOULD** 优先复用 C2PA 已有能力，包括 Manifest、Claim Signature、Hard Binding、Soft Binding、Actions、Ingredients、Manifest Repository 与 Durable Content Credentials。

GCPP 不应重复定义另一套通用 Manifest/Claim 格式。

具体 Internet Profile **MAY** 选择某个 C2PA 2.x 版本作为当前承载与签名基础；GCPP Core 语义本身仍保持版本和实现无关。

详见 `GCPP-C2PA-ALIGNMENT.md`。

## 3. Architectural invariants / 架构不变量

符合 GCPP Core 的实现 **MUST** 保持：

- `VERIFIED` provenance **MUST NOT** 被呈现为事实真实性；
- `UNVERIFIED` **MUST NOT** 被呈现为 Human/Fake/Illegal/Low Quality 的证明；
- watermark/RID **MUST NOT** 单独完成 Actor 或 Generation authentication；
- `MODEL_DECLARED` **MUST NOT** 自动升级为 `MODEL_EXECUTION_PROVEN`；
- `OUTPUT_PROVENANCE` **MUST NOT** 自动被解释成 `MODEL_LINEAGE`；
- Public provenance **MUST NOT** 要求用户账号、IP、设备 ID、手机号、邮箱或 raw prompt；
- Core verification **MUST NOT** 依赖单一全球在线 verifier；
- partial/transformed provenance **MUST** 是一等状态；
- 政策、法律、版权、作弊、真实性判断 **MUST** 位于协议事实层之外；
- C2PA、GB 45438、DID、X.509、Hash、水印、区块链、Transparency Log 等均属于可替换 Profile/Adapter/Evidence，而非永恒 Core 假设。

## 4. Layer model / 层模型

```text
Presentation
Verification
Evidence
Provenance
Identity
```

对于生成式 AI，再增加两个正交来源域：

```text
Asset / Output Provenance
Model / Training Lineage
```

## 5. Actor

```text
ActorIdentifier {
  method
  identifier
}
```

Actor 可以是 AI Provider、模型、Organization、Human、Software、Camera、Agent、Hardware Device 等。

Core 不绑定 DID、X.509、domain key 或 raw key。C2PA Trust List/X.509 可以作为当前 Internet Profile 的重要实现。

## 6. Provenance Event

`ProvenanceEvent` 表示一个声明的状态变化，例如：

```text
generate
capture
human-edit
ai-rewrite
translate
summarize
compose
render
transcode
publish
```

事件形成 DAG，并支持多个 parent。

## 7. GenerationID 与 RecoveryLocator

`GenerationID`（GID）是一次具体生成事件的权威标识。

`RecoveryLocator`（RID）是用于在 metadata/Manifest 丢失后发现候选 provenance record/manifest 的短 locator。

RID：

- **MUST NOT** 被当作 authentication；
- **MAY** 比 GID 短；
- **MAY** 碰撞或只恢复一部分；
- **MAY** 映射到 C2PA Soft Binding identifier；
- 必须经过签名与 content binding 验证才能归属。

## 8. Content binding

GCPP 自身不重新发明 C2PA hard/soft binding。对于 C2PA 承载 Profile：

- exact integrity 优先映射到 C2PA Hard Binding；
- durable recovery 优先映射到 C2PA Soft Binding；
- GCPP 可补充 partial authenticated coverage 与 generative text normalization/segmentation semantics。

## 9. Model assurance

GCPP 保留：

```text
MODEL_NONE
MODEL_DECLARED
MODEL_ATTESTED
MODEL_EXECUTION_PROVEN
```

普通 Provider signature 最多直接建立 `MODEL_DECLARED`。更强状态需要额外 attestation 或 verifiable execution evidence。

## 10. Model lineage

模型训练血缘必须与输出来源独立验证。

建议状态：

```text
LINEAGE_NONE
LINEAGE_DECLARED
LINEAGE_DATASET_COMMITTED
LINEAGE_TEACHER_ATTESTED
LINEAGE_WATERMARK_INDICATED
LINEAGE_INDEPENDENTLY_VERIFIED
```

详见 `GCPP-MODEL-LINEAGE.md`。

## 11. Evidence

Evidence 可以包括：

- C2PA Claim Signature；
- Hard/Soft Binding；
- watermark locator；
- timestamp/transparency/witness；
- hardware attestation；
- VC/identity evidence；
- model execution proof；
- dataset commitment；
- distillation-resistant watermark indication；
- future evidence。

Evidence 必须声明它证明的**对象和保证级别**。

## 12. Chinese regulatory adapter

中国 GB 45438—2025 `AIGC` metadata 与显式 AI 标识属于 regulatory labeling evidence，不等同 C2PA cryptographic provenance。

GCPP 应通过 Adapter 同时支持：

```text
GB45438 regulatory label
C2PA cryptographic provenance
GCPP generative semantics
```

而不是把三者压成一个真假字段。

## 13. Verification output

Verifier 输出至少分开：

```text
output_provenance
actor_authentication
record_signature
exact_integrity
partial_integrity
authenticated_coverage
locator_state
model_assurance
model_lineage_assurance
historical_evidence
regulatory_label_state
```

Presentation label 只是对上述向量的映射，不是权威真相。

## 14. Protocol independence

GCPP 0.2 的现实部署应与 C2PA 兼容，但长期 Core 语义不得依赖某个单一外部组织、算法、账本、模型架构或国家监管体系永久存在。

---

# English

## Scope

GCPP 0.2 is a **generative-content provenance profile/extension semantic layer**, not a new universal Content Credentials container parallel to C2PA.

It preserves four durable abstractions—Identity, Provenance, Integrity, and Evidence—and explicitly separates `OUTPUT_PROVENANCE` from `MODEL_LINEAGE`.

## C2PA relationship

GCPP **SHOULD** reuse C2PA manifests, signed claims, hard/soft bindings, actions, ingredients, manifest repositories, and Durable Content Credentials. A deployment profile **MAY** select a C2PA 2.x version as the contemporary carriage layer without making that version an eternal Core assumption.

## Key invariants

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
OUTPUT_PROVENANCE != MODEL_LINEAGE
```

## Model lineage

GCPP introduces a distinct model-lineage assurance dimension for training, distillation, synthetic-data generation, teacher models, dataset commitments, and related evidence. Asset credentials do not automatically prove training lineage.
