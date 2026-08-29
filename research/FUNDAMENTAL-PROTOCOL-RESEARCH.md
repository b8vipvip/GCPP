# GCPP 第一性原理协议研究 / GCPP Fundamental Protocol Research

> 状态 / Status: **Research Charter / 非规范性研究纲领**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> F0 最新研究状态 / Latest F0 research status: **2026-08-29**

# 简体中文

## 1. 研究目的

GCPP 不以“比 C2PA、SPDX、CycloneDX 更早实现某个功能”为目标，也不以寻找现有标准的短期空白为研发驱动力。

研究顺序固定为：

```text
社会/行业长期问题
    ↓
Problem
    ↓
Abstraction
    ↓
Invariant
    ↓
Protocol Primitive
    ↓
Evidence
    ↓
Implementation / Adapter
```

现有标准主要在最后一层参与实现与互操作。一个 GCPP Core 原语若只能通过“某个现有标准暂时没做”来证明存在价值，则不应进入 Core。

## 2. 核心研究问题

GCPP 的长期研究对象不是“某个文件是否带有凭证”，而是：

> **信息经过生成、传播、编辑、组合、转换、训练和再生成以后，来源声明的可验证含义如何不被丢失、扩大或错误升级？**

最初把这个问题暂称为 **Provenance Continuity / 来源连续性**。

F0 第一轮研究进一步发现：`Continuity` 很可能不应该成为一个单独存储的 Core primitive。它更适合作为从历史关系、preservation/transformation claims、scope、projection 和 Evidence Assessment 推导出的查询/视图。

因此研究中心正在收敛为：

> **Boundary-preserving provenance semantics / 保持验证边界的来源语义。**

## 3. F0 五个第一性问题

1. 什么是协议层最小的 Information Object / referent？
2. 什么叫两个对象之间存在来源、影响或转换关系？
3. 信息变化后，到底哪些属性/片段/关系仍可被验证？
4. Evidence 能证明什么、不能证明什么？
5. 一个长期公共协议最少需要哪些不可删除的语义约束？

## 4. 初始假设已被部分证伪

F0 开始时的研究假设是：

```text
Entity
Relation
Continuity
Evidence
```

该四元组**不再是当前推荐 Core 模型**。

F0 Round 1–4 的反证结果：

- `Entity + Relation graph` 已由 W3C PROV 等成熟体系广泛覆盖，不构成 GCPP 的独特价值；
- first-class Claim / claim-about-claim 也已有 Nanopublications、RDF reification/proposition 等成熟先例；
- `Continuity` 无法脱离 target/state、scope、projection/facet、relation 与 Evidence 而拥有绝对含义；
- `State`、`Event`、`Evidence`、`Assessment` 等可以在抽象层被表示成 generic referent/node 的不同 role，不一定需要平行的 Core container；
- `Scope` 的具体 selector 可以下放 Profile，但“Claim 必须能够被 scope-qualified”表现出强不可约性；
- provenance data 整体不能被强制视为 DAG；只有特定 process/causal projection 才可能具有无环约束。

因此 F0 当前不再追求“找出四个漂亮名词”，而是寻找**删除后会导致验证语义错误的长期不变量**。

## 5. 当前候选信息模型

最小对象层暂时可以非常薄：

```text
Referent / Node
Claim
```

但 GCPP 的潜在价值**不来自重新发明 Node 或 Claim graph**。

一个 Claim 的可验证含义必须被限定。F0 当前把这些限定压缩为四类研究边界：

```text
Referential Boundary
Interpretation Boundary
Temporal Boundary
Epistemic Boundary
```

### Referential Boundary

回答：

```text
which fixed target/state?
which source/target scope?
```

### Interpretation Boundary

回答：

```text
what proposition/predicate?
under which relation/projection/profile semantics?
```

### Temporal Boundary

区分：

```text
event time
claim issuance time
evidence observation time
assessment time
validity/freshness
retraction/supersession time
```

### Epistemic Boundary

回答：

```text
who asserted/observed/attested/inferred?
what evidence supports it?
what can that evidence actually prove?
what inference produced the result?
```

四类边界仍是研究假设，F0 下一轮必须继续尝试合并/删除。

## 6. Verification Envelope / 验证包络

F0 当前提出一个派生抽象：

> **Verification Envelope 表示某个 Assessment 能安全声称得到支持的最大语义范围。**

它不是新的 credential container，也不是 assurance score。

研究表达：

```text
Envelope(A) = {
  referential,
  interpretation,
  temporal,
  epistemic
}
```

同一 Claim 可以有多个 verifier、多个 Assessment、多个 Envelope 并存。

## 7. Verification Non-Amplification / 验证不增益

F0 当前最重要的新候选不变量：

