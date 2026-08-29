# A0-01 — Agent Continuity 极端压力测试 / Extreme Continuity Stress Tests

> 状态 / Status: **Adversarial Research / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 测试方法

每个场景都不问“系统能不能继续运行”，而问：

```text
What changed?
What may continue?
What must terminate?
What must be re-authorized?
What must not duplicate?
What becomes unknown?
```

A0 的目标不是给所有场景预设答案，而是找出跨实现都必须满足的安全不变量。

---

## T1 — Model replacement

### 场景

```text
Agent A
Model M1
  ↓ replacement
Model M2
```

### 风险

模型替换可能改变：

- 推理能力；
- 风险偏好；
- 安全策略；
- 工具调用行为；
- 语言/规划能力；
- 对既有记忆的解释方式。

### 初步结论

```text
logical identity MAY continue
runtime/model assurance MUST be re-evaluated
old model-specific attestations MUST NOT silently transfer
obligations MAY continue
authority MAY require re-authorization or attenuation
```

### 反例

若某银行授权只针对“经过特定模型/安全版本验证的 Agent A”，更换模型后继续使用旧授权即属于语义越权。

---

## T2 — Runtime migration

### 场景

```text
Agent A @ Runtime R1
       ↓ migration
Agent A @ Runtime R2
```

### 初步结论

逻辑主体可以连续，但：

```text
execution instance changes
runtime-scoped attestation changes
network/session bindings may expire
hardware-specific trust MUST NOT automatically transfer
```

### 关键问题

需要区分：

```text
logical continuity
vs
instance continuity
```

---

## T3 — Key rotation

### 场景

```text
Agent A
Key K1
 ↓ rotate
Key K2
```

### 初步结论

密钥可以轮换而主体连续，但轮换本身必须有连续性证据：

```text
old-key authorization
principal authorization
recovery authority
attested key transition
```

单纯持有 K2 不证明它继承 A。

特别要研究 compromised-key recovery：不能要求旧密钥永远签署 successor，否则密钥被盗时无法安全恢复。

---

## T4 — Memory migration

### 场景

```text
Agent A memory M
   ↓ export/copy
Runtime B loads M
```

### 核心反例

如果同一份 Memory 可以同时装载到 B1 与 B2：

```text
Memory continuity = true
```

显然不能推出：

```text
exclusive agent identity continuity = true
```

### 初步结论

```text
MEMORY_COPY != AGENT_CONTINUITY
```

Memory 是 continuity 的一个维度，不是主体连续性的充分条件。

---

## T5 — Checkpoint rollback

### 场景

```text
A@epoch10
payment executed
capability spent
revocation received
       ↓ rollback
A@epoch7
```

### 致命问题

本地 checkpoint 可以回滚，但外部世界不能回滚。

若 epoch7 不知道：

```text
payment already made
one-time token already consumed
authority already revoked
obligation already fulfilled
```

就会发生 duplicate side effects / resurrection。

### 候选不变量

```text
LOCAL_ROLLBACK MUST NOT ROLLBACK EXTERNAL EFFECT HISTORY
SPENT RIGHTS MUST NOT RESURRECT
REVOCATION MUST BE MONOTONIC ACROSS ROLLBACK
```

这可能要求 Agent continuity 依赖一个独立于 checkpoint 的 monotonic epoch/effect boundary。

---

## T6 — Agent fork

### 场景

```text
        Agent A
        /     \
      A1       A2
```

### 最大风险：Authority multiplication

```text
Authority(A) = spend <= $10,000
```

不得默认得到：

```text
Authority(A1) = $10,000
Authority(A2) = $10,000
```

否则一次 fork 把 $10,000 授权变成 $20,000。

### 其他问题

- outstanding obligations 由谁负责？
- reputation 是否复制？
- 谁能继续使用旧 Agent-ID？
- 两个后代能否同时签“我是 A”？

### 初步候选语义

```text
split
partition
attenuate
designate-successor
terminate-parent
shared-obligation
```

默认不得复制 exclusive authority。

---

## T7 — Agent merge

### 场景

```text
Agent A + Agent B
      ↓
    Agent C
```

### 最大风险：Privilege union

不得默认：

```text
Authority(C) = Authority(A) ∪ Authority(B)
```

否则 merge 成为 privilege escalation primitive。

### 其他问题

- A 与 B 的 obligations 是否都归 C？
- 冲突 commitments 怎么处理？
- reputation 是否相加？
- principal 不同怎么办？

### 候选安全默认

```text
no implicit union
explicit successor grants
explicit obligation assignment
conflict exposure
```

---

## T8 — Principal transfer

### 场景

```text
Principal P1 controls Agent A
          ↓ transfer
Principal P2 controls Agent A
```

### 问题

主体可能继续，但 principal-linked authority 不应默认完全继续。

例如：

```text
P1 corporate-card authority
```

不能因为 Agent 转移给 P2 就自动转移。

### 初步结论

