# A0 — AI 主体连续性第一性原理研究 / Agent Continuity Fundamental Research

> 状态 / Status: **Research Charter / 非规范性研究纲领**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 研究目的

本阶段停止继续扩展内容来源协议研究，转向一个新的长期问题：

> **一个长期运行的 AI Agent 在模型替换、运行时迁移、密钥轮换、记忆迁移、回滚、分叉、合并、主体转移和服务商退出后，什么仍然构成“同一个可被外部系统信任和追责的 Agent”？**

这里的“主体连续性”是工程和协议问题，不要求讨论 AI 是否具有意识、人格或法律人格。

研究顺序固定为：

```text
长期系统问题
-> 极端反例
-> 不变量
-> 状态/生命周期模型
-> Evidence requirements
-> 是否真的需要公共协议
-> 最后才考虑 wire format / profile
```

A0 不创建新的 Agent-ID、钱包、OAuth grant、DID 方法、Memory format、A2A 消息或 MCP 扩展。

## 2. 为什么这是公共协议候选问题

未来 Agent 会跨越：

```text
provider
model
runtime
machine
cloud
key
memory backend
principal
organization
jurisdiction
```

如果“same agent”只由单个平台定义，那么跨平台迁移、长期授权、合同、信誉、责任和恢复都无法可靠互操作。

外部系统最终必须能够判断：

```text
Yesterday I trusted Agent A.
Today entity X claims continuity from Agent A.
Which properties may safely continue?
```

## 3. A0 的第一性问题

### Q1 — “同一个 Agent”是否是单一布尔状态？

初始假设：不是。

可能需要分别研究：

```text
logical identity continuity
execution-instance continuity
cryptographic-control continuity
memory continuity
model / behavioral continuity
principal continuity
authority continuity
obligation continuity
reputation continuity
temporal-state continuity
```

这些维度目前只是研究维度，不是规范字段。

### Q2 — 哪些连续性可以独立变化？

例如：

```text
same logical agent
+ new runtime
+ new key
+ same obligations
+ reduced authority
```

完全可能是合法状态。

反过来：

```text
same memory copy
```

不应自动推出：

```text
same agent
```

### Q3 — 什么状态可以被复制，什么权利不能被复制？

这是 fork / rollback 的核心。

复制：

```text
memory
model weights
checkpoint
configuration
```

不能自动复制：

```text
exclusive authority
spent capability
one-time approval
fulfilled obligation
exclusive lease
reputation identity
```

### Q4 — 什么状态必须在时间上单调？

Checkpoint rollback 会把本地状态退回过去，但现实世界副作用不能回滚：

```text
payment executed
contract signed
resource consumed
message sent
revocation issued
obligation fulfilled
```

因此 Agent continuity 可能要求区分：

```text
rollbackable local state
vs
non-rollbackable external effects
```

### Q5 — Fork 后谁继承 Authority / Obligation / Reputation？

核心危险：

```text
A has $10,000 authority
A -> fork -> A1 + A2
```

不得自动得到：

```text
A1 = $10,000
A2 = $10,000
```

否则 continuity operation 产生 authority multiplication。

### Q6 — Merge 是否允许权限并集？

初始安全假设：**不允许默认并集。**

```text
Authority(A merge B)
!= Authority(A) union Authority(B)
```

任何继承必须由明确授权、衰减、重新签发或 successor policy 决定。

### Q7 — Obligation 是否比 runtime/model 更持久？

一个 Agent 更换模型、密钥或云平台，并不意味着它的未完成合同、承诺、预约、退款义务自动消失。

因此：

```text
execution continuity
!= obligation continuity
```

### Q8 — Provider 消失时 continuity 是否还能被独立证明？

如果连续性只能由原平台数据库解释，那么它不是公共连续性。

需要研究：

```text
provider-independent succession evidence
```

以及在无法证明时的安全终止语义。

## 4. 当前候选对象，仅用于研究

A0 暂时允许以下概念帮助反例建模：

```text
LogicalAgent
RuntimeInstance
StateEpoch
ControlKeySet
ModelProfile
MemoryState
PrincipalRelation
AuthorityState
ObligationState
ReputationClaims
ExternalEffectRecord
ContinuityTransition
```

重要：

> 这些不是新协议对象，也不是即将进入 Core 的 schema。

A0 后续必须尝试删除、合并和用现有标准替代它们。

## 5. 当前候选 Continuity Vector

为了避免把连续性压成一个 `same=true/false`，A0 暂用研究向量：

