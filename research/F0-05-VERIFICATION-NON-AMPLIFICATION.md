# F0-05 — 验证不增益原则 / Verification Non-Amplification Principle

> 状态 / Status: **F0 Research Hypothesis / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 研究动机

F0 前四轮逐步发现：

- 通用 provenance graph 不是新问题；
- first-class Claim 不是新问题；
- reification / claim-about-claim 不是新问题；
- `Continuity` 作为单一字段无法成立；
- 真正反复出现的行业错误，是 Claim 的限定条件在传播过程中被丢失，然后弱证据被解释成更强结论。

典型例子：

```text
partial provenance
    -> whole-document provenance

watermark detected
    -> provider authenticated

training dataset used
    -> arbitrary output attributed to dataset

provider self-declaration
    -> independently verified

historically valid credential
    -> currently valid credential

semantic similarity
    -> historical derivation

regulatory metadata
    -> cryptographic identity proof

recovered locator
    -> authenticated attribution
```

这些问题表面不同，底层结构相同：

> **验证语义被放大了。**

因此提出 F0 候选不变量：

# Verification Non-Amplification / 验证不增益

---

## 2. 原则定义（研究版）

设系统接收一个或多个已评估 Claim，并经过：

- 格式转换；
- Adapter 映射；
- 聚合；
- 摘要；
- metadata stripping；
- 跨平台传播；
- relation composition；
- inference；
- selective disclosure；
- credential re-packaging；

产生新的 Claim 或 Assessment。

候选原则：

> **若没有新增可验证 Evidence，一个处理步骤不得输出一个比其输入已验证语义更强的“已验证”结论。**

允许：

```text
preserve
weaken
downgrade to unknown/indeterminate
```

不允许静默：

```text
widen scope
strengthen predicate
increase authority status
assume freshness
invent identity binding
assume transitivity
upgrade probabilistic evidence to proof
```

---

## 3. 什么叫“更强”不能用一个总分定义

GCPP 不建立：

```text
assurance_score = 0..100
```

来比较所有 Claim。

“更强”至少是多维偏序问题。

例如：

```text
verified_scope
predicate semantics
projection semantics
authority/origin role
temporal validity
evidence capability
inference depth
```

因此 Verification Non-Amplification 不是：

```text
score(out) <= score(in)
```

而是：

> 输出的每个验证语义必须能够由输入 Assessment 在一个明确的、可审计的规则下蕴含；否则必须有新 Evidence。

---

## 4. Conservative Derivation / 保守推导

定义研究关系：

```text
C1 ⊢[P] C2
```

含义：

> 在注册的 inference/mapping Profile `P` 及其明确假设下，支持 Claim C1 足以安全地支持较弱或等价的 Claim C2。

注意：

- `⊢` 不是 GCPP 自己发明通用逻辑；
- Profile 可以使用简单确定规则、形式证明、标准映射或领域语义；
- 如果没有已知规则，则默认**不可推导**。

候选安全规则：

```text
supported(C1)
AND C1 ⊢[P] C2
=> derived-support(C2, sources=[C1], profile=P)
```

否则：

```text
NO NEW EVIDENCE
AND NO REGISTERED CONSERVATIVE DERIVATION
=> C2 MUST NOT inherit VERIFIED status
```

---

## 5. Scope 单调性示例

### Whole -> Part

如果 Claim 已验证：

```text
entire normalized text T is bound to Record R
```

在 selector Profile 允许的情况下，可以安全派生：

```text
span S of T is within the verified bound object
```

但它是否拥有独立可迁移 attribution，还需要 Profile 明确。

### Part -> Whole

绝不能自动：

```text
paragraph P verified
=> whole document verified
```

所以：

```text
PARTIAL -> WHOLE
requires new evidence or explicit proof
```

### Missing Scope

如果跨格式映射后 Scope 丢失：

```text
scope = unknown
```

而不是默认：

```text
scope = whole
```

候选 Core 不变量：

```text
MISSING_SCOPE != WHOLE_SCOPE
```

---

## 6. Projection 单调性示例

### Byte exact -> Normalized equality

如果 Profile `N` 是确定性的，并且：

```text
bytes(A) == bytes(B)
```

通常可以派生：

