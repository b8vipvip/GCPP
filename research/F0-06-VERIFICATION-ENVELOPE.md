# F0-06 — Verification Envelope：边界最小化与关系契约 / Verification Envelope — Boundary Minimization and Relation Contracts

> 状态 / Status: **F0 Research Hypothesis / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 从 7 类边界继续压缩

F0-04 暂列：

```text
Target Boundary
Scope Boundary
Projection Boundary
Temporal Boundary
Evidence Boundary
Authority Boundary
Inference Boundary
```

如果直接把七类都做成 Core 字段，会迅速退化成万能 metadata bag。

本轮目标是继续删除/合并，寻找最小且可测试的结构。

第一轮压缩结果：

```text
Referential Boundary
Interpretation Boundary
Temporal Boundary
Epistemic Boundary
```

这四个名字仍是研究概念，不是最终字段名。

---

## 2. Referential Boundary / 指称边界

合并：

```text
Target/State Boundary
+
Scope Boundary
```

回答：

> **这个 Claim 精确适用于哪个对象状态的哪些部分？**

候选结构：

```text
ReferentialBoundary {
  argument_refs[]
  state_binding_context[]?
  scopes[]?
}
```

核心不要求某种 selector 语法，但要求：

```text
unknown target != identified target
mutable subject != fixed state
unknown scope != whole scope
partial scope != whole scope
```

### 为什么 State 与 Scope 可以放在同一边界

因为二者都在限定 proposition 的“适用集合”：

```text
which version/state?
which portion of that state?
```

它们在数据模型里可以分别编码，但在验证理论里属于同一类问题。

---

## 3. Interpretation Boundary / 解释边界

合并：

```text
proposition/predicate semantics
+
projection/facet semantics
+
relation profile semantics
```

回答：

> **Claim 到底声称了什么，并且依据什么解释规则比较/理解对象？**

例如：

```text
byte equality
normalized-text equality
quoted-from
translated-from
used-in-training
watermark-detected
signed-by
```

都不是裸字符串；它们必须由 Profile 定义语义。

候选结构：

```text
InterpretationBoundary {
  claim_profile
  predicate
  projection_profile?
  relation_contract?
}
```

### 核心原则

```text
UNKNOWN PREDICATE SEMANTICS
=> NO INHERITED VERIFICATION
```

如果 Adapter 不理解 source predicate 的精确语义，不能只按名称相似进行强映射。

---

## 4. Temporal Boundary / 时间边界

保持独立。

原因是 provenance 系统至少同时存在多种时间：

```text
event occurrence time
claim issuance time
evidence observation time
assessment time
validity/freshness interval
retraction/supersession time
```

这些时间对验证含义有直接影响，不能全部塞进普通 context。

候选结构：

```text
TemporalBoundary {
  occurrence_time?
  issuance_time?
  observation_time?
  assessment_time?
  validity_interval?
  freshness_context?
}
```

不是每个 Claim 都需要所有字段。

Core 要求是语义角色不能静默互换。

---

## 5. Epistemic Boundary / 认识论边界

合并：

```text
Evidence Boundary
+
Authority / Origin Boundary
+
Inference Boundary
```

回答：

> **我们为什么认为这个 Claim 得到支持？谁观察/声明/验证？支持来自直接观察、第三方证明还是推导？证据能力的边界是什么？**

候选结构：

```text
EpistemicBoundary {
  claim_origin_role
  evidence_refs[]
  evidence_profiles[]
  inference_refs[]?
  verifier_ref?
  assessment_profile?
  assumptions[]?
  limitations[]?
}
```

### Origin Role

至少需要区分：

```text
asserted
observed
attested
inferred
reconstructed
```

再由 Profile 描述：

```text
first-party
counterparty
independent
regulatory
...
```

Core 不把这些角色排列成一个统一“可信度等级”。

---

## 6. Verification Envelope / 验证包络

F0 Round 4 提出一个新的研究抽象：

# Verification Envelope

它不是新的 credential container。

它表示：

> **某个 Assessment 能安全声称其已验证支持的最大语义范围。**

研究表达：

```text
Envelope(A) = {
  referential,
  interpretation,
  temporal,
  epistemic
}
```

重要：

```text
Envelope != Evidence payload
Envelope != Credential format
Envelope != Policy decision
```

同一 Evidence 可以通过不同 verification profile 产生不同 Envelope；同一 Claim 也可以拥有多个独立 Assessment/Envelope。

---

## 7. 为什么叫 Envelope，而不是 Assurance Level

`Level` 暗示：

```text
LOW < MEDIUM < HIGH
```

但 provenance 支持关系通常不可全序。

例如：

Assessment A：

```text
exact scope
first-party signature
fresh
```

Assessment B：

```text
whole object
independent audit
older
```

