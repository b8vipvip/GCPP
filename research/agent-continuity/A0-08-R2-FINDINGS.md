# A0-08 — R2 研究结论 / A0-R2 Findings

> 状态 / Status: **Research Findings / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. R2 没有证明需要 Agent Continuity Protocol

R2 的首要结果仍然是负面的：

> **大量看似“AI 主体连续性”的问题，实际已经可以被普通 identity / authorization / distributed-systems / workflow 机制吸收。**

目前没有理由开始定义新的 wire protocol。

## 2. 已明显被吸收的方向

```text
Key rotation
Runtime migration
Memory portability
Basic authority revocation
Delegation / actor-chain continuity
Transaction-context propagation
Rollback duplicate-effect prevention
Stale-instance fencing
Workflow durability
Saga compensation
```

这些不应继续作为 A0 独立创新点。

## 3. “same Agent”再次被降级

R2 进一步证明：

```text
same Agent
```

不是外部系统真正需要统一回答的唯一问题。

更现实的是：

```text
For relationship R,
is successor B recognized as the new subject / holder / obligor?
```

同一个 lifecycle transition 可以得到：

```text
Bank:          ACK_TRANSFER
Network:       REAUTH_REQUIRED
Contract:      ACK_SUCCESSOR
Reputation:    REISSUE_REQUIRED
License:       DENY_TRANSFER
Old provider:  UNAVAILABLE
```

因此 continuity 天然是 relationship-specific。

## 4. R2 当前最重要的新边界

候选不变量：

```text
SUCCESSOR DECLARATION != EXTERNAL RELATIONSHIP TRANSFER
```

以及：

```text
No subject may unilaterally transfer a relationship
whose validity depends on an independent issuer,
counterparty, evaluator, or resource authority.
```

这使 A0 从“主体身份连续性”进一步收敛成：

> **Cross-Domain Agent Relationship Succession / 跨域 Agent 外部关系继承。**

但这仍可能被已有 generic credentials + signed events + domain-specific reissuance 完全吸收。

## 5. 当前最难的三个场景

### 5.1 Outstanding obligations

ODRL 可以表达 Duty，workflow 可以跟踪未完成工作，但 lifecycle transition 后：

```text
who becomes the recognized obligor?
```

必须由 contract/counterparty semantics 决定。

### 5.2 Reputation inheritance

Reputation 是第三方对 subject 的 assessment，不是 Agent 可复制状态。

因此：

```text
fork
merge
memory clone
model replacement
```

均不自动产生 reputation succession。

### 5.3 Provider shutdown

若 issuer / provider 在 transition 完成前消失：

```text
no protocol can manufacture missing third-party authorization after the fact
```

只能通过事先：

```text
provider-independent identity
portable signed lifecycle evidence
external receipts
replicated status
escrow / recovery governance
```

降低依赖。

所以 provider shutdown 是“公共框架是否真有必要”的关键 test。

## 6. 一个非常重要的反直觉结果

A0 最开始可能想建立：

```text
Agent Continuity Certificate
```

但 R2 表明单一 certificate 很可能是错误抽象。

因为它容易让 verifier 误以为：

```text
identity continuity
=> authority continuity
=> obligation continuity
=> reputation continuity
```

而这些完全不成立。

如果未来仍需要公共层，更安全的抽象可能是：

```text
Lifecycle Transition Event
    predecessor(s)
    successor(s)
    operation
    effective time

+

Relationship Succession Records
    relationship reference
    authority domain
    decision
    scope
    effective time
    evidence
```

但这仍然只是研究草图，不进入 Core。

## 7. 可能的最终 Kill

R2 已经找到一个可能直接杀死独立协议方向的实现路线：

```text
Signed transition event (VC / COSE / JWS / other carrier)
+
standard identities
+
ODRL or domain policy for obligations
+
OAuth/capability reissuance for authority
+
VC reissuance/status for reputation/credentials
+
external durable logs / receipts
+
domain-specific acknowledgement
```

如果这种组合能通过剩余压力测试，并且只需要少量 Profiles / conventions：

> **A0 不应建立新的 Agent Continuity wire protocol。**

最多建立：

```text
Agent Succession interoperability profile
conformance suite
lifecycle threat model
cross-standard mapping
```

## 8. 仍值得继续的唯一研究问题

下一轮不再问：

```text
How do we identify the same Agent?
```

而问：

> **多个独立 relationship authority 能否仅靠已有通用 credential/policy mechanisms，对 fork/merge/provider-exit 形成一致、无双重继承、可发现 unresolved 状态的 succession choreography？**

这是 A0-R3 的生死问题。

如果答案是 YES：

```text
stop independent protocol research
```

如果答案是 NO，并且失败来自稳定的跨域 coordination gap，而不是某个产品缺功能：

```text
continue toward a minimal public succession coordination profile/framework
```

## 9. R3 建议测试

优先测试：

```text
R3-T1 Multi-Issuer Fork
  A has 5 relationships from 5 authorities
  fork -> A1, A2
  concurrent / conflicting succession decisions

R3-T2 Obligation Double Assignment
  same exclusive obligation accidentally assigned to both successors

R3-T3 Successor Race
  A1 and A2 both present predecessor evidence to different domains

R3-T4 Provider Dies Mid-Succession
  half of domains acknowledged, provider disappears

R3-T5 Reputation Split
  historical score attached to predecessor; issuers apply different successor policies

R3-T6 Merge with Conflicting Duties
  A and B have mutually incompatible obligations

R3-T7 Revocation During Succession
  transfer proposal exists, predecessor is revoked before acknowledgement completes

R3-T8 Partial Evidence Loss
  transition event survives but some acknowledgement records are unavailable
```

R3 应优先尝试使用现有 VC/JWS/ODRL/OAuth artifacts 模拟这些场景，不创建 A0 自有格式。

---

# English

A0-R2 does not justify a new Agent Continuity protocol. Most key-management, runtime, authorization, replay, stale-instance and workflow-durability problems are already substantially absorbed by existing mechanisms.

The remaining question is relationship-specific succession across independent authority domains. A successor declaration cannot itself transfer externally-defined grants, duties, reputation, licenses or standing. Each relevant issuer, counterparty or resource authority may independently acknowledge, reissue, attenuate, terminate or leave a relationship unresolved.

A0-R3 should therefore test whether ordinary signed lifecycle events plus existing credentials, OAuth/capability reissuance, ODRL duties, durable receipts and domain-specific acknowledgements are sufficient. If they are, independent protocol work should stop and the project should shrink to profiles, threat models and conformance tests.