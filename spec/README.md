# GCPP 规范集合 / GCPP Specification Set

> 默认语言：简体中文（zh-CN） / Default language: Simplified Chinese (zh-CN)

# 简体中文

## 当前规范定位

GCPP 0.2 是**面向生成式 AI 的 C2PA 兼容扩展/Profile 规范集合**。C2PA 已经成熟定义的通用 Content Credentials 能力不再由 GCPP 平行重定义。

## 规范文档

- `GCPP-CORE.md` — 生成式 provenance 核心语义与不变量；
- `GCPP-C2PA-ALIGNMENT.md` — GCPP 与 C2PA 的映射和边界；
- `GCPP-DATA-MODEL.md` — 抽象数据模型（后续需根据 0.2 scope 继续收敛）；
- `GCPP-VERIFY.md` — Verification Vector 与展示语义；
- `GCPP-THREAT-MODEL.md` — 威胁模型；
- `GCPP-MODEL-LINEAGE.md` — 模型训练/蒸馏血缘语义。

## Profiles

- `../profiles/GCPP-TEXT-0.1.md` — 低开销纯文本 Durable Locator / RID Profile。

## Research

- `../research/CHINA-AIGC-LABELING.md` — 中国 GB 45438—2025 与主流平台标识体系研究；
- `../research/DISTILLATION-PROVENANCE.md` — 蒸馏与来源继承研究。

## Supporting material

- `../registries/README.md` — Registry framework；
- `../test-vectors/README.md` — Conformance test plan；
- `../governance/PROCESS.md` — Standards process；
- `../ROADMAP.md` — 0.2 路线图。

## 规范边界

如果能力已经可以通过 C2PA Manifest、Claim、Hard/Soft Binding、Actions、Ingredients、Manifest Repository 等表达，GCPP **SHOULD NOT** 创建并行通用格式。

GCPP 新规范必须主要解决生成式 AI 特有问题，例如：

- single Generation identity；
- GID/RID separation；
- robust plain-text recovery；
- partial attribution；
- model assurance；
- model training/distillation lineage。

---

# English

GCPP 0.2 is a **C2PA-compatible generative provenance extension/profile suite**. It does not redefine mature C2PA Content Credentials mechanisms in parallel.

Current normative/pre-normative documents cover Core semantics, C2PA alignment, abstract data model, verification, threat model, model lineage, and the low-overhead text locator profile. Informative research notes cover China's GB 45438 labeling ecosystem and provenance inheritance through distillation.
