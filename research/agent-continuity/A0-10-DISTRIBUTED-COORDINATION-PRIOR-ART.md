# A0-10 — 分布式协调 Prior Art 反证 / Distributed Coordination Prior-Art Challenge

> 状态 / Status: **Adversarial Research / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 结论先行

A0-R3 发现：如果所谓 Agent Succession 协议只定义：

```text
PROPOSE
PREPARE
ACCEPT
COMMIT
ABORT
COMPENSATE
CLOSE
```

那么它几乎没有新的基础研究价值。

原因是这类跨自治参与方协调在分布式事务和跨组织业务事务领域已经有长期成熟 prior art。

## 2. WS-AtomicTransaction

WS-AtomicTransaction 定义了典型 2PC coordination，包括 participant registration、prepare、commit、rollback 等。

其核心问题是：

```text
multiple autonomous resources
must reach one atomic outcome
```

这和“多个 relationship authority 必须全部把同一 successor 接受后才算 transition committed”在协调结构上没有本质新意。

因此：

```text
multi-authority all-or-nothing commit
```

不能作为 A0 的创新点。

## 3. WS-BusinessActivity

长生命周期关系不能长期锁资源，且现实动作往往不可物理 rollback。

WS-BusinessActivity 已经为这类场景定义了：

```text
Complete
Completed
Close
Compensate
Cancel
CannotComplete
Fail
```

这与 Agent succession 中：

```text
credential reissue
contract reassignment
release old grant
compensate partial transition
```

高度同构。

因此：

```text
long-running succession + compensation
```

也不能作为新协议存在理由。

## 4. OASIS Business Transaction Protocol (BTP)

BTP 更直接针对：

> 在组织边界之外，自治参与方之间协调 loosely coupled business transactions。

这与“银行、客户、reputation issuer、network authority、provider 各自自治，却需要对一次 Agent lifecycle transition 作出各自决定”非常接近。

因此：

```text
cross-organization coordination
```

本身也不是 AI-specific gap。

## 5. Saga / Compensation

现代微服务 Saga 的基本事实：

```text
one logical business transaction
=
sequence of local transactions
+
compensating actions when later steps fail
```

且 Saga 天然支持 choreography 和 orchestration 两种风格。

所以 A0 不应该发明自己的：

```text
succession orchestrator
transition compensation
```

这些只可能成为 implementation pattern。

## 6. 真正要区分的是 coordination 与 semantics

传统事务协议可以回答：

```text
Did participants agree?
Was operation committed?
Was it compensated?
Did participant become unavailable?
```

但它们不会自动回答：

```text
May reputation transfer?
May an obligation split?
Is a license assignable?
Does model replacement invalidate a specific certification?
```

这些是 relationship-specific semantics。

然而“事务协议不替应用决定业务规则”不是 A0 的创新，而是分层设计的正常结果。

A0 若要继续，必须证明存在一个**跨 relationship 类型仍稳定成立、又不是普通 transaction semantics 的 Agent-specific invariant**。

## 7. R3 当前判断

目前看到的结构更像：

```text
Domain semantics
  defines whether / how relationship may transfer
            ↓
Generic coordination
  coordinates decisions across domains if needed
            ↓
Credential/event carriers
  carry signed decisions and receipts
```

而不是：

```text
New universal Agent Succession Protocol
  decides everything
```

## 8. 重要安全结论：原子性不是默认要求

不同 external relationships 可以合法选择不同 successor：

```text
Bank authority     -> successor B
Contract duty      -> successor C
Reputation         -> no transfer
Network admission  -> fresh admission
```

这不一定是“不一致”。

只有业务需求明确声明：

```text
these relationships MUST move atomically to one successor
```

时，才应该启动 atomic coordination。

因此一个全局 `sameAgent transition committed` 很可能再次是错误抽象。

## 9. 不可强制关系

若某 relationship 的有效性依赖一个已消失的 issuer/counterparty：

```text
missing authority
```

不能被协调协议替代。

这是一个基本边界：

```text
COORDINATION != AUTHORITY
```

协议可以协调已有决定，不能创造本不存在的授权决定。

---

# English

R3 finds strong prior art for any generic succession state machine based on prepare/commit/abort/compensate. WS-AtomicTransaction, WS-BusinessActivity, OASIS BTP and modern Saga patterns already cover coordination across autonomous resources and long-running business activities. A0 therefore cannot justify itself by inventing a new transaction vocabulary. Any remaining value must be an Agent-specific semantic invariant that cannot be reduced to generic coordination plus domain-specific transfer policy.