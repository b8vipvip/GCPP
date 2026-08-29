# F0-10 — 现有机制可行性反证：RDF / SHACL / RATS 是否已经足够？ / Existing-Mechanisms Feasibility Challenge

> 状态 / Status: **F0 Adversarial Feasibility Research / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 研究问题

F0 必须回答一个可能终止 GCPP 独立 Core 的问题：

> **如果 RDF 1.2 + SHACL 1.2 + W3C PROV + IETF RATS 已经能够表达和执行 Verification Non-Amplification / Coverage / Conflict 检查，那么 GCPP 还需要定义什么？**

本轮不假设 GCPP 必须有自己的语法、规则语言或 graph model。

---

## 2. RDF 1.2 可以承担什么

RDF 1.2 当前能力足以作为研究 substrate：

- 表达资源与关系；
- triple term / reification 引用 proposition；
- proposition 不必被自动断言为 fact；
- 对同一 proposition 建立多个 reifier/context；
- 表达潜在冲突 proposition；
- 通过 entailment regime 定义可推导语义。

因此 GCPP **不需要**重新定义：

```text
Graph syntax
Node syntax
Claim syntax
Claim-about-claim syntax
Basic entailment concept
```

---

## 3. SHACL 1.2 Core 可以承担什么

SHACL Core 可以描述：

```text
required properties
cardinality
datatypes
node/value constraints
cross-property constraints
profile conformance
```

并且可以声明需要的 entailment regime。

因此很多 GCPP 边界完整性规则可以通过 Shape 表达，例如：

```text
Assessment with result=SUPPORTED
must have verificationProfile

Partial claim
must preserve scope selector reference

Derived assessment
must reference source assessment(s)

Unknown profile
must not be emitted as SUPPORTED under known profile
```

这些不需要 GCPP 自己写 validator language。

---

## 4. SHACL 1.2 Rules 可以承担什么

SHACL 1.2 Rules 提供：

```text
infer(base graph, rules) -> inference graph
query(base graph, rules, goal) -> derivability result
```

因此 F0-09 的：

```text
Γ ⊨P C_out
```

可以先用 SHACL Rules / RDF entailment 作为**实验性 reference engine**。

例如 Profile 可以定义规则：

```text
byteExactEqual(A,B)
=> normalizedTextEqual(A,B)
```

但不定义反向规则。

或者：

```text
scopeGeneratedBy(P,M)
AND P partOf D
=> D containsSomeGeneratedContent M
```

而没有：

```text
P generatedBy M
=> D generatedBy M
```

这种规则引擎正适合验证 Non-Amplification 的 positive/negative test vectors。

---

## 5. W3C PROV 可以承担什么

PROV 可以承载：

```text
Entity / Activity / Agent
usage / generation / derivation
attribution / association
qualified relation
Bundle
```

所以 GCPP 的 Agent execution、training run、translation activity 等研究完全可以先映射 PROV，而不创建新 Activity model。

---

## 6. IETF RATS 可以提供什么架构纪律

RATS 提供成熟分层：

```text
Evidence
-> Verifier appraisal
-> Attestation Results
-> Relying Party policy
```

因此 GCPP 不需要发明：

```text
Evidence / Result / Policy separation
```

但可以测试来源场景中的：

```text
claim scope
historical relation
mapping/composition
coverage
cross-layer conflict
```

如何进入类似的 verifier-result 模型。

---

## 7. 第一轮结论：通用执行机制已经足够强

截至 F0，本项目**没有发现需要创建 GCPP 自有规则语言或 graph serialization 的理由**。

推荐实验栈：

```text
RDF 1.2
  -> claim/reification research representation

W3C PROV
  -> generic provenance/process vocabulary where applicable

SHACL 1.2 Core
  -> profile constraints

SHACL 1.2 Rules / RDF entailment
  -> conservative derivation experiments

RATS-inspired result separation
  -> Evidence / Assessment / Policy architecture
```

其他载体例如 C2PA / VC / SPDX / CycloneDX / in-toto 通过 Adapter 进入同一测试模型。

---

## 8. 但这些机制并不自动给出 provenance safety contract

现有机制提供：

```text
how to represent
how to constrain
how to infer
```

它们不会自动告诉实现者：

```text
which provenance mapping is semantically safe?
which scope inheritance is valid?
when must verification downgrade?
which evidence layer was not checked?
when are two valid claims in conflict?
what does watermark evidence support?
can training lineage propagate to output attribution?
what happens when a qualifier is stripped?
```

这些必须由 domain Profile / Contract 指定。

因此剩余问题不再是“需要新语言吗”，而是：

> **是否值得建立一套跨 provenance carrier 共用的安全契约、映射规则和 conformance corpus？**

---

## 9. GCPP 的候选最小产品形态被进一步压缩

若后续实验成立，GCPP 最小可能不是一个新的 wire protocol，而是：

```text
GCPP Semantic Safety Core
  ├─ invariants
  ├─ profile contract requirements
  ├─ downgrade rules
  ├─ coverage semantics
  ├─ conflict semantics
  └─ conformance methodology

GCPP Profiles
  ├─ C2PA mapping
  ├─ PROV/RDF mapping
  ├─ RATS/attestation mapping
  ├─ regulatory mapping
  └─ future carriers

GCPP Test Corpus
  ├─ safe entailment vectors
  ├─ unsafe amplification vectors
  ├─ scope loss vectors
  ├─ coverage/omission vectors
  ├─ conflict vectors
  └─ unknown-profile vectors
```

这里没有 GCPP 专有 Manifest。

---

## 10. Protocol 还是 Conformance Suite？

F0 必须接受一个可能结果：

