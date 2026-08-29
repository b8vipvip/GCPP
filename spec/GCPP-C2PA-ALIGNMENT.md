# GCPP 与 C2PA 对齐规范 0.2 / GCPP-C2PA Alignment 0.2

> 状态 / Status: **Working Draft — Adapter Boundary**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 目的

本文件定义 GCPP 与 C2PA 的互操作边界。

重要说明：

> **C2PA 是当前成熟且重要的实现/承载标准，但 C2PA 的功能边界不再决定 GCPP 的研究议程。**

GCPP 后续采用第一性原理方法研究信息来源关系、连续性和 Evidence 语义；当 C2PA 已经能够表达某项事实时，GCPP 直接映射和复用，而不是创建竞争格式。

详见：

- `../research/FUNDAMENTAL-PROTOCOL-RESEARCH.md`
- `GCPP-ARCHITECTURAL-PRINCIPLES.md`

## 2. 互操作原则

对于现实部署，GCPP 实现 **SHOULD** 优先复用 C2PA 已有能力，而不是创建语义重复但不兼容的新对象。

但这是一条 implementation / adapter 原则，不是：

```text
C2PA missing feature
        ↓
GCPP research target
```

GCPP 正确的研究路径是：

```text
real problem
-> stable semantics
-> evidence requirements
-> map to C2PA where appropriate
```

具体 Internet Profile **MAY** 要求某个 C2PA 2.x 版本作为承载/签名层；GCPP Core 仍保持实现和版本独立。

## 3. 当前能力映射

| 技术事实 / GCPP 研究概念 | C2PA 可承载能力 | GCPP 处理原则 |
|---|---|---|
| Actor/Signer claim | Claim Generator / Claim Signature / identity mechanisms | 复用，不造第二套身份签名 |
| Signed provenance object | C2PA Manifest / Claim | 复用 |
| Exact content binding | Hard Binding | 复用 |
| Durable approximate/recovery binding | Soft Binding | 复用算法框架；GCPP 可研究新的恢复问题 |
| Watermark locator | Invisible-watermark soft binding | 作为 Evidence/Profile，不等同认证 |
| Manifest recovery | Manifest Repository / Soft Binding Resolution API | 复用 |
| Transformation history | Actions / Ingredients | 优先复用；GCPP 研究跨实现 relation semantics |
| Derived asset lineage | Ingredients / relationships | 优先复用 |
| Generation execution relation | 可由 assertion/relationship 承载 | 是否属于 Core 需真实问题验证 |
| RecoveryLocator | 可映射 soft-binding identifier | 作为 discovery 研究，不重新定义 Manifest |
| Partial authenticated coverage | portions / hard binding + extension semantics | 研究验证语义，不重造区域容器 |
| Model assurance evidence | AI/ML assertions/attestations | GCPP 研究 Evidence Vector 与边界 |
| Model training/distillation evidence | model credentials / ingredients / assertions 可承载部分事实 | 聚焦跨标准的 distillation/influence evidence semantics |
| Provenance Continuity | C2PA 可提供部分 exact/soft/history Evidence | GCPP 研究更一般的跨变换连续性语义 |

## 4. Durable Text 的定位

C2PA 已支持非结构化文本、soft binding、invisible watermark、fingerprint 和 Manifest Repository。GCPP-TEXT 不声称“C2PA 不支持文本”。

GCPP 研究的问题是：

> 当完整 Manifest、metadata、sidecar 或特定 carrier 丢失后，信息在传播与编辑中是否仍有低成本可恢复的来源发现信号，以及这种信号能证明到什么程度？

推荐流程可以是：

```text
visible text
   ↓
recovery evidence / locator
   ↓
candidate provenance record
   ↓
C2PA Manifest Repository or another resolver
   ↓
signed record + binding evidence
   ↓
GCPP relation / continuity interpretation
```

固定边界：locator recovery 是 discovery，不是 attribution。

## 5. Relation / Continuity 与 C2PA

C2PA 的 Actions、Ingredients、Hard/Soft Binding 可以为大量 provenance relation 和 integrity 状态提供强 Evidence。

GCPP 不应复制这些数据结构。

GCPP 新研究重点是：

- 多来源关系如何跨不同 carrier 统一解释；
- transformation 后哪些关系仍成立；
- exact、segment、transform、semantic、historical 等不同连续性是否需要不同语义；
- partial / mixed / unknown / conflicting evidence 如何报告；
- 一个 Evidence 的证明边界如何被机器一致解释。

如果这些问题最终可以完全通过 C2PA 自身的标准语义解决，则 GCPP 应删除对应重复 Core 候选，而不是维持项目独占对象。

## 6. Model / Training 信息

C2PA 已可承载模型、数据集、Ingredient、Assertion 和相关 provenance 信息。其他供应链标准也可以表达 AI/ML BOM 和数据依赖。

因此 GCPP 不建立第二套通用 Model BOM。

模型研究聚焦：

```text
OUTPUT_PROVENANCE != MODEL_LINEAGE
```

以及 teacher distillation、synthetic data、reasoning traces、training-run evidence、authorization evidence、probabilistic indication、selective disclosure 等生成式 AI 特有的证据解释问题。

## 7. Trust 与身份

GCPP 承认 C2PA Trust List / X.509 等成熟机制的现实价值。

Core 仍区分：

- cryptographic signature validity；
- real-world actor identity assurance；
- local trust policy。

未来 DID、domain key、enterprise PKI 或其他身份方法通过 Adapter/Profile 接入，而不是写死到 Core。

## 8. 不重复造轮子的规则

如果 C2PA 已经可以标准表达一项技术事实，新的 GCPP 文档 **SHOULD NOT** 再定义并行通用格式，除非：

1. GCPP 研究的是跨 carrier 仍然存在的独立语义；或
2. 现有表示无法表达真实问题中的必要状态；或
3. 文档只是 Adapter/Profile mapping，而不是新的通用容器。

特别地：

> “C2PA 当前没有某个字段”本身不是创建 GCPP Core primitive 的充分理由。

## 9. 互操作目标

未来 GCPP-aware verifier 应能够接受 C2PA 作为 Evidence 来源之一：

```text
C2PA Manifest / Claim / Binding / Actions
                ↓
        evidence extraction
                ↓
GCPP relation / continuity semantics
                ↓
        Verification Vector
```

一个不理解 GCPP 的标准 C2PA consumer 仍可验证基础 Content Credential；GCPP-aware consumer 则在不改变 C2PA 基础语义的情况下解释更一般的来源关系和连续性。

## 10. 长期原则

GCPP 与 C2PA 的理想关系不是竞争，也不是永久从属。

```text
GCPP Core = stable problem semantics
C2PA      = important current evidence/carriage ecosystem
Adapter   = interoperability boundary
```

如果未来出现更好的承载标准，GCPP Core 应能够不改变长期语义地迁移。

---

# English

This document defines the interoperability boundary between GCPP and C2PA.

C2PA is an important mature credential and evidence ecosystem, but its current feature boundary no longer defines the GCPP research agenda. GCPP follows a first-principles path from real problems to stable semantics and evidence requirements, then maps those semantics to C2PA where appropriate.

GCPP should reuse C2PA manifests, signatures, hard/soft bindings, actions, ingredients, repositories, model credentials, and related mechanisms rather than duplicate them.

The new research focus is broader: evidence-backed relations, provenance continuity under transformation, partial/mixed/unknown/conflicting states, and explicit evidence capability boundaries. C2PA can provide strong evidence for many of those facts without becoming an eternal Core dependency.

A missing C2PA field alone is not sufficient justification for a GCPP Core primitive.
