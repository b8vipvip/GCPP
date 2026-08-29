# A0-03 — 现有标准边界与吸收假设 / Prior Art and Absorption Boundaries

> 状态 / Status: **Prior-Art Challenge / 非规范性研究**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 目的

A0 必须主动尝试证明：

> **Agent Continuity 可能已经可以由现有 identity / authorization / memory / runtime / workflow 技术组合解决。**

如果证明成立，就不应创建独立公共协议。

本文件只记录截至 2026-08-29 的公开工作边界。Internet-Draft 属于 work in progress，不代表 IETF 已形成正式标准结论。

---

## 2. IETF Agent Network Admission：已经触碰“continuity”

公开 Internet-Draft `draft-shang-agent-network-admission-01` 已经明确提出：

```text
restart
clone
migration
```

不得因为使用相同 image / host / IP 而自动继承旧 Agent admission binding；旧 binding 只有在 continuity 被明确证明时才能继承。

它还区分：

```text
Principal identity
Agent identity
Agent Instance
Agent Runtime
Network Context
```

并强调 Agent lifecycle 与 network lifecycle 不同。

### 对 A0 的意义

这证明以下问题不是我们凭空构造：

```text
new execution != old execution
clone != automatic continuity
migration requires explicit lifecycle semantics
```

### 但它当前主要解决

```text
network admission continuity
```

并不定义：

- fork 后 authority 如何分配；
- rollback 是否可以复活 revoked/spent rights；
- outstanding obligations 如何继承；
- reputation 如何处理；
- merge successor 如何定义；
- provider shutdown 后如何做跨平台 succession。

因此它是 A0 的重要 prior art，而不是完整吸收。

参考：
- https://datatracker.ietf.org/doc/draft-shang-agent-network-admission/

---

## 3. Agent Identity / Delegation 草案：身份与授权赛道已经拥挤

2026 年存在多份 Agent Identity / Delegation Internet-Draft，包括：

- `draft-aip-agent-identity-protocol-00`
- `draft-prakash-aip-00`
- `draft-singla-agent-identity-protocol-03`
- `draft-klrc-aiagent-auth-03`
- `draft-liu-agent-operation-authorization-02`
- `draft-niyikiza-oauth-attenuating-agent-tokens-00`

它们研究：

```text
agent identifier
principal -> agent delegation
capability attenuation
scope constraints
multi-hop delegation
runtime authorization
revocation
operation authorization
```

其中 attenuating tokens 明确追求：

```text
holder may narrow authority
holder cannot expand authority
```

### 对 A0 的意义

A0 **绝对不应**再做：

```text
new generic Agent-ID
new OAuth replacement
new capability token
new multi-hop delegation format
```

这些方向已有大量竞争性工作。

### 剩余问题

身份/授权 token 通常描述：

```text
who may do what now?
```

A0 研究：

```text
when the actor itself changes through fork/merge/rollback/migration,
which identity-linked rights/duties/history may continue?
```

如果现有 capability/delegation 模型可以自然表示全部 transition，则 A0 应被吸收。

---

## 4. MCP Authorization：资源访问，不是主体继承

MCP Authorization 基于 OAuth 2.1、Protected Resource Metadata、resource indicators 等机制，目标是让 MCP client 代表 resource owner 访问受保护 MCP server。

它回答：

```text
may this client access this resource?
```

而不是：

```text
is this restored/forked/migrated Agent the legitimate successor
of the previously authorized long-lived Agent?
```

因此 A0 应复用 MCP/OAuth 授权，不应修改 MCP transport auth。

参考：
- https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization

---

## 5. A2A：Agent 通信已经快速标准化

Linux Foundation A2A 已进入大规模产业采用，定位是 Agent-to-Agent communication / interoperability。

A0 不研究：

```text
how agents discover/talk/send tasks to each other
```

而研究 lifecycle succession。

如果未来 A2A 加入 Agent lifecycle identity profile，A0 应优先映射，而不是竞争。

参考：
- https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year

---

## 6. W3C AI Agent Memory Interoperability：Memory portability 不等于主体连续性

W3C AI Agent Memory Interoperability Community Group 2026 年已开始研究跨 vendor/model/framework 的 memory portability 和 verifiability。

其公开范围包括 memory cell、identity binding、encryption、sharing/revocation、audit、erasure；同时明确把 Agent runtime semantics 列为 out of scope。

### A0 的核心反例

```text
Memory M
-> copy to Agent B1
-> copy to Agent B2
```

两个实例都拥有完整 memory，不意味着两个实例都能继承：

```text
exclusive identity
authority
obligations
reputation
```

所以：

```text
MEMORY PORTABILITY != AGENT SUCCESSION
```

A0 应与 memory interop 对接，而不是定义自己的 memory format。

参考：
- https://www.w3.org/community/ai-agent-memory-interop/

