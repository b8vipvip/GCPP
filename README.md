# GCPP — 生成式内容来源扩展规范 / Generative Content Provenance Protocol Profiles

> **默认语言：简体中文（zh-CN）**。中文在前，英文在后。  
> **Default language: Simplified Chinese (zh-CN).** Chinese appears first, followed by English.

# 简体中文

## 项目定位

GCPP 是一组**面向生成式 AI 的来源、耐久恢复、模型保证与训练血缘扩展规范**。从 0.2 开始，GCPP 不再试图重新发明一套与 C2PA 平行的通用 Content Credentials 协议。

当前架构原则是：

- **C2PA 优先复用**：Manifest、Claim Signature、Hard Binding、Soft Binding、Actions、Ingredients、Manifest Repository 等成熟能力优先直接映射到 C2PA；
- **GCPP 专注生成式内容缺口**：生成事件身份、GID/RID 分离、低开销纯文本 Durable Locator、文本部分归属、模型保证等级、模型训练/蒸馏血缘；
- **Core 语义仍保持实现无关**：GCPP 的抽象语义不永久绑定某个 C2PA 版本、某个水印算法、DID、Hash、区块链或 AI 架构；
- **Internet Profile 可以选择 C2PA 作为当前推荐承载层**：这属于部署 Profile，而不是永恒 Core 假设。

## GCPP 与 C2PA 的边界

C2PA 已经成熟地解决：

- 内容凭证 Manifest；
- 签名 Claim；
- Hard Binding / Soft Binding；
- Actions / Ingredients / provenance history；
- Manifest Repository 与 Durable Content Credentials；
- 图片、音频、视频、文档及文本等资产类型。

GCPP 不重复这些能力。GCPP 重点研究和标准化：

1. **Generative Event Identity** — 精确标识一次生成事件；
2. **GID / RID Separation** — 权威 Generation ID 与可恢复短 Locator 分离；
3. **Durable Text Provenance** — metadata/sidecar/Unicode 丢失后仍尽量从可见文本恢复 provenance locator；
4. **Partial Attribution** — 只认证当前内容中真正能够绑定到来源的部分；
5. **Model Assurance** — `MODEL_DECLARED` / `MODEL_ATTESTED` / `MODEL_EXECUTION_PROVEN`；
6. **Model Lineage / Distillation Provenance** — 区分“本次输出是谁生成”与“模型能力/训练数据来自哪里”。

推荐关系：

```text
C2PA
├── Manifest / Claim / Signature
├── Hard Binding
├── Soft Binding
├── Actions / Ingredients
└── Manifest Repository
        │
        ▼
GCPP Generative Profiles
├── Generation Event Profile
├── GID / RID Profile
├── Durable Text Locator Profile
├── Partial Attribution Profile
├── Model Assurance Profile
└── Model Lineage / Distillation Profile
```

## 四个长期抽象问题

GCPP 仍保留四个长期不变量：

- **Identity** — 谁作出了声明？
- **Provenance** — 内容和模型经历了什么生成、编辑、训练或转换过程？
- **Integrity** — 当前对象与被声明对象还保持怎样的可验证关系？
- **Evidence** — 什么证据支持这些声明？

## 安全语义

以下边界继续保持：

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
OUTPUT_PROVENANCE != TRAINING_LINEAGE
```

尤其需要区分：

> **内容来源（output provenance）** 与 **模型训练/蒸馏来源（model lineage）** 是两个不同的问题。

一个模型可以合法地为自己新生成的输出创建 C2PA/GCPP 凭证，但这并不能自动证明其训练过程没有使用其他模型输出。

## 文档入口

- [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md) — 当前完整交接状态；
- [`spec/GCPP-CORE.md`](spec/GCPP-CORE.md) — GCPP 生成式语义核心；
- [`spec/GCPP-C2PA-ALIGNMENT.md`](spec/GCPP-C2PA-ALIGNMENT.md) — C2PA 映射与“不重复造轮子”边界；
- [`spec/GCPP-MODEL-LINEAGE.md`](spec/GCPP-MODEL-LINEAGE.md) — 模型训练/蒸馏血缘语义；
- [`profiles/GCPP-TEXT-0.1.md`](profiles/GCPP-TEXT-0.1.md) — 低开销纯文本 durable locator；
- [`research/CHINA-AIGC-LABELING.md`](research/CHINA-AIGC-LABELING.md) — 中国 AIGC 标识体系研究；
- [`research/DISTILLATION-PROVENANCE.md`](research/DISTILLATION-PROVENANCE.md) — 蒸馏与来源继承研究；
- [`ROADMAP.md`](ROADMAP.md) — 后续标准路线。

---

# English

## Positioning

GCPP is a suite of **generative-AI provenance, durable recovery, model-assurance, and model-lineage profiles**. Starting with 0.2, GCPP no longer attempts to reinvent a universal Content Credentials protocol parallel to C2PA.

The current architecture is:

- **Reuse C2PA first** for manifests, signed claims, hard/soft bindings, actions, ingredients, and manifest repositories;
- **Focus GCPP on generative gaps**: generation-event identity, GID/RID separation, low-overhead durable text recovery, partial attribution, model-assurance levels, and training/distillation lineage;
- **Keep Core semantics implementation-agnostic** and not permanently coupled to a C2PA version, watermark algorithm, DID, hash, blockchain, or AI architecture;
- **Allow an Internet Profile to select C2PA as the recommended contemporary carriage layer**, without turning that choice into an eternal Core dependency.

## GCPP versus C2PA

C2PA already provides mature mechanisms for manifests, signed claims, hard and soft bindings, actions/ingredients, manifest repositories, Durable Content Credentials, and many media/document/text asset types. GCPP does not duplicate them.

GCPP focuses on:

1. **Generative Event Identity**;
2. **GID / RID Separation**;
3. **Durable Text Provenance** after metadata or sidecar loss;
4. **Partial Attribution**;
5. **Model Assurance**: `MODEL_DECLARED`, `MODEL_ATTESTED`, `MODEL_EXECUTION_PROVEN`;
6. **Model Lineage / Distillation Provenance**.

## Persistent semantic boundaries

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
OUTPUT_PROVENANCE != TRAINING_LINEAGE
```

Output provenance and training/distillation lineage are separate questions. A model may correctly sign its newly generated outputs while that says nothing by itself about what teacher outputs or models influenced its training.
