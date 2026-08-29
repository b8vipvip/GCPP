# GCPP 开发进度与完整交接上下文 / GCPP Development Status and Full Handoff Context

> **默认语言：简体中文（zh-CN）**，英文镜像在后。  
> **Default language: Simplified Chinese (zh-CN)**, followed by an English mirror.  
> 最后更新 / Last updated: **2026-08-29**

# 简体中文

## 1. 当前项目定位（0.2 重构后）

GCPP 仍保留名称 **Generative Content Provenance Protocol**，但项目角色已从“独立通用内容来源协议”调整为：

> **与 C2PA 兼容的生成式内容来源扩展/Profile 体系，重点解决 C2PA 已有通用凭证机制之外的生成式 AI 专有问题。**

这是一次重要架构收敛，不是放弃原目标。

### C2PA 已成熟解决的能力，不再重复造轮子

- Manifest / Claim；
- Claim Signature；
- Hard Binding；
- Soft Binding；
- Actions / Ingredients；
- Manifest Repository；
- Durable Content Credentials；
- 多媒体、文档与文本资产支持。

### GCPP 0.2 重点

1. **Generative Event Identity**；
2. **GID / RID Separation**；
3. **Durable Text Provenance**；
4. **Partial Attribution / authenticated coverage**；
5. **Model Assurance**；
6. **Model Training / Distillation Lineage**；
7. **C2PA Adapter + 中国 GB 45438 Adapter**；
8. 统一 Verification Vector，严格区分来源事实、监管标签和训练血缘。

## 2. 当前仓库状态

- 仓库：`b8vipvip/GCPP`
- 默认分支：`main`
- 上一个稳定主线提交：`cc0c739dd5fcdf2ded79f4b9ce3b8231a1bb52ae`
- 当前重构工作分支：`standards/c2pa-alignment-0.2`
- 当前目标：完成 C2PA alignment 0.2 后开 PR 合并回 `main`。

## 3. 0.2 已确认的新不变量

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
OUTPUT_PROVENANCE != MODEL_LINEAGE
REGULATORY_LABEL != CRYPTOGRAPHIC_IDENTITY
WATERMARK_INDICATION != LEGAL_PROOF_OF_DISTILLATION
```

特别重要：

> **当前输出是谁生成的** 与 **模型能力/训练数据从哪里学来** 是两个不同 provenance domain。

## 4. C2PA 最新认识

截至 2026 年，C2PA 2.4 已经是成熟公共 Content Credentials 标准，并拥有：

- Conformance Program；
- C2PA Trust List；
- Hard/Soft Binding；
- Invisible Watermark / Fingerprint；
- Manifest Repository；
- Durable Content Credentials；
- unstructured text 等多种媒体类型支持。

OpenAI 等平台已经实际使用 C2PA，并将其与 SynthID 等 durable watermark 组合。

因此 GCPP 不再以“C2PA 不支持文本/水印/恢复”为主要差异点。

## 5. GCPP 相对 C2PA 的真正差异

### 5.1 GID / RID

- GID：权威 Generation Event ID；
- RID：短 recovery locator；
- RID 可映射到 C2PA Soft Binding identifier / repository lookup key；
- watermark/RID 只做发现，不能做身份认证。

### 5.2 Durable Text Profile

目标是在 metadata/sidecar/Unicode carrier 丢失后，仍尽量从正常可见文本的生成选择中恢复 RID。

Baseline 不允许：

- additional LLM pass；
- second model call；
- 大量完整句候选 rerank；
- per-token network / blockchain / ZK。

### 5.3 Partial Attribution

只认证当前内容中真正与来源绑定的片段，不能因少量原文/水印存在就认证全文。

### 5.4 Model Assurance

```text
MODEL_NONE
MODEL_DECLARED
MODEL_ATTESTED
MODEL_EXECUTION_PROVEN
```

### 5.5 Model Lineage

```text
LINEAGE_NONE
LINEAGE_DECLARED
LINEAGE_DATASET_COMMITTED
LINEAGE_TEACHER_ATTESTED
LINEAGE_WATERMARK_INDICATED
LINEAGE_INDEPENDENTLY_VERIFIED
```

这是 GCPP 0.2 新增的重点：训练、蒸馏、synthetic data、teacher model 与 reasoning trace 来源。

## 6. 中国当前 AIGC 标识体系研究结论

截至 2026 年，中国主流模型服务公开对齐的是：

- 《人工智能生成合成内容标识办法》；
- 强制国标 **GB 45438—2025**；
- TC260 配套实践指南。

结构主要是：

```text
Visible AI Label
+
AIGC File Metadata
  ├── Label
  ├── ContentProducer
  ├── ProduceID
  ├── ContentPropagator
  └── PropagateID