哪个“更高”没有通用答案。

所以 Envelope 表达的是边界，不是分数。

---

## 8. Relation Contract / 关系契约

F0 发现不能只注册 predicate 名称。

每种关系/Profile 若要支持自动推导，必须公开它的机器可测试 contract。

候选字段：

```text
RelationContract {
  predicate_id

  argument_roles
  required_boundaries

  scope_semantics
  projection_semantics
  temporal_semantics

  composition_rules[]
  inheritance_rules[]

  allowed_evidence_profiles[]?
  forbidden_inferences[]
}
```

这不是要求所有 relation 都有复杂逻辑。

最安全默认值是：

```text
composition = none
scope_inheritance = none
implicit_transitivity = false
```

---

## 9. 一个关键反例：Whole -> Part 也不能通用继承

直觉上似乎：

```text
whole object verified
=> each part verified
```

但这取决于 Claim。

### Claim A

```text
whole document contains some AI-generated content
```

不能推出：

```text
every paragraph contains AI-generated content
```

### Claim B

```text
whole archive contains file X
```

不能推出：

```text
every archive member contains X
```

### Claim C

```text
whole text bytes exactly equal source
```

若 selector mapping 确定，则某些子范围 equality 可以安全继承。

所以：

> **Scope inheritance is predicate-specific.**

候选 Core 不变量：

```text
NO IMPLICIT SCOPE INHERITANCE
```

只有 Relation/Claim Profile 明确声明的 heredity rule 才可使用。

---

## 10. Relation 的逻辑性质也不能默认

一个 predicate 可能具有：

```text
symmetric?
transitive?
reflexive?
functional?
scope-hereditary?
time-monotone?
```

GCPP Core 不替领域定义这些性质。

但如果系统要做自动 provenance composition，就必须从受信 Profile 获得这些性质。

### 例子

`byte-equal`：通常对固定字节对象是 equivalence relation。

`was-revision-of`：不能简单当成对所有属性都传递。

`was-quoted-from`：标签层面可能存在链，但具体 quoted scope 不自动传递。

`trained-on`：不能传递到输出来源。

`watermark-detected`：不是 provenance derivation relation。

---

## 11. Claim Profile 与 Evidence Profile 必须分开

一个常见设计错误是把：

```text
watermark profile
```

同时当成：

```text
claim semantics + detection algorithm + attribution policy
```

F0 建议分开：

### Claim / Relation Profile

定义：

```text
what proposition means
```

### Evidence Profile

定义：

```text
what is observed
how it is verified
what claim families it can support
limitations / assumptions
```

### Assessment Profile

定义：

```text
how evidence is appraised for a claim
```

这三个 Profile 可以由同一标准文档一起发布，但语义角色必须独立。

---

## 12. Safe Mapping Contract / 安全映射契约

跨标准 Adapter 需要证明：

```text
Envelope(output)
```

没有超过：

```text
ConservativeClosure(Envelope(inputs), NewEvidence)
```

候选 Mapping 类型：

```text
EQUIVALENT
CONSERVATIVE_WEAKENING
EVIDENCE_AUGMENTED
BOUNDARY_LOSSY
UNSAFE_AMPLIFICATION
UNKNOWN
```

### EQUIVALENT

四类边界语义均可保留。

### CONSERVATIVE_WEAKENING

主动输出更弱 Claim，例如：

```text
cryptographically authenticated actor
-> actor identifier present
```

### EVIDENCE_AUGMENTED

通过新增 Evidence 支持更强结论。

### BOUNDARY_LOSSY

某些 Scope/Projection/Time/Epistemic 信息无法表达，下游必须降级。

### UNSAFE_AMPLIFICATION

没有新增 Evidence，却输出 source semantics 不足以蕴含的已验证结论。

---

## 13. Envelope Preservation 的机器测试思想

未来 conformance test 不只比较 JSON 字段。

测试：

```text
Input Assessment
      ↓ Adapter
Output Assessment
```

检查：

1. target/state 是否相同或有明确 mapping；
2. scope 是否保持、缩小或丢失；
3. predicate/projection 是否等价或保守弱化；
4. time/freshness 是否保留；
5. Evidence origin/capability 是否被保留；
6. inference 是否有可审计 source claims；
7. 若输出更强，是否存在 new evidence。

这会直接发现“字段映射正常但含义升级”的错误。

---

## 14. Unknown Predicate / Unknown Profile 的安全行为

长期公共协议必须能面对未来扩展。

如果 verifier 不认识：

```text
claim_profile = future.example.foo
```

安全行为：

```text
record preserved
profile_unknown = true
verification semantics = not interpreted
```

不能：

- 把未知 relation 自动退化成 `derived-from`；
- 把未知 Evidence 当 generic proof；
- 假设 scope = whole；
- 丢弃 qualifier 后继续显示绿色 verified。

