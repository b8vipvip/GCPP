# F0-07 — 开放世界完整性与验证覆盖 / Open-World Completeness and Verification Coverage

> 状态 / Status: **F0 Research Hypothesis / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 为什么 Verification Non-Amplification 仍然不够

F0-05 提出了：

> **没有新增可验证 Evidence 或明确的保守推导规则，系统不得把输入中较弱/较窄的已验证语义升级成更强的 VERIFIED 结论。**

这可以阻止：

```text
partial -> whole
watermark detected -> actor authenticated
self-declared -> independently verified
training lineage -> output attribution
past-valid -> current-valid
```

但它不能完整处理另一类现实问题：

> **一个系统没有显式升级任何已有 Claim，却通过遗漏某些 Claim / Evidence / verification layer，使剩余的合法信息形成一个看起来“完整”的错误来源叙述。**

这不是单纯的 amplification，而是 **completeness / coverage ambiguity**。

---

## 2. 现实验证：Authenticated Contradictions / Integrity Clash

2026 年研究《Authenticated Contradictions from Desynchronized Provenance and Watermarking》展示：

```text
same digital asset
  ├─ cryptographically valid C2PA provenance statement
  └─ independently detectable AI watermark
```

两个验证层都可以分别通过各自验证，却表达互相冲突的来源信息。

研究进一步展示：不需要破坏签名；仅通过标准编辑流程和语义字段遗漏，就可能产生带有有效签名、但对 AI 来源产生误导的 provenance presentation。

因此：

```text
VALID CREDENTIAL != COMPLETE PROVENANCE STORY
VALID LAYER A != CONSISTENT WITH LAYER B
ABSENCE OF AI CLAIM != EVIDENCE OF HUMAN ORIGIN
```

这证明来源系统必须研究：

```text
what was checked?
what was expected to be checked?
what was unavailable?
what was omitted?
what conflicting evidence was observed?
```

而不能只输出：

```text
verified = true
```

---

## 3. Open-World Provenance / 开放世界来源语义

F0 提出默认原则：

> **Provenance is open-world by default.**

即：一个记录没有声明某事实，默认只意味着：

```text
that fact is not established by this record
```

而不是：

```text
the opposite fact is established
```

例如：

```text
no AI-generation assertion present
```

默认不能推出：

```text
human-generated
```

同样：

```text
no distillation evidence found
```

不能推出：

```text
no distillation occurred
```

候选不变量：

```text
NOT DISCLOSED != ABSENT
NOT OBSERVED != NOT PRESENT
NO POSITIVE CLAIM != NEGATIVE CLAIM
UNAVAILABLE EVIDENCE != NEGATIVE EVIDENCE
```

---

## 4. Closed-World Assertions 必须显式声明边界

某些场景确实需要证明：

```text
this list is complete
```

例如：

- 软件 SBOM 声明包含全部运行时依赖；
- 审计报告声明检查了指定训练数据目录的全部记录；
- 一个生成执行声明完整列出所有外部工具调用；
- 一个 provenance manifest 声明在 Profile P 下完整描述某一类 action。

这不是 Open World 的反例。

它意味着：

> **Completeness 本身必须成为一个有 Scope、Profile、Authority、Time 和 Evidence 的 Claim。**

不能存在裸：

```text
complete = true
```

更接近：

```text
CompletenessClaim {
  subject
  claim_family / domain
  scope
  temporal_interval
  completeness_profile
  asserted_by
  evidence
}
```

例如：

```text
“在生成执行 E 的 14:00:00–14:00:12 区间内，
 Profile tool-call-v1 要求记录的全部外部工具调用都已列出。”
```

这比：

```text
provenance complete
```

严格得多。

---

## 5. Verification Coverage / 验证覆盖

F0 提出一个新的候选 Assessment 维度：

# Verification Coverage

它回答：

> **这个 verifier 实际检查了哪些 Claim family / Evidence layer / Scope，以及哪些没有检查、无法检查或不适用？**

候选研究结构：

```text
VerificationCoverage {
  target_ref
  verification_profile

  claim_families_expected[]
  claim_families_checked[]
  claim_families_not_checked[]

  evidence_layers_expected[]
  evidence_layers_checked[]
  evidence_layers_unavailable[]

  scope_checked
  temporal_window?

  completeness_assumptions[]
  closed_world_domains[]
  diagnostics[]
}
```

这不一定最终成为一个存储对象；可以是 Assessment 的派生视图。

但“检查覆盖率/覆盖域”本身不能被一个布尔 `verified` 替代。

---

## 6. Evidence Coverage 与 Content Coverage 不同

必须分开：

### Content / Scope Coverage

回答：

```text
which parts of the subject are covered by a Claim?
```

### Verification Coverage

回答：

```text
which evidence/claim domains did the verifier actually evaluate?
```

例如一张图片可以：

```text
content_scope = whole image
C2PA_signature_checked = yes
watermark_layer_checked = no
```

因此：

```text
whole-content binding verified
```

仍然不等于：

```text
all provenance evidence layers checked
```

---

