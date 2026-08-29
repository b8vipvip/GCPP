# GCPP 路线图 / GCPP Roadmap

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror.

## 简体中文

本路线图描述的是**标准成熟度**，不是产品交付日期。

### Phase 0 — Core 概念架构冻结

目标：

- 稳定四个长期抽象：Identity、Provenance、Integrity、Evidence；
- 稳定 `GenerationID` 与 `RecoveryLocator` 的分离；
- 稳定 provenance DAG 语义；
- 稳定 Verification Vector 与展示标签；
- 冻结“watermark 是发现/恢复证据，而不是最终身份认证”的规则；
- 冻结隐私和政策中立不变量。

退出条件：不存在已知需求迫使 Core 依赖某个特定区块链、DID 方法、Hash、签名、水印、存储系统或 AI 架构。

### Phase 1 — Canonical Internet Profile

定义第一套可互操作的部署 Profile，采用具体但可替换的选择：

- canonical serialization；
- signature envelope；
- baseline hash/commitment schemes；
- key identifiers；
- record size limits；
- deterministic canonicalization；
- error behavior；
- self-contained 与 sidecar proof packaging。

退出条件：独立实现的 sign/verify 代码对同一输入产生完全相同的签名输入和结果。

### Phase 2 — Text Integrity Profile

定义：

- `norm.text-plain-1`；
- 精确 normalized-text binding；
- 稳健 segment/chunk binding；
- content-defined 或结构感知 segmentation；
- authenticated coverage 计算；
- normalization conformance vectors。

退出条件：两个独立实现对常见编辑后的 exact/partial integrity 得出相同结果。

### Phase 3 — Text Recovery Profile

研究并标准化一种高效的 in-band RecoveryLocator，要求：

- 不需要额外 LLM inference pass；
- 不需要大量候选语义重排；
- 对短文本/低熵输出支持明确 abstention；
- 提供 ECC/同步机制；
- 有可测量的 false-positive/false-negative 行为；
- 跨语言和常见复制/编辑路径测试；
- 将恢复行为仅视为 discovery。

退出条件：候选方案通过公开的稳健性、质量、吞吐、spoofing 和 transplant 测试。

### Phase 4 — Discovery 与 Transport Profiles

可选 Profile：

- `.well-known` Provider capability discovery；
- HTTPS record resolution；
- structured clipboard carriage；
- caching/mirroring；
- offline proof bundles。

退出条件：替换传输实现时不改变 Core verification。

### Phase 5 — 现有标准 Adapter

在适用场景开发对成熟生态的适配：

- C2PA/content credentials；
- DID/VC identity evidence；
- X.509/domain identity；
- transparency logs；
- trusted timestamping；
- media-specific watermark systems。

退出条件：Adapter 保持 GCPP 的验证区分，同时不把任何单一外部标准变成强制依赖。

### Phase 6 — Historical Evidence Profiles

为 append-only 和时间/存在性证据定义统一接口：

- transparency logs；
- witnesses/cross-logging；
- timestamp networks；
- blockchain/distributed-ledger anchors；
- future evidence systems。

退出条件：Verifier 能独立比较历史保证强度，而不把它与 Actor Signature 的有效性混为一谈。

### Phase 7 — Model Assurance Extensions

可选、非热路径机制：

- model commitments；
- selective disclosure；
- TEE/hardware attestation；
- verifiable inference；
- 在现实可行时使用 zero-knowledge execution proofs。

退出条件：更强的模型保证不会追溯性改变普通 `MODEL_DECLARED` 记录的语义。

### Phase 8 — 互操作与标准化就绪

在宣称稳定 1.0 前，应完成：

- 明确的 specification license/IPR policy；
- 独立实现；
- 完整正向/负向 test vectors；
- security review；
- privacy review；
- internationalization review；
- algorithm agility/deprecation procedure；
- 与相邻标准关系的正式说明；
- 稳定的 registry process。

### 路线图非目标

GCPP 不尝试构建全球内容审查权威、通用 AI 检测器、真相裁判、强制区块链或中央用户跟踪注册表。

---

# English

This roadmap is about standards maturity, not product delivery dates.

## Phase 0 — Architecture freeze for Core concepts

Goals:

- stabilize the four durable abstractions: Identity, Provenance, Integrity, Evidence;
- stabilize `GenerationID` vs `RecoveryLocator` separation;
- stabilize provenance DAG semantics;
- stabilize verification vector and presentation labels;
- freeze the rule that watermarks are discovery/recovery evidence, not final authentication;
- freeze privacy and policy-neutrality invariants.

Exit condition: no known requirement forces Core to depend on a specific blockchain, DID method, hash, signature, watermark, storage system, or AI architecture.

## Phase 1 — Canonical Internet Profile

Define a first interoperable deployment profile with concrete but replaceable choices:

- canonical serialization;
- signature envelope;
- baseline hash/commitment schemes;
- key identifiers;
- record size limits;
- deterministic canonicalization;
- error behavior;
- self-contained and sidecar proof packaging.

Exit condition: independently implemented sign/verify code produces identical signature inputs and results.

## Phase 2 — Text Integrity Profile

Define:

- `norm.text-plain-1`;
- exact normalized-text binding;
- robust segment/chunk binding;
- content-defined or structurally aware segmentation;
- authenticated coverage calculation;
- normalization conformance vectors.

Exit condition: two independent implementations agree on exact and partial integrity results after common edits.

## Phase 3 — Text Recovery Profile

Research and standardize an efficient in-band recovery locator that:

- does not require extra LLM inference passes;
- does not require large candidate semantic reranking;
- supports graceful abstention for short/low-entropy output;
- provides ECC/synchronization;
- has measured false-positive/false-negative behavior;
- is tested across languages and common copy/edit paths;
- treats recovery as discovery only.

Exit condition: a candidate scheme passes published robustness, quality, throughput, spoofing, and transplant tests.

## Phase 4 — Discovery and transport profiles

Optional profiles for:

- `.well-known` provider capability discovery;
- HTTPS record resolution;
- structured clipboard carriage;
- caching/mirroring;
- offline proof bundles.

Exit condition: transport can be replaced without changing Core verification.

## Phase 5 — Existing-standard adapters

Develop adapters for mature ecosystems where useful:

- C2PA/content credentials;
- DID/VC identity evidence;
- X.509/domain identity;
- transparency logs;
- trusted timestamping;
- media-specific watermark systems.

Exit condition: adapters preserve GCPP verification distinctions without making any one external standard mandatory.

## Phase 6 — Historical evidence profiles

Define common interfaces for append-only and time/existence evidence:

- transparency logs;
- witnesses/cross-logging;
- timestamp networks;
- blockchain/distributed-ledger anchors;
- future evidence systems.

Exit condition: verifiers can compare history assurance independently from actor signature validity.

## Phase 7 — Model assurance extensions

Optional, non-hot-path mechanisms:

- model commitments;
- selective disclosure;
- TEE/hardware attestation;
- verifiable inference;
- zero-knowledge execution proofs when practical.

Exit condition: stronger model assurance does not retroactively redefine ordinary `MODEL_DECLARED` records.

## Phase 8 — Interoperability and standardization readiness

Before a stable 1.0 claim:

- explicit specification license/IPR policy;
- independent implementations;
- complete positive/negative test vectors;
- security review;
- privacy review;
- internationalization review;
- algorithm agility/deprecation procedure;
- documented relationship to adjacent standards;
- stable registry process.

## Non-goals for the roadmap

GCPP will not attempt to build a global content-moderation authority, universal AI detector, truth oracle, mandatory blockchain, or central user-tracking registry.
