# GCPP 开发进度与完整交接上下文 / GCPP Development Status and Full Handoff Context

> **默认语言：简体中文（zh-CN）**，英文摘要在后。  
> **Default language: Simplified Chinese (zh-CN)**, followed by an English summary.  
> 最后更新 / Last updated: **2026-08-29**

# 简体中文

## 1. 当前一句话状态

> **GCPP 0.2 已正式合并到 `main`：项目已从“独立通用 Content Provenance 协议”收敛为“C2PA 兼容的生成式内容来源扩展/Profile 体系”，并新增 Model Lineage / Distillation Provenance 与中国 GB 45438 Adapter 两条主线。**

## 2. 仓库状态

- 仓库：`b8vipvip/GCPP`
- 默认分支：`main`
- GCPP 0.2 架构重构 PR：**#5**
- PR #5：**Merged**
- PR #5 merge commit：`29195b94ec87a3603f8fb0c61db3cef7cc5c9200`
- 历史工作分支：`standards/c2pa-alignment-0.2`，已同步到 merge commit；后续开发应从最新 `main` 新建分支。

## 3. 0.2 项目定位

GCPP 不再重新定义 C2PA 已成熟解决的：

- Manifest / Claim；
- Claim Signature；
- Hard Binding / Soft Binding；
- Actions / Ingredients；
- Manifest Repository；
- Durable Content Credentials；
- 通用媒体/文档 Content Credentials 容器。

GCPP 重点解决生成式 AI 特有问题：

1. **Generative Event Identity**；
2. **GenerationID (GID) / RecoveryLocator (RID) Separation**；
3. **Durable Text Provenance**；
4. **Partial Attribution / authenticated coverage**；
5. **Model Assurance**；
6. **Model Training / Distillation Lineage**；
7. **C2PA Adapter + 中国 GB 45438 Adapter**；
8. 生成式专用 Verification Vector。

## 4. 已固定的语义边界

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

最重要的新边界：

> **“当前这份输出是谁生成的”与“这个模型的能力/训练数据从哪里学来的”是两个完全不同的 provenance domain。**

## 5. C2PA 关系

GCPP 0.2 的默认方向是 **C2PA-first reuse**：

```text
C2PA
├── Manifest / Claim / Signature
├── Hard / Soft Binding
├── Actions / Ingredients
└── Manifest Repository
        │
        ▼
GCPP Generative Profiles
├── Generation Event / GID
├── RID / Durable Text Locator
├── Partial Attribution
├── Model Assurance
└── Model Lineage / Distillation
```

详见：`spec/GCPP-C2PA-ALIGNMENT.md`。

## 6. 中国 AIGC 标识研究结论

中国当前公开法定/标准化体系主要是：

- 《人工智能生成合成内容标识办法》；
- 强制国标 `GB 45438—2025`；
- TC260 配套实践指南。

典型结构：

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

DeepSeek、Kimi、豆包、腾讯混元的公开协议/服务条款均能找到对上述中国标识规则的引用或实现说明。

GCPP 不把监管标签与 C2PA cryptographic provenance 混为一谈；后续通过 `GB45438 Regulatory Adapter` 映射。

详见：`research/CHINA-AIGC-LABELING.md`。

## 7. 蒸馏来源问题的当前结论

不能把“许多中国模型都是蒸馏美国模型”当作未经区分的既定事实。公开存在针对 DeepSeek 等的未经授权蒸馏指控，但这不等于所有中国模型、所有能力或所有训练阶段都已被独立证明。

协议层的核心缺口是：

> **C2PA 和 GB 45438 主要证明具体输出资产，不证明 Student Model 的训练/蒸馏血缘。**

教师输出的 C2PA Manifest、数字签名或 `AIGC` 文件 metadata 不会因为优化/训练而自动转化为 Student 权重中的可验证来源链。

一些 token watermark 可能通过 distillation 留下统计 radioactivity，但这只是 evidence，不是密码学证明：