## 7. Completeness 是相对于 Domain 的，而不是绝对属性

任何可测试的 completeness 都必须有一个封闭域：

```text
Complete(X | Domain D, Profile P, Scope S, Time T)
```

例如：

```text
complete list of declared external tool calls
under Agent-Audit-Profile-v1
for execution E
```

不能推出：

```text
complete account of all causal influences on E
```

所以：

```text
DOMAIN-COMPLETE != UNIVERSALLY COMPLETE
```

这与 Verification Boundary 模型一致：complete claim 自己也有 Referential / Interpretation / Temporal / Epistemic boundaries。

---

## 8. Evidence of Absence / 不存在证据

F0 之前已经固定：

```text
ABSENCE OF EVIDENCE != EVIDENCE OF ABSENCE
```

现在进一步定义 Evidence of Absence 的最低研究要求。

若系统想支持：

```text
X was not present / did not occur
```

Evidence Profile 至少必须声明：

```text
search_space
coverage/completeness assumption
observation method
sensitivity / detection limit
time window
failure modes
unobservable regions
freshness
```

例如：

```text
“在 Profile W 支持检测的图像区域、阈值 θ、扰动模型 A 下未检测到 watermark。”
```

只能支持：

```text
not detected under W/θ/A
```

除非 Profile 对 detection completeness 有额外证明，否则不能支持：

```text
no watermark exists
```

候选不变量：

```text
NEGATIVE CLAIM REQUIRES EXPLICIT OBSERVATION DOMAIN
```

---

## 9. Cross-Layer Consistency / 跨层一致性

当多个 Evidence layer 同时存在时，GCPP 不应选一个“最权威字段”覆盖其他层。

候选模型：

```text
Layer A -> Assessment A
Layer B -> Assessment B
Layer C -> Assessment C

             ↓
Consistency Analysis
```

Consistency Analysis 可以输出：

```text
CONSISTENT
POTENTIALLY_CONFLICTING
DIRECTLY_CONFLICTING
INCOMPARABLE
INSUFFICIENT_SEMANTIC_MAPPING
NOT_CHECKED
```

这些名称仍是研究词汇。

关键是：

> **两份分别有效的 Evidence 可以支持相互冲突的 Claims。密码学有效性不会自动消解语义冲突。**

---

## 10. Conflict 本身不意味着哪一方是假的

例如：

```text
Claim C1: human editing occurred
Claim C2: AI-generation watermark detected
```

它们可能：

- 真正矛盾；
- 同时成立（AI 生成后又由人编辑）；
- 只在错误 UI 下看似矛盾；
- Claim scope 不同；
- 时间不同；
- 一个是 origin claim，一个是 modification claim。

所以 Conflict Analyzer 必须先比较：

```text
predicate semantics
scope
temporal boundaries
claim origin
evidence capability
```

不能只比较字符串。

---

## 11. Omission Laundering / 遗漏洗白

F0-05 定义了多类 Provenance Claim Laundering。

本轮新增一种更基本形式：

# Omission Laundering

定义：

> 一个系统保留了某些正面、合法、已验证 Claim，却丢弃了能够改变用户解释的其他已知相关 Claim / Evidence / coverage information，从而产生一个语义上过度完整的叙述。

例子：

```text
Known:
  C2PA manifest valid
  watermark positive

Exported UI:
  “Content Credentials verified”
  [watermark result omitted]
```

如果 UI/Adapter 没有声称“human-generated”，它可能不违反狭义 Non-Amplification；但它仍可能产生完整性误导。

所以需要：

```text
Non-Amplification
+
Coverage Transparency
```

两者正交。

---

## 12. “相关 Evidence”不能无限扩张

如果要求 verifier 检查世界上所有可能 Evidence，协议不可实现。

因此需要 Profile 定义：

```text
Expected Evidence Set
```

候选：

```text
VerificationProfile {
  claim_families
  required_evidence_layers
  optional_evidence_layers
  prohibited_inferences
  completeness_domain
  conflict_rules
  downgrade_rules
}
```

例如一个 `AI-Origin-Audit-v1` Profile 可以要求：

```text
- C2PA/credential layer
- registered watermark detectors supported for this asset type
- regulatory AIGC metadata if jurisdiction adapter enabled
```

如果某层不可用，输出：

```text
coverage incomplete
```

而不是：

```text
origin not AI
```

Core 不规定具体需要哪些技术层。

---

## 13. Completeness Claims 也可能冲突

例如：

```text
Provider A:
  “this is the complete generation action history”

Independent Auditor B:
  “tool call T was omitted”
```

这不是特殊情况。

Completeness 仍然只是一个 Claim，必须允许：

```text
support
challenge
contradict
supersede
retract
```

因此 GCPP 不建立中心化“最终完整记录”。

---

## 14. Selective Disclosure 与 Completeness 的张力

隐私系统可能有：

```text
all required events committed
but only some events disclosed
```

协议必须区分：

```text
record completeness
```

和：

```text
disclosure completeness
```

例如可以证明：

```text
Merkle root commits to N events
Auditor attests all required event classes are represented
Public disclosure reveals only 3 events
```

