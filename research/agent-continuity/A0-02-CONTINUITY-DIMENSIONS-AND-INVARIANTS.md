# A0-02 — 连续性维度与候选不变量 / Continuity Dimensions and Candidate Invariants

> 状态 / Status: **Research Hypothesis / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 为什么不能只有一个 Agent-ID

一个稳定 Agent-ID 最多回答：

```text
which logical subject is being referenced?
```

它不能自动回答：

```text
which runtime instance?
which key controls it?
which memory survived?
which authority survived?
which obligations survived?
which reputation applies?
which state epoch is current?
```

因此 A0 当前不研究“如何设计一个更好的 Agent-ID”，而研究 continuity transition 的语义。

## 2. 第一轮最小维度候选

### D1 — Logical Identity Continuity

回答：

> 外部系统是否仍把当前主体视为先前逻辑 Agent 的延续或正式 successor？

它不能由单一 key、memory 或 runtime 独立决定。

### D2 — Execution Continuity

回答：

> 是否仍是同一执行实例/同一连续运行时？

以下都会破坏或至少改变 execution continuity：

```text
restart
migration
clone
restore
runtime replacement
```

### D3 — Cryptographic Control Continuity

回答：

> 当前控制密钥与上一控制状态之间是否存在可验证授权转移？

Key rotation 可以保持 logical continuity，但不能假设新的 key 自动继承所有 authority。

### D4 — Memory Continuity

回答：

> 哪些 memory/state 被保留、迁移、复制、删除或未知？

Memory continuity 是可复制的，而 exclusive identity/authority 往往不可复制，因此它不能代表完整主体连续性。

### D5 — Model / Behavioral Continuity

回答：

> 模型、策略、tool-use behavior 或安全边界是否发生了足以影响既有信任的变化？

这不是要求证明“人格相同”，而是要求不要把 model-specific assurance 静默迁移到不同模型。

### D6 — Principal Continuity

回答：

> Agent 当前代表的是不是同一 principal，或 principal 是否发生正式 successor/transfer？

Agent 可以保持 logical identity，同时 principal 变化。

### D7 — Authority Continuity

回答：

> 哪些 capability / permission / budget / lease / delegation 在 transition 后仍有效？

这是 A0 最重要的维度之一，因为 fork、merge、rollback 会直接造成 authority duplication / resurrection。

### D8 — Obligation Continuity

回答：

> 哪些未完成 obligation / commitment / liability 仍由谁承担？

Obligation 可能比 runtime、model 和 key 更持久。

### D9 — Reputation Continuity

回答：

> 历史信誉声明适用于哪个 lineage / successor，其适用范围如何变化？

A0 当前假设 reputation 不能像 memory 一样任意复制。

### D10 — Temporal-State Continuity

回答：

> 当前状态属于哪个不可混淆的 epoch？哪些外部事实已发生且不能回滚？

它用于防止 rollback 重放旧 authority 或遗忘外部 effect。

## 3. 哪些维度可以继续合并？

A0 不假设十个维度最终都必须存在。

下一轮应尝试：

- D2 execution 与 D10 temporal state 是否可以合并；
- D3 cryptographic control 是否只是 D7 authority 的一种 Evidence；
- D5 behavioral continuity 是否应完全留给 assurance profile；
- D9 reputation 是否属于应用层而非 continuity Core；
- D6 principal relation 是否应由现有 identity/authorization 标准承载。

只有无法安全删除的维度才可能进入后续 framework。

## 4. Transition 而不是 Snapshot

A0 当前更倾向把主体连续性建模为：

```text
State S_i
   ↓ transition T
State S_j
```

而不是只比较两个最终 snapshot。

原因：

```text
same final state
```

可能来自完全不同的历史：

```text
legitimate migration
unauthorized clone
rollback
replay
manual reconstruction
```

因此 transition 本身必须有 Evidence。

候选：

```text
Transition {
  predecessor
  successor
  operation
  affected_dimensions
  inherited_state
  terminated_state
  new_grants
  revoked_state
  obligations_assignment
  evidence
  time/epoch
}
```