+
Optional Digital Watermark
```

DeepSeek、Kimi、豆包、腾讯混元公开协议均能找到对这套中国规则/标准的引用或实现说明。

这与 C2PA 的 signed Manifest / Trust List / Hard-Soft Binding 不是同构体系。

因此 GCPP 应提供：

```text
C2PA Adapter
GB45438 Regulatory Adapter
```

并将两种结果分开显示。

## 7. 蒸馏与“来源被洗掉”的当前技术结论

不能笼统断言“中国很多模型都是蒸馏美国前沿模型”。公开存在针对 DeepSeek 等的未经授权蒸馏指控，但不能外推为整个中国模型行业的既定事实。

真正的协议问题是：

> C2PA 和 GB 45438 主要证明**具体输出资产**，不是证明**模型训练血缘**。

典型过程：

```text
Teacher output asset
   ↓
text/data extraction
   ↓
training representation
   ↓
optimization
   ↓
Student weights
   ↓
new Student output
```

教师输出的外部 C2PA Manifest、数字签名或 `AIGC` 文件元数据不会自动变成 Student 权重中的可验证 lineage。

因此很多“来源消失”并不需要先执行某种特殊清洗，而是因为资产级 provenance 在进入训练过程时跨越了协议边界。

一些 LLM token watermark 可以在 distillation 后留下统计 radioactivity，但研究同时证明这类信号在对抗环境中并非不可消除。因此：

```text
DISTILLATION_WATERMARK = EVIDENCE
DISTILLATION_WATERMARK != CRYPTOGRAPHIC PROOF
```

仓库不提供去除/规避来源水印的操作流程。

## 8. 0.2 新增/修改关键文件

### 新增

- `spec/GCPP-C2PA-ALIGNMENT.md`
- `spec/GCPP-MODEL-LINEAGE.md`
- `research/CHINA-AIGC-LABELING.md`
- `research/DISTILLATION-PROVENANCE.md`

### 重写/升级

- `README.md`
- `spec/GCPP-CORE.md`
- `spec/GCPP-DATA-MODEL.md`
- `spec/GCPP-VERIFY.md`
- `spec/GCPP-THREAT-MODEL.md`
- `spec/README.md`
- `profiles/GCPP-TEXT-0.1.md` → 0.2 语义
- `registries/README.md`
- `ROADMAP.md`
- `DEVELOPMENT_STATUS.md`

## 9. 下一步 P0

### 9.1 完成 C2PA-based Internet Profile

需要确定：

- 目标 C2PA baseline version；
- GCPP Generation assertion schema；
- GID/RID 如何映射到 Manifest/Soft Binding；
- Model Assurance assertion；
- Model Lineage assertion；
- extension namespace；
- canonical test fixtures。

### 9.2 实现最小 C2PA-aware Verifier

验收要求：

```text
standard C2PA validation
+
GCPP extension parsing
+
Verification Vector
```

### 9.3 Text Integrity Profile

先完成 normalization、segment binding、coverage，再 benchmark robust RID watermark。

### 9.4 GB 45438 Adapter

解析中国 `AIGC` metadata，但与 C2PA signature 状态分开输出。

## 10. 下一步 P1

- Model Lineage machine-readable schema；
- dataset commitment profile；
- authorized distillation credential；
- training-run/teacher attestation；
- distillation-watermark evidence profile；
- selective disclosure；
- independent audit model。

## 11. 当前 Issues

旧 Issues #2/#3/#4 仍有价值，但 Issue #3 的方向应从“自建 canonical Internet serialization”改为“**C2PA-based GCPP Internet Profile**”。Issue #4 继续作为低开销 durable text locator benchmark。

建议新增：

- C2PA alignment tracking issue；
- GB 45438 adapter issue；
- model-lineage/distillation provenance issue。

## 12. 新聊天启动指令

> 继续开发 `b8vipvip/GCPP`。先读取 `DEVELOPMENT_STATUS.md`、`spec/GCPP-C2PA-ALIGNMENT.md`、`spec/GCPP-CORE.md`、`spec/GCPP-MODEL-LINEAGE.md`、`research/CHINA-AIGC-LABELING.md` 和 `research/DISTILLATION-PROVENANCE.md`。GCPP 0.2 已不再重新发明通用 Content Credentials，而是优先复用 C2PA，重点推进 GID/RID、Durable Text、Partial Attribution、Model Assurance、Model Lineage 和 GB45438 Adapter。不要把 output provenance 与 training lineage 混淆。

---

# English

GCPP 0.2 repositions the project as a **C2PA-compatible generative provenance profile/extension suite** rather than a competing universal credential system.

The main generative-specific work is generation-event identity, GID/RID separation, durable plain-text locator recovery, partial attribution, model-assurance levels, and a new model-training/distillation lineage dimension.

Research on China shows that major Chinese services publicly align with the Measures for Labeling AI-Generated Synthetic Content, mandatory GB 45438—2025, and TC260 implementation guidance rather than a single public C2PA deployment mandate. GCPP should therefore support both C2PA cryptographic provenance and a separate GB 45438 regulatory-label adapter.

Asset-level credentials do not automatically prove training lineage. Teacher C2PA manifests, signatures, or Chinese AIGC file metadata do not naturally become verifiable student-model lineage through optimization. Distillation-radioactivity watermarks may provide evidence, but they are not cryptographic proof and are not universally robust.