此时：

```text
public details incomplete
```

但可能存在：

```text
confidential completeness evidence
```

所以 selective disclosure 不应自动降低所有 provenance 到 unknown；关键是不要虚假宣称“你看到的就是全部”。

候选不变量：

```text
COMPLETE COMMITMENT != COMPLETE DISCLOSURE
```

---

## 15. Verification Coverage 与 Non-Amplification 的组合

F0 当前提出两个正交安全轴：

### Axis A — Strength Safety

Verification Non-Amplification：

```text
No unsupported semantic strengthening.
```

### Axis B — Coverage Safety

Verification Coverage Transparency：

```text
Do not present an unchecked/partial evidence space as exhaustive.
```

这两者共同防止：

```text
weak -> strong
```

以及：

```text
partial view -> complete story
```

---

## 16. Candidate Assessment 输出

研究版：

```text
Assessment {
  claim_ref
  result
  envelope

  verification_coverage {
    checked_domains
    unchecked_domains
    unavailable_domains
    closed_world_assumptions
  }

  conflicts[]
  diagnostics[]
}
```

Presentation 层若只显示“Verified”，必须能同时保留/展示必要的：

```text
verified what?
under which profile?
what was not checked?
```

否则 UI 本身可能造成 provenance semantic amplification。

---

## 17. 与监管 Required Disclosure 的边界

法律/监管可以要求某些字段必须存在。

例如某法域规定必须标注 AI 生成。

GCPP Core 不判断：

```text
legal_compliance = true/false
```

但 Adapter/Profile 可以表达：

```text
required claim family present / missing / malformed / not checked
```

再由 Policy 层判断合规。

因此：

```text
REQUIRED BY POLICY
!=
TRUE BY PROTOCOL
```

---

## 18. F0 当前新增候选不变量

```text
PROVENANCE IS OPEN-WORLD BY DEFAULT
NOT DISCLOSED != ABSENT
NOT OBSERVED != NOT PRESENT
NO POSITIVE CLAIM != NEGATIVE CLAIM
VALID CREDENTIAL != COMPLETE PROVENANCE STORY
DOMAIN-COMPLETE != UNIVERSALLY COMPLETE
NEGATIVE CLAIM REQUIRES EXPLICIT OBSERVATION DOMAIN
COMPLETE COMMITMENT != COMPLETE DISCLOSURE
UNCHECKED EVIDENCE DOMAIN MUST NOT BE PRESENTED AS NEGATIVE EVIDENCE
```

同样，这些目前仍是 Research Invariants，不是 normative Core。

---

## 19. 下一轮必须反驳

1. `Verification Coverage` 是否只是已有 verifier diagnostic 的换名？
2. Expected Evidence Set 是否会让 GCPP 退化成中心化 profile registry？
3. 如何避免“检查得越多越可信”的错误总分思维？
4. 如何表达未知 Evidence layer 而不导致无限枚举？
5. cross-layer conflict 是否可以通过 Claim graph + Profile 完全表达而无需新 primitive？
6. completeness claim 是否能够用通用 Claim 语义表示，不需要专门对象？
7. 两个独立 verifier 对相同 coverage profile 能否得到一致 checked/unchecked 结果？
8. selective disclosure 下的 completeness 能否被机器验证，而不泄露隐藏内容？

---

## 20. 参考资料 / References

- Nemecek et al., “Authenticated Contradictions from Desynchronized Provenance and Watermarking”, arXiv:2603.02378, 2026: https://arxiv.org/abs/2603.02378
- W3C RDF 1.2 Concepts and Abstract Data Model: https://www.w3.org/TR/rdf12-concepts/
- W3C PROV-DM: https://www.w3.org/TR/prov-dm/
- IETF RFC 9334 — RATS Architecture: https://www.rfc-editor.org/rfc/rfc9334.html

---

# English

F0 finds that Verification Non-Amplification is necessary but insufficient. A provenance system can avoid explicitly strengthening any claim yet still mislead by omitting relevant claim/evidence layers and presenting the remaining valid information as a complete provenance story.

The 2026 “Authenticated Contradictions from Desynchronized Provenance and Watermarking” study demonstrates a concrete form of this problem: independently valid provenance metadata and AI watermark verification can produce semantically conflicting provenance signals without any cryptographic break.

GCPP therefore adopts an **open-world provenance** research default: missing or undisclosed provenance does not establish the opposite fact. Completeness must itself be an evidence-backed, domain-scoped, time-scoped claim under an explicit profile.

A new candidate assessment dimension, **Verification Coverage**, records what claim families and evidence layers a verifier expected, checked, did not check, or could not access. Content/scope coverage and verification/evidence coverage are distinct.

F0 now studies two orthogonal safety axes:

```text
Verification Non-Amplification
  -> do not make supported semantics stronger without evidence

Verification Coverage Transparency
  -> do not present a partial or unchecked evidence space as exhaustive
```

Negative claims require an explicit observation domain and completeness/sensitivity assumptions. Selective disclosure may hide evidence content, but complete commitment must not be confused with complete public disclosure.
