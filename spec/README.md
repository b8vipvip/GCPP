# GCPP 规范集合 / GCPP Specification Set

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror.

## 简体中文

本目录包含 Generative Content Provenance Protocol（GCPP）的规范性和规范前（pre-normative）协议文档。

### 当前 Working Draft

- `GCPP-CORE.md` — 范围、不变量、分层模型和抽象协议语义。
- `GCPP-DATA-MODEL.md` — 与具体实现无关的对象模型。
- `GCPP-VERIFY.md` — Verification Vector、状态语义和可互操作标签。
- `GCPP-THREAT-MODEL.md` — 对手、非目标、残余风险、隐私与可用性威胁。

### Profile 文档

Profile 选择可替换技术或媒体特定行为，而不改变 Core Semantics。

- `../profiles/GCPP-TEXT-0.1.md` — 实验性纯文本来源与 Robust Locator Profile。

### 支撑标准材料

- `../registries/README.md` — 初始参数 Registry 框架。
- `../test-vectors/README.md` — 必需一致性测试案例。
- `../governance/PROCESS.md` — 标准成熟度与变更流程。
- `../ROADMAP.md` — 标准路线图。

### 规范边界

标记为 **Working Draft** 的文档并不稳定。只有在满足互操作性和安全标准后，项目才会明确标记 Candidate Draft 和 Stable Standard 成熟度。

仓库目前尚无最终 Internet Deployment Profile。因此被标记为 `provisional` 的 Identifier、Algorithm、Media Type 和具体 Serialization Choice 都不是永久的互操作保证。

### 设计规则

如果新技术能够以 Registry Entry、Adapter、Carrier、Evidence Scheme 或 Deployment Profile 的形式引入，就不应要求修改 Core Semantics。

---

# English

This directory contains the normative and pre-normative protocol documents for the Generative Content Provenance Protocol.

## Current working drafts

- `GCPP-CORE.md` — scope, invariants, layer model, abstract protocol semantics.
- `GCPP-DATA-MODEL.md` — implementation-independent object model.
- `GCPP-VERIFY.md` — verification vector, state semantics, and interoperable labels.
- `GCPP-THREAT-MODEL.md` — adversaries, non-goals, residual risk, privacy and availability threats.

## Profile documents

Profiles select replaceable technologies or media-specific behavior without changing Core semantics.

- `../profiles/GCPP-TEXT-0.1.md` — experimental plain-text provenance and robust locator profile.

## Supporting standards material

- `../registries/README.md` — initial parameter registry framework.
- `../test-vectors/README.md` — required conformance cases.
- `../governance/PROCESS.md` — standards maturity and change process.
- `../ROADMAP.md` — standards roadmap.

## Normative boundary

A document labelled **Working Draft** is not stable. The project will explicitly mark Candidate Draft and Stable Standard maturity when interoperability and security criteria are met.

The repository currently has no final Internet deployment profile. Therefore identifiers, algorithms, media types, and concrete serialization choices marked `provisional` are not permanent interoperability guarantees.

## Design rule

If a new technology can be introduced as a registry entry, adapter, carrier, evidence scheme, or deployment profile, it should not require a Core semantic change.
