# F0-09 — 保守蕴含模型：把 Verification Envelope 从对象降级为语义闭包 / Conservative Entailment Model

> 状态 / Status: **F0 Formalization Research / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 为什么继续删除 Verification Envelope

F0-06 暂时提出：

```text
Verification Envelope =
  Referential Boundary
  + Interpretation Boundary
  + Temporal Boundary
  + Epistemic Boundary
```

它有助于解释“一个 Assessment 到底验证到了哪里”。

但如果把 Envelope 做成独立 Core object，可能再次创造一个不必要的 container。

F0 本轮尝试：

> **完全删除显式 Verification Envelope 对象，只用 Claim semantics + Profile-defined entailment + Assessment provenance 推导它。**

---

## 2. 用 Entailment 定义“安全变弱”

W3C RDF 等语义体系使用一个非常一般的思想：

```text
A entails B
```

表示所有使 A 成立的解释也使 B 成立。

GCPP 不需要复制 RDF semantics，但可以复用这个抽象原则。

设 verifier 已支持 Claim 集合：

```text
Γ = {C1, C2, ... Cn}
```

在明确的 Claim/Mapping Profile `P` 下：

```text
Γ ⊨P C_out
```

表示：

> 在 Profile P 声明的语义与假设下，输入已支持 Claims 足以保守地支持输出 Claim。

如果不成立：

```text
Γ ⊭P C_out
```

则没有新增 Evidence 时，输出不能继承 VERIFIED/SUPPORTED 状态。

这给 Verification Non-Amplification 一个更精确的形式：

```text
NO NEW EVIDENCE
AND Γ ⊭P C_out
=> C_out MUST NOT be marked supported-by-inherited-verification
```

---

## 3. “更强/更弱”不需要统一 Assurance Score

定义 Claim `A` 比 `B` 语义更强的一种方式：

```text
A ⊨ B
but
B ⊭ A
```

例如：

```text
A: byte-exact-equal(X,Y)
B: normalized-text-equal(X,Y)
```

在某个确定 normalization Profile 下可能：

```text
A ⊨P B
```

但通常：

```text
B ⊭P A
```

所以从 A 继承到 B 可能安全，反向不安全。

这比：

```text
A assurance = 90
B assurance = 70
```

更精确，也避免把 Scope、Authority、Time、Evidence capability 压成单一分数。

---

## 4. Scope 直接进入 Claim 语义，而不是外部等级

考虑：

```text
C1: paragraph P was generated-by Model M
C2: document D was generated-by Model M
```

如果 `P ⊂ D`：

```text
C1 ⊭ C2
```

所以 `partial -> whole` 自动升级自然被 entailment 阻止。

但：

```text
C3: document D contains-some-content-generated-by M
```

若 Profile 定义 `generated-by(P,M)` 且 `P ⊂ D` 足以支持 `contains-some-content-generated-by(D,M)`，则：

```text
C1 ⊨P C3
```

这说明 Scope inheritance 不是全局规则，而是 predicate/profile entailment 的一部分。

---

## 5. Relation Composition 同样由 Entailment Profile 控制

输入：

```text
C1: A R B
C2: B S C
```

默认：

```text
{C1,C2} ⊭ A T C
```

除非 Profile 显式定义：

```text
R ∘ S => T
```

并满足：

- argument/state alignment；
- scope mapping；
- temporal compatibility；
- projection semantics；
- required Evidence conditions。

因此：

```text
NO IMPLICIT PROVENANCE TRANSITIVITY
```

可以直接实现为：

```text
no entailment rule => no inherited support
```

---

## 6. Evidence 不是前提事实，而是 Assessment 的支持基础

必须避免一个逻辑误区：

```text
Evidence E
```

本身不等于：

```text
Claim C is true
```

所以研究模型至少分两层：

### Evidence Appraisal

```text
Evidence E
+ Verification Profile V
=> Assessment A supports Claim C
```

### Claim Entailment / Mapping

```text
supported Claims Γ
+ Claim/Mapping Profile P
=> derived Claim C_out
```

