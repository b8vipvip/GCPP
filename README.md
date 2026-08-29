# GCPP

> **默认语言：简体中文（zh-CN）**。本文件先提供完整简体中文版本，随后提供完整英文版本。协议标识符、状态码和 BCP 14 规范关键词保持英文原样。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English version. Protocol identifiers, state codes, and BCP 14 normative keywords remain in English.

## 简体中文

**GCPP — Generative Content Provenance Protocol（生成式内容来源协议）**，是一套与具体实现无关、政策中立、用于可验证数字内容来源的公共协议。

GCPP 被设计为公共协议层，而不是区块链项目、中央注册中心、AI 检测器或政府验证服务。

### 四个长期问题

GCPP 标准化四个长期存在的问题：

- **Identity（身份）** — 谁作出了来源声明？
- **Provenance（来源/演化）** — 哪些生成或转换事件产生了当前内容？
- **Integrity（完整性/关联性）** — 当前内容与这些事件所绑定的内容之间是什么关系？
- **Evidence（证据）** — 哪些可验证证据支持这些声明？

除此之外的具体技术均应视为可替换实现细节。

### 架构立场

GCPP Core 的长期目标是保持：

- 存储无关（storage-agnostic）；
- 传输无关（transport-agnostic）；
- 身份系统无关（identity-system-agnostic）；
- 密码算法可敏捷替换（cryptographic-algorithm-agile）；
- 水印技术无关（watermark-agnostic）；
- 证据/锚定系统无关（evidence/anchor-system-agnostic）；
- AI 模型架构无关（AI-model-architecture-agnostic）；
- 平台无关（platform-agnostic）；
- 政策中立（policy-neutral）。

区块链可以承载历史证据，但 GCPP 不要求区块链。DID 可以实现身份层，但 GCPP 不要求 DID。SHA-256 或 Ed25519 可以出现在某个 Internet Profile 中，但它们不是永久的 Core 假设。

### 开发交接

如需了解当前仓库完整状态、架构决策、已确认约束、开放问题、未完成任务和下一开发会话的准确继续计划，请阅读：

**[`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md)**

在进一步修改协议前，应优先阅读该文件。

### 不可妥协的语义边界

1. `VERIFIED` 来源状态**不等于**内容事实为真。
2. `UNVERIFIED` **不等于**人类创作、虚假、违法或低质量。
3. Watermark（水印）或 RID 是发现/恢复证据，**不是身份认证本身**。
4. 公共内容来源证明不要求用户身份。
5. 验证必须能够在不依赖一个全球特权在线验证器的情况下进行。
6. 部分来源和修改后来源必须是一等状态。
7. 模型声明不自动等于模型真实执行证明。
8. 政策判断必须位于协议密码学验证结果之外。

### 当前规范集合

从 [`spec/README.md`](spec/README.md) 开始阅读。

- [`spec/GCPP-CORE.md`](spec/GCPP-CORE.md) — 核心语义与不变量。
- [`spec/GCPP-DATA-MODEL.md`](spec/GCPP-DATA-MODEL.md) — 抽象协议对象。
- [`spec/GCPP-VERIFY.md`](spec/GCPP-VERIFY.md) — 验证向量与结果语义。
- [`spec/GCPP-THREAT-MODEL.md`](spec/GCPP-THREAT-MODEL.md) — 攻击、非目标与残余风险。
- [`profiles/GCPP-TEXT-0.1.md`](profiles/GCPP-TEXT-0.1.md) — 实验性的低开销纯文本来源 Profile。
- [`registries/README.md`](registries/README.md) — 可扩展协议注册表。
- [`test-vectors/README.md`](test-vectors/README.md) — 一致性测试计划。
- [`governance/PROCESS.md`](governance/PROCESS.md) — 开放标准流程。
- [`ROADMAP.md`](ROADMAP.md) — 从架构草案到可互操作标准的路线图。

### 文本来源方向

基线文本 Profile 明确避免会显著增加模型成本的机制，例如额外 LLM 推理或大量多候选语义重排。

推荐架构：

```text
main model forward pass
        -> lightweight sampling/logit locator carrier
        -> token output

parallel / post-generation:
        -> content bindings
        -> signed provenance record
        -> optional external historical evidence
```

完整生成身份无需强行隐藏进短文本。GCPP 明确分离：

- **GenerationID (GID)** — 权威的生成事件身份；
- **RecoveryLocator (RID)** — 紧凑、可恢复的发现值。

恢复 RID 后，仍必须解析到签名记录并通过内容绑定验证，才能进行归属判断。

### 当前状态

仓库目前处于 **Working Draft** 阶段。现有文本不会被宣传为稳定的 1.0 标准。

在达到正式标准成熟度之前，GCPP 仍需要明确的规范许可/IPR 政策、具体的 canonical Internet deployment profile、机器可读测试样例、独立实现，以及外部安全/隐私审查。

### 贡献

参见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。实质性协议变更应保持实现独立性，并同时考虑安全、隐私、互操作性和测试向量。

---

# English

**Generative Content Provenance Protocol** — an implementation-agnostic, policy-neutral public protocol for verifiable digital-content provenance.

GCPP is being designed as a public protocol layer, not as a blockchain project, central registry, AI detector, or government verification service.

## The four durable questions

GCPP standardizes:

- **Identity** — who made the provenance claim?
- **Provenance** — what generation or transformation events produced the content?
- **Integrity** — how does the current content relate to the content bound by those events?
- **Evidence** — what verifiable evidence supports those claims?

Everything else is replaceable implementation detail.

## Architectural stance

GCPP Core is intended to remain:

- storage-agnostic;
- transport-agnostic;
- identity-system-agnostic;
- cryptographic-algorithm-agile;
- watermark-agnostic;
- evidence/anchor-system-agnostic;
- AI-model-architecture-agnostic;
- platform-agnostic;
- policy-neutral.

A blockchain can carry historical evidence, but GCPP does not require a blockchain. DID can implement identity, but GCPP does not require DID. SHA-256 or Ed25519 can appear in an Internet profile, but they are not permanent Core assumptions.

## Development handoff

For the complete current repository state, architecture decisions, confirmed constraints, open issues, unfinished work, and the exact continuation plan for a new development session, read:

**[`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md)**

