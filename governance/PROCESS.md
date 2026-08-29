# GCPP 标准流程 / GCPP Standards Process

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror.

## 简体中文

状态：**治理流程草案（Draft governance process）**

GCPP 的目标是成为开放技术标准，而不是由某一个实现控制的产品规范。本文件明确区分**标准协调**与**运行控制**。

### 1. 目标

标准流程应优先保证：

- 技术精确、实现独立的规范；
- 公开评审和可追溯的设计理由；
- 可互操作的独立实现；
- 在稳定前完成安全与隐私审查；
- 算法与基础设施可替换；
- 历史 Registry 信息长期可获得；
- 不存在能够特权性改写已签名来源历史的权力。

### 2. 规范成熟度

文档依次经历：

1. **Exploration** — 问题定义和替代方案；非规范性。
2. **Working Draft** — 具体协议文本；预期会变化。
3. **Candidate Draft** — 语义已经稳定到足以支持多个实现和测试向量。
4. **Proposed Standard** — 已具备互操作和安全证据。
5. **Stable Standard** — 成熟、版本化的公开规范。
6. **Historic** — 已被替代，但为历史记录验证而继续保留。

文档成熟度独立于任何特定软件实现的成熟度。

### 3. 变更机制

实质性变更 SHOULD 通过公开 Issue 和 Pull Request 提出。提案应说明：

- 要解决的问题；
- 受影响的协议层；
- 是否改变 Core 语义；
- 隐私影响；
- 安全影响；
- 互操作影响；
- 向后兼容性；
- 替代方案；
- test-vector 影响。

能够通过 Registry 或 Profile 解决的变更 SHOULD NOT 修改 GCPP Core。

### 4. Core 变更门槛

Core 变更应具有较高门槛。只有当 Identity、Provenance、Integrity、Evidence 或 Verification 的语义无法通过现有 Extension/Profile 机制表达时，才有理由修改 Core。

新增 Hash、水印、区块链、身份系统、AI 架构、序列化、传输或存储方式，通常**不是** Core 变更。

### 5. Registry 变更

Registry 新条目必须具有足够稳定的公开规范，使独立实现能够互操作。推荐条目或安全敏感条目应接受专家评审。

Registry 维护者只协调标识符，不认证 Provider、不决定法律政策，也不判断内容事实真伪。

历史/弃用算法条目必须继续保留文档，以便解释旧来源记录。

### 6. 互操作要求

文档在进入 Candidate Draft 之后的更高成熟阶段前，SHOULD 至少拥有两个独立实现，或一个实现加上由独立方生成/验证的测试向量，用来证明关键语义。

Core 进入更高阶段必须覆盖负向案例，而不仅是 happy path。

### 7. 安全与隐私审查

Candidate Draft 需要对以下问题有记录的审查：

- signature substitution/confusion；
- canonicalization ambiguity；
- identifier correlation；
- locator transplant/spoofing；
- partial-provenance inflation；
- key compromise and revocation；
- history equivocation；
- downgrade/algorithm agility；
- parser robustness；
- public/append-only evidence 中的隐私泄露。

### 8. 共识

项目应追求粗略技术共识（rough technical consensus），而不是 token-weighted voting 或 ownership-weighted voting。合并重大规范变更时，维护者应总结未解决异议及合并理由。

对协议文本达成共识，并不赋予维护者对 Provider Log、Verifier、网络、Evidence System 或 Signed Record 的运行控制权。

### 9. 参考实现

Reference Implementation 不具权威性。如果代码与规范性文本冲突，在规范被修正前，以规范和公开测试向量为准。

符合规范的 Verifier 不得仅因为参考实现依赖某个项目自营中央服务，就强制要求访问该服务。

### 10. Profile

Deployment Profile 可以为了某一时期的互操作性选择具体技术，例如 canonical serialization、signature algorithm set、HTTP discovery mechanism 或 text-locator scheme。

Profile MUST 明确哪些选择只是暂时的部署要求，而不是永久 Core 假设。

### 11. 兼容性

未知的 non-critical extension 应保持向前兼容。Major version 只应用于语义不兼容变化。

算法和 Registry 的演进通常不应要求 Core major-version 变化。

### 12. IPR 与许可

GCPP 在宣称正式标准成熟度之前，项目 MUST 采用适合开放实现的明确 specification copyright/license 和 contributor IPR policy。

在该政策确定前，贡献者应避免引入权利不清晰的第三方规范文本或专利机制。

### 13. 与其他标准的关系