因此：

```text
raw Evidence entailment
```

与：

```text
claim semantics entailment
```

必须分离。

这与 IETF RATS 的 Evidence -> Verifier Result -> Relying Party 分层兼容。

---

## 7. Assessment Provenance 不能丢失

一个 Derived Assessment 必须能够回答：

```text
which input assessments?
which claim entailment profile?
which profile version?
which assumptions?
was new evidence added?
what information was lost?
```

候选研究结构：

```text
DerivedAssessment {
  output_claim
  input_assessment_refs[]
  entailment_profile
  entailment_profile_version
  new_evidence_refs[]
  lost_qualifications[]
  result
}
```

这本身也可以表示成 generic Claim/PROV structure，不要求新 container。

核心要求只是：

> **派生支持必须可追溯到输入支持与明确推导规则。**

---

## 8. Verification Envelope 改成 Derived View

删除显式 Envelope 后，可以定义：

```text
SupportedClosure(Γ, P)
  = { C | Γ ⊨P C }
```

它表示：

> 在当前 Profile 下，不增加新 Evidence 时，输入支持 Claims 可以安全派生出的 Claim 集合。

这就是原 Verification Envelope 更精确的语义版本。

因此：

```text
Verification Envelope
```

可以降级为：

```text
human-facing name for SupportedClosure / boundary view
```

而不是 normative storage object。

---

## 9. Open-World Completeness 不能仅靠 Entailment 解决

Entailment 解决：

```text
what follows from known supported claims?
```

但不解决：

```text
are all relevant claims known?
```

例如：

```text
Γ contains no AI-origin claim
```

不能推出：

```text
human-origin
```

因为 provenance 默认 Open World。

所以 F0-07 的 Verification Coverage 仍是正交需求。

形式上：

```text
absence(C from Γ)
```

不等于：

```text
Γ ⊨ ¬C
```

除非存在显式 Closed-World / Completeness Claim：

```text
Complete(Γ | domain D, profile P, scope S, time T)
```

并且 Profile 定义 negative inference。

---

## 10. Completeness Claim 本身也进入 Entailment

若有：

```text
C_complete:
  all events of class ToolCall
  for execution E
  under profile P
  during interval T
  are represented in set S
```

并且：

```text
ToolCall X not in S
```

能否推出：

```text
X did not occur
```

仍取决于：

- completeness Evidence；
- Profile 的 closed-world semantics；
- observation sensitivity；
- event identity rules；
- time/scope alignment。

所以 negative entailment 应默认关闭。

候选不变量：

```text
NEGATIVE ENTAILMENT REQUIRES EXPLICIT CLOSED-WORLD PROFILE
```

---

## 11. Cross-Layer Conflict 可转成 Satisfiability / Compatibility 问题

多个 independently supported Claims：

```text
Γ = {C1, C2, C3}
```

可以研究：

```text
Compatible(Γ | P)?
```

或：

```text
Satisfiable(Γ | P)?
```

但现实 provenance predicate 未必都有完整形式逻辑。

因此 Profile 可以只定义有限 conflict rules：

```text
C1 conflicts-with C2 when boundaries align
```

未知 relation 不得自动判断冲突。

### 重要区别

```text
logical contradiction
```

与：

```text
operational provenance conflict
```

可能不同。

例如：

```text
AI-generated
human-edited
```

通常可以同时成立。

只有：

```text
exclusively-human-origin
```

与：

```text
AI-generated-origin
```

在相同 Scope/Time/Profile 下才可能直接冲突。

---

## 12. Mapping Contract 最小化

F0 不需要定义一个巨大的 global relation ontology。

一个 Adapter 只需声明它实际支持的有限 mapping：

```text
MappingRule {
  source_profile
  source_claim_pattern
  target_profile
  target_claim_pattern
  direction
  conditions
  proof/test vectors
}
```

方向可为：

```text
EQUIVALENT
SOURCE_ENTAILS_TARGET
TARGET_ENTAILS_SOURCE
INCOMPARABLE
```

