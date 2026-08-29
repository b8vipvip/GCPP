# C0-00 — Prior Art Challenge / 现有工作反证

> 状态：Research only / 非规范性

## 1. C0 不能把“assume/guarantee”当成创新

形式化方法领域已有长期 contract-based design：环境满足 assumption 时，组件提供 guarantee；已有 probabilistic/stochastic contracts、refinement、parallel composition、conjunction、runtime assumption monitoring，以及 learning-enabled autonomous systems 的 assume-guarantee verification。

因此：

```text
ASSUMPTION -> GUARANTEE
```

本身不是 C0 创新。

## 2. C0 不能把 AI quality/capability 描述当成创新

当前标准化已覆盖：

- ISO/IEC 42102：AI methods/capabilities descriptors；
- ISO/IEC 25059：AI quality model，明确考虑 probabilistic outcomes、learning behavior、data reliance；
- IEEE P3777：AI Agent benchmark、performance metrics、evaluation/reporting；
- SLO/error-budget 工程实践：metric + threshold + attainment window + error budget。

因此：

```text
metric / benchmark / descriptor / quality target
```

不是独立协议理由。

## 3. C0 不能把 assurance evidence graph 当成创新

OMG SACM 已提供 Structured Assurance Case Metamodel 和机器可读模型。Dynamic Assurance Cases 研究也已经把运行时证据和持续 assurance 纳入系统。

所以：

```text
claim + argument + evidence
```

也不是新东西。

## 4. 当前唯一可能的窄缺口

旧 contract theory 常假设组件/模型有可定义的行为模型；而黑盒学习型 AI 的保证往往是：

```text
empirical
version-scoped
distribution-scoped
prompt/tool/context-dependent
nonstationary
evaluator-dependent
correlation-sensitive
```

可能缺少的不是 contract 数学，而是一个跨供应商运行时机器关系：

```text
AssumptionSet A
EvidenceSet E
ComponentState V
Context C
   =>
Guarantee G is currently applicable
```

以及：

```text
A violated / V changed / C changed / E stale
=> G must be downgraded or invalidated
```

但这仍可能只是 existing standards 的 profile。

## 5. Kill Criteria

若普通元数据即可表达并执行：

```text
component/version identity
assumption scope
metric semantics
benchmark/evaluator evidence
validity interval
runtime monitor state
dependency/correlation assumptions
invalidation conditions
composition rule reference
```

且这些字段可由 SACM/VC/PROV/ISO descriptors 等承载，则不建立独立 C0 wire protocol。

### 更严格 Kill

即便需要一个共同 vocabulary/profile，也不能自动算“新公共协议”。必须证明该语义：

1. 跨多个行业重复出现；
2. 不能自然上游到既有标准；
3. 是执行安全所必需，不只是便利；
4. 能机器验证，而不是模糊的信任评分。