---

## 7. 普通 PKI / key rotation 是否足够？

企业身份系统长期能够处理：

```text
key rotation
certificate renewal
key revocation
account recovery
```

因此 A0 的 `Key rotation` 本身绝不是新问题。

真正需要测试的是：

> key continuity 是否足以决定 authority / obligation / reputation / state succession？

当前反例：

```text
same/recovered key
+ stale checkpoint
```

仍可能尝试使用已撤销 capability 或重复执行 external effect。

所以 key continuity 可能只是 Agent continuity 的 Evidence，而不是完整主体模型。

---

## 8. Event sourcing / workflow engine 是否已经解决 rollback 与 obligations？

成熟 workflow/event-sourcing 系统可以提供：

```text
append-only events
idempotency keys
sagas / compensation
retry semantics
workflow state
```

因此：

```text
rollback is dangerous
```

本身不是 AI 独有创新。

A0 必须证明更严格的问题：

> 一个 Agent 跨 provider/runtime/identity technology 迁移、fork 或 merge 时，是否仍缺少公共的 authority + obligation + successor semantics？

如果单纯 event log + capability store 已足够，则相关 A0 维度应删除。

---

## 9. Capability theory 是否已经解决 Authority Non-Multiplication？

线性资源、一次性 token、leases、macaroons/Biscuit 式 attenuation、capability revocation 等已有丰富理论和实现。

因此 A0 不应发明新的权限代数。

真正的候选问题是：

```text
lifecycle operation itself
(fork/merge/restore/succession)
```

是否需要一个跨授权系统都能理解的 transition contract：

```text
this successor receives these grants
these grants terminate
these obligations transfer
these branches do not inherit X
```

若 capability systems 已天然拥有这种 lifecycle transition semantics，则 A0 不需要独立层。

---

## 10. 当前 Absorption Matrix

| A0 问题 | 已有机制覆盖程度 | 当前判断 |
|---|---|---|
| Agent communication | A2A | 不做 |
| Tool authorization | MCP/OAuth | 不做 |
| Agent identity | 多个 AIP/AgentID drafts | 不做新 ID |
| Delegation | OAuth/capability/AIP drafts | 优先复用 |
| Key rotation | PKI/KMS | 已成熟 |
| Memory portability | W3C Memory Interop | 不做 memory format |
| Runtime network admission | IETF Agent Network Admission draft | 已部分覆盖 |
| Fork authority inheritance | capability theory 可部分覆盖 | **待证明** |
| Merge privilege semantics | 零散机制 | **待证明** |
| Rollback + external effects | event sourcing 可大量覆盖 | **待证明是否还需跨系统层** |
| Obligation succession | workflow/contract systems 可局部覆盖 | **待证明** |
| Reputation succession | 应用层/身份体系零散 | **待证明但可能不属 Core** |
| Provider-independent succession | 尚未看到成熟通用层 | **高优先级研究** |
| Partial-state continuity downgrade | 零散恢复机制 | **高优先级研究** |

---

## 11. 当前真正值得继续的研究中心

Prior-art 压力测试后，A0 不应围绕“身份”本身展开，而应围绕：

> **Lifecycle Succession Semantics**

即：

```text
predecessor
   ↓ transition
successor(s)
```

过程中：

```text
identity references
authority
obligations
reputation applicability
revocation
external effects
```

如何被明确：

```text
preserved
partitioned
attenuated
re-authorized
transferred
terminated
unknown
```

## 12. A0 Absorption Hypothesis

下一阶段主动尝试证明：

> **Agent Continuity 根本不需要新协议，只需要现有 Agent Identity + capability authorization + event sourcing + memory portability + workflow semantics 的组合。**

只有找到以下结构性失败，才继续：

1. 每个局部系统都能正确工作；
2. 但 lifecycle transition 跨系统后产生不可避免的歧义；
3. 歧义会造成权利复制、撤销复活、责任丢失或错误 successor；
4. 需要一个跨实现都稳定的 transition contract 才能解决；
5. 该 contract 不依赖某个特定 Agent-ID、OAuth token、cloud 或 model。

如果找不到这一类失败，A0 应终止独立协议方向。

---

# English

A0 is deliberately avoiding the already crowded agent identity, delegation, authorization, communication, and memory-format spaces. Current IETF drafts cover agent identity and capability delegation extensively, MCP uses OAuth-based resource authorization, A2A covers agent communication, W3C is actively standardizing memory interoperability, and an IETF Internet-Draft already states that restart/clone/migration must not automatically inherit network admission without explicit continuity proof.

The remaining hypothesis is narrower: long-lived **lifecycle succession semantics** across fork, merge, rollback, principal transfer and provider shutdown. A0 must prove that existing capability, event-sourcing, identity and workflow mechanisms cannot already solve these cases before proposing any independent framework.