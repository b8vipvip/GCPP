# A0-06 — Relationship Sovereignty / 外部关系主权模型

> 状态 / Status: **A0-R2 Research Hypothesis / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. R2 的关键转向

A0 第一轮把问题从“same Agent?”推进到 rights / duties / history succession。

R2 继续反证后发现还需要进一步收紧：

> **Agent 的大多数重要连续关系，并不由 Agent 自己拥有最终解释权。**

Agent 可以控制或复制：

```text
model state
memory
configuration
checkpoint
local plan
local identifiers
```

但它不能单方面决定以下关系的有效性：

```text
bank spending authority
OAuth grant
enterprise access
contractual obligation
lease
license
reputation credential
regulatory standing
third-party certification
```

这些关系由其他 authority / counterparty / issuer 共同定义。

## 2. Relationship Sovereignty

A0-R2 暂称这一事实为：

> **Relationship Sovereignty / 外部关系主权**

它不是指政治主权，而是一个工程边界：

> 某项 relationship 是否成立、能否被转移、能否被继承，其最终决定权属于定义该 relationship 的 authority set，而不是仅属于 relationship 的 subject。

抽象表达：

```text
R = relationship(subject, external_party_or_domain)

Transfer(R, A -> B)
requires authorization from AuthoritySet(R)
```

而不是：

```text
A declares successor B
=> Transfer(all relationships)
```

## 3. 四类最重要关系

### 3.1 Authority Relationship

例如：

```text
A may spend up to $10,000 from account X
```

关系 authority 可能是：

```text
bank
enterprise authorization server
resource owner
capability issuer
```

Agent A 的 continuity statement 没有权力自行让 B 继承。

### 3.2 Obligation Relationship

例如：

```text
A must deliver result Y before T
```

真正相关的 authority/counterparty 可能是：

```text
contract counterparty
workflow owner
principal
service provider
legal entity
```

若 A fork：

```text
A -> A1 + A2
```

不能靠复制 task memory 来决定：

```text
A1 和 A2 都承担完整义务
```

或者：

```text
只有 A1 承担
```

除非 relationship contract 本身允许或 counterparty 接受。

### 3.3 Reputation Relationship

例如：

```text
Rater Q says Agent A has reliability = 0.98
```

这个评价属于：

```text
Q's assessment of A
```

而不是 A 可复制的状态。

所以：

```text
copy(A.memory) -> B
```

不能推出：

```text
Q's reputation(A) -> reputation(B)
```

甚至：

```text
A is merged into C
```

也不能默认：

```text
reputation(C) = reputation(A) + reputation(B)
```

### 3.4 External-Effect Relationship

例如：

```text
payment P executed
email E sent
order O placed
resource R consumed
```

这些事实存在于 external system。

Checkpoint rollback 不能改变：

```text
external-effect history
```

因此它们必须由 external authority/state system 作为高优先级事实源。

## 4. Transition Authority Matrix

候选研究矩阵：

| Relationship | Subject alone can transfer? | Typical authority needed |
|---|---:|---|
| Local memory ownership | often yes | local owner / privacy policy |
| Agent display name | often yes | naming registry if externally registered |
| Cryptographic key | rotation may be self-authorized | current controller / recovery authority |
| OAuth/capability grant | no | authorization server / resource owner |
| Network admission | no | network admission authority |
| Contract obligation | usually no | contract rules / counterparty / principal |
| Reputation credential | no | rater / credential issuer |
| License/certification | usually no | license/certification issuer |
| Outstanding payment state | no | payment system |
| Workflow task ownership | depends | workflow owner / orchestrator |

## 5. Succession Proposal 与 Relationship Transfer 分离

如果 A0 最终继续发展，必须保持：

```text
SuccessionProposal
!=
RelationshipTransfer
```

例如：

```text
A -> proposes A1 as successor
```

这只能表达：

```text
predecessor-side intent / evidence
```

各 relationship authority 随后可以：

```text
ACK_TRANSFER
REISSUE
ATTENUATE
PARTITION
RETAIN_ON_PREDECESSOR
TERMINATE
DENY
MARK_UNRESOLVED
```

