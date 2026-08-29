# GCPP — 生成式信息来源与连续性协议研究 / Generative Provenance & Continuity Protocol Research

> **默认语言：简体中文（zh-CN）**。中文在前，英文在后。  
> **Default language: Simplified Chinese (zh-CN).** Chinese appears first, followed by English.

# 简体中文

## 项目定位

GCPP 是一个面向 AI 时代信息来源问题的**公共协议研究项目**。

从当前研究阶段开始，GCPP 不再以“寻找 C2PA、SPDX、CycloneDX 等现有标准尚未实现的功能并抢先补齐”为研发逻辑，也不以标准发布时间、功能数量或命名空间为竞争目标。

GCPP 的研究顺序固定为：

```text
社会/行业长期问题
    ↓
Problem
    ↓
Abstraction
    ↓
Invariant
    ↓
Protocol Primitive
    ↓
Evidence
    ↓
Implementation / Adapter
```

现有标准主要位于最后的实现与互操作层。

## 当前核心研究问题

GCPP 正在把研究问题从“某个文件是谁生成的”提升为：

> **信息经过生成、传播、编辑、组合、翻译、摘要、训练、蒸馏和再生成以后，哪些来源关系仍然存在，哪些关系可以被验证，以及证据到底能证明什么。**

这一长期问题暂称为：

**Provenance Continuity / 来源连续性**。

当前第一性原理研究假设是，一个长期稳定的公共语义层可能需要研究四个最小概念：

```text
Entity
Relation
Continuity
Evidence
```

这些仍是研究假设，不是已经冻结的 Core 数据模型。

## 为什么不是“第二套 C2PA”

GCPP 不重新定义成熟标准已经能够完成的通用能力。

例如当前生态可以继续承担：

- **C2PA**：内容凭证、签名、Hard/Soft Binding、资产历史；
- **SPDX / CycloneDX**：软件、AI、模型和数据供应链描述；
- **VC / 身份体系**：身份与授权凭证；
- **in-toto / attestation**：过程证明；
- **SCITT / transparency systems**：登记、透明度与审计证据；
- **GB 45438 等监管体系**：特定法域的 AIGC 标识要求。

GCPP 的价值不来自“再造这些对象”，而来自研究**跨这些承载层仍然成立的来源关系、连续性与证据语义**。

## 核心架构纪律

一个候选 GCPP Core 原语不能只因为“某个现有标准暂时没有该字段”而进入 Core。

它至少应该满足：

1. 解决真实且长期存在的问题；
2. 跨厂商、跨模型、跨平台仍然成立；
3. 不永久依赖某个算法、签名体系或监管制度；
4. 即使其他标准未来加入相似字段，该原语仍具有独立语义价值；
5. 可以由不同 Evidence 技术实现；
6. 支持 partial / mixed / unknown / conflicting 状态；
7. 不把事实、真实性、合法性、版权或政策结论混成一个字段。

详见 [`spec/GCPP-ARCHITECTURAL-PRINCIPLES.md`](spec/GCPP-ARCHITECTURAL-PRINCIPLES.md)。

## 来源不是单链，而是关系图

真实的信息流通常不是：

```text
A -> B -> C
```

而可能是：

```text
Source A ----quoted-from----\
                          \
Source B ----summarized-from---> Result X
                          /
Human C ------edited-by------/
                          \
Model D ----translated-by-----> Result Y
```

每条关系可以拥有不同的 Evidence、不同的可验证范围和不同的 Continuity 状态。

因此 GCPP 把 partial、mixed、transformed、unknown 和 conflicting evidence 视为正常状态，而不是协议失败。

## 长期语义边界

