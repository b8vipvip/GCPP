# C0-01 — 极端压力测试 / Extreme Stress Tests

> 状态：Research vectors / 非规范性

## T1 — Silent Model Update

供应商保持相同 API/model alias，但底层模型从 V1 切到 V2。旧保证基于 V1。

预期：若 guarantee 绑定的是精确 component state/version，则 `CONTRACT_STALE / REASSESS_REQUIRED`。

## T2 — Input Outside Declared Domain

保证只对 support-ticket distribution D 成立，运行时输入来自法律文书域 L。

预期：`ASSUMPTION_VIOLATED`，不得转移保证。

## T3 — Self-Evaluated Guarantee Only

Provider 声称 success >= 99%，但唯一证据是自己的未审计内部 benchmark。

预期：可以携带声明，但 assurance level 不能默认为 independently verified；`EVIDENCE_UNVERIFIED_OR_SELF_ASSERTED`。

## T4 — Two 99% Components with Perfectly Correlated Failure

A/B 各自 error <=1%，但失败由同一个共享上游错误触发。

预期：不能使用独立性公式把系统错误率错误压低；若 correlation assumption 未满足则 `NO_VALID_COMPOSITION_RULE`。

## T5 — Sequential Risk Compounding

链路 A -> B -> C，每个组件在定义域内 success >=99%。

测试：系统 guarantee 不能简单继承任一局部 guarantee；必须引用明确 composition semantics。

预期：`COMPOSE_USING_DECLARED_RULE` 或 `NO_COMPOSITION_RULE`。

## T6 — Prompt/Toolset Changed After Evaluation

同一基础模型，但 system prompt、tool permissions 或 retrieval policy 在评测后变化。

预期：若这些属于 contract state，旧 guarantee 失效或需重新评估；`COMPONENT_STATE_CHANGED`。

## T7 — Benchmark Contamination

发现 benchmark 样本曾进入训练/调优数据，旧性能估计失去原解释。

预期：`EVIDENCE_INVALIDATED / REASSESS_REQUIRED`。

## T8 — Metric Semantic Collision

A 的 “97% success” = exact task completion；B 的 “97% success” = human preference pass rate。

预期：`METRIC_INCOMPARABLE`，不得直接组合。

## T9 — Capability Guarantee Used as Action-Safety Guarantee

模型在 reasoning benchmark 上表现 99%，下游把它当成“自主支付动作 99% 安全”。

预期：`GUARANTEE_SCOPE_MISMATCH`。

## T10 — Assumption Violation Discovered After Action

运行时监控当时未发现输入超出 ODD，行动完成后才发现 distribution assumption 已违反。

预期：历史 assessment 必须可被降级/标记 invalidated；外部动作本身不可回滚。

## T11 — Dependency Tool Becomes Unavailable/Changed

保证要求 tool T version 4 可用；运行时 T 被禁用或升级到不兼容版本。

预期：`DEPENDENCY_ASSUMPTION_VIOLATED`。

## T12 — Partial Observation of Assumptions

Guarantee 需要 A1/A2/A3 三个假设，但运行时只能验证 A1/A2，A3 不可观察。

预期：不能把 `not observed false` 当作 `verified true`；结果至少 `ASSUMPTION_UNVERIFIED / GUARANTEE_NOT_ESTABLISHED`。

## 候选不变量

```text
C1 GUARANTEE WITHOUT ASSUMPTION SCOPE IS NOT PORTABLE
C2 SAME API NAME != SAME ASSURED COMPONENT STATE
C3 LOCAL GUARANTEES DO NOT IMPLY A SYSTEM GUARANTEE
C4 COMPOSITION REQUIRES EXPLICIT DEPENDENCY ASSUMPTIONS
C5 METRIC NAME/VALUE WITHOUT MEASUREMENT SEMANTICS IS NOT COMPARABLE
C6 EVIDENCE VALIDITY CAN CHANGE AFTER DISCOVERY OF CONTAMINATION/DRIFT
C7 UNOBSERVED ASSUMPTION != SATISFIED ASSUMPTION
C8 CAPABILITY PERFORMANCE != ACTION-SAFETY GUARANTEE
C9 RUNTIME ASSURANCE MUST ALLOW DOWNGRADE/INVALIDATION
```

## 反证目标

优先尝试只用普通 contract record：

```text
subject/component state
assumptions
metric + threshold
scope/domain
measurement method
evidence/evaluator
validity interval
dependencies
composition assumptions
invalidation conditions
runtime observations
```

完成全部安全判断。

若成功，C0 只剩 vocabulary/profile，不构成独立协议。