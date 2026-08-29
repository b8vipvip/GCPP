# A0-09 — R3 吸收/反证假设 / R3 Absorption & Falsification Hypothesis

> 状态 / Status: **Research Hypothesis / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. R3 的目标

R2 之后，A0 已经不再把 `sameAgent=true`、key rotation、memory migration、rollback fencing、普通 authorization continuity 当作独立创新。

R3 只研究一个剩余问题：

> **多个彼此独立的 relationship authorities，能否仅依靠已有的通用凭证、分布式事务、durable log、workflow / Saga 与 domain acknowledgement，对 Agent fork / merge / provider-exit 形成安全、可收敛、可保留 UNKNOWN 的 succession choreography？**

如果答案为 YES，则 A0 不应建立独立 Agent Continuity / Succession wire protocol。

## 2. 强吸收假设

R3 主动假设以下组合已经足够：

```text
standard identity / credential carriers
+
authority-owned relationship state
+
version / epoch / compare-and-swap
+
2PC / atomic commit where true atomicity is possible
+
Saga / compensation for long-running activities
+
durable event log / receipts
+
domain-specific acknowledgement / reissuance
```

A0 必须优先证明该组合失败，才有继续协议化的理由。

## 3. 三类 succession coordination

### A. Atomic-transferable

某组关系必须一起成功或一起失败，并且参与方允许 prepare/commit。

```text
PROPOSE
PREPARE
COMMIT | ABORT
```

这属于经典 distributed atomic commit 领域。

### B. Long-running / compensatable

关系变更不能长期锁定，但可以通过反向动作、撤销、再发行或业务补偿恢复。

```text
PROPOSE
LOCAL ACCEPT
...
CLOSE | COMPENSATE | PARTIAL OUTCOME
```

这属于 Saga / Business Activity 类问题。

### C. Non-forceable / authority-dependent

某关系只有特定 authority / counterparty 有权决定是否转移；若该 authority 消失或拒绝：

```text
UNRESOLVED
DENIED
REISSUE_REQUIRED
```

是正确结果。

协议不能凭空制造第三方同意。

## 4. R3 反例集合

必须覆盖：

```text
R3-T1 Multi-Issuer Fork
R3-T2 Obligation Double Assignment
R3-T3 Successor Race
R3-T4 Provider Dies Mid-Succession
R3-T5 Reputation Split
R3-T6 Merge with Conflicting Duties
R3-T7 Revocation During Succession
R3-T8 Partial Evidence Loss
```

## 5. 必须挑战的核心假设

### H1 — 多方 commit 是 AI-specific 吗？

若传统 WS-Coordination / BTP / WS-AtomicTransaction / Saga 已能表达协调，则不是。

### H2 — fork/merge 是否需要新全局 Agent transaction？

如果每个 relationship authority 独立拥有其 relation，并能通过版本化状态避免 double transfer，则不需要。

### H3 — 是否必须存在单一 global successor？

R2 已发现不同域完全可能接受不同 successor。

因此默认：

```text
GLOBAL_SUCCESSOR = not assumed
```

只有应用明确要求同一 successor 承接一组关系时，才产生跨 authority coordination transaction。

### H4 — provider shutdown 能否被协议解决？

若 provider 本身是不可替代 authority，答案可能是 NO。

正确安全语义是：

```text
missing indispensable authority
=> unresolved / abort
```

而不是自动继承。

## 6. Kill Criteria

如果 R3 证明：

1. exclusive relation 的 double transfer 可由 authority-side version/epoch/CAS 解决；
2. all-or-nothing succession 可由现有 atomic coordination 解决；
3. long-running succession 可由 Saga / compensation 解决；
4. obligation / reputation / license 等 relation 的语义仍必须由 domain authority 决定；
5. provider disappearance 时不存在任何可由通用协议“补造”的授权；
6. partial evidence 时安全结果就是 UNKNOWN / UNRESOLVED；

则：

> **停止把 A0 推向独立 wire protocol。**

最多保留：

```text
Agent Succession threat model
cross-standard interoperability profile
conformance vectors
recommended lifecycle receipts
```

---

# English

R3 aggressively assumes that the remaining multi-authority succession problem can be absorbed by existing distributed coordination mechanisms: authority-owned state, versioning/fencing, atomic commit when applicable, Saga/compensation for long-running activities, durable receipts, and domain-specific acknowledgements. Only failures that are both cross-domain and not naturally expressible with those mechanisms can justify an independent Agent Succession protocol.