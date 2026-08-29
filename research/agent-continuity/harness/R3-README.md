# A0-R3 Multi-Authority Succession Harness / 多权威继承反证 Harness

> 状态 / Status: **Research Prototype / 非规范性**

## 中文

这个 Harness 不实现新的 Agent Succession 协议。

它故意只使用通用概念：

```text
relationship authority
relationship version / epoch
exclusive relation constraint
atomic consistency group
ACK / DENY / UNAVAILABLE / CONFLICT / REISSUE_REQUIRED
```

目的是验证 R2 剩下的问题是否可以继续被传统分布式协调机制吸收。

运行：

```bash
cd research/agent-continuity/harness
python r3_run.py
```

当前结果：

```text
8 / 8 matched expected
```

覆盖：

```text
Multi-Issuer Fork
Obligation Double Assignment
Successor Race
Provider Dies Mid-Succession
Reputation Split
Merge with Conflicting Duties
Revocation During Succession
Partial Evidence Loss
```

### 实验纪律

```text
AUTHORITY OWNS RELATIONSHIP DECISION
COORDINATION DOES NOT CREATE AUTHORITY
STALE VERSION MUST NOT COMMIT
EXCLUSIVE RELATION MUST NOT DOUBLE-TRANSFER
MISSING REQUIRED RECEIPT => UNRESOLVED
DOMAIN CONFLICT MUST NOT BE SILENTLY RESOLVED
```

### 当前限制

- 只有一个 Python evaluator；
- 没有真实 OAuth/VC/ODRL/WS-BA carrier；
- 没有 Byzantine authority；
- 没有 equivocation / conflicting signed receipts；
- 没有网络分区和时钟问题；
- 没有 participant discovery；
- 没有第二独立实现。

所以 8/8 只说明：

> 第一组 multi-authority succession safety outcomes 可以被 generic coordination primitives 表达。

它不是协议必要性的证据，反而削弱了新 wire protocol 的理由。

## English

This harness deliberately models multi-authority succession with generic relationship-owned state, versions/epochs, exclusivity constraints and optional atomic groups. Eight initial vectors pass. The result is evidence for absorption into existing distributed coordination patterns, not evidence that a new Agent Succession protocol is required. Byzantine, open-world, participant-discovery and cross-implementation tests remain for R4.