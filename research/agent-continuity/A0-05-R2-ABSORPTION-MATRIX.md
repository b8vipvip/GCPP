# A0-05 — R2 吸收矩阵 / Absorption Matrix

> 状态 / Status: **A0-R2 Adversarial Research / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. R2 的目标

A0-R2 不尝试证明 Agent Continuity 需要新协议，而是主动尝试用已有机制把 A0 第一轮的 13 个极端场景全部吸收。

主要吸收栈：

```text
OAuth / Token Exchange / Identity Chaining
Capability attenuation / PoP / revocation
Workload identity / runtime attestation / network admission
PKI / DID / KERI key rotation
Memory portability
Event sourcing / durable workflow / idempotency
Saga / compensation
Leases / epochs / fencing tokens
ODRL duties / obligations
VC / credential status
```

判定不是“能不能拼出来一个系统”，而是：

> **现有机制是否已经能自然、完整、跨供应商一致地解决该 lifecycle transition 的安全语义。**

## 2. 判定等级

```text
ABSORBED
  已有成熟通用机制，A0 不应重复标准化。

MOSTLY_ABSORBED
  主要安全问题已有成熟解法，剩余部分主要是部署/配置/Profile。

PARTIALLY_ABSORBED
  某个维度已有解法，但跨 relationship succession 仍缺统一语义。

NOT_ABSORBED_CROSS_DOMAIN
  可以定制实现，但没有看到自然、通用、跨发行方/相对方的 succession 语义。
```

## 3. 13 个极端场景

| 场景 | R2 判定 | 已有机制可吸收部分 | 剩余问题 |
|---|---|---|---|
| Model replacement | MOSTLY_ABSORBED | logical identity 可独立于模型；授权可重新评估；模型相关 assurance 可失效 | 不应把 behavioral assurance 自动继承，但这主要是 policy/attestation 问题 |
| Runtime migration | ABSORBED / MOSTLY | workload identity、runtime attestation、重新 admission；旧 binding 不自动继承 | continuity proof 的具体 Profile 尚可不同，但问题已被现有工作直接识别 |
| Key rotation | ABSORBED | PKI、DID rotation、KERI key-event log、recovery authority | 无需 A0 新 key-rotation 协议 |
| Memory migration | ABSORBED FOR MEMORY | W3C memory interoperability 正在做 portability/verifiability/revocation | memory copy 本身不提供主体/权利 continuity；这是边界规则而非 memory 协议缺口 |
| Checkpoint rollback | MOSTLY_ABSORBED | event sourcing、durable history、idempotency key、at-most-once strategy、epoch/fencing | 若外部系统不参与 fencing/去重，则任何 continuity protocol 也无法单方面保证 |
| Agent fork | PARTIALLY_ABSORBED | sender-constrained capability、attenuation、fresh admission、resource fencing 可防 authority 复制 | obligations、reputation、exclusive external relationships 由谁承接仍未统一 |
| Agent merge | PARTIALLY_ABSORBED | merged instance 默认无权获得 parents 权限并集；可要求 fresh grants | 两个 predecessor 的义务/信誉/关系冲突和承接仍是 domain-specific |
| Principal transfer | PARTIALLY_ABSORBED | OAuth delegation/identity chaining 可显式建立新 principal relation | principal-scoped rights/duties 是否转移必须由各 issuer/counterparty 决定 |
| Authority revocation | MOSTLY_ABSORBED | OAuth revocation/status、short-lived tokens、global revocation proposals、freshness | 跨 issuer 的统一传播不是 Agent Continuity 特有问题 |
| Outstanding obligations | NOT_ABSORBED_CROSS_DOMAIN | ODRL 可表达 Duty/Obligation；workflow/event store 可跟踪 fulfillment | agent 退场后哪个 successor 成为新 obligor，不由 ODRL policy inheritance 自动解决 |
| Reputation inheritance | NOT_ABSORBED_CROSS_DOMAIN | VC 可表达 issuer 对 subject 的评价/属性 | reputation 不应复制/相加；successor 是否适用必须由 reputation issuer/evaluator 重新判断 |
| Provider shutdown | NOT_ABSORBED_CROSS_DOMAIN | KERI/self-certifying identity 可降低 identifier/key 对 provider 的依赖；export 可保存部分 state | provider-issued grants/status/records 若未提前外部化，shutdown 后不能靠 Agent 自证恢复 |
| Partial state loss | MOSTLY_ABSORBED LOCALLY / PARTIAL CROSS-DOMAIN | external event log、fail-closed、credential/status re-fetch 可恢复 | 不知道哪些 relationship records 缺失时，仍需跨 domain reconciliation |