> **没有新增可验证 Evidence，转换、Adapter、聚合、推导或重新包装步骤不得输出比输入已验证语义更强的“已验证”结论。**

允许：

```text
preserve
conservatively weaken
downgrade to unknown / indeterminate
```

不得静默：

```text
widen scope
strengthen predicate
increase authority role
assume freshness
invent identity binding
assume provenance transitivity
upgrade probabilistic evidence to proof
```

一个更强结论只有两种合法来源：

```text
new independently verifiable evidence
OR
explicit conservative derivation under a registered profile
```

## 8. 当前最强候选不变量

```text
CLAIM != FACT
IDENTIFIER != IDENTITY PROOF
REFERENCE != BINDING
LOCATOR != AUTHENTICATION
CONTENT EQUALITY != PROVENANCE
SEMANTIC SIMILARITY != DERIVATION
HISTORICAL DEPENDENCY != CONTENT PRESERVATION
EVIDENCE != ASSESSMENT
ASSESSMENT != POLICY
MISSING_SCOPE != WHOLE_SCOPE
NO IMPLICIT SCOPE INHERITANCE
NO IMPLICIT PROVENANCE TRANSITIVITY
RE-SIGNING != INDEPENDENT VERIFICATION
PAST_VALIDITY != CURRENT_VALIDITY
LOSS OF QUALIFIER MUST NOT INCREASE VERIFIABILITY
NO VERIFICATION AMPLIFICATION WITHOUT NEW EVIDENCE OR CONSERVATIVE DERIVATION
```

这些仍是 F0 research invariants，不是已经冻结的 normative requirements。

## 9. Provenance Claim Laundering / 来源声明洗白

F0 将以下问题作为新的真实行业威胁类研究：

> **一个系统因为恶意、简化 UI、schema 不兼容、metadata stripping 或实现错误，丢失限定条件，却让下游看到更强的正面 provenance 结论。**

候选类型：

```text
Scope laundering
Evidence laundering
Authority laundering
Lineage laundering
Temporal laundering
Projection laundering
Inference laundering
```

例如：

```text
verified paragraph
-> selector lost
-> UI says verified document
```

或：

```text
watermark detected
-> source field copied
-> next system says provider authenticated
```

F0 后续必须把这些转化成可复现实验和 conformance test，而不是停留在概念名称。

## 10. Scope 与 Relation Contract

F0 已发现：即便 `whole -> part` 也不能作为通用继承规则。

例如：

```text
whole document contains some AI-generated content
```

不能推出：

```text
every paragraph contains AI-generated content
```

所以每种自动可组合 relation / Claim Profile 必须显式定义自己的机器可测试 contract，例如：

```text
scope semantics
projection semantics
temporal semantics
composition rules
inheritance rules
forbidden inferences
```

默认值应是：

```text
implicit_transitivity = false
scope_inheritance = none
composition = none
```

## 11. Claim / Evidence / Assessment / Policy 必须分层

候选架构：

```text
Claim
  ↓ references
Evidence-role artifacts / records
  ↓ appraisal
Assessment-role Claim
  ↓ local policy
Decision / Presentation
```

关键分离：

```text
Evidence payload != Claim truth
Evidence != Assessment
Assessment != Policy decision
Observation != Inference
Inference != Policy
```

## 12. “同一个信息”不再作为裸问题

协议不问：

```text
Are A and B the same information?
```

而问：

```text
Does claim/relation P hold
between A.scope and B.scope
under profile/projection π
with evidence E
at temporal context τ?
```

因此：

```text
byte equality
normalized-text equality
logical-work identity
semantic similarity
historical derivation
```

必须保持分离。

## 13. 隐私与选择性披露

真实来源系统不能要求公开完整训练数据、raw prompt、用户身份、内部工具调用或商业秘密。

Core 研究必须允许：

```text
prove/support a claim
without disclosing all underlying data
```

Profile 可以使用：

- commitment；
- selective disclosure；
- confidential audit；
- TEE attestation；
- ZK proof；
- transparency receipt；
- future evidence systems。

但选择性披露不能把 Evidence capability 隐藏到只剩：

```text
verified = true
```

否则违反 Non-Amplification。

## 14. 与现有标准的关系

GCPP 不与成熟标准进行功能竞赛。

已有体系可以承载许多对象、图、凭证和 Evidence：

```text
W3C PROV      -> general provenance entities/activities/relations
RDF           -> graph/proposition/reification substrate
Nanopubs      -> fine-grained assertions + provenance
C2PA          -> content credentials / signatures / bindings
SPDX/CDX      -> AI/software/dataset supply-chain description
VC            -> credentials / identity / authorization claims
in-toto       -> process attestations
RATS          -> evidence -> verifier result -> relying-party policy architecture
SCITT/logs    -> transparency / registration evidence
GB 45438      -> Chinese regulatory AIGC labeling
```

