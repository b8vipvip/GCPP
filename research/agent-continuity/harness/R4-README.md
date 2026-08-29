# A0-R4 Ultimate Attack Harness

> **Research prototype / 非规范性**

## 中文

本目录的 R4 harness 用于反证是否真的需要一个独立的 Agent Continuity / Succession wire protocol。

它**不是**：

- 密码学实现；
- BFT 共识实现；
- transparency log；
- trust discovery protocol；
- Agent Continuity parser；
- 规范性 conformance suite。

它只测试一个问题：

> R4 的 Byzantine / open-world 安全结果，是否可以用通用的 signed-evidence、version/epoch、quorum 和 conservative UNKNOWN/PENDING 语义表达？

文件：

```text
r4_vectors.json
r4_open_world_model.py
r4_result-v0.1.json
```

执行：

```bash
python research/agent-continuity/harness/r4_open_world_model.py
```

第一轮结果：

```text
12 / 12 matched expected
```

### 重要解释

12/12 不代表“新协议成功”。

恰恰相反，它说明当前终极攻击向量仍可用现有通用理论的抽象表达：

```text
signature authenticity
transparency / auditability
epoch / version
quorum / BFT where applicable
trust policy
open-world scoped completion
UNKNOWN / PENDING / UNRESOLVED
```

所以结果削弱了独立 Agent-specific wire protocol 的必要性。

### 尚未实现

- 真正的 JWS/COSE/VC 签名验证；
- RFC 9162 / RFC 9943 transparency receipt；
- gossip/witness；
- PBFT/HotStuff/Raft 等 consensus engine；
- authority discovery；
- credential status；
- 多实现互操作。

这些缺失不应通过发明 A0 自有替代机制补齐；若需要真实实现，应复用成熟实现。

## English

The R4 harness is a falsification model, not a protocol implementation. It checks whether conservative Byzantine/open-world succession outcomes can be represented using generic signed evidence, version/epoch semantics, quorum policy, and explicit UNKNOWN/PENDING/UNRESOLVED states. The initial 12/12 result weakens the case for a new Agent-specific wire protocol.