## 4. 第一轮吸收结果

A0 第一轮最强的四个候选不变量：

```text
Authority Non-Multiplication
Revocation / External-Effect Monotonicity
Obligation Conservation
Explicit Succession
```

在 R2 中已经发生明显分化。

### 4.1 Authority Non-Multiplication 被大量吸收

Capability security 本身就要求：

```text
derived authority <= parent authority
```

OAuth BCP、sender-constrained credentials、attenuating authorization token 研究、fresh instance admission 都在解决同一类风险。

因此：

> **“fork 不能自动复制权限”不构成独立 Agent Continuity Core 的充分理由。**

### 4.2 Revocation / External-Effect Monotonicity 被分布式系统大量吸收

Rollback / stale clone 的核心风险是：

```text
old local state
acts after newer external state exists
```

成熟 distributed-systems 解法已经包括：

```text
external authoritative log
idempotency key
at-most-once / exactly-once orchestration where feasible
lease
monotonic epoch
fencing token at the resource boundary
```

因此：

> **“rollback 不能复活旧执行权”也不是 AI Agent 独有的新基础理论。**

## 5. R2 后剩余最困难的问题

经过吸收，问题被压缩为：

```text
Agent lifecycle transition
        ↓
multiple external relationships
        ↓
relationship owners / issuers / counterparties are independent
        ↓
who acknowledges which successor?
```

关键 external relationships 至少包括：

```text
authority / capability        -> authority issuer / resource owner
obligation / contract         -> counterparty / contract authority
reputation / standing         -> rater / credential issuer / community
audit / external effects      -> affected external system
principal relationship        -> principal / identity-authority domain
```

Agent 自己不是这些关系的唯一权威。

所以：

```text
Agent says "A1 is my successor"
```

不能推出：

```text
A1 inherits every grant
A1 inherits every obligation
A1 inherits every reputation credential
A1 inherits every external standing
```

## 6. 新的核心反证命题

R2 当前提出：

> **SUCCESSOR DECLARATION != EXTERNAL RELATIONSHIP TRANSFER**

以及：

> **No subject may unilaterally transfer a relationship whose validity depends on an independent issuer, counterparty, evaluator, or resource authority.**

中文：

> **主体不能单方面把由独立第三方成立的外部关系转移给 successor。**

这不是规范结论，仍需继续挑战。

## 7. 一个危险的“伪 Continuity”实现

如果设计一个：

```text
Agent Continuity Credential:
  predecessor = A
  successor = A1
  inherits = all
```

它看起来方便，但语义上可能是错误的。

因为 A 没有权力替：

```text
Bank
Employer
Counterparty
Reputation issuer
Resource owner
Regulator
```

决定这些关系全部转给 A1。

因此未来若存在 succession layer，它更可能是：

```text
Succession Proposal
        +
relationship-specific acknowledgements / reissuance
        +
explicit unresolved relationships
```

而不是一个万能 `sameAgent=true`。

## 8. Kill Criteria 更新

若最终可以证明：

```text
VC / OAuth / ODRL / event records
+
普通签名的 succession event
+
每个 external relationship issuer 自行 reissue / revoke / acknowledge
```

已经足够实现跨供应商安全互操作，且不需要新的 shared semantics，A0 应停止独立协议工作。

只有当多个独立 relationship domain 需要一套共同的：

```text
transition vocabulary
acknowledgement semantics
unresolved-state semantics
conservation / conflict rules
cross-domain conformance tests
```

才能继续证明公共 Agent Succession framework 的必要性。

---

# English

A0-R2 aggressively attempts to absorb all thirteen lifecycle stress cases into existing identity, authorization, credential, workflow, distributed-systems and memory mechanisms.

The result is deliberately unfavorable to a new protocol: key rotation, runtime migration, memory portability, basic revocation, rollback replay safety, and much of fork/merge authority safety already have mature mechanisms. Authority non-multiplication and stale-state rejection are not uniquely agentic problems.

The remaining candidate gap is narrower: succession of externally-defined relationships whose validity is controlled by independent issuers, counterparties, raters, or resource authorities. A predecessor agent cannot unilaterally declare that every authority, obligation, reputation credential or standing transfers to a successor. A future framework, if needed at all, would therefore need relationship-specific acknowledgement/reissuance and explicit unresolved states rather than a universal `sameAgent=true` assertion.