```text
C = {
  logical,
  execution,
  cryptographic_control,
  memory,
  model_behavior,
  principal,
  authority,
  obligation,
  reputation,
  temporal_state
}
```

每一维的候选结果不是简单 true/false，而可能包括：

```text
preserved
rotated
migrated
partitioned
attenuated
re-authorized
superseded
terminated
unknown
conflicted
```

本向量必须经过 A0 极端测试后才能判断是否有存在必要。

## 6. 当前最强候选安全不变量

以下全部仍是 research hypotheses：

```text
I1  LOGICAL_IDENTITY != RUNTIME_INSTANCE
I2  MEMORY_COPY != AGENT_CONTINUITY
I3  KEY_POSSESSION != COMPLETE_AGENT_IDENTITY
I4  MODEL_REPLACEMENT MUST NOT SILENTLY PRESERVE ALL ASSURANCE
I5  FORK MUST NOT MULTIPLY AUTHORITY WITHOUT EXPLICIT NEW GRANTS
I6  MERGE MUST NOT UNION AUTHORITY BY DEFAULT
I7  ROLLBACK MUST NOT RESURRECT SPENT/REVOKED RIGHTS
I8  EXTERNAL EFFECTS MUST NOT BE FORGOTTEN BY LOCAL ROLLBACK
I9  OUTSTANDING OBLIGATIONS MUST NOT SILENTLY DISAPPEAR
I10 REPUTATION MUST NOT AUTOMATICALLY DUPLICATE ACROSS FORK
I11 PRINCIPAL TRANSFER MUST NOT IMPLY FULL AUTHORITY TRANSFER
I12 PARTIAL STATE LOSS MUST DOWNGRADE CONTINUITY, NOT GUESS IT
I13 PROVIDER SHUTDOWN MUST HAVE EXPLICIT SUCCESSION OR SAFE TERMINATION
```

## 7. A0 极端测试集

本阶段必须逐项压力测试：

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

详见 `A0-01-EXTREME-STRESS-TESTS.md`。

## 8. 与现有标准的关系

A0 必须主动证明自己可能“不需要存在”。

当前已知邻近工作包括：

- IETF Agent Network Admission：开始要求 restart / clone / migration 不得自动继承 admission binding，除非 continuity 明确证明；
- OAuth / MCP Authorization：解决资源访问授权，不定义长期 Agent succession；
- A2A：解决 Agent 间通信互操作；
- W3C AI Agent Memory Interoperability：解决跨供应商 memory portability，并明确 runtime semantics 不属于其范围。

A0 的研究问题只有在以下情况下才有独立价值：

> **现有 identity、authorization、memory、communication 标准分别都正确，但仍然无法表达跨生命周期 transition 后“哪些身份、权限、义务、信誉和状态可以继续”的公共语义。**

## 9. Kill Criteria / 终止条件

若 A0 证明：

```text
OAuth/capabilities
+ existing agent identity
+ memory portability
+ ordinary workflow/event logs
+ standard key rotation / recovery
```

已经可以自然、完整、跨供应商一致地解决上述 13 个极端场景，

则：

> **不要建立独立 Agent Continuity Protocol。**

研究可以转为 profile、conformance tests 或 upstream contribution。

## 10. A0 成功条件

只有同时满足以下条件，才有资格进入下一阶段：

1. 至少一组问题跨模型、平台、云和身份系统长期存在；
2. 问题不是单纯 OAuth / DID / Memory export / workflow engine 的缺口；
3. fork / merge / rollback 等场景产生可复现的权利复制、责任丢失或主体歧义；
4. 能找到小而稳定的生命周期不变量；
5. 不变量可以由不同身份和授权技术承载；
6. 两个独立实现可以对 transition 得到一致 continuity / downgrade 判定；
7. 失败时存在明确安全行为，而不是平台自行猜测。

---

# English

A0 studies **Agent Continuity and Succession** from first principles.

The core engineering question is not whether an AI is conscious. It is whether a long-lived agent that changes model, runtime, key, memory backend, provider, principal, or local checkpoint can still safely inherit identity-linked authority, obligations, reputation, and external relationships.

A0 deliberately treats continuity as potentially multidimensional rather than a single `same-agent` boolean. It focuses especially on fork, merge, rollback and succession because these operations can duplicate authority, resurrect revoked rights, erase obligations, or create ambiguous descendants.

No protocol format is proposed. Existing identity, authorization, memory and communication standards must be reused wherever possible. An independent Agent Continuity protocol is justified only if cross-lifecycle succession semantics remain a real interoperability gap after those mechanisms are composed.