```text
N(A) == N(B)
```

### Normalized equality -> Byte exact

不能反向。

### Semantic similarity -> Derivation

没有一般安全推导：

```text
semantic_similarity(A,B)=0.98
⊬
B derived-from A
```

除非有额外 historical/process Evidence。

所以：

```text
SIMILARITY EVIDENCE
MUST NOT inherit DERIVATION verification
```

---

## 7. Evidence 能力不能被放大

### Signature

输入：

```text
signature valid for Claim C
```

安全结论：

```text
identified signing key signed C
```

不能自动：

```text
C objectively true
```

### Watermark

输入：

```text
signal profile W detected
```

不能自动：

```text
Provider P authenticated
```

### RID

输入：

```text
locator RID recovered
```

只能先支持：

```text
candidate provenance record discovered
```

必须继续验证 record signature + binding + applicable scope 才能 attribution。

### Hardware attestation

输入：

```text
measurement M attested under environment profile E
```

不能自动：

```text
output is factually correct
```

---

## 8. Authority / Claim Origin 不增益

以下角色不是单调的统一等级，但不能静默互换：

```text
self-asserted
first-party observed
counterparty attested
independent observed
independent audited
regulatory/court statement
```

转换格式时：

```text
self-asserted
```

不能因为重新签名变成：

```text
independently verified
```

新的 wrapper 签名只能证明 wrapper signer 的行为，不能改变原 Claim 的 epistemic origin。

候选不变量：

```text
RE-SIGNING != INDEPENDENT VERIFICATION
```

---

## 9. 时间不增益

输入：

```text
Claim C valid / observed at T1
```

不能因为在 T2 被读取就升级：

```text
C currently valid at T2
```

除非 Evidence/Profile 支持持续有效性或重新检查。

类似地：

```text
fresh attestation at T1
```

随着时间推移通常只会失去 freshness，而不会自动变新。

候选原则：

```text
READ_TIME != EVIDENCE_TIME
ISSUE_TIME != EVENT_TIME
PAST_VALIDITY != CURRENT_VALIDITY
```

---

## 10. Relation Composition 不得默认传递

这是 provenance laundering 的重要来源。

若：

```text
A R B
B S C
```

GCPP 不默认存在：

```text
A T C
```

除非某 Profile 定义：

```text
compose(R,S) -> T
```

并且满足：

- scope 对齐；
- state 对齐；
- temporal constraints；
- projection constraints；
- Evidence/Assessment requirements。

### Quotation 示例

B 引用了 A 的第 2 段。

C 引用了 B 的第 8 段。

即使：

```text
B quoted-from A
C quoted-from B
```

如果 C 引用的 B 第 8 段并不是来自 A 的第 2 段，则不能推导：

```text
C quoted-from A
```

所以：

```text
RELATION LABEL TRANSITIVITY
```

远远不够，必须有 scope mapping。

候选 Core 不变量：

```text
NO IMPLICIT PROVENANCE TRANSITIVITY
```

---

## 11. Transformation Composition

设：

```text
A --f--> B --g--> C
```

即使两个 transformation event 都 VERIFIED，也不代表任意 preservation property 可传递。

需要区分：

```text
historical chain exists
```

和：

```text
property X survives A -> C
```

后者需要 composition rule：

```text
Preserves(f, X1)
Preserves(g, X2)
composition_profile(f,g)
=> maybe Preserves(g∘f, X3)
```

没有 Profile 时只能安全报告 historical chain，不应猜测 end-to-end semantic continuity。

---

## 12. Claim Laundering / 来源声明洗白

F0 将如下模式定义为研究对象：

> 一个系统通过删除、模糊或重新包装限定信息，使下游消费者看到比上游 Evidence 实际支持范围更强的 provenance claim。

暂称：

# Provenance Claim Laundering

不是法律术语，也不等同恶意行为；可以由无意的格式转换造成。

### 类型 L1 — Scope Laundering

```text
verified paragraph
-> provenance metadata loses selector
-> UI shows verified document
```

### L2 — Evidence Laundering

```text
watermark indication
-> serialized as source=ProviderP
-> next system treats ProviderP authenticated
```

### L3 — Authority Laundering