```text
DISTILLATION_WATERMARK = EVIDENCE
DISTILLATION_WATERMARK != CRYPTOGRAPHIC PROOF
```

详见：`research/DISTILLATION-PROVENANCE.md` 与 `spec/GCPP-MODEL-LINEAGE.md`。

## 8. 当前关键文件

### Core / alignment

- `spec/GCPP-CORE.md`
- `spec/GCPP-C2PA-ALIGNMENT.md`
- `spec/GCPP-DATA-MODEL.md`
- `spec/GCPP-VERIFY.md`
- `spec/GCPP-THREAT-MODEL.md`
- `spec/GCPP-MODEL-LINEAGE.md`

### Profiles / research

- `profiles/GCPP-TEXT-0.1.md`（内容已升级为 0.2 语义）
- `research/CHINA-AIGC-LABELING.md`
- `research/DISTILLATION-PROVENANCE.md`
- `registries/README.md`
- `ROADMAP.md`

## 9. 当前 Issues

- **#2** — specification license / contributor IPR policy；
- **#3** — 已重构为 `C2PA-based GCPP Internet Profile 0.2`；
- **#4** — low-overhead robust RecoveryLocator benchmark；
- **#6** — China GB 45438—2025 regulatory labeling adapter；
- **#7** — model-lineage and distillation provenance assurance profile。

## 10. 下一步 P0

### P0.1 — Issue #3：C2PA-based Internet Profile 0.2

需要具体定义：

- C2PA 2.x baseline；
- GCPP namespace / assertion IDs；
- GID assertion；
- RID ↔ C2PA Soft Binding / Manifest Repository mapping；
- Partial Attribution assertion；
- Model Assurance assertion；
- Model Lineage assertion；
- canonical fixtures / test vectors。

### P0.2 — 最小 C2PA-aware reference verifier

```text
standard C2PA validation
+
GCPP extension parsing
+
Verification Vector
```

### P0.3 — Text Integrity

先完成：

```text
normalization
→ exact binding
→ segment/chunk binding
→ authenticated coverage
```

之后再推进 Issue #4 的 robust RID watermark benchmark。

### P0.4 — Issue #6：GB 45438 Adapter

解析中国 `AIGC` metadata/visible label，并与 C2PA signature 状态分开报告。

## 11. 下一步 P1 — Model Lineage

围绕 Issue #7 定义 machine-readable：

- `teacher-distilled-from`；
- `synthetic-data-generated-by`；
- dataset commitment；
- training-run attestation；
- teacher attestation；
- authorized distillation credential；
- watermark indication；
- selective disclosure / independent audit。

## 12. 新聊天启动提示

> 继续开发 `https://github.com/b8vipvip/GCPP.git`。先读取 `DEVELOPMENT_STATUS.md`、`spec/GCPP-C2PA-ALIGNMENT.md`、`spec/GCPP-CORE.md`、`spec/GCPP-MODEL-LINEAGE.md`、`research/CHINA-AIGC-LABELING.md` 和 `research/DISTILLATION-PROVENANCE.md`，并检查 Issues #2/#3/#4/#6/#7。GCPP 0.2 已基于 C2PA-first reuse 重构，不再重新发明通用 Content Credentials。优先推进 Issue #3 的 C2PA-based Internet Profile 和 machine-readable assertions/test vectors，不要把 output provenance、model lineage 和 regulatory labeling 混为一谈。

---

# English

GCPP 0.2 has been merged into `main` via PR #5 (`29195b94ec87a3603f8fb0c61db3cef7cc5c9200`). The project is now a **C2PA-compatible generative provenance profile/extension suite**, not a competing universal Content Credentials system.

The main workstreams are GenerationID/RecoveryLocator, durable plain-text provenance, partial attribution, model assurance, model training/distillation lineage, C2PA interoperability, and a China GB 45438 regulatory-label adapter.

The key new rule is `OUTPUT_PROVENANCE != MODEL_LINEAGE`: a valid credential for a student model's new output does not prove clean or independent training lineage. Distillation-watermark radioactivity can be evidence but is not cryptographic proof.
