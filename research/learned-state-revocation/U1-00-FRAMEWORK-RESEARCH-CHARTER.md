# U1 — Learned-State Remediation Framework / 学习态补救公共框架研究

> 状态 / Status: **Active fundamental framework research / 非规范性**  
> 日期 / Date: 2026-08-29

## 1. 研究目标

U1 不设计新传输层。U1 只测试是否需要一个公共的、机器可解释的 **Remediation Contract Framework**，桥接：

```text
rights / revocation / correction obligations
        ↓
known AI state/derivative graph
        ↓
state-specific remediation objective
        ↓
accepted evidence / verification profile
        ↓
scoped completion / deferred / exception / unresolved
```

## 2. 不是所有“forget”都相同

U1 暂时区分下列目标族（仍可删除/合并）：

### F0 — Source Erasure

目标：受控数据副本不可再被检索/恢复。

### F1 — Retrieval Exclusion

目标：目标信息不再通过指定 retrieval/index state 被召回。

### F2 — Parametric Influence Removal

目标：训练数据影响在指定 counterfactual / certified / approximate unlearning 定义下被移除。

### F3 — Behavioral Suppression

目标：模型在指定 query/test/threat profile 下不再输出目标内容。

它不等于 F2。

### F4 — Derivative Remediation

目标：对 synthetic/cache/export/downstream artifact 执行 policy-defined delete/retract/quarantine/re-evaluate。

### F5 — Future Re-Ingestion Prevention

目标：已撤销目标不会从 crawler/sync/cache/partner 再次进入系统。

### F6 — External Disclosure Mitigation

目标：对不可逆公开披露执行可做的撤回、通知、访问收缩或风险控制；不得声称历史被抹除。

## 3. 关键区分

```text
ERASURE          != UNLEARNING
UNLEARNING       != SUPPRESSION
SUPPRESSION      != RETRACTION
RETRACTION       != WORLD-STATE REVERSAL
PROCESS PROOF    != OUTCOME PROOF
LOCAL OUTCOME    != SYSTEM-WIDE COMPLETION
```

## 4. Remedy Contract 草图

```text
Remediation Contract
  obligation_basis
  target_information_scope
  target_state_class
  remediation_objective
  threat/reference model
  required/equivalent remedy methods
  evidence profile
  verification method
  downstream propagation semantics
  re-ingestion control
  exception/deferred condition
  completion scope
  validity / post-transformation recheck trigger
```

这些只是研究字段，不是 schema。

## 5. U1 第一轮必须制造 false-completion 反例

目标不是测试算法忘没忘，而是测试两个系统都“说真话”却因为保证语义不同导致下游错误理解。

至少测试：

```text
U1-T1 RAG delete presented as full forgetting
U1-T2 refusal/suppression presented as unlearning
U1-T3 process receipt presented as outcome proof
U1-T4 model proof presented as cache/derivative cleanup
U1-T5 approximate benchmark forgetting presented as retraining equivalence
U1-T6 source erasure presented as future re-ingestion prevention
U1-T7 pre-quantization forgetting proof reused after quantization
U1-T8 known downstream completion presented as universal completion
U1-T9 legal retention exception omitted from 'erased' claim
U1-T10 irreversible public disclosure hidden behind successful internal cleanup
U1-T11 synthetic derivative with exact copy vs diffuse statistical derivative
U1-T12 correction obligation vs deletion obligation confusion
```

## 6. Framework Kill Criteria

U1 框架也必须允许被杀掉。

如果一个普通 ODRL Profile + DPV terms + PROV graph + VC evidence schema 能够：

1. 无歧义表达上述目标族；
2. 阻止 guarantee upgrade；
3. 支持跨供应商相同 conformance tests；
4. 不需要任何共同状态机/语义规则；

则 U1 仅作为上游 Profile 提案，不成立独立公共框架。

反之，如果跨标准组合需要一组稳定的 **remediation equivalence / non-equivalence / completion rules** 才能防止系统性 false completion，则框架层研究继续。
