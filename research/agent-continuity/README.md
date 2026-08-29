# Agent Continuity Research / AI 主体连续性研究

> 当前分支 / Current branch: `research/a0-agent-continuity`  
> 状态 / Status: **A0 Fundamental Research — active, unmerged**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 当前目标

本目录开启一个与原 Content Provenance 方向分离的新研究主题：

> **AI Agent Continuity & Succession / AI 主体连续性与继承**

研究对象是长期 Agent 跨模型、运行时、密钥、记忆、principal、provider 和本地状态变化时，哪些主体关系、权限、义务、信誉和外部历史能够安全连续。

A0 当前不建立独立协议，不修改现有 GCPP normative Core，也不默认未来一定沿用 `GCPP` 名称。

## 当前文件

- `A0-00-RESEARCH-CHARTER.md`
  - 第一性原理研究纲领；
  - continuity multidimensional hypothesis；
  - candidate invariants；
  - kill criteria。

- `A0-01-EXTREME-STRESS-TESTS.md`
  - 13 个极端场景压力测试；
  - model replacement / migration / rollback / fork / merge 等第一轮结论。

- `A0-02-CONTINUITY-DIMENSIONS-AND-INVARIANTS.md`
  - 候选连续性维度；
  - authority non-multiplication；
  - no revocation resurrection；
  - obligation conservation；
  - provider-independence test。

- `A0-03-PRIOR-ART-AND-BOUNDARIES.md`
  - IETF Agent Network Admission；
  - Agent Identity / Delegation drafts；
  - MCP Authorization；
  - A2A；
  - W3C Agent Memory Interoperability；
  - PKI/capability/event-sourcing absorption challenge。

- `a0-stress-vectors.json`
  - 13 个机器可读研究向量；
  - 用于后续 executable lifecycle-safety harness。

## 第一轮最重要发现

### 1. `sameAgent=true` 很可能不是安全抽象

当前更像是多个相互独立维度：

```text
logical identity
execution
cryptographic control
memory
model/behavior
principal
authority
obligation
reputation
temporal state
```

这些维度仍需要继续删除/合并。

### 2. Agent Continuity 的核心可能不是“身份”，而是 succession

现有 Agent identity / delegation 赛道已很拥挤。

A0 当前真正值得继续验证的是：

```text
predecessor
  ↓ lifecycle transition
successor(s)
```

过程中：

```text
rights
obligations
historical responsibility
revocation
external effects
```

如何不会因为复制、回滚、分裂或合并而出错。

### 3. 当前三个最强危险

```text
fork     -> authority multiplication
rollback -> revoked/spent rights resurrection
merge    -> privilege union
```

另两个高价值场景：

```text
provider shutdown -> succession without original provider
partial state loss -> safe downgrade instead of false full continuity
```

## 下一步 A0

优先继续：

### A0-R2 — Absorption/Falsification

主动尝试只用：

```text
OAuth/capabilities
PKI/KMS
Agent identity drafts
W3C memory portability
event sourcing
workflow/saga semantics
```

解决全部 13 个场景。

### A0-R3 — Fork/Merge/Rollback formalization

特别研究：

```text
Authority Non-Multiplication
Revocation Monotonicity
External-Effect Monotonicity
Obligation Conservation
```

是否可以形成跨授权系统的生命周期不变量。

### A0-R4 — Executable vectors

将 `a0-stress-vectors.json` 发展为可执行测试：

```text
transition input
pre-state
post-state
explicit grants/revocations
expected safe inheritance
detected violation
```

### A0-R5 — Provider shutdown / succession

模拟原供应商永久不可用时：

```text
can counterparties verify successor?
can obligations survive?
can old authority be safely terminated?
can continuity avoid provider lock-in?
```

## 不允许的捷径

A0 不应因为一个概念听起来新颖就立即创建：

```text
Agent Continuity Token
Agent Continuity Blockchain
Agent Continuity DID
Agent Continuity Wallet
Agent Continuity Manifest
```

只有第一性原理研究和 executable falsification 证明独立公共层确有必要后，才考虑协议化。

---

# English

This directory starts A0 research on **Agent Continuity and Succession**. It is intentionally separate from the prior content-provenance direction and does not modify the current normative Core.

The first round suggests that long-lived agent continuity is not safely represented by a single identity flag. Fork can multiply authority, rollback can resurrect revoked or spent rights, merge can accidentally union privilege, obligations can be orphaned, reputation can be cloned, and provider shutdown can make succession unverifiable.

The next phase will actively attempt to solve all cases using existing identity, capability, memory, event-sourcing and workflow mechanisms. Only residual cross-system lifecycle semantics should remain candidates for a future public framework.