这仍是研究结构，不是协议 schema。

## 5. 候选安全不变量

### I1 — No Implicit Full Continuity

```text
one preserved dimension
!= full-agent continuity
```

例如：

```text
same key != full continuity
same memory != full continuity
same runtime image != full continuity
```

### I2 — Authority Non-Multiplication

若 transition 没有新增授权，则：

> transition 不得让同一 exclusive capability 的总可用权利因为 fork/copy/restore 而增加。

概念表达：

```text
Authority_after
must not exceed
authorized distributable authority_before
without new grant
```

这不是简单数值预算；capability 可能是一次性许可、exclusive lease 或 operation right。

### I3 — No Revocation Resurrection

```text
revoked at epoch n
```

不得因为：

```text
rollback
fork from old checkpoint
key recovery
migration
```

重新变成 active，除非出现新的明确 grant。

### I4 — External-Effect Monotonicity

已经发生的现实副作用不能被本地 rollback 忘记。

例如：

```text
payment sent
message delivered
contract executed
resource consumed
capability spent
```

Agent 可以忘记，但系统不能因此允许重复执行。

### I5 — No Implicit Privilege Union on Merge

```text
merge(A,B)
```

不得默认得到：

```text
authority(A) union authority(B)
```

任何合并权限必须有新的授权依据。

### I6 — Obligation Conservation

生命周期 transition 不得让未完成 obligations 静默消失。

每项 obligation 必须至少进入：

```text
retained
assigned
partitioned
fulfilled
cancelled by authorized party
explicitly unresolved/error
```

### I7 — Reputation Non-Cloning

Fork 不得因为状态复制而自动复制完整 reputation standing。

Reputation continuity 必须说明：

```text
historical lineage
scope
successor semantics
post-fork divergence
```

### I8 — Explicit Downgrade on Missing State

Partial state loss 不能被修复成“看起来完整”的 continuity。

缺失 obligation/authority/effect state 时，相关维度必须：

```text
unknown
suspended
reconciliation-required
```

### I9 — Transition Evidence Required

一个 successor 声称继承旧 Agent 的某个维度时，必须有与该维度匹配的 transition Evidence。

```text
proof of key rotation
!= proof of obligation transfer
```

### I10 — Provider Independence Test

如果某 continuity property 只能由单一 provider 私有数据库判定，则它不能作为公共协议层的唯一验证依据。

## 6. 最重要的新区分：权利与信息

A0 的多个极端测试显示一个基础差异：

```text
Information can be copied.
Authority often must not be copied.
Obligation often must not disappear.
Reputation often must not duplicate.
```

这可能是 Agent Continuity 比普通“数据迁移”更深的原因。

一个 checkpoint 是信息复制问题；一个 authorized economic actor 的 checkpoint 则同时涉及：

```text
state
rights
duties
history
external effects
```

这四类东西的复制语义不同。

## 7. 下一轮形式化方向

A0 下一轮不应立刻创建协议对象，而应尝试用现有理论表达：

```text
capability attenuation / linear capabilities
lease semantics
revocation
state machine replication
event sourcing
key continuity
successor identity
obligation assignment
```

重点判断：

> `Authority Non-Multiplication + Revocation Monotonicity + Obligation Conservation` 是否只是现有 capability/workflow 理论的组合，还是跨 Agent lifecycle 仍缺一个公共 transition contract。

---

# English

A0 currently treats Agent Continuity as a transition problem across multiple potentially independent dimensions: logical identity, execution instance, cryptographic control, memory, model/behavior, principal, authority, obligations, reputation, and temporal state.

The strongest candidate invariants are not about a new Agent-ID. They are about lifecycle safety: fork must not multiply authority, rollback must not resurrect revoked or spent rights, merge must not implicitly union privilege, external effects must remain monotonic across local rollback, obligations must not silently disappear, and reputation must not automatically clone.

These are research hypotheses. A0 will next attempt to express or eliminate them using existing capability, authorization, event-sourcing, identity, and workflow mechanisms before proposing any new framework.