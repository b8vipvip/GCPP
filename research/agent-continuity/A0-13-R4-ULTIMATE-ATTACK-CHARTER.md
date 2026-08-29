# A0-13 — R4 终极攻击研究纲领 / Ultimate Byzantine & Open-World Attack Charter

> 状态 / Status: **Research / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. R4 的目标

R4 是 A0 的最终生死测试。

R1-R3 已经把大量候选问题吸收到现有机制：

- identity / authorization；
- key rotation；
- memory portability；
- event sourcing / fencing；
- workflow / saga；
- distributed transaction / commit；
- relationship-authority-specific reassignment。

R4 不再寻找普通的生命周期状态机，而专门攻击以下最坏条件：

```text
unknown authority set
malicious authority
authority equivocation
conflicting signed receipts
no common coordinator
no shared clock
network partition
offline authorities
partial trust graph
dynamic authority-set changes
transparency split view
partial evidence loss
late-discovered relationships
```

目标不是证明 Agent Continuity Protocol 可行，而是尝试证明：

> 即使使用签名声明、透明日志、trust policy、gossip/witness、BFT/consensus、version/epoch、choreography，也仍有一类 Agent-specific succession safety problem 无法安全表达。

若无法找到，则停止独立 Agent Continuity / Succession wire protocol 方向。

## 2. R4 吸收假设

### H-R4

任何恶意、开放世界或无中心协调的 Agent lifecycle succession 安全问题，都可分解为：

```text
A. Authority / trust semantics
B. Authentic signed decisions
C. Ordering / version / epoch
D. Transparency / equivocation detection
E. Generic distributed agreement or conservative non-completion
```

若该假设成立，则不需要 Agent-specific global succession primitive。

## 3. Kill Criteria

如果以下极端场景都没有留下不可约 Agent-specific primitive：

1. 可见双签；
2. 隔离双签；
3. authority set 未知；
4. authority set 动态变化；
5. 无共享时钟；
6. 网络分区；
7. 恶意 coordinator；
8. transparency split-view；
9. verifier trust policy 不一致；
10. transition 后发现遗漏关系；
11. Byzantine quorum；
12. 不可替代 authority 永久消失；

则判定：

```text
NO JUSTIFICATION FOR AN INDEPENDENT
AGENT CONTINUITY / SUCCESSION WIRE PROTOCOL
```

可保留成果仅限：

- threat model；
- safety guidance；
- interoperability profiles；
- conformance/adversarial test corpus。

## 4. 特别禁止的伪创新

R4 明确禁止把下列成熟概念重新命名为 AI 协议创新：

```text
quorum
consensus
2PC
Saga
fencing token
append-only log
Merkle transparency
gossip
witness cosigning
signed receipt
version vector / epoch
credential status
trust policy
UNKNOWN / PENDING state
```

## 5. 最终研究问题

> 在一个开放世界、可能恶意、没有共同协调者、没有共享时钟的多域系统中，是否存在一种只有“长期 AI Agent 的主体继承”才需要、而通用数字凭证、透明性、分布式一致性和 domain authority 语义无法表达的安全不变量？

若答案为 NO，A0 终止协议化。

---

# English

R4 is the final falsification round for A0. It attacks Byzantine, open-world and no-coordinator conditions. The independent-protocol hypothesis survives only if an Agent-specific lifecycle succession safety primitive remains after decomposing the problem into authority/trust semantics, signed decisions, versioning, transparency/equivocation detection, and generic distributed agreement or conservative non-completion.