以下边界继续保持：

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
SIMILARITY != PROVENANCE
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
OUTPUT_PROVENANCE != MODEL_LINEAGE
REGULATORY_LABEL != CRYPTOGRAPHIC_IDENTITY
ABSENCE_OF_EVIDENCE != EVIDENCE_OF_ABSENCE
```

GCPP verifier 应优先输出可验证事实和 Evidence Vector；真实性、合规、版权、作弊、责任或发布决策属于独立 Policy / Application 层。

## 技术独立性

GCPP Core 不永久绑定：

```text
C2PA
SPDX
CycloneDX
DID / VC
X.509
specific hash
specific watermark
blockchain
transparency log
AI architecture
national regulation
```

它们都可以是某一时期非常优秀的 Profile、Adapter 或 Evidence carrier。

## 当前研究主线

1. **Information Object** — 信息对象最小抽象；
2. **Relation Model** — 来源、转换、贡献与影响关系；
3. **Provenance Continuity** — 信息变化后关系还能验证到什么程度；
4. **Evidence Semantics** — 每类证据能证明什么、不能证明什么；
5. **Partial / Mixed Provenance** — 多来源和部分可验证内容；
6. **Conflict / Unknown / Time** — 冲突声明、未知状态、时间与撤销；
7. **Privacy-preserving Provenance** — 在不公开敏感信息的前提下证明关系；
8. **Real-world validation** — 用新闻、科研、Agent、模型训练、内容平台等真实场景验证原语。

Durable Text、Generation Execution、Model Lineage、监管 Adapter 等既有方向继续保留，但需要接受上述第一性原理框架重新审查：属于 Core、Profile、Adapter 还是单纯的实现研究，将由实际问题决定。

## 文档入口

- [`research/FUNDAMENTAL-PROTOCOL-RESEARCH.md`](research/FUNDAMENTAL-PROTOCOL-RESEARCH.md) — 第一性原理研究纲领；
- [`spec/GCPP-ARCHITECTURAL-PRINCIPLES.md`](spec/GCPP-ARCHITECTURAL-PRINCIPLES.md) — 后续规范工作的架构纪律；
- [`spec/GCPP-CORE.md`](spec/GCPP-CORE.md) — 当前 Core 工作草案；
- [`spec/GCPP-C2PA-ALIGNMENT.md`](spec/GCPP-C2PA-ALIGNMENT.md) — 与 C2PA 的实现映射边界；
- [`spec/GCPP-MODEL-LINEAGE.md`](spec/GCPP-MODEL-LINEAGE.md) — 模型训练/蒸馏血缘研究；
- [`profiles/GCPP-TEXT-0.1.md`](profiles/GCPP-TEXT-0.1.md) — Durable Text / RecoveryLocator 研究；
- [`research/CHINA-AIGC-LABELING.md`](research/CHINA-AIGC-LABELING.md) — 中国 AIGC 标识体系研究；
- [`research/DISTILLATION-PROVENANCE.md`](research/DISTILLATION-PROVENANCE.md) — 蒸馏与来源继承研究；
- [`ROADMAP.md`](ROADMAP.md) — 后续路线图；
- [`DEVELOPMENT_STATUS.md`](DEVELOPMENT_STATUS.md) — 当前开发与研究交接状态。

---

# English

## Positioning

GCPP is a **public protocol research project for provenance in the AI era**.

It is not driven by a race to implement features before C2PA, SPDX, CycloneDX, or other standards. The research order is:

```text
real long-term problem
-> abstraction
-> invariant
-> protocol primitive
-> evidence
-> implementation / adapter
```

The principal research question is **provenance continuity**: after information is generated, copied, edited, combined, translated, summarized, trained on, distilled, or regenerated, which source relationships still exist, which can be verified, and what exactly does each item of evidence prove?

The current first-principles hypothesis is:

```text
Entity
Relation
Continuity
Evidence
```

This is still a research hypothesis, not a frozen Core data model.

GCPP reuses mature standards instead of competing with them. C2PA, SPDX, CycloneDX, VC, in-toto, SCITT, regulatory labeling systems, watermarks, PKI systems, and future technologies may all serve as carriers, adapters, or evidence sources. GCPP's long-term value must come from semantics that remain meaningful across those implementations.

Provenance is treated as an evidence-backed relation graph. Partial, mixed, transformed, unknown, and conflicting states are first-class. Evidence must not exceed its proof boundary, and policy/legal conclusions remain outside the protocol fact layer.
