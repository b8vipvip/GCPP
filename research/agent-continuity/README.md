# Agent Continuity Research / AI 主体连续性研究

> 当前分支 / Current branch: `research/a0-agent-continuity`  
> 状态 / Status: **A0 complete — independent protocol hypothesis killed; unmerged research branch**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 最终结论

A0 已完成 R1 → R4 第一性原理与可执行反证。

最终判定：

```text
INDEPENDENT AGENT CONTINUITY / SUCCESSION WIRE PROTOCOL:
NOT JUSTIFIED — STOP PROTOCOLIZATION
```

研究没有证明需要新的：

- Agent Continuity Token；
- global successor certificate；
- Agent-specific consensus；
- Agent-specific transparency ledger；
- Agent-specific distributed transaction protocol；
- Agent-specific credential container。

A0 的主要问题最终可以分解为：

```text
relationship/domain authority semantics
+
identity / authorization / credentials
+
version / epoch / causal ordering
+
transparency / audit / gossip
+
generic transaction / workflow / BFT coordination where required
+
conservative UNKNOWN / PENDING / UNRESOLVED
```

## A0 的研究轨迹

### R1 — Extreme lifecycle stress

研究：

```text
Model replacement
Runtime migration
Key rotation
Memory migration
Checkpoint rollback
Agent fork
Agent merge
Principal transfer
Authority revocation
Outstanding obligations
Reputation inheritance
Provider shutdown
Partial state loss
```

关键发现：

```text
STATE COPY != RELATIONSHIP COPY
```

### R2 — Absorption / Falsification

发现大量问题可以被现有：

```text
OAuth/capability
PKI/KMS
event sourcing
fencing
workflow
credential lifecycle
```

吸收。

研究中心收敛为：

```text
Cross-Domain Agent Relationship Succession
```

关键边界：

```text
SUCCESSOR DECLARATION != EXTERNAL RELATIONSHIP TRANSFER
```

R2 harness：

```text
8 / 8 matched expected
```

### R3 — Distributed coordination falsification

多 authority fork / merge / obligation / provider-exit 问题继续被分解为：

```text
Relationship Authority Semantics
+
Generic Distributed Coordination
```

2PC / Saga / durable workflow / versioning 已覆盖协调形态。

R3 harness：

```text
8 / 8 matched expected
```

关键原则：

```text
COORDINATION CANNOT CREATE AUTHORITY
```

### R4 — Byzantine / Open-World ultimate attack

最终攻击：

```text
malicious authority
signed equivocation
isolated views
unknown authority universe
dynamic authority set
no shared clock
network partition
malicious coordinator
transparency split view
trust-policy divergence
late-discovered relationships
Byzantine committee
indispensable authority loss
```

R4 harness：

```text
12 / 12 matched expected
```

所有结果仍可由通用：

```text
signed evidence
transparency
epoch/version
quorum/BFT
trust policy
scoped completion
UNKNOWN/PENDING/UNRESOLVED
```

表达。

因此没有留下不可约 Agent-specific protocol primitive。

## 最终保留的安全原则

```text
STATE COPY != AUTHORITY / DUTY / REPUTATION COPY
SUCCESSOR DECLARATION != EXTERNAL RELATIONSHIP TRANSFER
COORDINATION CANNOT CREATE AUTHORITY
LOCAL VALIDITY != GLOBAL NON-EQUIVOCATION
KNOWN SET != COMPLETE UNIVERSE
WALL_CLOCK != CAUSAL ORDER
SAFETY MAY REQUIRE NON-COMPLETION
```

尤其：

```text
GLOBAL_SUCCESSION_COMPLETE = true
```

在 open world 中通常是不安全的表达。

完成状态必须限定：

```text
relationship set
authority set
policy epoch
evidence / receipts
```

## 文件索引

### R1

- `A0-00-RESEARCH-CHARTER.md`
- `A0-01-EXTREME-STRESS-TESTS.md`
- `A0-02-CONTINUITY-DIMENSIONS-AND-INVARIANTS.md`
- `A0-03-PRIOR-ART-AND-BOUNDARIES.md`
- `A0-04-FIRST-ROUND-FINDINGS.md`

### R2

- `A0-05-R2-ABSORPTION-MATRIX.md`
- `A0-06-RELATIONSHIP-SOVEREIGNTY.md`
- `A0-07-DISTRIBUTED-SYSTEMS-FALSIFICATION.md`
- `A0-08-R2-FINDINGS.md`

### R3

- `A0-09-R3-ABSORPTION-HYPOTHESIS.md`
- `A0-10-DISTRIBUTED-COORDINATION-PRIOR-ART.md`
- `A0-11-R3-STRESS-TESTS.md`
- `A0-12-R3-FINDINGS.md`

### R4

- `A0-13-R4-ULTIMATE-ATTACK-CHARTER.md`
- `A0-14-BYZANTINE-OPEN-WORLD-PRIOR-ART.md`
- `A0-15-R4-ULTIMATE-STRESS-TESTS.md`
- `A0-16-R4-FINAL-FINDINGS-AND-KILL-DECISION.md`

### Harness

- `a0-stress-vectors.json`
- `a0-test-plan.md`
- `harness/r2_*`
- `harness/r3_*`
- `harness/r4_*`

## 未来如何处理 A0

A0 不应继续向独立协议发展。

可保留为：

```text
Agent Lifecycle & Succession Threat Model
Security Guidance
Cross-standard interoperability profile
Adversarial conformance corpus
```

只有未来出现无法由 domain authority semantics、existing credentials、transparency、distributed coordination、BFT/quorum 与 conservative unknown-state 正确表达的真实跨行业反例时，才重新开启协议研究。

---

# English

A0 is complete. After four rounds of first-principles falsification, the evidence does not justify an independent Agent Continuity or Agent Succession wire protocol. The useful residue is a lifecycle/succession threat model, security guidance, interoperability profiles, and adversarial conformance vectors. The direction should only be reopened if a real cross-industry Agent lifecycle safety problem survives decomposition into domain authority semantics, existing credentials, transparency, generic distributed coordination/BFT, and conservative unknown states.