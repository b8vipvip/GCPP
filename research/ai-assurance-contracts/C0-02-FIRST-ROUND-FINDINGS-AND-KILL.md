# C0-02 — 第一轮结论与 Kill Decision / Findings

> 状态 / Status: **Final C0 finding for independent-protocol hypothesis / 非规范性**

## 1. 判定

C0 的问题是真问题：学习型 AI 的保证确实具有 distribution、version、prompt/tool/context、evidence 和 dependency 条件。

但目前没有证据证明需要一个新的独立：

```text
AI Assurance Contract Protocol
AI Behavioral Guarantee Wire Format
```

### Kill Decision

```text
INDEPENDENT C0 WIRE PROTOCOL:
NOT JUSTIFIED — STOP PROTOCOLIZATION
```

## 2. 为什么

首轮 12 个黑盒 AI 极端场景全部可由通用字段和既有 contract/assurance 理论保守处理：

```text
component state binding
assumption scope
metric semantics
evidence status
dependency assumptions
runtime observations
validity/invalidation
composition-rule reference
```

结果为 12/12 matched expected。

## 3. Prior art 已覆盖核心理论

现有生态已经分别覆盖：

- probabilistic/stochastic assume-guarantee contracts；
- runtime monitoring of assumptions；
- learning-enabled system assume-guarantee verification；
- dynamic assurance cases；
- ISO/IEC AI quality/capability descriptors；
- IEEE Agent benchmarking；
- SACM machine-readable assurance cases；
- SLO / error-budget monitoring；
- statistical risk monitoring under distribution shift。

因此 C0 最合理的未来形态只是这些机制之间的 interoperability profile，而不是独立栈。

## 4. 保留的长期原则

```text
GUARANTEE WITHOUT ASSUMPTION SCOPE IS NOT PORTABLE
SAME API ALIAS != SAME ASSURED COMPONENT STATE
LOCAL GUARANTEES != SYSTEM GUARANTEE
COMPOSITION REQUIRES EXPLICIT DEPENDENCY ASSUMPTIONS
METRIC VALUE WITHOUT MEASUREMENT SEMANTICS IS NOT COMPARABLE
UNOBSERVED ASSUMPTION != SATISFIED ASSUMPTION
CAPABILITY PERFORMANCE != ACTION-SAFETY GUARANTEE
ASSURANCE MUST SUPPORT DOWNGRADE / INVALIDATION
```

## 5. 结论

这些原则有工程价值，但它们更适合作为：

```text
AI assurance interoperability profile
runtime assurance guidance
adversarial conformance corpus
upstream proposals to existing assurance/benchmark standards
```

而不是 GCPP 的新独立公共协议方向。
