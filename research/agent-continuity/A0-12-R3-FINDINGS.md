# A0-12 — R3 研究结论 / A0-R3 Findings

> 状态 / Status: **Research Findings / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. R3 对独立协议假设非常不利

R3 当前没有发现一个必须由新 Agent Succession wire protocol 承担的跨域 coordination primitive。

相反，剩余问题不断被分解成：

```text
Relationship Authority Semantics
        +
Generic Distributed Coordination
```

其中：

- Relationship Authority Semantics 决定某项权利/义务/信誉/许可到底能否转移、由谁确认、是否需要 reissue；
- Generic Distributed Coordination 负责 prepare/commit/abort/compensate/version/recovery/receipt。

这两层都已有成熟理论和实现基础。

## 2. Candidate Decomposition Hypothesis

R3 提出一个需要继续反驳的分解假设：

> **任何安全的 Agent lifecycle succession，都可以被表示为一组由各自 relationship authority 控制的关系状态转换；若这些转换之间存在联合一致性要求，则使用通用事务/工作流协调，而不需要 Agent-specific global succession primitive。**

形式化草图：

```text
Agent transition T: A -> {B1 ... Bn}

For each external relationship Ri:
  Authority(Ri) decides
    transfer / reissue / deny / retain / split / unresolved

If consistency group G requires joint outcome:
  Coordinate({decision(Ri) | Ri in G})
  using generic atomic or compensating mechanism
```

A0 必须找到一个无法被这个分解安全表达的真实场景，才能继续独立协议方向。

## 3. 全局 successor 不是默认不变量

R3 进一步确认：

```text
one lifecycle transition
!= one universal successor for all relationships
```

例如：

```text
bank grant -> B
contract duty -> C
reputation -> reissue required
network admission -> fresh auth
license -> non-transferable
```

这些可以同时正确。

因此任何 `Agent Continuity Certificate` 或 `sameAgent=true` 如果被下游解释成所有关系整体继承，都存在过度声明风险。

## 4. 原子 succession 只是条件性需求

如果业务要求：

```text
R1, R2, R3 must all transfer to B or none transfer
```

那么它就是一个 atomic business transaction。

WS-AtomicTransaction / 2PC 等 prior art 已覆盖协调形态。

如果事务很长且允许补偿：

```text
R1 committed
R2 committed
R3 fails
=> compensate R2/R1 where defined
```

则属于 Saga / WS-BusinessActivity 类问题。

所以：

```text
atomic succession
compensating succession
```

都不是新理论。

## 5. Provider shutdown 不会产生“魔法协议”

R3 把 provider shutdown 分成两类：

### Coordinator disappears

这是可靠分布式系统问题，可以使用 durable state、replication、participant receipts、recovery protocol、choreography 等降低风险。

### Indispensable authority disappears before decision

这是信息/授权缺失问题。

正确结果是：

```text
UNRESOLVED
ABORT
REISSUE_FROM_ALTERNATE_AUTHORITY (only if pre-authorized)
```

而不是协议自行确认 transfer。

重要不变量：

```text
COORDINATION CANNOT CREATE AUTHORITY
```

## 6. Obligation 仍重要，但不是通用 succession primitive

Outstanding obligations 仍然是高价值场景，但 R3 发现：

```text
obligation persistence
```

与：

```text
obligor reassignment
```

必须分离。

ODRL、workflow/event sourcing 可以表示并保持 duty；是否允许从 A 改成 B，仍然必须由 contract/counterparty semantics 决定。

公共层可以携带决定，但不能替代决定。

## 7. Reputation 同样不是可守恒资产

Reputation 是某 evaluator/issuer 对 subject 的评价关系。

因此：

```text
fork => no automatic copy
merge => no additive union
migration => no automatic applicability
```

可由 issuer：

```text
reissue
reassess
reference predecessor history
deny inheritance
```

处理。

这更像 credential lifecycle，而不是 Agent-specific succession transaction。

## 8. R3 可执行结果

R3 harness 使用：

```text
authority-owned relationship state
version/epoch
exclusive relation constraint
optional atomic consistency group
```

测试：

```text
Multi-Issuer Fork
Obligation Double Assignment
Successor Race
Provider Dies Mid-Succession
Reputation Split
Merge with Conflicting Duties
Revocation During Succession
Partial Evidence Loss
```

第一实现结果：

```text
8 / 8 matched expected
```

这只证明这些安全结果可被通用 coordination model 表达，不证明跨实现互操作，更不证明需要新协议。

## 9. A0 当前生死判定

经过 R1/R2/R3，以下独立创新候选基本被淘汰或大幅降级：

```text
same-agent identity
key continuity
memory continuity
runtime continuity
authority non-multiplication
rollback fencing
multi-party commit state machine
compensation state machine
```

尚未发现无法被已有机制组合吸收的核心 primitive。

因此当前默认研究立场应改成：

> **Independent Agent Continuity/Succession Protocol is NOT justified unless a new counterexample survives decomposition.**

## 10. 是否立即终止 A0？

不立即关闭研究，因为还需要最后一轮更强反证：

### R4 — Open-World / Byzantine / No-Coordinator Challenge

重点测试：

```text
unknown authorities
malicious or equivocal authority
conflicting signed acknowledgements
offline authorities
partial trust graph
no shared coordinator
no shared clock
cross-domain discovery of required participants
relationship authority set changes during transition
```

如果这些仍然可以被：

```text
standard signed statements
trust policy
transparency / durable logs
consensus/fencing where needed
generic choreography
```

自然吸收，那么 A0 应正式判定：

```text
NO NEW PUBLIC WIRE PROTOCOL
```

后续价值只保留为 threat model / conformance suite / interoperability guidance。

---

# English

R3 strongly weakens the case for an independent Agent Continuity/Succession protocol. The remaining problem currently decomposes into relationship-authority semantics plus generic distributed coordination. Atomic succession reduces to distributed commit; long-running succession reduces to business activity/Saga compensation; missing indispensable authority must remain unresolved. A final R4 Byzantine/open-world/no-coordinator challenge is required before terminating the protocol direction.