GCPP 应尽可能复用或适配既有成熟工作，而不是重复建设。候选集成领域包括 Content Credential 格式、去中心化或证书型身份、Verifiable Credentials、Transparency Log、Timestamp Protocol 以及媒体专用水印标准。

Adapter 必须保持 GCPP 的关键语义区分，特别是 `provenance != truth`、`unverified != fake` 和 `locator != authentication`。

---

# English

Status: **Draft governance process**

GCPP is intended to be an open technical standard rather than a product specification controlled by one implementation. This document separates standards coordination from operational control.

## 1. Goals

The process should optimize for:

- technically precise, implementation-independent specifications;
- public review and archived design rationale;
- interoperable independent implementations;
- security and privacy review before stabilization;
- algorithm and infrastructure agility;
- long-term availability of historic registry information;
- no privileged power to rewrite signed provenance history.

## 2. Specification maturity

Documents progress through:

1. **Exploration** — problem statement and alternatives; not normative.
2. **Working Draft** — concrete protocol text; expected to change.
3. **Candidate Draft** — semantics frozen enough for multiple implementations and test vectors.
4. **Proposed Standard** — interoperability and security evidence available.
5. **Stable Standard** — mature, versioned public specification.
6. **Historic** — superseded but retained for verification of old records.

A document's maturity is independent from the maturity of any particular software implementation.

## 3. Change mechanism

Substantive changes SHOULD be proposed through a public issue and pull request. The proposal should state:

- problem being solved;
- affected protocol layer;
- whether Core semantics change;
- privacy impact;
- security impact;
- interoperability impact;
- backwards compatibility;
- alternative approaches;
- test-vector implications.

Changes that can be handled through registries or profiles SHOULD NOT modify GCPP Core.

## 4. Core change bar

Core changes have a deliberately high bar. A Core change is justified when the meaning of identity, provenance, integrity, evidence, or verification cannot be expressed through existing extension/profile mechanisms.

A new hash, watermark, blockchain, identity system, AI architecture, serialization, transport, or storage method is normally **not** a Core change.

## 5. Registry changes

Registry additions require a stable public specification sufficient for interoperable implementation. Recommended or security-sensitive entries should receive expert review.

Registry maintainers coordinate identifiers; they do not certify providers, decide legal policy, or determine content truth.

Historic/deprecated algorithm entries remain documented so old provenance can be interpreted.

## 6. Interoperability requirement

Before a document advances beyond Candidate Draft, there SHOULD be at least two independent implementations or one implementation plus independently generated/verified test vectors demonstrating the key semantics.

Core advancement requires test coverage for negative cases, not only happy paths.

## 7. Security and privacy review

Candidate drafts require documented review of:

- signature substitution/confusion;
- canonicalization ambiguity;
- identifier correlation;
- locator transplant/spoofing;
- partial-provenance inflation;
- key compromise and revocation;
- history equivocation;
- downgrade/algorithm agility;
- parser robustness;
- privacy leakage in public or append-only evidence.

## 8. Consensus

The project should seek rough technical consensus rather than token-weighted voting or ownership-weighted voting. Maintainers are expected to summarize unresolved objections and rationale when merging major normative changes.

Consensus on protocol text does not give maintainers operational control over provider logs, verifiers, networks, evidence systems, or signed records.

## 9. Reference implementations

Reference implementations are non-authoritative. If code and normative specification disagree, the specification and published test vectors govern until the specification is corrected.

No conforming verifier may require access to a project-operated central service merely because the reference implementation does.

## 10. Profiles

Deployment profiles can choose concrete technologies for interoperability at a given time, for example a canonical serialization, signature algorithm set, HTTP discovery mechanism, or text-locator scheme.

Profiles MUST state which choices are temporary deployment requirements rather than permanent Core assumptions.

## 11. Compatibility

Unknown non-critical extensions should remain forward compatible. Major versions are reserved for semantic incompatibility.

Algorithm and registry evolution should normally occur without a Core major-version change.

## 12. IPR and licensing

Before GCPP claims formal standards maturity, the project MUST adopt an explicit specification copyright/license and contributor IPR policy suitable for open implementation.

Until that policy is selected, contributors should avoid incorporating text or patented mechanisms from third parties without clear rights and attribution.

## 13. Relationship to other standards

GCPP should reuse or adapt established work where possible rather than duplicate it. Candidate integration areas include content-credential formats, decentralized or certificate-based identity, verifiable credentials, transparency logs, timestamp protocols, and media-specific watermark standards.

Adapters must preserve GCPP's semantic distinctions, especially `provenance != truth`, `unverified != fake`, and `locator != authentication`.