这与 algorithm agility 同等重要，可称为：

# Semantic Agility / 语义敏捷性

---

## 15. Boundary Stripping / 边界剥离

定义研究攻击：

```text
Input Claim + boundaries
        ↓
intermediate system removes qualifiers
        ↓
output retains positive provenance label
```

这可能是：

- 恶意；
- UI 简化；
- schema 不兼容；
- metadata sanitizer；
- export tool bug；
- legacy database limitation。

无论原因，协议结果都应一样：

> **无法表达的验证边界必须导致验证降级，而不是维持原状态。**

---

## 16. Selective Disclosure 的约束

隐私要求允许隐藏 Evidence payload，但不能隐藏到使 proof boundary 被误解。

例如可以披露：

```text
evidence_type = confidential-audit
claim_family = dataset-used-in-training
scope = dataset-version-X
verifier = auditor-A
result = supported
full audit report = withheld
```

但不能只剩：

```text
verified = true
```

所以 selective disclosure 必须保留足够的 Envelope 元信息，或者明确降级为无法判断。

候选原则：

```text
SELECTIVE DISCLOSURE MAY HIDE EVIDENCE CONTENT
BUT MUST NOT MISREPRESENT EVIDENCE CAPABILITY
```

---

## 17. Verification Envelope 是否真需要成为存储对象？

尚未确定。

有两个方案：

### Option A — Explicit Envelope Object

Verifier 输出统一 Envelope 结构。

优点：

- 易测试；
- 易跨标准映射；
- UI/Policy 易消费。

缺点：

- 可能过度抽象；
- 容易重复 Assessment schema。

### Option B — Derived Envelope View

Envelope 从 Claim + Assessment + Profiles 推导。

优点：

- Core 更小；
- 不重复存储。

缺点：

- 不同 verifier 可能推导不一致；
- Adapter conformance 更复杂。

F0 暂不决定。

---

## 18. 当前最小候选架构

对象类型继续保持极少：

```text
Referent / Node
Claim
```

但 GCPP 的价值不来自这两个对象。

真正候选 Core 是一组验证不变量：

```text
Boundary-qualified claims
+ Profile-defined semantics
+ Evidence capability boundaries
+ Conservative derivation
+ Non-amplification
+ Explicit downgrade on information loss
```

因此 GCPP 可能最终更像：

> **A semantic safety protocol for provenance interoperability**

而不是：

> another provenance storage format.

---

## 19. F0 当前需要重点反驳的新假设

新的危险是：

> “Verification Boundary Model 听起来很好，所以直接标准化。”

不能这样做。

下一步必须尝试反驳：

1. 四类 Boundary 是否其实可以完全由现有 PROV/RDF/RATS + Profile 组合解决？
2. Non-Amplification 是否已经是某个成熟 trust/information-flow formalism 的直接实例？
3. `Verification Envelope` 是否只是换名的 attestation result？
4. Scope/Projection 是否能跨媒体形成足够稳定的抽象？
5. Relation Contract 会不会发展成不可维护的全球 ontology？
6. 保守推导是否能做到无需中心治理？
7. Mapping conformance 是否能被两个独立实现一致计算？

如果这些问题回答不好，GCPP 仍不应进入新 Core。

---

## 20. 参考资料 / References

- W3C PROV-O: https://www.w3.org/TR/prov-o/
- W3C RDF 1.2 work: https://w3c.github.io/rdf-schema/spec/
- IETF RFC 9334 — RATS Architecture: https://www.rfc-editor.org/rfc/rfc9334.html
- Nanopublications: https://nanopub.net/
- PREMIS v3.0: https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf

---

# English

F0 compresses seven provisional verification-boundary dimensions into four research boundaries:

```text
Referential
Interpretation
Temporal
Epistemic
```

The **Referential Boundary** identifies which fixed target/state and which scopes a claim applies to. The **Interpretation Boundary** defines the proposition, predicate, projection/facet and relation semantics. The **Temporal Boundary** separates event, issuance, observation, assessment, validity and freshness semantics. The **Epistemic Boundary** captures claim origin, evidence capability and inference provenance.

Together they form a candidate **Verification Envelope**: not a credential container or trust score, but the maximum semantic extent that an assessment can safely claim as supported.

A central finding is that even whole-to-part inheritance is not universally safe. Predicate semantics determine whether scope narrowing preserves a claim. Therefore GCPP should default to no implicit scope inheritance, no implicit transitivity and no relation composition unless a profile publishes an explicit machine-testable contract.

The candidate Core value is increasingly not an object model, but a semantic safety layer: boundary-qualified claims, profile-defined semantics, explicit evidence capability, conservative derivation, verification non-amplification, and mandatory downgrade when qualification information is lost.
