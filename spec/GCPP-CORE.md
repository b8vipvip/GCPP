# GCPP Core 0.2 / GCPP 核心规范 0.2

> 状态 / Status: **Working Draft — Fundamental Architecture Review**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. Scope / 范围

GCPP Core 当前处于第一性原理架构复审阶段。

GCPP 不再把自己定义为“围绕 C2PA 缺口增加生成式 assertion 的扩展集合”，也不以追赶或抢先 C2PA、SPDX、CycloneDX 等标准的功能开发为目标。

当前研究目标是寻找一组能够长期表达以下问题的最小公共协议语义：

> 信息经过生成、传播、编辑、组合、转换、训练、蒸馏和再生成后，哪些来源关系仍然存在，哪些关系能够被验证，以及每份证据究竟证明什么。

详见：

- `../research/FUNDAMENTAL-PROTOCOL-RESEARCH.md`
- `GCPP-ARCHITECTURAL-PRINCIPLES.md`

## 2. 当前 Core 研究假设

此前 0.2 使用：

```text
Identity
Provenance
Integrity
Evidence
```

作为长期抽象。

在下一阶段，这组抽象将与以下研究模型进行比较：

```text
Entity
Relation
Continuity
Evidence
```

目前 **两组模型都未因本次文档更新而被宣告为最终 0.3 Core**。

研究需要回答：

- `Identity` 是否应成为 Entity 的一种可验证属性；
- `Provenance` 是否更准确地表示为 evidence-backed relation graph；
- `Integrity` 是否只能描述 exact binding，还是应升级为更一般的 Continuity；
- `Evidence` 如何明确自己的 capability 与 limitation。

## 3. 第一性原理研发纪律

GCPP Core 候选 **MUST NOT** 仅因为以下理由被标准化：

- 某个外部标准当前没有该字段；
- 某个厂商还没实现该功能；
- GCPP 可以更早发布；
- GCPP 可以拥有更多 assertion。

候选原语应首先证明：

1. 它解决真实、长期、跨实现的问题；
2. 即使底层标准和算法被替换，它仍有意义；
3. 即使其他标准未来增加相似表示，它仍有独立语义价值；
4. 至少存在两类不同 Evidence 技术可以支持它；
5. 它不把事实与政策/法律结论混合。

## 4. 与现有标准的关系

GCPP **SHOULD** 复用成熟标准已经能够表达的事实，但“复用”是互操作策略，不是研究问题的来源。

当前可用的实现层包括但不限于：

```text
C2PA
SPDX
CycloneDX
VC / DID / X.509
in-toto / attestations
SCITT / transparency systems
regulatory labeling systems
```

GCPP Core 不重新定义第二套通用 Manifest、AI BOM、身份凭证、透明日志或监管标签格式。

具体 Profile **MAY** 选择某个标准版本作为当代承载层，但 Core 语义不得因此永久依赖该标准。

## 5. Evidence-backed relation graph

真实来源应被假设为图，而非只有一个 parent 的版本链。

研究模型：

```text
Entity A --Relation R1 / Evidence E1--> Entity X
Entity B --Relation R2 / Evidence E2--> Entity X
Entity C --Relation R3 / Evidence E3--> Entity X
Entity X --Relation R4 / Evidence E4--> Entity Y
```

每条边可以具有：

- 独立 scope；
- 独立 Evidence；
- 独立 Continuity；
- unknown state；
- conflicting evidence；
- temporal context。

## 6. Provenance Continuity / 来源连续性

GCPP 将研究“对象变化后，来源关系还剩下什么”作为核心问题。

候选维度包括：

```text
exact continuity
structural continuity
segment continuity
transform continuity
semantic continuity
causal influence
historical relation
unknown
```

这些名称目前是研究词汇，不是稳定 registry。

协议 **MUST NOT** 假设所有 transformation 都可以被一个统一 similarity score 正确表示。

例如：

- byte-level 修改；
- normalization；
- 摘录；
- 拼接；
- 翻译；
- 摘要；
- 多轮 rewrite；
- 训练；
- 蒸馏；

具有不同类型的连续性和证据边界。

## 7. Partial / Mixed / Unknown / Conflict

以下必须被视为一等状态：

```text
PARTIAL
MIXED
TRANSFORMED
UNKNOWN
CONFLICTING_EVIDENCE
```

GCPP verifier 应报告当前可验证的事实范围，而不是强制把整个对象压成 `verified/unverified` 二元状态。

`authenticated coverage` 继续作为重要研究结果，但它不假设所有媒体和 transformation 都能用同一种百分比表达。

## 8. Architectural invariants / 架构不变量

