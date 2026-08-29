# E0 — Epistemic Interoperability / AI 认知证据互操作研究

> 状态 / Status: **Fundamental Research — active, non-normative**  
> 分支 / Branch: `research/e0-epistemic-interoperability`  
> 日期 / Date: 2026-08-29

## 中文

E0 不是“再造一个 confidence 字段协议”。它研究一个更窄、也更危险的问题：

> 当多个异构 AI / Agent 对同一问题给出判断时，下游系统如何区分“新增独立信息”与“同一信息被复制、重述、共享上下文同步或互相说服后形成的相关共识”？

当前核心风险：

```text
AGREEMENT != INDEPENDENT EVIDENCE
NUMERIC CONFIDENCE != COMPARABLE PROBABILITY
SELF-REPORTED CONFIDENCE != CALIBRATED ERROR RATE
SHARED CONTEXT CAN CREATE CORRELATED FAILURE
MORE AGENTS != MORE INFORMATION
```

E0 的目标不是强迫所有 AI 使用同一种概率理论，而是先验证是否存在一个跨模型、跨供应商稳定的最小互操作安全问题：

```text
Can a receiver determine whether a new AI judgment
adds independent epistemic support,
adds dependent/redundant support,
or is not safely aggregable with prior judgments?
```

### 当前文件

- `E0-00-NOVELTY-SCREEN.md` — 新方向筛选与已淘汰候选。
- `E0-01-PROBLEM-HYPOTHESIS.md` — Epistemic Contribution 假设与候选不变量。
- `E0-02-PRIOR-ART-CHALLENGE.md` — W3C uncertainty、ISO UQ、expert aggregation、conformal prediction 等反证。
- `E0-03-EXTREME-STRESS-TESTS.md` — 12 个极端测试。
- `e0-stress-vectors.json` — 机器可读研究向量。

### Kill Criteria

如果以下组合已经足够：

```text
existing probabilistic / uncertainty representations
+
calibration metadata
+
ordinary provenance / dependency graphs
+
standard statistical aggregation
+
domain policy
```

并且不需要任何 AI-specific interoperable semantic contract，则停止 E0 协议化。

只有当出现跨供应商反复存在的失败：

```text
locally valid judgments
+
locally valid confidence/uncertainty
+
valid transport/provenance
=> unsafe confidence amplification after composition
```

且现有理论缺少一个可机器验证的跨系统边界时，才继续研究公共层。

## English

E0 investigates **epistemic interoperability** for heterogeneous AI systems: not merely how to serialize a confidence number, but how a receiver can distinguish new independent support from correlated, duplicated, shared-context, or persuasion-amplified support. The research will aggressively attempt to reduce the problem to existing uncertainty representation, calibration, provenance, expert aggregation, and statistical methods before proposing any new protocol.