如果：

```text
SOURCE_ENTAILS_TARGET
```

则 source -> target 可以保守继承支持；反向不可以。

如果 `INCOMPARABLE`：只能携带原 Claim 或降级为 unknown/uninterpreted。

---

## 13. Mapping 的“安全性”可以用 Test Vectors 而不是全局证明

现实 Profile 可能无法提供机器可证明的完整逻辑。

公共标准仍可要求：

- normative rule text；
- positive entailment vectors；
- negative/non-entailment vectors；
- boundary-loss vectors；
- conflict vectors；
- unknown-profile behavior；
- version migration vectors。

两个独立实现必须对这些向量得到相同结果。

这样 GCPP 的价值更接近：

```text
semantic conformance discipline
```

而不是新的 theorem prover。

---

## 14. 一个更小的 Candidate Core 形态

经过 F0-09，甚至可以继续删除大量对象模型。

候选 Core 可能只需要规定：

```text
1. Claim profiles have explicit semantics.
2. Evidence appraisal produces traceable support for claims.
3. Support may be inherited only through declared conservative entailment/mapping rules.
4. Missing qualification causes downgrade, not widening.
5. Absence is open-world unless an explicit completeness/closed-world profile applies.
6. Conflicts among independently supported claims remain visible.
7. Mapping/derivation provenance is preserved.
8. Unknown profiles never inherit positive verification by default.
```

而：

```text
Node
Claim
Evidence serialization
Signature format
Graph syntax
```

全部复用现有标准。

---

## 15. F0 当前最重要的理论变化

原来问题是：

```text
What are the universal provenance objects?
```

现在变成：

> **What are the minimum semantic safety rules for transferring verification support between provenance claims?**

中文：

> **来源声明之间“验证支持”在跨系统转移时，最小的语义安全规则是什么？**

这比定义新的 Manifest / Entity / Evidence container 更小，也更可能长期稳定。

---

## 16. 仍需反驳

1. 是否可以直接采用 RDF entailment + SHACL/SHACL Rules，不需要任何 GCPP Core？
2. Claim Profile semantics 能否做到跨非-RDF carrier 一致？
3. `Γ ⊨P C` 在复杂 AI/semantic relation 上是否可计算？
4. 如果大量 Profile 只能靠 prose + test vectors，是否仍足够形成公共协议？
5. Mapping Profile 谁治理？如何去中心化发现与版本化？
6. malicious profile 是否可以声明危险 entailment？需要什么 trust policy？
7. conservative entailment 与 Evidence strength/quality 如何正交表示？
8. Closed-world completeness 如何证明而不产生隐私泄露？

---

## 17. 参考资料 / References

- W3C RDF 1.2 Concepts and Abstract Data Model: https://www.w3.org/TR/rdf12-concepts/
- W3C RDF 1.2 Semantics: https://www.w3.org/TR/rdf12-semantics/
- W3C PROV-O: https://www.w3.org/TR/prov-o/
- IETF RFC 9334 — RATS Architecture: https://www.rfc-editor.org/rfc/rfc9334.html

---

# English

F0 further minimizes the Verification Envelope concept. It does not need to become a new Core object. Instead, verification support can be modeled through **conservative entailment** over explicitly profiled claim semantics.

Given supported claims `Γ`, an output claim may inherit support without new evidence only if `Γ` entails that output under an explicit mapping/claim profile. This naturally prevents partial-to-whole scope escalation, unsafe relation transitivity and other verification amplification without requiring a global assurance score.

A derived view such as `SupportedClosure(Γ,P) = { C | Γ entails C under P }` can replace a stored Verification Envelope.

Open-world completeness remains orthogonal: absence of a claim from `Γ` is not evidence for its negation. Negative inference requires an explicit closed-world/completeness profile with a defined observation domain and supporting evidence.

This pushes the candidate GCPP Core toward a much smaller role: semantic safety rules for transferring verification support between provenance claims, while reusing existing standards for graph syntax, claims, signatures, evidence containers and transport.
