# F0-08 — Prior-Art Challenge：验证边界是否真的需要 GCPP？ / Prior-Art Challenge: Does Verification-Boundary Semantics Need GCPP?

> 状态 / Status: **F0 Adversarial Research / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 目的：主动证明 GCPP 可能“不需要存在”

公共协议研究最危险的路径是：

```text
提出一个听起来新颖的概念
-> 给它命名
-> 写 schema
-> 把已有理论重新包装成项目创新
```

F0 必须反过来做：

> **先假设 Verification Boundary、Verification Envelope、Non-Amplification 都已经被其他领域解决，然后尝试证明 GCPP 仍然有不可替代的问题。**

如果证明失败，GCPP 应缩减为研究/映射工具，甚至停止创建独立 Core。

---

## 2. Challenge A — W3C PROV 已经有通用 provenance graph

W3C PROV 已经标准化：

```text
Entity
Activity
Agent
Generation
Usage
Derivation
Attribution
Association
Delegation
Influence
qualified relations
Bundles / provenance of provenance
```

因此以下都不能作为 GCPP 的创新声明：

```text
provenance is a graph
process/activity nodes matter
relations can be qualified
provenance can have provenance
```

### GCPP 还能剩什么？

PROV 擅长表达：

```text
what provenance statements exist
```

F0 当前真正关心：

```text
what verification semantics may safely survive
when those statements are mapped, stripped, aggregated,
partially disclosed, re-signed, transformed or combined
across heterogeneous verification systems
```

这不是说 PROV 做不到表达这些 metadata。

真正的问题是：

> **是否存在跨载体、跨 Evidence 技术的统一“安全映射/降级/不增益”契约，而不仅是 provenance vocabulary？**

这必须通过实现测试证明，而不能靠文档声称。

---

## 3. Challenge B — RDF 1.2 已经解决 Proposition / Reification

RDF 1.2 的 triple terms / reification 能：

- 引用 proposition 而不自动断言为 fact；
- 给 proposition 添加来源、上下文等 metadata；
- 表达未断言甚至互相矛盾的 proposition；
- 给同一 proposition 建立多个不同 reifier。

因此以下不能成为 GCPP 的创新：

```text
CLAIM != FACT
claim-about-claim
conflicting claims coexist
statement metadata
```

### GCPP 还能剩什么？

不是发明新的 Claim container。

如果 GCPP 有价值，它必须提供的是：

```text
verification semantics over claims
```

例如：

- Scope 被删除后必须怎样降级；
- 未知 predicate/profile 是否允许继承 VERIFIED；
- 一个 Adapter 如何证明 mapping 是 conservative；
- 一个 verified claim 何时能安全 composition；
- Evidence capability 如何阻止 watermark -> identity；
- 一层未检查时 UI 是否可以输出 exhaustive-looking conclusion。

这些规则可以**用 RDF 表达**，但“可以表达”不等于已经存在跨 provenance 系统的一致 conformance semantics。

如果最终发现 RDF Shapes / OWL / rules 已可完整解决且已有行业采用，则 GCPP 不应重复。

---

## 4. Challenge C — Nanopublication 已有 Assertion + Provenance + Publication Info

Nanopublication 长期强调细粒度可引用 assertion，并把 assertion provenance / publication info 分开。

因此：

```text
fine-grained claim provenance
claim identity
provenance of an assertion
```

不是 GCPP 的新概念。

### 仍待验证的问题

GCPP 的候选空间只可能在：

```text
machine-testable verification boundary preservation
```

尤其是异构 Evidence 与格式转换，而不是 assertion publication mechanism。

---

## 5. Challenge D — IETF RATS 已经有 Evidence -> Result -> Policy

RFC 9334 已明确架构：

```text
Attester
  -> Evidence
Verifier
  -> Attestation Results
Relying Party
  -> local Appraisal Policy
  -> application decision
```

RATS 还强调：raw Evidence 往往设备/厂商特定，而 Attestation Results 的互操作标准化更重要。