GCPP 当前研究价值只可能来自：

> **这些系统交换 provenance 时，如何保留 Claim 的验证边界并阻止无证据的语义升级。**

如果这个问题最终可以完全由现有标准组合解决，GCPP 应缩减或停止创建新的 Core，而不是为了项目存在而继续造协议。

## 15. 当前 F0 研究文档

- `F0-01-INFORMATION-OBJECT-IDENTITY.md` — Information Object / identity / reference-binding-locator 分离；
- `F0-02-CLAIM-CONTINUITY-EVIDENCE.md` — evidence-backed Claim graph 与 Continuity 反证；
- `F0-03-REAL-WORLD-STRESS-TESTS.md` — 真实行业场景压力测试；
- `F0-04-MINIMALITY-AND-BOUNDARY-MODEL.md` — primitive 删除实验与 Verification Boundary；
- `F0-05-VERIFICATION-NON-AMPLIFICATION.md` — 验证不增益与 provenance claim laundering；
- `F0-06-VERIFICATION-ENVELOPE.md` — 四类边界、Verification Envelope 与 relation contract。

## 16. 下一轮 F0 必须继续反驳

不能因为 Verification Boundary / Non-Amplification 看起来有价值就立刻标准化。

F0-R4/R5 必须回答：

1. 四类 Boundary 是否还可以继续合并/删除？
2. Verification Envelope 是否只是换名的 Attestation Result？
3. Non-Amplification 是否可以直接复用成熟 information-flow / trust formalism？
4. Scope / Projection 是否能跨媒体形成稳定抽象？
5. relation contract 会不会退化成不可维护的全球 ontology？
6. conservative derivation 能否在无全球中心的条件下互操作？
7. adapter 能否机器判定 verification-boundary lossless / lossy？
8. selective disclosure 是否可以在隐藏 Evidence 内容时仍保留 proof boundary？
9. 两个独立实现能否对同一 mapping 得到一致的 amplification 判定？
10. 上述模型是否真正降低现实系统的误归属、过度声明和 provenance laundering？

## 17. Core 晋级标准

任何候选 GCPP Core 原语/不变量进入规范前都必须回答：

1. 它解决的现实问题是什么？
2. 该问题是否跨平台、跨模型、跨法域长期存在？
3. 为什么已有一般概念不足以表达？
4. 如果现有标准明天加入类似字段，它是否仍有意义？
5. 是否依赖某个具体算法或厂商？
6. 是否可以由至少两种不同 Evidence 技术实现？
7. 是否把事实与政策/法律判断混在一起？
8. 是否支持 unknown / partial / conflicting？
9. 是否避免不必要的个人数据或商业秘密？
10. 独立实现是否可能得到一致验证结果？
11. 它能否通过删除实验：删除后是否真的导致无法安全表达现实问题？
12. 它能否通过 non-amplification test：跨系统转换后是否仍阻止验证语义被无证据扩大？

## 18. 成功标准

GCPP 的成功不定义为：

- 比其他标准更早发布；
- assertion 数量更多；
- 支持更多算法；
- 创建自己的加密容器；
- 让所有行业迁移到 GCPP 专有格式。

成功定义为：

> **找到一组足够小、足够稳定、可独立实现和测试的 provenance semantic-safety invariants，使来源声明跨系统、跨转换、跨 AI 执行传播时不会变得比真实 Evidence 更强。**

---

# English

GCPP F0 is no longer centered on the initial `Entity / Relation / Continuity / Evidence` four-tuple. Primitive-deletion and prior-art tests show that generic graph, relation, claim, reification and provenance-of-provenance capabilities are already broadly covered by W3C PROV, RDF, Nanopublications and related systems.

The current research center is **boundary-preserving provenance semantics**. A claim's supported meaning is provisionally described by four boundaries:

```text
Referential
Interpretation
Temporal
Epistemic
```

These boundaries form a candidate `Verification Envelope`, not a credential container or scalar assurance score.

The strongest current F0 hypothesis is **Verification Non-Amplification**: without new verifiable evidence or an explicit conservative derivation rule, transformations, adapters, aggregators and inference steps must not output a verified claim whose semantics are stronger than those supported by the inputs. Missing qualifiers must cause downgrade or indeterminacy, never silent widening.

F0 also rejects implicit scope inheritance and implicit provenance transitivity. Relation/Claim profiles that support automated composition must publish machine-testable scope, projection, temporal, composition and inheritance semantics.

The project will not standardize this hypothesis until further rounds show that the boundary model is irreducible, independently implementable, not already fully solved by existing trust/information-flow formalisms, and measurably useful against real provenance-laundering failures.