```text
provider self-declaration
-> aggregator re-signs record
-> consumer treats aggregator signature as independent confirmation
```

### L4 — Lineage Laundering

```text
Model M trained-on D
-> M generated O
-> consumer reports O sourced-from D
```

### L5 — Temporal Laundering

```text
credential once valid
-> revocation/freshness context stripped
-> presented as currently valid
```

### L6 — Projection Laundering

```text
normalized text match
-> qualifier stripped
-> presented as byte-identical original
```

### L7 — Inference Laundering

```text
inferred relation
-> inference provenance stripped
-> presented as directly observed relation
```

这些是 F0 后续 benchmark / test vector 的候选攻击类。

---

## 13. Boundary Loss 的默认处理

候选原则：

> **Lost qualifier causes downgrade, never silent widening.**

例如：

```text
scope known -> scope lost
```

输出：

```text
scope_state = unknown
verification = indeterminate for whole-object attribution
```

而不是猜测 whole。

类似：

```text
projection profile lost
=> exact preservation must not be assumed

authority origin lost
=> independent status must not be assumed

evidence freshness lost
=> current-validity must not be assumed
```

候选不变量：

```text
LOSS OF QUALIFIER => LOSS OR WEAKENING OF VERIFIABILITY
```

---

## 14. 新 Evidence 如何合法“增强”

Non-Amplification 不是禁止建立更强结论。

允许：

```text
old evidence
+
new independent evidence
+
explicit assessment
=> stronger supported claim
```

例如：

```text
MODEL_DECLARED
+
TEE execution attestation
+
input/output binding
+
accepted verification profile
=> stronger execution-related assessment
```

关键在于：

> 增强必须可归因于新增 Evidence 或明确保守推导，而不是来自信息丢失/重新包装。

---

## 15. Proof-Carrying Mapping / 带依据映射

Adapter 不应只输出：

```text
source field X -> target field Y
```

候选研究结构：

```text
MappingAssessment {
  input_claim_refs[]
  output_claim_ref
  mapping_profile
  mapping_kind:
    equivalent
    conservative-weakening
    evidence-augmented
    lossy
    non-preserving

  preserved_boundaries[]
  lost_boundaries[]
  new_evidence_refs[]
}
```

这不一定最终成为 Core 对象，但它表达了一个重要目标：

> **跨标准 mapping 本身也应该可审计。**

因此 C2PA -> GCPP -> GB45438 -> internal database 的转换，不应只是字段拷贝，而应能说明哪些验证语义被保留、丢失或新增。

---

## 16. Lossless / Lossy Interoperability 的新定义

传统 schema mapping 常说：

```text
all fields mapped = lossless
```

F0 认为对 provenance 不够。

新的判据应该是：

### Syntactically lossless

字段/值可逆。

### Semantically lossless

Claim proposition 和 qualification 含义保留。

### Verification-boundary lossless

目标格式仍能表达：

- target/state boundary；
- scope；
- projection；
- temporal semantics；
- evidence capability；
- authority/origin；
- inference provenance。

所以一个字段全部拷贝的映射也可能：

```text
syntactically lossless
but verification-boundary lossy
```

这可能成为 GCPP Adapter 体系真正有用的 conformance 概念。

---

## 17. 形式化研究草图

设 `A` 是一个 Assessment，它支持 Claim `C`，并携带边界集合：

```text
B(A) = {
  target,
  scope,
  projection,
  temporal,
  evidence,
  authority,
  inference
}
```

一个 mapping `M` 产生 Assessment `A'`。

最粗略的 Non-Amplification 条件：

```text
VerifiedSemantics(A')
⊆
Closure_P(VerifiedSemantics(A), NewEvidence)
```

其中：

- `Closure_P` 只允许 Profile P 明确注册的保守推导；
- `NewEvidence` 是 mapping 阶段新增并独立验证的 Evidence；
- 未知/丢失边界不能扩大 `VerifiedSemantics`。

这只是研究记号，后续必须寻找更精确、可机器测试的定义。

---

## 18. 与信息流安全的类比，但不是同一个问题

安全领域长期研究：

- information-flow labels；
- noninterference；
- declassification；
- endorsement；
- policy-preserving transformations。

GCPP 可以借鉴“信息不能未经授权从高约束变成低约束”的思想。

