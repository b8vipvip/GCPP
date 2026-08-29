# 参与 GCPP / Contributing to GCPP

> **默认语言：简体中文（zh-CN）**。中文版本在前，英文完整镜像在后。协议标识符与 BCP 14 关键词保持英文原样。
>
> **Default language: Simplified Chinese (zh-CN).** The Chinese version appears first, followed by the complete English mirror. Protocol identifiers and BCP 14 keywords remain in English.

## 简体中文

GCPP 作为开放公共协议进行开发。贡献应优先提升互操作性、安全性、隐私、实现独立性或规范清晰度，而不是针对某一家厂商的产品架构进行优化。

### 提交变更前

请先确认变更影响哪一层：

- Identity（身份）
- Provenance（来源/演化）
- Integrity（完整性）
- Evidence（证据）
- Verification（验证）
- Presentation（展示）
- Registry（注册表）
- Deployment profile（部署 Profile）
- Test vectors（测试向量）

如果一个变更可以表达为新的算法、身份适配器、证据方案、Carrier、Normalization Profile、传输方式、存储方法或 Deployment Profile，则通常**不应**修改 GCPP Core。

### 提案内容

实质性提案应包括：

1. 问题描述；
2. 建议语义；
3. 已考虑的替代方案；
4. 安全考虑；
5. 隐私考虑；
6. 向后/向前兼容性；
7. 互操作影响；
8. 预期测试向量变化；
9. 该变更属于 Core、Registry 还是 Profile 范围。

### 设计规则

贡献必须保持以下语义边界：

- provenance 不等于 truth；
- unverified 不等于 fake 或 human；
- locator/watermark 不等于 authentication；
- model declaration 不等于 execution proof；
- 当前内容完整性与历史签名记录本身的有效性必须区分；
- 公共内容来源不要求用户身份；
- policy 必须位于 Core verification 之外。

### 对性能敏感的 AI Profile

面向生产的基线 Profile 应避免会显著提高模型推理成本的要求，包括额外 LLM 推理、多候选完整句语义重排、逐 token 网络操作或逐 token 证明生成。

Profile 可以定义更强的可选机制，但必须明确其成本和保证级别。

### Pull Request

在实际可行时，应清楚区分规范性修改与解释性修改。凡改变规范行为的修改，都应新增或更新一致性测试案例。

大型 Core 修改应先通过设计 Issue 讨论，再将实现文本视为稳定方案。

### 规范语言

只有规范性要求才使用 BCP 14 的 requirement keywords。避免含糊使用 `trusted`、`authentic`、`verified`、`original` 等词，应明确指出具体指的是哪一个证据维度。

### 第三方工作

除非复用权利明确，否则不得复制第三方标准或论文中的规范文本、代码或专利机制。优先采用引用、Adapter 和独立撰写的互操作规范文本。

### 许可状态

在达到正式标准成熟度之前，仓库仍需确定明确的规范文档许可和贡献者 IPR 政策。该决定独立跟踪，并应在要求外部实现者依赖任何专利/许可保证之前完成。

---

# English

GCPP is being developed as an open public protocol. Contributions should improve interoperability, security, privacy, implementation independence, or clarity rather than optimize one vendor's product architecture.

## Before proposing a change

Please identify which layer is affected:

- Identity
- Provenance
- Integrity
- Evidence
- Verification
- Presentation
- Registry
- Deployment profile
- Test vectors

If a change can be expressed as a new algorithm, identity adapter, evidence scheme, carrier, normalization profile, transport, storage method, or deployment profile, it should normally **not** modify GCPP Core.

## Proposal content

Substantive proposals should include:

1. problem statement;
2. proposed semantics;
3. alternatives considered;
4. security considerations;
5. privacy considerations;
6. backwards/forward compatibility;
7. interoperability implications;
8. expected test-vector changes;
9. whether the change is Core, registry, or profile scope.

## Design rules

Contributions must preserve these semantic boundaries:

- provenance is not truth;
- unverified is not fake or human;
- a locator/watermark is not authentication;
- model declaration is not execution proof;
- current-content integrity is distinct from validity of a historical signed record;
- user identity is not required for public content provenance;
- policy remains outside Core verification.

## Performance-sensitive AI profiles

Baseline production profiles should avoid requirements that materially increase model inference cost, including additional LLM passes, multi-candidate full-sentence semantic reranking, per-token network operations, or per-token proof generation.

A profile may define stronger optional mechanisms, but their cost and assurance level must be explicit.

## Pull requests

Keep normative and explanatory changes clearly separated when practical. Add or update conformance cases for normative behavior changes.

Large Core changes should begin with a design issue before implementation text is treated as stable.

## Specification language

Use BCP 14 requirement keywords only for normative requirements. Avoid ambiguous uses of words such as `trusted`, `authentic`, `verified`, and `original`; specify exactly which evidence dimension is meant.

## Third-party work

Do not copy normative text, code, or patented mechanisms from third-party standards or papers unless reuse rights are clear. Prefer references, adapters, and independently written interoperability text.

## Licensing status

The repository still requires an explicit standards-document license and contributor IPR policy before formal standards maturity. That decision is tracked separately and should be resolved before external implementers are asked to rely on patent/license assurances.