因此 F0 的：

```text
EVIDENCE != ASSESSMENT
ASSESSMENT != POLICY
```

不是原创。

### Verification Envelope 是否只是换名 Attestation Result？

这是必须严肃回答的问题。

如果 Envelope 只是：

```text
Verifier says what it believes after checking Evidence
```

那就应直接复用 RATS/attestation result 思想。

F0 当前认为可能存在的差异不是 Result container，而是：

> **来源声明在跨内容、跨片段、跨转换、跨 lineage、跨 registry 关系组合时的语义边界 preservation / safe weakening / non-amplification。**

RATS 主要围绕 Attester 状态与远程证明架构；GCPP 研究的是 provenance claims 之间的历史/转换/部分覆盖关系以及异构 carrier mapping。

但这只是研究区分，仍需要 prove by construction。

---

## 6. Challenge E — Information-Flow Security 已有“what/who/where/when”边界思想

信息流安全和 declassification 领域长期研究：

```text
what information may be released?
who may release it?
where may release occur?
when may it occur?
```

并研究：

- noninterference；
- declassification；
- endorsement；
- robust declassification；
- semantic consistency；
- policy-preserving transformations。

这与 F0 暂定：

```text
Referential
Interpretation
Temporal
Epistemic
```

具有明显结构相似。

因此：

> **四类 Verification Boundary 本身不能宣称是新理论。**

### Non-Amplification 是否只是 information-flow lattice monotonicity？

也可能。

安全标签系统常要求转换不能违反 label flow policy。

如果 provenance support semantics 可以直接编码为既有 lattice / IFC label，则 GCPP 应复用已有理论。

但目前存在几个必须验证的差异：

1. provenance Claim 并不天然形成全序或单一 lattice；
2. scope inheritance 是 predicate-specific；
3. historical relation composition 与 confidentiality flow 不同；
4. Evidence capability 会随着算法/观测模型变化；
5. open-world completeness 与 conflicting claims 很重要；
6. 同一对象可同时存在多个互不支配 Assessment；
7. “语义更强”依赖 relation/profile entailment，而不是单一 security label。

F0 下一步应尝试使用已有 order/lattice/abstract interpretation 理论表达这些结构，而不是自己造数学体系。

---

## 7. Challenge F — Digital Preservation 已研究 Significant Properties

数字保存长期面对：

```text
format migration 后哪些性质必须保存？
```

Significant Properties / Essential Characteristics 思想说明：

```text
same information
```

通常必须相对于 preservation objective / property set 定义。

这与 F0 的 Projection Boundary 直接相似。

因此：

```text
preservation is facet-dependent
```

也不是 GCPP 原创。

### GCPP 的候选差异

仍然只能是：

> 把“哪些性质被保留”的 qualification 与 provenance Evidence、Scope、Relation Composition 和跨系统 verifier semantics 结合，并使丢失这些 qualification 时能够机器降级。

---

## 8. Challenge G — Database Provenance 已区分 Why / Where / How

数据库 provenance 很早就证明“来源”不是单一关系。

不同问题包括：

```text
why is this output present?
where did this output value come from?
how was this output derived?
```

Provenance semiring 又进一步研究组合语义。

因此 GCPP 不能宣称：

```text
provenance needs more than one relation
```

这是成熟研究结论。

### GCPP 仍需回答

跨 AI 内容、Agent、模型训练、媒体、凭证和监管系统时，能否建立：

```text
explicit composition contract
+
verification-boundary preservation
+
open-world coverage
```

而不重建数据库 provenance algebra。

---

## 9. Challenge H — “Provenance Laundering”术语也不是 GCPP 首创

2026 年 Authenticated Contradictions 研究已经直接讨论 metadata washing / provenance-laundering 现象。

所以 GCPP 不应声称发明了这个术语或问题。

GCPP 当前只是在尝试把它一般化为：

```text
scope laundering
evidence laundering
authority laundering
lineage laundering
temporal laundering
projection laundering
inference laundering
omission laundering
```

