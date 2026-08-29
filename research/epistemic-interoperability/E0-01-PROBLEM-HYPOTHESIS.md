# E0-01 — 问题假设 / Problem Hypothesis

> 状态：Research Hypothesis / 非规范性

## 1. 不是“confidence 标准化”

E0 当前不假设所有 AI 都能、都应该输出一个可直接比较的概率。

不同系统中的 `0.9` 可能分别表示：

- token/logit-derived confidence；
- verbal self-confidence；
- empirical correctness estimate；
- calibrated probability；
- conformal coverage target；
- ensemble agreement fraction；
- heuristic score；
- policy threshold；
- belief mass。

因此：

```text
SAME NUMBER != SAME SEMANTICS
```

## 2. 核心对象：Epistemic Contribution

对于已有判断集合 Γ，新消息 M 的价值不能只由内容相同/不同判断。

研究问题：

```text
Contribution(M | Γ)
```

至少需要区分：

```text
NEW_INDEPENDENT_SUPPORT
NEW_DEPENDENT_SUPPORT
REDUNDANT_SUPPORT
CONTRADICTORY_SUPPORT
INCOMPARABLE_UNCERTAINTY
OUT_OF_CALIBRATION_DOMAIN
UNVERIFIED_SELF_REPORT
UNKNOWN_DEPENDENCE
```

这些只是研究分类，不是规范枚举。

## 3. 为什么多 Agent 让问题变得危险

传统 expert aggregation 早已知道 dependent experts 会导致重复计算共同信息。

LLM/Agent 系统把这个问题放大：

```text
shared base model
shared pretraining corpus
shared RAG evidence
shared system prompt
shared tool output
conversation-induced persuasion
agent copying another agent's answer
common evaluator/judge
```

这些相关性经常对 orchestrator 不透明。

于是：

```text
5 votes
```

可能实际只有：

```text
1 informational source + 4 transformations
```

## 4. 候选安全不变量

### P1 — No Agreement Amplification by Default

```text
AGREEMENT != INDEPENDENT EVIDENCE
```

没有独立性/依赖信息时，不应因为多个 Agent 一致就默认提升到更强置信结论。

### P2 — Confidence Comparability Requires Semantics

```text
NUMERIC CONFIDENCE != COMPARABLE PROBABILITY
```

只有 measurement semantics、target proposition、calibration scope 等兼容时才允许数值聚合。

### P3 — Calibration Is Conditional

```text
CALIBRATED_ON(D1) != CALIBRATED_ON(D2)
```

校准依赖任务域、数据分布、时间、模型版本、推理流程和测量方法。

### P4 — Self-Report Is Evidence About a Report

```text
SELF_REPORTED_CONFIDENCE != EMPIRICAL_RELIABILITY
```

除非有外部校准或验证关系。

### P5 — Shared Evidence Limits Marginal Contribution

若两个判断完全依赖相同证据或一个由另一个派生，则第二个判断不能被默认计为完整独立支持。

### P6 — Unknown Dependence Must Downgrade Aggregation

```text
UNKNOWN_DEPENDENCE => NO INDEPENDENCE ASSUMPTION
```

### P7 — Abstention Is First-Class

安全系统必须允许：

```text
INCOMPARABLE
UNKNOWN
NOT_CALIBRATED_HERE
INSUFFICIENT_NEW_INFORMATION
```

而不是强迫输出一个统一 confidence。

## 5. 最关键的创新风险

这些原则本身并不新：expert judgment、Dempster-Shafer、Bayesian pooling、probabilistic graphical models 都处理依赖性。

E0 真正需要证明的是：

> 是否存在一个**跨供应商机器互操作缺口**：统计理论知道“必须考虑依赖”，但接收方没有标准方式知道一个远程 AI judgment 的 uncertainty semantics、calibration contract 与 information-dependency contract，因此无法选择正确的已知聚合方法。

如果这个缺口只需普通 provenance + metadata schema 即可解决，E0 仍应被终止。

## English summary

E0 focuses on the boundary between *statistical aggregation theory* and *cross-system machine interoperability*. Existing mathematics already explains why correlated experts must not be treated as independent. The unresolved hypothesis is whether heterogeneous AI systems need a portable contract that tells receivers what a confidence measure means, where it is calibrated, and how its information dependencies relate to other judgments.