但这里研究的是：

```text
provenance verification semantics
```

不是 confidentiality label。

类比：

```text
security declassification
≈ explicit authorized weakening of confidentiality constraints

provenance mapping
≈ explicit, auditable preservation/weakening of verification claims
```

F0 后续应调查是否已有成熟形式系统可以直接复用，而不是重新发明证明理论。

---

## 19. 当前最强候选 Core 不变量

截至 F0 Round 3：

```text
CLAIM != FACT
IDENTIFIER != IDENTITY PROOF
REFERENCE != BINDING
LOCATOR != AUTHENTICATION
CONTENT EQUALITY != PROVENANCE
SIMILARITY != DERIVATION
HISTORICAL DEPENDENCY != CONTENT PRESERVATION
EVIDENCE != ASSESSMENT
ASSESSMENT != POLICY
MISSING_SCOPE != WHOLE_SCOPE
NO IMPLICIT PROVENANCE TRANSITIVITY
RE-SIGNING != INDEPENDENT VERIFICATION
PAST_VALIDITY != CURRENT_VALIDITY
LOSS OF QUALIFIER MUST NOT INCREASE VERIFIABILITY
NO VERIFICATION AMPLIFICATION WITHOUT NEW EVIDENCE OR CONSERVATIVE DERIVATION
```

这些规则目前比任何具体 C2PA/SPDX/CycloneDX 字段更稳定。

---

## 20. 如果这个方向成立，GCPP 的核心社会价值是什么？

不是：

```text
store more provenance
```

而是：

> **Prevent provenance meaning from becoming stronger than its evidence as information moves through society.**

中文：

> **防止信息在社会传播、AI 转换、平台聚合和跨标准交换过程中，其“来源含义”变得比真实证据更强。**

这直接服务于：

- 新闻；
- 科研；
- AI Agent；
- AI 内容标识；
- 模型训练审计；
- 企业合规；
- 公共档案；
- 法律证据链；
- 机器自动决策。

它不是 Truth Protocol。

它解决的是：

```text
Do not overstate what provenance evidence establishes.
```

---

## 21. 下一轮 F0-R4

1. 尝试把 7 类 Verification Boundary 继续压缩，避免任意 metadata bag；
2. 为 `VerifiedSemantics` 建立可计算模型；
3. 定义 scope / projection composition 的最小 algebra；
4. 对 `no implicit transitivity` 做 relation composition matrix；
5. 为 Provenance Claim Laundering 建立 threat model；
6. 研究 selective disclosure 是否能保持 Non-Amplification；
7. 设计一组 adapter conformance tests：lossless / weakening / lossy / illegal amplification；
8. 检查与 PROV、RDF 1.2、RATS、VC、安全 information-flow 形式系统的可复用关系。

---

# English

## Research hypothesis

F0 proposes **Verification Non-Amplification** as a candidate cross-system invariant:

> Without new verifiable evidence, a transformation, adapter, aggregator, inference step, or repackaging process must not produce a verified claim whose semantics are stronger than those safely implied by the verified inputs.

This is not a scalar assurance rule. Verification strength is multidimensional: scope, predicate/projection semantics, authority/origin, temporal validity, evidence capability and inference provenance are not interchangeable.

A derived claim may inherit support only through an explicitly registered conservative derivation/mapping rule, or through new evidence. Missing qualifiers must cause downgrade or indeterminacy, never silent widening.

The principle prohibits common provenance-laundering patterns such as partial-to-whole scope escalation, watermark-to-identity escalation, training-lineage-to-output attribution, self-assertion-to-independent-verification, stale-to-current validity, semantic-similarity-to-derivation, or recovered-locator-to-authenticated-attribution.

GCPP should also reject implicit provenance transitivity: `A R B` and `B S C` do not justify `A T C` unless a profile defines a valid composition rule and scope/state/temporal/projection conditions align.

This leads to a stronger interoperability concept: a mapping can be syntactically lossless yet **verification-boundary lossy**. GCPP may provide value by making such losses explicit and testable across standards and platforms.

The next research round will minimize the boundary dimensions, formalize safe composition, build claim-laundering threat models and test whether selective disclosure and cross-standard adapters can preserve verification semantics without amplification.