这套分类是否有价值，需要用 threat model + reproducible test vectors 证明。

---

## 10. Prior-Art Challenge 后，GCPP 剩余候选价值被压缩为五项

如果 F0 能成立，GCPP 的独立价值可能只剩：

### A. Verification-Boundary Preservation

跨 carrier / adapter / transform 交换 provenance 时，明确哪些被验证语义被保留、缩小、丢失或无法解释。

### B. Verification Non-Amplification

没有新增 Evidence 或保守 entailment，不允许 verified semantics 无依据变强。

### C. Open-World Verification Coverage

没有检查/没有披露/没有观察到不能被解释成相反事实；verifier 必须能表达 checked / unchecked / unavailable domains。

### D. Cross-Layer Consistency

多个独立 Evidence layer 分别有效时，必须显式发现 semantic conflict / incomparability，而不是让某一层“绿色通过”覆盖其他层。

### E. Testable Interoperability Semantics

Adapter conformance 不只测试字段是否被映射，而测试：

```text
verification semantics preserved?
conservatively weakened?
coverage lost?
unsafe amplification occurred?
conflict hidden?
```

如果这五项也能由现有标准组合完整、自然、可互操作地实现，GCPP 就没有必要建立新 Core。

---

## 11. 重新定义“原创性”

F0 不再寻找：

```text
new nouns
new graph
new credential
new signature
new hash
new ontology
```

真正有意义的原创性可能是：

> **一个新的跨系统安全性质（safety property）和可验证 conformance discipline。**

类似互联网协议并不总通过“发明新数据结构”产生价值；有时价值来自：

- 明确系统间必须保持的不变量；
- 定义失败时的安全行为；
- 定义跨实现一致的 conformance；
- 防止局部正确组件组合成全局错误语义。

这正是目前 GCPP 最值得继续证明的方向。

---

## 12. Composition Problem / 组合正确性可能是真正核心

F0 当前最大的理论转向：

```text
individual layer correctness
!=
composed provenance correctness
```

例如：

```text
valid signature
+
valid watermark detector
+
valid metadata parser
+
valid adapter
```

仍然可能产生：

```text
misleading provenance conclusion
```

原因包括：

- 语义冲突未检测；
- Scope 丢失；
- Evidence capability 被错误升级；
- relation 误传递；
- omission；
- time/freshness 被忽略。

这与分布式系统/安全系统中的 compositionality 问题类似。

因此 F0 可把核心研究问题进一步改写为：

> **Under what conditions does composition of individually valid provenance components preserve globally valid verification semantics?**

中文：

> **多个局部都正确的来源组件，在什么条件下组合后仍保持全局验证语义正确？**

这比“如何再定义一份 provenance record”更接近基础协议问题。

---

## 13. Candidate Safety Properties

截至本轮，不是 Core，只作为要被形式化/反驳的性质：

```text
P1 Boundary Preservation
P2 Non-Amplification
P3 Explicit Downgrade on Boundary Loss
P4 Open-World Default
P5 Coverage Transparency
P6 No Implicit Relation Transitivity
P7 No Implicit Scope Inheritance
P8 Evidence-Capability Preservation
P9 Cross-Layer Conflict Visibility
P10 Observation/Inference/Policy Separation
```

问题不是这十项是否“听起来对”，而是：

- 是否独立？
- 是否可合并？
- 是否可机器测试？
- 是否已有成熟形式系统？
- 是否两个实现能一致判断？
- 是否真实减少行业错误？

---

## 14. Kill Criteria / 终止条件

为了避免项目自我合理化，F0 为这条新方向设置终止条件。

若出现以下任一情况，应停止把 Verification-Boundary architecture 推向独立 GCPP Core：

