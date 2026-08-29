# A0-07 — Distributed-Systems Falsification / 用成熟分布式系统理论反证 A0

> 状态 / Status: **A0-R2 Adversarial Research / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 目标

A0 第一轮把 fork、rollback、revocation resurrection 看成很强的 Agent Continuity 问题。

R2 必须问：

> **这些问题是否其实只是已有 distributed-systems failure modes 在 AI Agent 上的重新出现？**

如果是，就不应创建 Agent-specific primitive。

## 2. Checkpoint rollback ~= stale worker / stale leader

Agent 从旧 checkpoint 恢复：

```text
A(epoch=7)
```

但现实系统已经推进：

```text
world(epoch=9)
```

此时 Agent 可能：

```text
repeat payment
reuse old lease
retry one-shot action
use revoked authority
replay old task
```

这与经典 stale client / stale leader 问题结构相同：

```text
old process pauses or loses connectivity
new process becomes current
old process resumes
old process still believes it may act
```

因此 rollback safety 首先应复用 distributed-systems primitives。

## 3. Fencing token 吸收大量问题

成熟做法：

```text
Coordinator issues monotonically increasing epoch/fencing token
        ↓
Every protected mutation carries epoch
        ↓
Resource remembers highest accepted epoch
        ↓
Reject stale lower epoch
```

例如：

```text
A_old token=7
A_new token=9

resource has seen 9
A_old sends write(7)
=> reject
```

这个规则甚至不要求 stale Agent 自己知道已经失效。

安全边界位于：

```text
resource where the side effect occurs
```

而不是：

```text
Agent's own belief
```

因此候选不变量：

```text
old Agent must know it is stale
```

应该被删除。

更正确的是：

```text
stale Agent effects must be rejectable by authoritative resources
```

但这仍不是 Agent-specific 新理论。

## 4. Idempotency 吸收 duplicate side effect

对于：

```text
send payment
create order
provision VM
```

若 external service 支持 idempotency key：

```text
same logical operation id
=> repeated request does not create second effect
```

Durable workflow systems也已经明确区分：

```text
at-least-once
at-most-once
exactly-once workflow semantics where offered
```

Agent Continuity 不应自己重新定义执行语义。

## 5. Event sourcing 吸收“本地历史不是现实历史”

若关键 lifecycle / effect events 被写入独立 durable log：

```text
AuthorityRevoked
PaymentExecuted
ObligationFulfilled
SuccessorActivated
```

旧 checkpoint 恢复以后可以 replay authoritative log 并重建新状态。

因此：

```text
checkpoint snapshot
```

不应被当作完整世界状态。

这与 event sourcing 的既有原则一致。

## 6. Saga 吸收一部分 outstanding workflow

长事务/多服务工作流已经有：

```text
forward recovery
compensating transaction
orchestration
choreography
```

这些机制可以保证单一业务 workflow 在失败/迁移后继续处理未完成步骤。

所以：

> **“Agent 有 unfinished task”本身并不足以证明需要 Agent Succession protocol。**

真正仍待研究的是：

```text
workflow owner changes from A to successor B
across provider / trust-domain boundary
and external counterparties need to recognize B
```

也就是 ownership/succession，而不是 workflow persistence。

## 7. Fork ~= split-brain + delegated authority

Fork：

```text
A -> A1 + A2
```

若 A1/A2 都持有同一个可复制 bearer credential：

```text
authority duplicates
```

但已有机制包括：

```text
sender-constrained tokens
proof-of-possession keys
instance binding
attenuating capability derivation
short lifetime
fresh admission
fencing at protected resource
```

它们已经提供强安全基础。

因此 A0 不应该标准化：

```text
fork token format
```

真正未被吸收的是：

> 非纯 authorization relationship 在 fork 后如何被多个独立外部 authority 重新承认。

## 8. Merge ~= fresh subject + explicit grants

从安全角度：

```text
A(auth X) + B(auth Y) -> C
```

最安全且现有机制可实现的默认是：

```text
C gets neither X nor Y automatically
```

然后：

```text
Issuer X -> explicitly grant C
Issuer Y -> explicitly grant C
```

所以 `no implicit privilege union` 本身也不需要新协议。

Merge 剩余问题依旧集中在：

```text
obligations
reputation applicability
contractual succession
external standing
```

## 9. Provider shutdown 不能由 fencing 解决

Distributed-systems techniques依赖某个 authoritative resource / log / coordinator 仍然存在。

Provider shutdown 的特殊问题是：

```text
authority itself disappears
```

若：

```text
credential issuer gone
status service gone
provider-local event log gone
```

fencing/token/idempotency 均不能恢复不存在的 trust authority。

因此 provider shutdown 仍是 A0 最强公共性压力测试之一。

## 10. R2 对原不变量的判定

### Authority Non-Multiplication

判定：**mostly absorbed**。

已有 capability attenuation、PoP、sender constraining、resource-side enforcement。

### Revocation / External-Effect Monotonicity

判定：**mostly absorbed**。

已有 revocation state、epochs/fencing、idempotency、durable event history。

### Obligation Conservation

判定：**workflow-local absorbed; cross-domain succession unresolved**。

Workflow persistence 可解决“任务别丢”，但不能单方面让 successor 成为第三方认可的新 obligor。

### Explicit Succession

判定：**still under test**。

不是因为缺一个 successor ID，而是因为不同 relationship authority 必须分别确认。

## 11. 一个更严格的结论

未来 A0 不应再把：

```text
replay protection
revocation propagation
epoch
fencing
idempotency
workflow durability
```

作为独立创新点。

如果未来 framework 有价值，它必须在这些成熟原语之上，只解决：

```text
cross-domain relationship succession coordination
```

而且必须证明普通 VC / signed event / policy profile 无法自然完成。

---

# English

A0-R2 uses mature distributed-systems theory to falsify several apparently agent-specific primitives. Checkpoint rollback maps closely to stale-worker/stale-leader failures; fencing tokens and monotonic epochs prevent stale instances from mutating authoritative resources. Idempotency and durable workflow semantics address duplicate side effects and replay. Event sourcing keeps irreversible external history outside rollbackable local state, and saga patterns maintain long-running workflow consistency.

Consequently, replay protection, external-effect monotonicity, epochs, fencing, idempotency and workflow persistence should not be reinvented by Agent Continuity. The remaining problem, if any, is cross-domain succession of relationships whose authorities are independent of the agent runtime.