> GCPP 最终可能更像 **semantic interoperability / conformance standard**，而不是传统意义上的新 wire protocol。

这并不降低价值。

TLS 的价值来自 wire protocol；Unicode 的价值来自编码标准；Web Platform Tests 的价值来自跨实现一致性；某些安全规范的核心价值则来自 conformance requirements。

如果 GCPP 真正解决的是：

```text
provenance semantics cannot silently strengthen or become falsely complete across systems
```

那么：

```text
normative invariants + profiles + test corpus
```

可能比自建 serialization 更合理。

---

## 11. GCPP 仍需证明的独立价值

现有工具足以实现，不等于现有生态已经形成共同安全约束。

GCPP 只有在以下问题得到实证时才继续：

### Gap 1 — Cross-carrier mapping safety

同一个 provenance fact 从 C2PA -> RDF -> internal DB -> regulatory metadata 时，是否存在可复现 verification-boundary loss？

### Gap 2 — Multi-layer consistency

C2PA、watermark、attestation、regulatory metadata 同时存在时，现有 verifier 是否会漏掉 semantic clash？

### Gap 3 — Scope preservation

局部来源在跨格式/跨 UI 后是否经常被错误提升成 whole-object 来源？

### Gap 4 — Coverage transparency

verifier 是否能清楚告诉消费者“没检查哪些 Evidence domain”？

### Gap 5 — Conservative derivation portability

同一个 Profile rule 在两个独立引擎上能否得到相同 supported / unsupported result？

如果这些 gap 不存在或成本极低地由现有标准项目修复，则 GCPP 应转为 contribution upstream，而不是建立独立标准。

---

## 12. 实验建议：不要先写 GCPP parser

F0 下一个工程实验不应开发 GCPP serialization parser。

应该开发一个极小 Research Harness：

```text
Input normalized Claim graph
+ Profile/Rules
+ Expected result
      ↓
Reference evaluator
      ↓
SUPPORTED / UNSUPPORTED / UNKNOWN / CONFLICT
+ diagnostics
```

第一版可直接使用：

```text
RDF + SHACL
```

目标是验证思想，不是建立生产依赖。

如果 SHACL 实验失败，再分析失败是：

- 工具限制；
- 表达能力限制；
- GCPP 问题定义错误；
- 需要更强形式系统。

---

## 13. 第一批必须做的 executable vectors

### V1 Scope laundering

```text
source: paragraph-level generated-by claim
mapping: scope stripped
output: whole-document generated-by
expected: UNSAFE_AMPLIFICATION
```

### V2 Safe weakening

```text
source: cryptographically authenticated provider
output: provider identifier present
expected: CONSERVATIVE_WEAKENING
```

### V3 Watermark escalation

```text
source: watermark detected
output: actor authenticated
expected: NOT_ENTAILED / UNSAFE
```

### V4 Lineage escalation

```text
source: model trained-on dataset D
source: model generated output O
output: O sourced-from D
expected: NOT_ENTAILED
```

### V5 Omission coverage

```text
C2PA checked = yes
watermark checked = no
output: “no AI evidence”
expected: INVALID / COVERAGE_INCOMPLETE
```

### V6 Cross-layer clash

```text
credential claim: exclusively-human-origin
watermark assessment: AI-origin signal positive
same aligned scope/time
expected: CONFLICT
```

### V7 Unknown profile

```text
source claim profile unknown
output generic derived-from VERIFIED
expected: INVALID INHERITANCE
```

### V8 Past/current

```text
credential valid at T1
revocation/freshness unknown at T2
output currently-valid
expected: NOT_ENTAILED
```

---

## 14. 当前结论

F0 已经反证了“GCPP 需要自己的通用图/Claim/规则语言”。

当前最合理的研究路线是：

> **复用 RDF/PROV/SHACL/RATS 作为实验 substrate，验证是否存在一个独立的 provenance semantic-safety conformance layer。**

只有 executable vectors 证明真实跨系统问题，并且同一 invariants 可服务多个行业，才考虑 Core Candidate。

---

## 15. 参考资料 / References

- W3C RDF 1.2 Concepts: https://www.w3.org/TR/rdf12-concepts/
- W3C RDF 1.2 Schema: https://www.w3.org/TR/rdf12-schema/
- W3C SHACL 1.2 Core: https://www.w3.org/TR/shacl12-core/
- W3C SHACL 1.2 Rules: https://www.w3.org/TR/shacl12-rules/
- W3C PROV-O: https://www.w3.org/TR/prov-o/
- IETF RFC 9334 — RATS Architecture: https://www.rfc-editor.org/rfc/rfc9334.html

---

# English

F0 finds no current justification for a GCPP-specific graph syntax, claim serialization or rule language. RDF 1.2 can serve as a claim/reification research substrate, W3C PROV can represent generic provenance/process structure, SHACL 1.2 can validate profile constraints and execute inference rules, and the IETF RATS architecture already provides a mature Evidence -> Verifier Result -> Policy separation.

These mechanisms provide representation, constraint and inference machinery, but they do not automatically define provenance-specific semantic safety contracts: safe cross-carrier mappings, scope inheritance, downgrade behavior, evidence coverage, cross-layer conflict, or the exact limits of what an evidence mechanism can support.

Therefore the remaining candidate value of GCPP is further narrowed to a **semantic interoperability/conformance layer** consisting of invariants, profile-contract requirements, downgrade and coverage semantics, conflict rules, and a public executable test corpus.

The next engineering step should not be a GCPP parser. It should be a minimal RDF/SHACL-based research harness that executes positive and negative semantic mapping vectors. If existing mechanisms can already solve all identified failures naturally, GCPP should contribute upstream or shrink rather than invent an unnecessary Core protocol.