1. 现有 PROV + RDF + RATS + SHACL/规则体系可以无需新增公共语义层完整实现全部 safety properties；
2. “verified semantics stronger/weaker”无法跨 Profile 做机器一致判断；
3. Scope/Projection 的跨媒体抽象无法形成稳定 conformance；
4. Relation Contract 必须依赖一个中心化、不可维护的全球 ontology；
5. 两个独立实现对 amplification/lossless mapping 结果长期无法一致；
6. 实际行业测试显示这些错误可完全由现有 verifier UI 修复，而不需要协议层语义；
7. 增加边界信息的复杂度/隐私成本明显高于避免的风险。

F0 必须允许最终结论是：

```text
Do not create GCPP Core 0.3.
```

---

## 15. Continue Criteria / 继续条件

只有至少满足以下条件，才考虑进入 Candidate Core：

1. 能构造真实跨标准案例，字段合法但 verification semantics 被洗白；
2. Safety properties 能检测这种错误，而现有单标准 verifier 无法独立检测；
3. 能定义小型、非中心化的 Profile Contract；
4. 两个独立实现能对 test vectors 得到相同结果；
5. 能证明未知/丢失信息始终安全降级；
6. 能与 C2PA / PROV / RDF / RATS / VC 等现有载体共存而不替代它们；
7. 真实应用（新闻、Agent、科研、AI 来源、模型 lineage）至少两个领域受益于同一套 invariant。

---

## 16. 下一轮研究

F0-R5 应集中在形式化和可执行实验，而不是继续增加理论文档：

1. 用偏序/entailment 而非 assurance score 定义 verified semantics；
2. 建立 minimal `ClaimProfileContract`；
3. 建立 `MappingContract` 的 lossless / weakening / lossy / amplification 判据；
4. 设计 cross-layer contradiction vectors；
5. 设计 omission/coverage vectors；
6. 设计 scope-stripping vectors；
7. 尝试用 SHACL / RDF entailment / existing policy engines 实现同样检查；
8. 若现有机制完全足够，则把 GCPP 收敛为 profile/conformance suite 而非新 protocol core。

---

## 17. 参考资料 / References

- W3C PROV-O: https://www.w3.org/TR/prov-o/
- W3C PROV-DM: https://www.w3.org/TR/prov-dm/
- W3C RDF 1.2 Concepts: https://www.w3.org/TR/rdf12-concepts/
- W3C RDF 1.2 Schema: https://www.w3.org/TR/rdf12-schema/
- Nanopublications: https://nanopub.net/
- IETF RFC 9334 — RATS Architecture: https://www.rfc-editor.org/rfc/rfc9334.html
- Sabelfeld & Sands, Dimensions and Principles of Declassification: https://doi.org/10.1109/CSFW.2005.15
- PREMIS v3.0: https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf
- Nemecek et al., Authenticated Contradictions from Desynchronized Provenance and Watermarking: https://arxiv.org/abs/2603.02378

---

# English

This document aggressively challenges the emerging F0 model against prior art.

Generic provenance graphs are already covered by W3C PROV. First-class propositions, reification and contradictory statements are covered by RDF 1.2 and related knowledge representation systems. Fine-grained assertion provenance is covered by Nanopublications. Evidence-to-verifier-result-to-relying-party-policy separation is a core part of IETF RATS. Facet-dependent preservation has mature digital-preservation precedent. Declassification research already studies boundary dimensions such as what/who/where/when and policy-preserving release.

Therefore GCPP must not claim novelty for nodes, claims, graphs, assessments, boundaries as generic concepts, or provenance laundering as a term.

After this challenge, the only plausible independent value is narrowed to a provenance-specific compositional safety problem:

```text
Verification-Boundary Preservation
Verification Non-Amplification
Open-World Verification Coverage
Cross-Layer Consistency
Testable Interoperability Semantics
```

The core research question becomes: **under what conditions does composition of individually valid provenance components preserve globally valid verification semantics?**

F0 explicitly defines kill criteria. If existing PROV/RDF/RATS/policy tooling can naturally and completely implement these safety properties, or if independent implementations cannot consistently decide semantic amplification/loss, GCPP should not create a new Core protocol merely to justify its existence.