符合 GCPP 方向的实现 **MUST** 保持：

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
SIMILARITY != PROVENANCE
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
OUTPUT_PROVENANCE != MODEL_LINEAGE
REGULATORY_LABEL != CRYPTOGRAPHIC_IDENTITY
ABSENCE_OF_EVIDENCE != EVIDENCE_OF_ABSENCE
```

另外：

- Public provenance **MUST NOT** 默认要求用户账号、IP、设备 ID、手机号、邮箱或 raw prompt；
- Core verification **MUST NOT** 依赖单一全球在线 verifier；
- partial/transformed provenance **MUST** 是正常状态；
- 政策、法律、版权、作弊、真实性和内容质量判断 **MUST** 位于协议事实层之外；
- C2PA、SPDX、CycloneDX、GB 45438、DID、X.509、Hash、水印、区块链、Transparency Log 等均属于可替换 Profile/Adapter/Evidence。

## 9. Generation identity

此前 `GenerationID (GID)` 被定义为一次具体生成事件的权威标识。

该概念现在进入复审：

- 如果它只是另一个 asset UUID，则不应进入 Core；
- 如果真实场景需要独立标识“一次生成执行”，并让多个输出共享该执行关系，则可继续研究 `Generation Execution Identity`；
- 是否进入 Core 必须由实际案例证明，而不是由命名空间需求证明。

## 10. RecoveryLocator

`RecoveryLocator (RID)` 继续作为实验性研究方向，用于在 metadata / sidecar / credential carrier 丢失以后发现候选 provenance record。

固定边界：

- RID **MUST NOT** 被当作 authentication；
- locator recovery 只完成 discovery；
- attribution 必须依赖额外 Evidence 与 binding verification；
- GCPP 不要求使用自有水印算法；
- 如果外部算法更优，应允许直接作为 Profile/Evidence 使用。

## 11. Model assurance

此前的：

```text
MODEL_NONE
MODEL_DECLARED
MODEL_ATTESTED
MODEL_EXECUTION_PROVEN
```

保留为可能的 Presentation / Policy convenience states，但底层研究优先转向正交 Evidence Vector，例如：

```text
model_identity_evidence
provider_attestation
runtime_attestation
model_binary_binding
execution_attestation
request_output_binding
hardware_attestation
```

协议不得因为单一证据存在就自动升级为更强结论。

## 12. Model lineage

`OUTPUT_PROVENANCE != MODEL_LINEAGE` 继续保持。

模型血缘研究聚焦生成式 AI 特有的影响与证据问题，例如：

```text
teacher-distilled-from
synthetic-data-generated-by
reasoning-traces-generated-by
preference-signals-generated-by
```

普通模型 BOM、数据集清单、依赖关系等已有标准能够表达的事实应优先映射，不重复定义。

此前线性的 lineage assurance level 进入复审，优先研究正交 Evidence Vector：

```text
provider_declaration
dataset_commitment
source_model_credential
teacher_attestation
training_run_attestation
watermark_indication
confidential_audit
independent_verification
authorization_evidence
```

## 13. Evidence

每份 Evidence 应明确：

```text
subject
claimed relation / property
scope
verification method
assumptions
failure modes
issuer / observer
validity / time context
```

可能的实现包括：

- digital signature；
- hard / soft binding；
- watermark / fingerprint；
- timestamp / transparency evidence；
- identity credential；
- hardware / execution attestation；
- dataset commitment；
- confidential audit；
- selective disclosure；
- future evidence。

Evidence 必须声明它证明的对象和保证边界。

## 14. Verification output

Verifier 的目标不是输出单一“真假”。

候选结构：

```text
entities[]
relations[]
continuity[]
evidence[]
coverage
unknowns[]
conflicts[]
regulatory_observations[]
```

现有 `Verification Vector` 思路继续保留，但将在第一性原理研究后重新定义 schema。

Presentation / Policy 只是对上述事实的解释，不是权威真相。

## 15. Privacy and selective disclosure

GCPP 必须允许证明关系而不公开全部底层数据。

Profile 可以使用 commitment、selective disclosure、confidential audit、TEE、ZK 或未来技术，但 Core 不绑定任何一种。

## 16. Protocol independence

GCPP 的长期 Core 语义不得依赖某个单一外部组织、算法、账本、模型架构、国家监管体系或厂商永久存在。

一个协议原语如果随着某个实现标准升级就失去存在价值，则更适合作为 Adapter/Profile，而不是 Core。

---

# English

## Scope

GCPP Core is under a first-principles architecture review. It is no longer defined primarily as a collection of generative assertions filling gaps in existing standards, and it is not pursuing a feature or publication race with C2PA, SPDX, CycloneDX, or other ecosystems.

The principal research problem is **provenance continuity**: after information is generated, copied, edited, combined, transformed, trained on, distilled, or regenerated, which source relationships remain, which can be verified, and what exactly does each item of evidence prove?

The previous `Identity / Provenance / Integrity / Evidence` model is being compared with a new research hypothesis:

```text
Entity
Relation
Continuity
Evidence
```

Neither model is declared final for a future Core revision by this document alone.

GCPP should model provenance as an evidence-backed relation graph, treat partial/mixed/transformed/unknown/conflicting states as first-class, preserve strict evidence boundaries, minimize sensitive-data requirements, and remain independent from specific credential formats, PKI systems, hashes, watermarks, ledgers, AI architectures, or regulations.

Existing standards remain important implementation and interoperability layers, but they do not define the research agenda.
