# E0-00 — 新方向筛选 / Novelty Screen

> 状态：Research only / 非规范性

## 1. 本轮筛选原则

新的研究方向只有在满足以下条件时才值得进入：

1. 未来 AI 规模化后问题会系统性出现；
2. 单一厂商无法通过产品内部约定彻底解决；
3. 问题跨供应商、跨模型、跨组织存在；
4. 不能自然降解为已有 identity / auth / transaction / provenance / PKI / workflow / database 问题；
5. 存在可测试的安全不变量，而不是泛泛的“需要更安全”。

## 2. 已直接淘汰/降级的候选

### 2.1 用户意图跨 Agent 保真

2026 年已经出现多份 IETF 草案：Intent Token、Intent Admission Assertions、Delegation Receipt Protocol、Agentic JWT 等，直接研究 intent-bound authorization、consent、multi-hop delegation 和 audit。该方向重要，但已经进入标准竞赛。

**判定：不进入。**

### 2.2 Agent 身份、授权、能力证明

IETF/OAuth、MCP、A2A、RATS/EAT 和多份 Agent authorization/capability attestation 草案正在快速覆盖；ISO/IEC 42102 也在标准化 AI system methods/capabilities characterization。

**判定：不进入。**

### 2.3 Agent action receipts / accountability

IETF 已有 execution/action receipts、SCITT AI-agent receipt、accountability composition；W3C 也已有 AI Judgement Event Community Group。

**判定：不进入。**

### 2.4 Agent dispute / recourse

已经存在 Agentic Dispute Protocol、ADRP，以及 2026 年公开的 Legal Context Protocol 等工作。

**判定：不进入。**

### 2.5 Physical-agent coordination

Open-RMF、VDA 5050、ISO 21423、IEEE 工业 Agent interoperability 已形成明显标准化路径。

**判定：不进入。**

### 2.6 一般 uncertainty representation

不是新问题。W3C URW3 在 2008 年已经明确指出 Web 缺少标准化不确定性表示，并设计过 uncertainty ontology；ISO/IEC TS 25223 目前正在研究 AI uncertainty quantification。

**判定：不能以“统一 uncertainty 格式”为创新点。**

## 3. 暂时留下的新候选

### Epistemic Contribution / 认知增量互操作

问题不是：

```text
How do we serialize confidence=0.9?
```

而是：

```text
Given an existing evidence/judgment set Γ,
what new epistemic support does message M actually add?
```

例如：

- 5 个 Agent 都说 90%，但它们是同一个基础模型的 5 个副本；
- 5 个不同模型都说 90%，但它们全部读取同一份错误 RAG 摘要；
- Agent B 的结论完全来自 Agent A，但 aggregator 把 A+B 当成两个专家；
- 多轮 debate 让所有参与者收敛，却没有任何新的外部证据进入；
- 一个模型报告 self-confidence=0.9，另一个报告 conformal coverage=90%，数字相同但语义完全不同；
- 某置信度只在医学题域校准，却被金融 Agent 当成通用 90% 概率。

这里的潜在公共问题不是 probability aggregation 本身，而是：

> **跨实现接收方是否能知道这些“看起来像多份支持”的判断，究竟是否具有可安全合并的独立性、校准语义和适用域。**

## 4. 进入 E0 但保持高风险状态

这个候选仍很可能被以下 prior art 杀掉：

```text
W3C uncertainty ontology
probabilistic graphical models
expert-judgment aggregation
Dempster-Shafer dependence handling
Bayesian opinion pooling
calibration / conformal prediction
ordinary provenance / dependency graphs
```

因此 E0 不是协议设计阶段，而是 **novelty falsification** 阶段。

## English summary

The initial screen rejects crowded agent identity, authorization, intent, receipts, disputes, physical-agent coordination, and generic uncertainty serialization. The surviving candidate is narrower: whether heterogeneous AI judgments can safely communicate their *epistemic contribution*—especially independence, dependence, calibration scope, and comparability—so downstream systems do not convert correlated agreement into false confidence.