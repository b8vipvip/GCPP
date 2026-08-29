# GCPP 与 C2PA 对齐规范 0.2 / GCPP-C2PA Alignment 0.2

> 状态 / Status: **Working Draft**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 目的

本文件定义 GCPP 与 C2PA 的边界与映射。目标不是复制 C2PA，而是让 GCPP 的生成式内容扩展尽可能直接落在 C2PA 已有的 Content Credentials 机制上。

## 2. 核心原则

GCPP 实现 **SHOULD** 优先复用现有 C2PA 能力，而不是创建语义重复但不兼容的新对象。

GCPP Core 仍保持抽象语义独立；具体 Internet Profile **MAY** 要求某个 C2PA 2.x 版本作为承载/签名层。

## 3. 能力映射

| GCPP 概念 | C2PA 对应能力 | GCPP 是否重复定义 |
|---|---|---|
| Actor/Signer claim | Claim Generator / Claim Signature / identity mechanisms | 否 |
| Signed provenance object | C2PA Manifest / Claim | 否 |
| Exact content binding | Hard Binding | 否 |
| Durable approximate/recovery binding | Soft Binding | 否 |
| Watermark locator | Invisible-watermark soft binding | 只定义生成式 Profile |
| Manifest recovery | Manifest Repository / Soft Binding Resolution API | 否 |
| Transformation history | Actions / Ingredients | 否 |
| Derived asset lineage | Ingredients / relationships | 否 |
| Generation event identity | 可作为 GCPP assertion/identifier 映射到 C2PA | 是，定义生成式语义 |
| GID/RID separation | RID 映射到 soft-binding identifier；GID 作为权威 generation-event ID | 是 |
| Text partial attribution | C2PA hard-binding portions + GCPP coverage semantics | 是，补充统一语义 |
| Model assurance levels | C2PA AI/ML assertions/attestations + GCPP assurance taxonomy | 是 |
| Training/distillation lineage | C2PA ingredients/model credentials 可承载，GCPP 定义生成式训练血缘语义 | 是 |

## 4. Durable Text 的定位

C2PA 已支持非结构化文本、soft binding、invisible watermark、fingerprint 和 Manifest Repository。GCPP-TEXT 不再声称“C2PA 不支持文本”。

GCPP-TEXT 的差异目标是：

- 不要求把完整 Manifest 永久藏入文本；
- 用短 `RecoveryLocator` 承载最小发现信息；
- 为 RID 预留 ECC、同步和冗余空间；
- 基线不得额外调用大模型或做大量句级候选重排；
- locator 被恢复后仍必须通过 C2PA/GCPP signed record 与内容绑定才能归属。

推荐流程：

```text
visible text
   ↓
low-overhead robust locator
   ↓
RID candidate(s)
   ↓
C2PA Manifest Repository / compatible resolver
   ↓
C2PA Manifest + GCPP generative assertions
   ↓
Claim Signature + Hard/Soft Binding verification
   ↓
GCPP Verification Vector
```

## 5. 信任模型

C2PA 当前使用 C2PA Trust List / X.509 trust anchors 作为其正式信任机制之一。GCPP 不应否定这一成熟生态。

同时，GCPP Core 继续区分：

- cryptographic signature validity；
- real-world actor identity assurance；
- local trust policy。

未来如果存在 DID、域名密钥、企业 PKI 或其他身份方法，应该通过 Adapter/Profile 与 C2PA/GCPP 结合，而不是把某一种身份方式写死为 GCPP Core。

## 6. 不重复造轮子的规则

如果某项能力已经可以通过 C2PA 的标准对象表达，新的 GCPP 文档 **SHOULD NOT** 再定义另一套并行格式，除非：

1. C2PA 无法表达所需语义；或
2. 已有表达缺少生成式内容所需的互操作语义；或
3. GCPP 只是定义一个可映射到 C2PA 的 profile/assertion，而非新的通用容器。

## 7. GCPP 仍然独立存在的理由

GCPP 的价值从“通用内容凭证容器”转为生成式 AI 的专门语义与恢复机制：

- 单次 Generation 身份；
- GID/RID 分离；
- 低开销纯文本 durable locator；
- partial authenticated coverage；
- model assurance taxonomy；
- model training / distillation lineage；
- 生成式内容特有的 verification semantics。

## 8. 互操作目标

未来 GCPP Internet Profile 应能够实现：

```text
GCPP generative assertion
      ↕
C2PA Manifest / Claim
      ↕
C2PA hard/soft binding
      ↕
existing C2PA validators
```

一个不理解 GCPP 扩展但理解 C2PA 的消费者，仍应能够验证基础 C2PA Claim；一个理解 GCPP 的消费者则可以进一步解析 Generation、Model Assurance、RID、Coverage 和 Model Lineage。

---

# English

## 1. Purpose

This document defines the boundary and mapping between GCPP and C2PA. GCPP should not duplicate C2PA; generative-specific extensions should be carried by existing Content Credentials mechanisms wherever practical.

## 2. Core principle

A GCPP implementation **SHOULD** reuse C2PA capabilities rather than create semantically redundant incompatible objects. GCPP Core remains abstract, while an Internet Profile **MAY** require a C2PA 2.x version as the contemporary carriage/signature layer.

## 3. Durable Text

C2PA already supports unstructured text, soft bindings, invisible watermarks, fingerprints, and manifest repositories. GCPP-TEXT therefore focuses on a different target: a compact `RecoveryLocator`, low-overhead embedding, ECC/synchronization headroom, graceful low-entropy abstention, and strict separation between locator recovery and attribution.

## 4. Trust

GCPP acknowledges the mature C2PA X.509/Trust List ecosystem while preserving a conceptual distinction between signature validity, real-world actor identity assurance, and local trust policy. Alternative identity systems belong in adapters/profiles, not permanent Core semantics.

## 5. Non-duplication rule

If C2PA can already express a capability, GCPP **SHOULD NOT** create a parallel general-purpose format unless C2PA cannot express the required semantics or GCPP is defining a mapped generative profile/assertion.

## 6. GCPP's remaining scope

GCPP focuses on single-generation identity, GID/RID separation, durable text locator recovery, partial authenticated coverage, model-assurance taxonomy, model training/distillation lineage, and generative-specific verification semantics.
