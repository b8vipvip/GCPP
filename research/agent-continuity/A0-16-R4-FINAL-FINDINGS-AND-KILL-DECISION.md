# A0-16 — R4 最终研究结论与 Kill Decision / Final Findings

> 状态 / Status: **Final A0 Research Finding / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 最终判定

经过 A0-R1 / R2 / R3 / R4，当前研究证据**不支持**创建一个独立的：

```text
Agent Continuity Protocol
Agent Succession Protocol
```

尤其不支持新的：

- wire format；
- global successor certificate；
- Agent-specific consensus；
- Agent-specific transparency ledger；
- Agent-specific credential container；
- Agent-specific distributed transaction protocol。

### Kill Decision

```text
INDEPENDENT AGENT CONTINUITY / SUCCESSION WIRE PROTOCOL:
NOT JUSTIFIED — STOP PROTOCOLIZATION
```

这不是研究失败，而是第一性原理反证成功。

## 2. R4 没有留下不可约 Agent-specific primitive

R4 攻击：

```text
malicious authority
signed equivocation
isolated views
unknown authority universe
dynamic authority membership
no shared clock
network partitions
malicious coordinator
transparency split-view
different verifier trust policies
late-discovered relationships
Byzantine committees
indispensable authority loss
```

所有安全结论目前都可以被分解为：

```text
relationship/domain authority semantics
+
authentic signed statements
+
version/epoch/causal ordering
+
transparency/audit/gossip when required
+
generic quorum/BFT/transaction coordination when required
+
conservative UNKNOWN/PENDING/UNRESOLVED
```

没有出现必须由“AI 主体连续性协议”定义的新 primitive。

## 3. R1-R4 被淘汰的候选

### R1/R2 吸收

```text
same-Agent identity
key continuity
runtime migration
memory portability
authority non-multiplication
rollback fencing
revocation resurrection prevention
```

主要被 identity / OAuth / capabilities / PKI / event sourcing / fencing 吸收。

### R2/R3 吸收

```text
fork succession state machine
merge succession state machine
obligation transfer choreography
multi-authority commit
compensation
provider coordinator failure
```

被 domain authority semantics + distributed transaction / workflow / saga 吸收。

### R4 吸收

```text
malicious double-signing
multi-view inconsistency
Byzantine committee agreement
network-partition behavior
unknown completion
trust-policy divergence
```

被 signatures / transparency / gossip / BFT / open-world conservative semantics 吸收。

## 4. 真正保留下来的长期原则

虽然不需要新协议，A0 仍得到一组有价值的安全原则。

### 4.1 State copy is not relationship copy

```text
STATE COPY != AUTHORITY / DUTY / REPUTATION COPY
```

### 4.2 Successor declaration is not relationship transfer

```text
SUCCESSOR DECLARATION != EXTERNAL RELATIONSHIP TRANSFER
```

### 4.3 Coordination cannot create authority

```text
COORDINATION CANNOT CREATE AUTHORITY
```

### 4.4 Local validity is not global non-equivocation

```text
LOCAL VALIDITY != GLOBAL NON-EQUIVOCATION
```

### 4.5 Known relationship set is not universal completeness

```text
KNOWN SET != COMPLETE UNIVERSE
```

### 4.6 Safety may require non-completion

```text
SAFETY MAY REQUIRE PENDING / UNKNOWN / UNRESOLVED
```

### 4.7 Completion must be scope-bounded

安全声明应类似：

```text
Complete(
  relationship_set = R,
  authority_set = A,
  policy_epoch = E,
  evidence = V
)
```

而不是：

```text
Agent succession globally complete = true
```

## 5. 为什么 open-world completion 也不足以支撑新协议

R4 最有希望的新问题是：开放世界中无法证明“没有未发现的关系”。

但它最终只是一个一般性的 epistemic / open-world limitation：

```text
absence of evidence != evidence of universal absence
```

解决办法不是创造新 Agent transport，而是：

- 声明 closed-world scope；
- 声明 authority set；
- 声明 policy epoch；
- 对未知部分保持 UNKNOWN；
- 不允许无边界 completeness claim。

这适合作为安全 profile / conformance rule，而不是独立 wire protocol。

## 6. A0 最终推荐形态

如果保留 A0 成果，建议仅作为：

```text
Agent Lifecycle & Succession Threat Model
Agent Succession Security Guidance
Cross-standard interoperability profile
Adversarial conformance test corpus
```

可映射：

```text
OAuth / capability
VC / COSE / JWS
PKI / KMS
SCITT / CT-like transparency
event sourcing / workflow
Saga / distributed transaction
BFT / quorum where domain requires
W3C memory portability
A2A / MCP transport
```

不应创建 A0 自有替代栈。

## 7. 对仓库方向的意义

当前仓库不应因为已经投入 A0 研究，就强行把项目转成 Agent Continuity 标准。

正确动作是：

```text
archive findings
preserve harness and threat model
stop protocolization
choose a new research direction only if it passes a fresh first-principles novelty screen
```

## 8. 什么时候可以重新打开这个方向

只有未来出现如下反例时才值得 reopen：

> 存在一类长期 AI Agent 生命周期安全问题，无法被 domain authority semantics、existing credentials、transparency、generic distributed coordination、BFT/quorum 与 conservative unknown-state 正确表达，并且该问题跨厂商、跨行业反复出现。

在出现这种证据以前：

```text
A0 protocol work remains killed.
```

---

# English

A0-R4 does not identify an irreducible Agent-specific lifecycle succession primitive. The remaining safety problems decompose into domain relationship authority, signed statements, version/epoch semantics, transparency/audit, generic distributed coordination or BFT where required, and conservative unknown/pending states. The research therefore kills the independent Agent Continuity/Succession wire-protocol direction. The useful residue is a lifecycle threat model, security guidance, interoperability profiles, and adversarial conformance vectors.