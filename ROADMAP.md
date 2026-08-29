# GCPP 路线图 / GCPP Roadmap

> 默认语言：简体中文（zh-CN） / Default language: Simplified Chinese (zh-CN)

# 简体中文

本路线图从 0.2 起以“**C2PA 兼容的生成式内容扩展/Profile**”为主线，而不是重新建设通用 Content Credentials 容器。

## Phase 0 — C2PA 对齐与范围收敛

目标：

- 明确 C2PA 已有能力与 GCPP 不再重复定义的部分；
- 固定 `OUTPUT_PROVENANCE != MODEL_LINEAGE`；
- 固定 GID/RID、partial attribution、model assurance 等生成式专用语义；
- 建立 C2PA mapping document。

退出条件：GCPP 的每个新对象都能回答“为什么 C2PA 现有对象不够”。

## Phase 1 — GCPP Internet Profile 0.2（C2PA-based）

定义第一套现实可互操作 Profile：

- 选定兼容的 C2PA 2.x baseline；
- 定义 GCPP assertions/identifiers 如何进入 Manifest；
- 定义 GenerationID / RecoveryLocator 表示；
- 定义 Model Assurance / Model Lineage assertions；
- 定义 canonical extension encoding；
- 生成 byte-level test vectors。

退出条件：独立实现能用标准 C2PA validator 验证基础 Claim，并用 GCPP-aware verifier 得到相同扩展语义。

## Phase 2 — Text Integrity Profile

定义：

- `norm.text-plain-1`；
- exact normalized-text binding；
- segment/chunk binding；
- authenticated coverage；
- C2PA hard-binding mapping。

## Phase 3 — Durable Text Locator Profile

研究并 benchmark：

- 低开销 token/logit locator；
- RID capacity；
- ECC / synchronization；
- copy/paste 与编辑鲁棒性；
- multilingual；
- spoofing / transplant；
- low-entropy abstention。

硬约束：不要求额外 LLM pass、大量候选句 rerank、逐 token 网络/账本/ZK。

目标是作为 C2PA Soft Binding 的候选生成式文本算法，而不是另一套 Manifest。

## Phase 4 — Model Lineage / Distillation Profile

定义：

- teacher/source model relation；
- synthetic-data generator relation；
- dataset commitment；
- authorized distillation credential；
- training-run attestation；
- distillation-watermark evidence；
- selective disclosure；
- assurance states。

退出条件：可以明确区分 self-declared lineage、committed lineage、attested lineage 与 probabilistic watermark indication。

## Phase 5 — 中国 GB 45438 Adapter

定义中国监管标识映射：

- `AIGC.Label`；
- `ContentProducer`；
- `ProduceID`；
- `ContentPropagator`；
- `PropagateID`；
- Reserved security fields；
- visible label state。

要求：regulatory labeling 与 cryptographic provenance 分开报告。

## Phase 6 — Existing-standard adapters

继续支持：

- DID / VC；
- X.509/domain identity；
- Transparency Log / Timestamp；
- media-specific watermarks；
- future execution attestations。

## Phase 7 — Interoperability

- machine-readable fixtures；
- reference signer/verifier；
- 至少两个独立实现；
- security/privacy review；
- algorithm agility/deprecation；
- IPR/license policy。

## 非目标

GCPP 不构建：

- 第二套 C2PA；
- 全球 AI 审批中心；
- 通用 AI 检测器；
- 真相裁判；
- 强制区块链；
- 用户追踪系统。

---

# English

Starting with 0.2, the roadmap treats GCPP as a **C2PA-compatible generative provenance extension/profile suite**, not a replacement universal credential format.

Key phases are: C2PA alignment, a C2PA-based Internet Profile, text integrity, durable text locator recovery, model-lineage/distillation provenance, a China GB 45438 adapter, additional identity/history adapters, and independent interoperability implementations.

The durable-text baseline must not require extra LLM passes, large multi-candidate semantic reranking, per-token network/ledger operations, or per-token ZK proofs.