This file is the preferred handoff entry point before making further protocol changes.

## Non-negotiable semantics

1. `VERIFIED` provenance does **not** mean factually true.
2. `UNVERIFIED` does **not** mean human, fake, illegal, or low quality.
3. A watermark or RID is discovery/recovery evidence, **not authentication**.
4. User identity is not required for public content provenance.
5. Verification must be possible without one globally privileged online verifier.
6. Partial and modified provenance are first-class states.
7. Model declaration is not automatically proof of actual model execution.
8. Policy decisions remain outside the protocol's cryptographic result.

## Current specification set

Start here: [`spec/README.md`](spec/README.md)

- [`spec/GCPP-CORE.md`](spec/GCPP-CORE.md) — core semantics and invariants.
- [`spec/GCPP-DATA-MODEL.md`](spec/GCPP-DATA-MODEL.md) — abstract protocol objects.
- [`spec/GCPP-VERIFY.md`](spec/GCPP-VERIFY.md) — verification vector and result semantics.
- [`spec/GCPP-THREAT-MODEL.md`](spec/GCPP-THREAT-MODEL.md) — attacks, non-goals, and residual risks.
- [`profiles/GCPP-TEXT-0.1.md`](profiles/GCPP-TEXT-0.1.md) — experimental low-overhead plain-text provenance profile.
- [`registries/README.md`](registries/README.md) — extensible protocol registries.
- [`test-vectors/README.md`](test-vectors/README.md) — conformance test plan.
- [`governance/PROCESS.md`](governance/PROCESS.md) — open standards process.
- [`ROADMAP.md`](ROADMAP.md) — route from architecture draft to interoperable standard.

## Text provenance direction

The baseline text profile intentionally avoids high-cost mechanisms such as additional LLM passes or large multi-candidate semantic reranking.

The preferred architecture is:

```text
main model forward pass
        -> lightweight sampling/logit locator carrier
        -> token output

parallel / post-generation:
        -> content bindings
        -> signed provenance record
        -> optional external historical evidence
```

The full generation identity does not need to be hidden inside short text. GCPP separates:

- **GenerationID (GID)** — authoritative event identity;
- **RecoveryLocator (RID)** — compact, recoverable discovery value.

A recovered RID must still resolve to a signed record and pass content-binding verification before attribution.

## Status

The repository is in **Working Draft** stage. Current text is deliberately not advertised as a stable 1.0 standard.

Before formal standards maturity, GCPP still needs a public IPR/specification licensing policy, a concrete canonical Internet deployment profile, machine-readable test fixtures, independent implementations, and external security/privacy review.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Substantive protocol changes should preserve implementation independence and include security, privacy, interoperability, and test-vector considerations.
