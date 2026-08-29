# A0-04 — 第一轮研究结论 / First-Round Findings

> 状态 / Status: **Research Findings / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 第一轮没有证明“需要新协议”

A0 当前只证明：

> **长期 Agent 生命周期存在一组比普通 Agent-ID 更复杂的 succession 问题。**

但尚未证明这些问题必须由一个新的公共协议解决。

现有：

```text
identity
capability authorization
revocation
key management
memory portability
event sourcing
workflow engines
```

可能已经可以吸收大量问题。

因此 A0 下一轮必须继续反证，而不是开始写 wire format。

## 2. “主体连续性”比预期更像 Rights/Duties/History Succession

最初问题是：

```text
When is it the same Agent?
```

13 个压力测试后，更有工程价值的问题变成：

```text
After lifecycle transition,
what rights survive?
what duties survive?
what historical claims still apply?
what state must never be duplicated or forgotten?
```

这意味着未来真正的研究中心可能不是抽象哲学意义上的 identity continuity，而是：

> **Digital Agent Succession Semantics / 数字 Agent 继承语义**

## 3. 信息可复制与权利不可复制形成核心张力

Agent 的本地状态天然适合复制：

```text
checkpoint
memory
model
configuration
```

而以下东西不能简单复制：

```text
exclusive authority
one-time capability
budget
lease
revocation state
outstanding obligation
reputation standing
external-effect history
```

这形成一个长期结构性问题：

```text
copyable computational state
vs
non-copyable / conserved external relationships
```

Fork 和 rollback 把这个矛盾放大到最明显。

## 4. Fork 是当前最强极端测试

Fork 证明：

```text
state duplication
```

不能等价于：

```text
subject/right duplication
```

如果一个具备经济权限的 Agent 可以无限 fork，而每个后代自动继承父 Agent 全部 authority / reputation，那么系统会出现：

```text
authority inflation
reputation inflation
obligation ambiguity
identity ambiguity
```

因此任何长期 Agent 框架都必须在某层面对 fork 定义明确语义。

## 5. Rollback 是第二强测试

Rollback 暴露：

```text
local state time
!= external world time
```

AI Agent 比普通应用更危险，因为它会主动规划并重试行动。

旧 checkpoint 若恢复：

```text
old intention
old budget
old authorization view
old task state
```

可能再次执行已经发生的现实动作。

因此至少存在一个非常强的候选不变量：

> **Agent 本地可回滚状态不得支配已经发生的不可回滚外部事实。**

是否需要新协议仍待证明；成熟 event sourcing / idempotency 可能可以解决大部分问题。

## 6. Merge 是第三强测试

Merge 证明 successor 的 authority 不能由 parent state 做简单 union。

否则：

```text
A authorized for system X
B authorized for system Y
A+B -> C
```

会产生一个从未被任何 principal 明确授权、却同时访问 X/Y 的新主体。

所以：

```text
state merge
!= authority merge
```

## 7. Provider shutdown 是公共协议必要性的关键测试

如果 continuity 只在 provider 内部有意义：

```text
Provider X says this is still Agent A
```

那么 X 一旦消失，Agent 与外部世界的：

```text
identity relationship
authority relationship
obligations
reputation
```

都可能无法验证。

这是 A0 判断“是否天然需要公共协议”的关键问题。

如果 provider-independent succession 可以仅靠现有 PKI/DID/capability/workflow records 完整解决，则不需要新的协议。

如果不能，则这里可能形成真正独立的公共层。

## 8. 当前最值得继续证明的四个不变量

第一轮 13 场景后，暂时优先四项：

```text
P1 Authority Non-Multiplication
P2 Revocation / External-Effect Monotonicity
P3 Obligation Conservation
P4 Explicit Succession under Fork/Merge/Provider Exit
```

它们比 `sameAgent=true` 更可测试，也比“新 Agent-ID”更有长期价值。

## 9. 暂时降级的方向

以下暂时不应成为独立 Core 中心：

```text
memory portability
key rotation
runtime migration
agent communication
basic agent identity
basic authorization
```

因为已有标准和成熟系统已经大量覆盖。

它们仍是 stress-test input，但不应成为新协议卖点。

## 10. 下一阶段的生死问题

A0 下一轮只需要回答一个问题：

> **现有 capability + identity + event sourcing + workflow + memory mechanisms，在跨 provider 的 fork/merge/rollback/succession 场景中，是否能自然形成一致的生命周期继承语义？**

如果 YES：

```text
stop independent protocol work
```

如果 NO，并且失败是一整类跨厂商长期问题：

```text
continue toward a public Agent Succession framework
```

---

# English

The first A0 round does not establish the need for a new protocol. It does establish a narrower and more concrete engineering problem than generic identity continuity: **succession of rights, duties, reputation applicability and irreversible external history across agent lifecycle transitions**.

Fork, rollback and merge are currently the strongest adversarial cases. They expose authority multiplication, revocation resurrection, duplicate external effects, obligation ambiguity and privilege union. Provider shutdown is the key public-interoperability test because a continuity system that depends forever on the original provider is not genuinely portable.

The next A0 round will attempt to absorb these findings into existing capability, identity, event-sourcing and workflow mechanisms before any independent framework is proposed.