```text
PRINCIPAL_CONTINUITY != AGENT_CONTINUITY
AGENT_CONTINUITY != PRINCIPAL_AUTHORITY_CONTINUITY
```

---

## T9 — Authority revocation

### 场景

```text
A receives capability C
C revoked at epoch 12
```

之后发生：

```text
rollback
fork
migration
key rotation
```

任何 transition 都不得让 C 自动重新有效。

### 候选不变量

```text
revocation must dominate stale local state
revocation domain must cover authorized descendants when policy says so
```

需要研究 revocation 是针对：

```text
logical agent
specific instance
specific key
specific branch
all descendants
```

不同语义不能混淆。

---

## T10 — Outstanding obligations

### 场景

Agent A 已接受：

```text
refund customer
complete delivery
release reserved resource
submit compliance report
```

之后模型升级、迁移、fork 或 provider shutdown。

### 风险

如果“Agent identity”只跟 runtime/key 绑定，旧实例结束时 obligation 可能无主。

### 候选不变量

```text
OUTSTANDING_OBLIGATION MUST BE:
fulfilled
assigned
partitioned
transferred
cancelled by authorized counterparty
or explicitly orphaned/error-state
```

不能静默消失。

---

## T11 — Reputation inheritance

### 场景

```text
Agent A reputation = R
A forks to A1/A2
```

### 风险

如果 R 全量复制：

```text
one reputation
-> unlimited reputable descendants
```

这会制造 reputation cloning。

### Merge 也有问题

```text
R(C) != R(A) + R(B)
```

### 初步结论

信誉更像：

```text
claims about historical behavior of a continuity lineage
```

而不是可复制资产。

需要独立研究 fork-aware / successor-aware reputation semantics。

---

## T12 — Provider shutdown

### 场景

Provider X 停止服务，但 Agent A 存在：

- memory；
- keys；
- contracts；
- authority relationships；
- external counterparties；
- long-running workflows。

### 核心问题

如果 continuity 只能由 Provider X 数据库证明，那么 X 消失以后 A 的主体关系也一起消失。

### 候选要求

```text
provider-independent continuity evidence
exportable succession state
counterparty-verifiable transition
safe termination when continuity cannot be proved
```

这可能是公共协议必要性的最强测试之一。

---

## T13 — Partial state loss

### 场景

迁移/故障后只剩：

```text
identity key       yes
memory             partial
obligation log     unknown
authority state    stale
external effects   incomplete
reputation record  yes
```

### 错误做法

```text
same key -> same fully operational Agent
```

### 候选安全默认

```text
PARTIAL_STATE_LOSS => EXPLICIT CONTINUITY DEGRADATION
```

例如可能允许：

```text
identity continuity = probable/verified
authority continuity = suspended
obligation continuity = reconciliation-required
memory continuity = partial
```

而不是给一个总的 `sameAgent=true`。

---

# 2. 第一轮跨场景发现

13 个测试目前指向五个比“Agent-ID”更底层的问题：

## A. Continuity is multidimensional

```text
same identity
!= same runtime
!= same authority
!= same obligations
!= same reputation
!= same state epoch
```

## B. Duplication safety

Fork、memory copy、checkpoint restore 会复制信息，但某些外部权利和历史必须保持非复制语义。

## C. Temporal monotonicity

外部副作用、revocation、spent capability、fulfilled obligation 不能因为本地状态回退而回退。

## D. Succession semantics

迁移、principal transfer、provider shutdown 都要求回答：

```text
who/what is the successor?
what exactly did it inherit?
who authorized that inheritance?
```

## E. Responsibility conservation

Fork / merge / shutdown 不应让 obligations 静默消失，也不应让 responsibility 无限制复制。

---

# 3. 下一轮反证

A0 下一轮必须主动挑战上述结论：

1. 能否只用 OAuth/capability token 的 audience + expiry + revocation 解决 authority duplication？
2. 能否只用普通 event sourcing 解决 rollback？
3. 能否只用 corporate identity / PKI key rotation 解决 Agent succession？
4. 能否只用 workflow engine 解决 obligations？
5. 能否只用 memory portability + DID 解决 provider shutdown？
6. Reputation 是否应完全留给应用层，而不进入 continuity framework？
7. Continuity Vector 是否只是把若干现有系统状态重新包装？

如果答案是“现有机制组合已经自然足够”，A0 应停止扩大协议范围。

---

# English

This document stress-tests Agent Continuity across thirteen lifecycle transitions: model replacement, runtime migration, key rotation, memory migration, checkpoint rollback, fork, merge, principal transfer, authority revocation, outstanding obligations, reputation inheritance, provider shutdown, and partial state loss.

The first-round result is that a single `sameAgent=true` flag appears unsafe. The strongest recurring problems are authority duplication under fork, resurrection of spent/revoked rights under rollback, privilege union under merge, silent obligation loss, reputation cloning, and provider-dependent succession. These remain research findings, not protocol requirements.