这比一个统一 `inherits=true` 更接近现实系统。

## 6. 为什么这不是简单的 DID key rotation

Key rotation 解决：

```text
same controlled identifier
old key -> new key
```

但不会自动解决：

```text
same obligor?
same reputation subject?
same authorized workload instance?
same contract party?
same budget holder?
```

所以 key continuity 只能是 succession evidence 的一个维度。

## 7. 为什么这不是 OAuth Token Exchange

OAuth Token Exchange / Identity Chaining 很强，可以：

```text
preserve subject/actor/authorization context
cross trust domains
```

但授权关系仍由 Authorization Server 决定。

这正好支持 Relationship Sovereignty：

> downstream authority must explicitly issue/accept authority rather than trusting the Agent's self-declared succession.

因此 A0 不应重新设计 delegation token。

## 8. 为什么 ODRL 仍未直接解决 Succession

ODRL 可以表达：

```text
Permission
Prohibition
Duty
Obligation
Consequence
Assigner
Assignee
Policy inheritance
```

但 ODRL `inheritFrom` 主要描述 Policy Rules 的继承。

这与：

```text
Agent A terminates
Agent B becomes the recognized obligor of an already-active external relationship
```

不是同一个问题。

事实上，若简单复制 parent policy 到 child Agent，反而可能导致：

```text
duplicated obligation
or
unauthorized assignee substitution
```

所以 obligation succession 必须区别于 policy rule inheritance。

## 9. Fork / Merge 的真正公共问题

在 purely local system 内，orchestrator 可以随便定义 succession。

真正困难的是：

```text
A has relationships with domains X, Y, Z

A -> fork A1, A2
```

X 可能决定：

```text
only A1 inherits
```

Y 可能决定：

```text
both get attenuated new grants
```

Z 可能决定：

```text
neither; re-registration required
```

因此 continuity 不是：

```text
boolean sameAgent
```

更可能是：

```text
relationship-specific succession graph
```

但这仍只是研究模型。

## 10. Provider Shutdown 的特殊性

如果原 provider 消失：

```text
provider-local identity DB gone
provider-local event log gone
provider-local credential status gone
```

Agent 自己不能创造这些 missing third-party acknowledgements。

可提前缓解：

```text
provider-independent identifier
portable key history
exported signed events
third-party receipts
external credential status
escrow / replicated state
```

但如果 shutdown 前没有外部化，任何新协议都不能在事后凭空恢复信任。

因此 A0 必须避免宣传：

```text
protocol guarantees continuity after arbitrary provider disappearance
```

更准确的目标只能是：

> make the transition state exportable and independently acknowledgeable before failure, and make missing acknowledgements explicit after failure.

## 11. 当前候选不变量

R2 暂时增加：

```text
SUCCESSOR_DECLARATION != RELATIONSHIP_TRANSFER

RELATIONSHIP TRANSFER REQUIRES AUTHORITYSET(R) ACKNOWLEDGEMENT

NO ACKNOWLEDGEMENT != TRANSFER

MISSING ISSUER != SUCCESSOR MAY SELF-ISSUE

REPUTATION IS AN EXTERNAL ASSESSMENT, NOT COPYABLE AGENT STATE

OBLIGATION STATE MUST NOT DISAPPEAR WITH RUNTIME STATE
```

这些仍需继续尝试由现有 VC / ODRL / OAuth / workflow mechanisms 完整吸收。

---

# English

A0-R2 introduces the research concept of **Relationship Sovereignty**: the validity and transferability of an externally-defined relationship is controlled by the authority set that defines that relationship, not unilaterally by the agent that is its subject.

A successor declaration can therefore provide predecessor-side intent but cannot automatically transfer OAuth grants, contractual duties, reputation credentials, licenses, network admission or external-effect history. Each relationship may require acknowledgement, reissuance, attenuation, partition, termination or an explicit unresolved state from its relevant issuer, counterparty or resource authority.

This model substantially weakens the case for a universal `sameAgent=true` protocol. If Agent Succession requires a public layer at all, it is more likely to coordinate relationship-specific succession acknowledgements than to define identity, authorization, memory, or keys.