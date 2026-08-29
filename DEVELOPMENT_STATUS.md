# GCPP 开发进度与完整交接上下文 / GCPP Development Status and Full Handoff Context

> **默认语言：简体中文（zh-CN）**。本文件先提供完整简体中文交接内容，随后提供完整英文镜像。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Simplified Chinese handoff appears first, followed by the complete English mirror.
>
> 最后整理日期 / Last updated: **2026-08-29**

---

# 简体中文

## 1. 文档用途

本文件是 GCPP 后续新聊天、开发者和审阅者的长期交接入口。阅读本文件后，应能在不依赖此前聊天记录的情况下理解项目目标、仓库状态、架构决策、已完成工作、不可破坏的语义边界、已确认风险、未完成任务和下一步执行顺序。

所有仓库文档的默认阅读语言为**简体中文**，同时保留完整英文版本。协议结构名、字段名、Registry ID、状态码以及 BCP 14 的 `MUST` / `SHOULD` / `MAY` 等关键词保持英文原样，以避免翻译造成规范强度或互操作语义变化。

## 2. 项目定位

**GCPP — Generative Content Provenance Protocol（生成式内容来源协议）**。

GCPP 不是 AI 检测器、监管平台、区块链项目、内容数据库或单一产品，而是一套长期演进、允许不同实现独立开发并互操作的**公共数字内容来源协议**。

GCPP 标准化四个长期抽象问题：

1. **Identity（身份）**：谁作出了来源声明？
2. **Provenance（来源/演化）**：哪些生成、编辑、转换或组合事件产生了内容？
3. **Integrity（完整性/关联性）**：当前内容与声明绑定的原始内容还保持怎样的可验证关系？
4. **Evidence（证据）**：凭什么相信身份、来源、完整性和历史声明？

协议必须能够在底层技术更换时继续存在，例如区块链消失、SHA-256 淘汰、DID 被替换、Ed25519 被后量子签名替换、水印技术换代、Transformer/LLM 架构变化，或存储/传输/Transparency 基础设施完全改变。

### 明确非目标

GCPP **不是**：

- AI 监管中心；
- AI 内容中央数据库；
- 全球 Provider 审批系统；
- 区块链协议；
- 强制某一种水印算法；
- AI / Human 二元检测器；
- 真相认证系统；
- 内容审查/删除系统；
- 版权裁判系统；
- 用户跟踪系统；
- 由某个政府、公司或平台控制的唯一认证服务。

GCPP 提供的是来源事实、内容关系和证据状态，不提供政策判断。

## 3. 仓库与分支状态

- Repository：`b8vipvip/GCPP`
- URL：`https://github.com/b8vipvip/GCPP`
- Visibility：Public
- Default branch：`main`
- 本轮规范工作分支：`standards/gcpp-core-0.1`
- Public PR：**#1 — `spec: establish GCPP Core 0.1 public standards draft`**
- Issues：#2、#3、#4 仍是后续关键标准议题。

在 2026-08-29 本次整理中，仓库所有 Markdown 文档已统一改为“简体中文在前、英文完整镜像在后”的双语格式，并要求将 `standards/gcpp-core-0.1` 合并至 `main`。完成合并后，应以 `main` 作为唯一开发主线；若历史工作分支仍保留，其内容应与主线保持已合并/同步状态，而不再承载独立未合并规范。

## 4. 当前标准成熟度

当前阶段：**GCPP Core 0.1 — Working Draft**。

尚未达到：

- Candidate Draft；
- Proposed Standard；
- Stable 1.0；
- 已证明的跨实现互操作；
- 已选定的生产级 Text Recovery Profile。

已完成的是：从概念讨论进入结构化公共标准仓库，形成 Core、Data Model、Verification、Threat Model、Text Profile 约束、Registry 框架、Test Vector 计划、Security Policy、Governance 和 Roadmap。

## 5. 最高层架构

GCPP 采用五层逻辑模型：

```text
┌──────────────────────────────────┐
│ Layer 5 — Presentation           │
│ 人类如何看到验证结果              │
├──────────────────────────────────┤
│ Layer 4 — Verification           │
│ 如何验证及输出统一语义            │
├──────────────────────────────────┤
│ Layer 3 — Evidence               │
│ Signature / Watermark / Anchor   │
├──────────────────────────────────┤
│ Layer 2 — Provenance             │
│ Generation / Transform / Lineage │
├──────────────────────────────────┤
│ Layer 1 — Identity               │
│ Actor / Provider / Model / Keys  │
└──────────────────────────────────┘
```

数据库、HTTP、P2P、本地文件、云、Transparency Log、Timestamp、Blockchain 等均属于**物理实现层**，不属于 Core 的永久依赖。

Core 必须保持：

- Storage-Agnostic；
- Transport-Agnostic；
- Identity-System-Agnostic；
- Algorithm-Agile；
- Watermark-Agnostic；
- Evidence/Anchor-System-Agnostic；
- Model-Architecture-Agnostic；
- Platform-Agnostic；
- Policy-Neutral。

## 6. 核心对象与已冻结设计决策

### 6.1 Actor / Identity

`Actor` 可以是 AI Provider、Human、Organization、Editing Tool、Camera/Recorder、Autonomous Agent 或 Hardware Device。

```text
ActorIdentifier {
  method
  identifier
}
```

Core 不绑定 DID、X.509、raw key 或 domain key。

必须区分：

- **Cryptographic Identity**：谁控制某个 Key/Identifier；
- **Real-World Identity Claim**：该 Key 是否对应现实中的某个公司、品牌或组织。

密码学不能凭空证明“某公钥就是某现实公司”；这需要 Domain Control、VC、第三方 Attestation、Key Continuity 等 Evidence。

### 6.2 Provenance Event 与 DAG

协议基本单位是一次内容状态变化事件，而不是文件。Event 可表示 Generate、Capture、Human Edit、AI Rewrite、Translate、Summarize、Compose、Render、Transcode、Publish 等。

Provenance 结构必须支持**多 Parent DAG**，而不是单 Parent 链，因为内容可能由多个来源组合。

### 6.3 GenerationID（GID）与 RecoveryLocator（RID）分离

这是当前最重要的 Core 决策之一。

- **GID**：标识某一次具体 Generation Event 的权威高熵 Identifier。
- **RID**：在纯文本复制、Metadata 丢失等情况下用于找回 Candidate Provenance Record 的短 Recovery Locator。

RID：

- 不是身份凭证；
- 可以更短、部分恢复或碰撞；
- 可以解析到多个 Candidate Record；
- 只用于 Discovery/Recovery；
- 必须继续验证 Signed Record + Content Binding 才能归属。

因此：**Watermark/RID ≠ Authentication**。

### 6.4 Provenance Record

当前抽象结构：

```text
ProvenanceRecord {
  version
  event {
    id
    type
    time?
  }
  actor {
    identifier
  }
  subject {
    media_type
    bindings[]
  }
  model_claim?
  parents[]
  carriers[]
  evidence[]
  extensions[]
}
```

Core 不写死序列化格式。Canonical Encoding 由 Internet Profile 决定。

### 6.5 Model Claim 分级

至少区分：

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

普通 Provider Signature 最多直接建立 `MODEL_DECLARED`。TEE、Verifiable Inference、ZK Execution 等只作为未来可选 Evidence，不能成为第一代主推理热路径的强制要求。

### 6.6 Content Binding

```text
ContentBinding {
  binding_type
  algorithm
  normalization_profile
  value
}
```

Core 不绑定某个固定 Hash。一个 Subject 可以同时拥有 raw-bytes、normalized-text、structured representation、segment/chunk commitment 等多个 Binding。

Full Hash Mismatch 不能自动抹掉仍然有效的 Partial Provenance。

### 6.7 Exact 与 Partial Integrity

必须区分：

- Exact Content Binding；
- Segment/Chunk Binding；
- Authenticated Coverage；
- Unknown/New Content；
- Lineage-Based Derivative Validation。

攻击者不能保留一小块真实来源内容，就把整个伪造 Document 认证为同一来源。

### 6.8 Evidence 可插拔

```text
Evidence {
  evidence_type
  scheme
  subject
  proof
  parameters?
}
```

Evidence 可以由 Signature、Watermark Recovery、Transparency Inclusion、Timestamp、Witness、Blockchain Anchor、VC、Hardware Attestation、Execution Proof 或未来机制实现。

区块链只是其中一种实现，不是 Core。

### 6.9 Carrier 与 Proof 分离

Carrier 只搬运 Record 或 Locator，例如 Embedded Manifest、Sidecar、Clipboard、Document Metadata、Robust Watermark、Remote Reference。

关键原则：**Proof is authoritative; transport is not.**

通过不可信服务器、缓存或 P2P 节点获得的 Record，只要 Signature 与 Binding 验证通过，仍可成立。

## 7. 已冻结验证语义

GCPP 输出结构化 `VerificationVector`，而不是单一 AI/Human Boolean。至少包含：

- actor authentication；
- record signature；
- model assurance；
- exact integrity；
- partial integrity / authenticated coverage；
- locator state；
- lineage state；
- historical evidence；
- unsupported critical features。

可派生展示标签：

- `VERIFIED_ORIGINAL`
- `VERIFIED_DERIVATIVE`
- `PARTIAL_PROVENANCE`
- `LOCATOR_ONLY`
- `UNVERIFIED`

以下语义是项目不变量：

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
```

来源认证永远不能自动升级为事实真实性、合法性、质量、作弊判断或内容处置政策。

## 8. Text Profile 当前结论

纯文本是 GCPP 最具区别化价值、也最困难的场景。目标是在 HTML/Metadata/Custom Clipboard Information 丢失后，仍尽量通过可见文本中的低开销 Locator Carrier 恢复 RID，再通过外部 Signed Record 完成真正认证。

### 硬性能边界

Baseline **不得要求**：

- 额外 LLM inference pass；
- 第二模型调用；
- 每句大量完整候选后再 rerank；
- 大规模语义候选重排；
- 每 token 网络调用；
- 每 token 区块链/日志调用；
- 每 token ZK proof。

推荐热路径：

```text
model forward
    ↓
logits
    ↓
lightweight locator/watermark processor
    ↓
sampling
    ↓
token
```

Content Binding、Chunk State、ECC State 可以旁路/流式计算；Record Finalize/Sign 在生成完成后进行；Historical Evidence 可异步批处理。

### 短文本与低熵输出必须允许 Abstain

极短文本、Code、JSON、Formula、Deterministic Output、低可选 Token 场景不应为了强塞水印而破坏正确性。可以 fallback 到 Attached Proof、Sidecar、Clipboard Provenance 或 Signed Record。

### 尚未选定具体 Watermark Algorithm

当前 `GCPP-TEXT-0.1.md` 只定义架构约束和评估要求。Issue #4 必须通过 Benchmark 后再决定 Candidate Scheme，包括吞吐、质量、多语言、False Positive/Negative、插入/删除/替换、Copy/Paste、Paraphrase、Translation、Spoofing、Watermark Stealing、RID Transplant 和 ECC Recovery Curve。

## 9. Canonicalization 是当前最高技术瓶颈

GCPP 还没有第一套真正可执行、byte-for-byte 一致的 Canonical Serialization，因此目前还不能宣称跨实现互操作。

必须标准化：

- Serialization；
- Domain Separation；
- Signing Input；
- Unicode Normalization；
- Line Ending；
- Whitespace；
- Control Character；
- Visible Text Extraction；
- HTML/Markdown/JSON Canonicalization；
- Chunking Boundary；
- Normalization Profile ID。

下一阶段需要正式定义 `norm.text-plain-1` 等 Profile 及 Machine-Readable Test Vector。

## 10. 历史证据 / Transparency

GCPP Core 不要求区块链。真正的抽象问题是：是否存在额外 Evidence 证明某个 Commitment 在某时间之前已经存在，并降低 Provider 无痕重写历史的能力？

可实现为：

- CT-style Append-Only Transparency Log；
- Witness/Cross-Logging；
- Timestamp Service/Network；
- Blockchain/Distributed Ledger；
- Federated Append-Only Log；
- Future Evidence System。

Actor Signature Assurance 与 Historical Evidence Assurance 必须分开。

## 11. 隐私边界

Public GCPP Provenance 默认不得要求：

- User Name；
- Platform Account ID；
- Email / Phone；
- IP；
- Device ID；
- Geolocation；
- Raw Prompt；
- Session ID。

Generation ID 必须按事件独立、不可预测、不编码用户身份，避免成为跨内容 Tracking Identifier。

如果企业审计需要 Input Binding，应采用 Salted/Randomized Commitment + Selective Disclosure。

## 12. Provider / 模型平台接受度原则

GCPP 不能成为模型输出延迟来源：

- token path 不等待外部服务；
- 不等待 Blockchain/Transparency Confirmation 才返回内容；
- 不强制重型 Semantic Reranking；
- 不强制 ZKML/TEE；
- Historical Evidence 可异步批处理；
- Internal Routing/Checkpoint 不默认公开。

Provider 的价值包括品牌防伪、证明“没有可验证的本平台来源”、企业审计、统一来源接口和更清晰的责任边界。代价是 Key Management、Signing、Logging、Watermark/Carrier 和兼容性成本，因此协议必须保持低开销和隐私友好。

## 13. 当前关键文件

### 根目录

- `README.md` — 项目入口、架构立场与核心语义。
- `DEVELOPMENT_STATUS.md` — 本交接文档。
- `ROADMAP.md` — Phase 0–8 标准成熟度路线。
- `CONTRIBUTING.md` — 贡献与规范变更要求。
- `SECURITY.md` — 安全报告与安全语义边界。

### `spec/`

- `spec/README.md` — 规范索引。
- `spec/GCPP-CORE.md` — Core 语义、不变量和主要抽象。
- `spec/GCPP-DATA-MODEL.md` — 与物理序列化无关的抽象对象模型。
- `spec/GCPP-VERIFY.md` — Verification Vector 与 Label 语义。
- `spec/GCPP-THREAT-MODEL.md` — 攻击、非目标和残余风险。

### 其他

- `profiles/GCPP-TEXT-0.1.md` — 低开销纯文本来源 Profile。
- `registries/README.md` — Registry 框架。
- `test-vectors/README.md` — Conformance Test Plan。
- `governance/PROCESS.md` — 开放标准治理流程。

## 14. 已确认不可轻易退回的设计不变量

1. `Provenance != Truth`。
2. `UNVERIFIED != FAKE / HUMAN / ILLEGAL / LOW_QUALITY`。
3. `Watermark / RID != Authentication`。
4. Public Provenance 不需要 User Identity。
5. Verification 不依赖唯一中央 Online Verifier。
6. Core 不永久绑定 Storage / Transport / Identity / Hash / Signature / Watermark / Ledger / Model Architecture。
7. Partial Provenance 必须是一等状态。
8. Policy Decision 位于 GCPP 之外。
9. GID 与 RID 分离。
10. Model Claim 区分 Declared / Attested / Execution-Proven。
11. Physical Infrastructure 是实现，不是协议本体。
12. 新技术优先通过 Registry/Profile/Extension 引入，而不是修改 Core。

## 15. 已确认风险与现实边界

- 文本水印无法在“任意彻底重写”后保证存在；目标是提高剥离成本，而不是永久追踪。
- 短文本没有足够容量承载完整 GID + Signature + 高冗余 ECC；因此采用 GID/RID 分离和 Abstention。
- Provider Signature 证明“谁声明了什么”，不自动证明 Provider 没撒谎；更强模型执行证明需要额外 Evidence。
- 现实品牌身份无法仅从密码学自动得到，需要外部 Identity Evidence。
- 区块链不是必要条件，只是一种 Historical Evidence 实现。
- 当前尚缺 Canonical Bytes、Machine-Readable Fixtures 和 Independent Reference Implementations。
- Specification License / Contributor IPR 仍未确定。

## 16. 当前开放 Issues

### Issue #2 — Specification License / Contributor IPR

在 Candidate Draft 前明确规范文本许可、参考代码许可、专利/IPR 要求、第三方算法引用规则和历史版本可再分发性。

### Issue #3 — GCPP Internet Profile 0.1

当前最高优先级。需要定义第一套具体但可替换的 Canonical Encoding、Signature Envelope、Baseline Algorithm、Key ID、Limits、Packaging 和 Downgrade/Deprecation 行为。

### Issue #4 — Low-Overhead Robust RecoveryLocator

只在硬性能边界内 Benchmark Candidate Text Recovery Scheme，先测试后标准化。

## 17. 未完成任务与优先级

### P0

1. 完成 GCPP Internet Profile 0.1（Issue #3）。
2. 生成 Machine-Readable Test Vectors。
3. 实现最小 Reference Signer + Verifier。
4. 最好建立第二个独立语言/实现进行互操作验证。

成功标准：两个独立实现对相同 Abstract Record 得到完全一致的 Canonical Signing Bytes 和 Verification Result。

### P1

1. 定义 `norm.text-plain-1` 与 Text Integrity Profile。
2. 定义 Robust Chunk/Segment Binding 与 Coverage。
3. 推进 Issue #4 Text Recovery Benchmark。
4. 定义 Clipboard/Sidecar Carrier Profile。

正确顺序必须是：

```text
Canonical Text
→ Exact Binding
→ Partial/Chunk Binding
→ Coverage
→ RecoveryLocator Watermark
```

### P2

- C2PA Adapter；
- DID / VC / X.509 Identity Adapter；
- Transparency / Timestamp / Witness Evidence Adapter。

### P3

- Model Commitment；
- Selective Disclosure；
- TEE Attestation；
- Verifiable Inference；
- 在成本现实可接受时研究 ZKML。

这些不得阻塞 Core、Internet Profile 和 Text Integrity。

## 18. 下一聊天的直接执行顺序

新聊天收到“继续开发 GCPP”后：

1. 检查 `b8vipvip/GCPP` 当前 `main`、PR 和 Issues 状态；
2. 先读 `DEVELOPMENT_STATUS.md`；
3. 再读 `spec/GCPP-CORE.md`、`GCPP-DATA-MODEL.md`、`GCPP-VERIFY.md`、`GCPP-THREAT-MODEL.md`、`ROADMAP.md`；
4. 检查 Issues #2/#3/#4 是否有新讨论；
5. 不重新把项目设计成 Blockchain AI Watermark、Central Registry 或单一监管系统；
6. 优先推进 Issue #3：Internet Profile 0.1；
7. 重大规范变更继续使用 Branch + PR + Test Vector；
8. Core 变化必须解释为什么不能用 Profile/Registry/Extension 解决；
9. 不将任何 Blockchain、DID、Hash、Watermark、Provider 写成永久 Core Dependency；
10. 不使用会明显拖慢模型的大量候选语义重排作为 Text Baseline；
11. 不把 RID/Watermark Recovery 当 Provider Authentication；
12. 不把 `UNVERIFIED` 呈现为 Fake/Human；
13. 不把 `VERIFIED` 呈现为 Factually True；
14. 优先构建可执行 Test Vector 和 Independent Interoperability，而不是继续堆叠抽象概念。

## 19. 公共标准治理原则

GCPP 借鉴 DNS、TLS、OAuth、Certificate Transparency 等长期协议的设计思想：

- 协议语义与物理实现分离；
- Stable Core + Replaceable Profile/Algorithm；
- Mechanism 与 Policy 分离；
- Transport 不必可信，Proof 必须可验证；
- 分布式运行，不要求全球唯一 Server；
- 可以有 Registry/标准协调，但不赋予运行控制权；
- Caching/Offline Verification 是重要能力；
- Algorithm Agility / Deprecation 从第一版考虑；
- Forward Compatibility 需要明确 Extension Behavior；
- Append-Only Correction 优先于 Silent History Rewrite。

目标不是“完全没有治理”，而是：**标准可以被协调，但运行事实不能由单一机构任意改写。**

## 20. 最终愿景

GCPP 最终不是“AI Watermark 2.0”，而是尝试定义：

> **Content Provenance Layer of the Internet — 互联网内容来源层。**

DNS 回答名字指向哪里；TLS 回答正在和谁安全通信、通信是否被篡改；OAuth 回答谁被授权做什么；GCPP 希望回答：

> **我现在看到的数字内容从哪里来、由谁声明产生、经历过什么变化、当前内容还保留多少原始来源关系，以及这些结论凭什么可以被独立验证？**

## 21. 新聊天可直接使用的启动提示

> 继续开发 GitHub 仓库 `https://github.com/b8vipvip/GCPP.git`。先读取仓库根目录 `DEVELOPMENT_STATUS.md`，再读取 `spec/GCPP-CORE.md`、`spec/GCPP-DATA-MODEL.md`、`spec/GCPP-VERIFY.md`、`spec/GCPP-THREAT-MODEL.md`、`ROADMAP.md`，并检查 Issues #2/#3/#4 和当前 PR/branch 状态。不要重新设计已确认的 Core，也不要把协议退回区块链/中央监管/单一水印方案。优先推进 Issue #3：GCPP Internet Profile 0.1 的 canonical encoding、signature envelope、baseline algorithms 和 byte-for-byte test vectors，然后实现最小 reference signer/verifier，并以跨实现互操作作为验收标准。

## 22. 一句话状态

> **GCPP 已完成从概念到 Core 0.1 公共标准 Working Draft 的结构化落库，并完成仓库文档中英双语化；下一核心里程碑是通过 Internet Profile + Canonical Bytes + Machine-Readable Test Vectors + Independent Signer/Verifier，把抽象规范变成真正可互操作的协议。**

---

# English

## 1. Purpose of this document

This file is the long-term handoff entry point for future chats, developers, and reviewers. After reading it, a contributor should understand the project goal, repository state, architectural decisions, completed work, semantic invariants, confirmed risks, unfinished tasks, and the correct continuation order without relying on earlier chat history.

All repository documents use **Simplified Chinese as the default reading language**, followed by a complete English mirror. Protocol structure names, field names, Registry IDs, state codes, and BCP 14 keywords such as `MUST`, `SHOULD`, and `MAY` remain in English so translation cannot silently change normative strength or interoperability semantics.

## 2. Project positioning

**GCPP — Generative Content Provenance Protocol**.

GCPP is not an AI detector, regulatory platform, blockchain project, content database, or single product. It is intended to be a long-lived **public digital-content provenance protocol** that can be independently implemented and interoperated.

GCPP standardizes four durable abstractions:

1. **Identity** — who made the provenance claim?
2. **Provenance** — what generation, editing, transformation, or composition events produced the content?
3. **Integrity** — what verifiable relationship remains between the current content and the content bound by the claims?
4. **Evidence** — why should identity, provenance, integrity, and history claims be believed?

The protocol must survive replacement of its physical technologies: blockchains may disappear, SHA-256 may be deprecated, DID may be replaced, Ed25519 may give way to post-quantum signatures, watermarking may change completely, Transformer/LLM architectures may disappear, and storage/transport/transparency infrastructure may be replaced.

### Explicit non-goals

GCPP is **not**:

- an AI regulatory authority;
- a central AI-content database;
- a global provider approval system;
- a blockchain protocol;
- a mandatory single watermark algorithm;
- an AI/human binary detector;
- a truth-certification system;
- a content censorship/deletion system;
- a copyright court;
- a user-tracking system;
- a verification service controlled by one government, company, or platform.

GCPP reports provenance facts, content relationships, and evidence states. Policy judgments remain outside the protocol.

## 3. Repository and branch state

- Repository: `b8vipvip/GCPP`
- URL: `https://github.com/b8vipvip/GCPP`
- Visibility: Public
- Default branch: `main`
- Standards working branch used for this draft: `standards/gcpp-core-0.1`
- Public PR: **#1 — `spec: establish GCPP Core 0.1 public standards draft`**
- Issues #2, #3, and #4 remain key follow-up standards work.

During the 2026-08-29 consolidation, all Markdown documentation was converted to a bilingual format with Simplified Chinese first and a complete English mirror after it, and `standards/gcpp-core-0.1` was scheduled to be merged into `main`. After consolidation, `main` is the primary development line. If a historical working branch remains, it should contain only already-merged/synchronized material rather than independent unmerged normative text.

## 4. Current standards maturity

Current stage: **GCPP Core 0.1 — Working Draft**.

Not yet reached:

- Candidate Draft;
- Proposed Standard;
- Stable 1.0;
- demonstrated cross-implementation interoperability;
- a selected production-grade Text Recovery Profile.

Completed work is the transition from concept discussion to a structured public standards repository containing Core, Data Model, Verification, Threat Model, Text Profile constraints, Registry framework, Test Vector plan, Security Policy, Governance, and Roadmap.

## 5. Top-level architecture

GCPP uses five logical layers:

```text
┌──────────────────────────────────┐
│ Layer 5 — Presentation           │
│ human-readable results           │
├──────────────────────────────────┤
│ Layer 4 — Verification           │
│ verification and common semantics│
├──────────────────────────────────┤
│ Layer 3 — Evidence               │
│ Signature / Watermark / Anchor   │
├──────────────────────────────────┤
│ Layer 2 — Provenance             │
│ Generation / Transform / Lineage │
├──────────────────────────────────┤
│ Layer 1 — Identity               │
│ Actor / Provider / Model / Keys  │
└──────────────────────────────────┘
```

Databases, HTTP, P2P, local files, cloud storage, transparency logs, timestamp systems, and blockchains are physical implementation choices outside permanent Core dependencies.

Core must remain storage-agnostic, transport-agnostic, identity-system-agnostic, algorithm-agile, watermark-agnostic, evidence/anchor-system-agnostic, model-architecture-agnostic, platform-agnostic, and policy-neutral.

## 6. Core objects and frozen design decisions

### 6.1 Actor / Identity

An `Actor` can be an AI provider, human, organization, editing tool, camera/recorder, autonomous agent, or hardware device.

```text
ActorIdentifier {
  method
  identifier
}
```

Core does not bind to DID, X.509, raw keys, or domain keys.

Cryptographic identity must be distinguished from real-world identity claims. Cryptography can establish control of a key/identifier; it cannot magically prove that a key corresponds to a real-world company or brand. Domain control, VC, third-party attestations, and key continuity are examples of separate identity evidence.

### 6.2 Provenance Event and DAG

The basic protocol unit is a content-state transition event, not a file. Events can represent generation, capture, human edit, AI rewrite, translation, summarization, composition, rendering, transcoding, publication, and future registered transforms.

Provenance must support a **multi-parent DAG**, because content can combine multiple sources.

### 6.3 GenerationID (GID) and RecoveryLocator (RID)

This is one of the most important Core decisions.

- **GID** is the authoritative high-entropy identifier for one generation event.
- **RID** is a compact recovery locator used to discover candidate provenance records after plain-text copying or metadata loss.

An RID is not authentication, may be shorter, partial, collision-prone, or resolve to multiple candidates. It is discovery/recovery material only. Signed record and content-binding verification are still required for attribution.

Therefore: **Watermark/RID ≠ Authentication**.

### 6.4 Provenance Record

Current abstract structure:

```text
ProvenanceRecord {
  version
  event {
    id
    type
    time?
  }
  actor {
    identifier
  }
  subject {
    media_type
    bindings[]
  }
  model_claim?
  parents[]
  carriers[]
  evidence[]
  extensions[]
}
```

Core does not fix a serialization format. Canonical encoding belongs to the Internet Profile.

### 6.5 Model Claim assurance levels

At minimum:

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

A normal provider signature can directly establish at most `MODEL_DECLARED`. TEE, verifiable inference, or ZK execution proofs are future optional evidence and must not be mandatory in the first-generation model hot path.

### 6.6 Content Binding

```text
ContentBinding {
  binding_type
  algorithm
  normalization_profile
  value
}
```

Core does not bind to a permanent hash. A Subject may have multiple bindings such as raw bytes, normalized text, structured representation, and segment/chunk commitments.

A full-hash mismatch must not automatically erase valid partial provenance.

### 6.7 Exact and Partial Integrity

The protocol must distinguish exact content binding, segment/chunk binding, authenticated coverage, unknown/new content, and lineage-based derivative validation.

Keeping one small authentic fragment must not allow an attacker to authenticate an entire forged document as originating from that source.

### 6.8 Pluggable Evidence

```text
Evidence {
  evidence_type
  scheme
  subject
  proof
  parameters?
}
```

Evidence can be implemented through signatures, watermark recovery, transparency inclusion, timestamps, witnesses, blockchain anchors, VCs, hardware attestation, execution proofs, or future schemes.

Blockchain is one possible implementation, not Core.

### 6.9 Carrier versus Proof

A Carrier only transports a Record or Locator, such as an embedded manifest, sidecar, clipboard format, document metadata, robust watermark, or remote reference.

Key principle: **Proof is authoritative; transport is not.**

A record obtained through an untrusted server, cache, or P2P node can still be valid if signatures and bindings verify.

## 7. Frozen verification semantics

GCPP emits a structured `VerificationVector`, not an AI/human boolean. It includes actor authentication, record signature, model assurance, exact integrity, partial integrity/authenticated coverage, locator state, lineage state, historical evidence, and unsupported critical features.

Derived presentation labels include:

- `VERIFIED_ORIGINAL`
- `VERIFIED_DERIVATIVE`
- `PARTIAL_PROVENANCE`
- `LOCATOR_ONLY`
- `UNVERIFIED`

Project invariants:

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
```

Provenance authentication must never automatically become factual truth, legality, quality, cheating detection, or content-policy action.

## 8. Current Text Profile conclusions

Plain text is the most distinctive and difficult GCPP use case. After HTML, metadata, or custom clipboard data is lost, the goal is to recover an RID through a low-overhead visible-text locator carrier and then perform real authentication through an external signed record.

### Hard performance boundary

The baseline must not require additional LLM inference passes, a second model call, large full-sentence candidate reranking, per-token network calls, per-token blockchain/log calls, or per-token ZK proofs.

Preferred hot path:

```text
model forward
    ↓
logits
    ↓
lightweight locator/watermark processor
    ↓
sampling
    ↓
token
```

Content bindings, chunk state, and ECC state can be computed in parallel/streaming paths. Record finalization/signing occurs at generation completion, and historical evidence can be batched asynchronously.

### Short and low-entropy output must allow abstention

Very short text, code, JSON, formulas, deterministic output, and constrained low-entropy decoding should not sacrifice correctness merely to force a watermark. They may fall back to attached proof, sidecars, clipboard provenance, or signed records.

### No production watermark algorithm has been selected

`GCPP-TEXT-0.1.md` currently defines architecture constraints and evaluation requirements only. Issue #4 must benchmark candidate schemes for throughput, quality, multilingual behavior, false positives/negatives, insert/delete/substitute edits, copy/paste, paraphrase, translation, spoofing, watermark stealing, RID transplant, and ECC recovery curves before standardization.

## 9. Canonicalization is the highest current technical bottleneck

GCPP does not yet define the first executable byte-for-byte canonical serialization, so cross-implementation interoperability cannot yet be claimed.

The next phase must standardize serialization, domain separation, signing input, Unicode normalization, line endings, whitespace, control characters, visible-text extraction, HTML/Markdown/JSON canonicalization, chunking boundaries, and normalization profile IDs.

Profiles such as `norm.text-plain-1` need normative definitions and machine-readable vectors.

## 10. Historical evidence / Transparency

GCPP Core does not require blockchain. The abstract problem is whether additional evidence can show that a commitment existed before a time and reduce the ability of a provider to silently rewrite history.

Possible implementations include CT-style append-only logs, witnesses/cross-logging, timestamp services/networks, blockchains/distributed ledgers, federated append-only logs, and future evidence systems.

Actor-signature assurance and historical-evidence assurance remain separate dimensions.

## 11. Privacy boundary

Public GCPP provenance does not require user names, platform account IDs, email/phone, IP, device IDs, geolocation, raw prompts, or session IDs.

Generation IDs must be event-specific, unpredictable, and non-user-encoding to avoid becoming tracking identifiers.

Enterprise input binding should use salted/randomized commitments plus selective disclosure.

## 12. Provider/model-platform acceptance principles

GCPP must not become a model-output latency source. The token path does not wait for external services; content is not held for blockchain/transparency confirmation; heavy semantic reranking and mandatory ZKML/TEE are excluded from the baseline; historical evidence can be asynchronous; internal routing/checkpoints are not public by default.

Provider value includes brand anti-forgery, evidence that content lacks a verifiable origin from the provider, enterprise auditability, common provenance interfaces, and clearer responsibility boundaries. Costs include key management, signing, logging, carrier/watermark integration, and compatibility work, so the protocol must remain low-overhead and privacy-preserving.

## 13. Key files

Root: `README.md`, `DEVELOPMENT_STATUS.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `SECURITY.md`.

Specifications: `spec/README.md`, `spec/GCPP-CORE.md`, `spec/GCPP-DATA-MODEL.md`, `spec/GCPP-VERIFY.md`, `spec/GCPP-THREAT-MODEL.md`.

Supporting material: `profiles/GCPP-TEXT-0.1.md`, `registries/README.md`, `test-vectors/README.md`, `governance/PROCESS.md`.

## 14. Design invariants not to regress

1. `Provenance != Truth`.
2. `UNVERIFIED != FAKE / HUMAN / ILLEGAL / LOW_QUALITY`.
3. `Watermark / RID != Authentication`.
4. Public provenance does not require user identity.
5. Verification does not depend on one central online verifier.
6. Core does not permanently bind storage, transport, identity, hash, signature, watermark, ledger, or model architecture.
7. Partial provenance is first-class.
8. Policy decisions remain outside GCPP.
9. GID and RID remain separated.
10. Model claims distinguish declared, attested, and execution-proven states.
11. Physical infrastructure is implementation, not protocol essence.
12. New technologies should enter through registries, profiles, or extensions whenever possible.

## 15. Confirmed risks and physical limits

Text watermarks cannot be guaranteed to survive arbitrary total rewriting. Very short text lacks capacity for full GID/signature/high-redundancy ECC. Provider signatures prove who declared what, not that the provider is incapable of lying. Real-world brand identity needs external identity evidence. Blockchain is optional. Canonical bytes, machine-readable fixtures, independent implementations, and final licensing/IPR policy remain unfinished.

## 16. Open issues

### Issue #2 — Specification License / Contributor IPR

Define the specification-text license, reference-code license, patent/IPR requirements, third-party algorithm rules, and historical redistribution guarantees before Candidate Draft.

### Issue #3 — GCPP Internet Profile 0.1

Highest current priority. Define the first concrete but replaceable canonical encoding, signature envelope, baseline algorithms, key IDs, limits, packaging, and downgrade/deprecation behavior.

### Issue #4 — Low-Overhead Robust RecoveryLocator

Benchmark candidate text recovery schemes only within the hard performance boundary. Measure first, standardize later.

## 17. Unfinished work and priority

### P0

1. Complete GCPP Internet Profile 0.1.
2. Produce machine-readable test vectors.
3. Implement a minimal reference signer and verifier.
4. Preferably create a second implementation in another language/library.

Success criterion: independent implementations produce identical canonical signing bytes and verification results for the same abstract record.

### P1

Define `norm.text-plain-1`, Text Integrity Profile, robust chunk/segment binding and coverage, run Issue #4 benchmarks, and define clipboard/sidecar carrier profiles.

Required order:

```text
Canonical Text
→ Exact Binding
→ Partial/Chunk Binding
→ Coverage
→ RecoveryLocator Watermark
```

### P2

C2PA adapter, DID/VC/X.509 identity adapters, and transparency/timestamp/witness evidence adapters.

### P3

Model commitments, selective disclosure, TEE attestation, verifiable inference, and ZKML only when practical. These must not block Core, Internet Profile, or Text Integrity.

## 18. Direct continuation order for a new chat

1. Inspect current `main`, PRs, and Issues in `b8vipvip/GCPP`.
2. Read `DEVELOPMENT_STATUS.md` first.
3. Then read Core, Data Model, Verify, Threat Model, and Roadmap.
4. Check Issues #2/#3/#4 for new discussion.
5. Do not redesign GCPP back into a blockchain AI-watermark project, central registry, or single regulator system.
6. Prioritize Issue #3, the Internet Profile.
7. Keep major normative changes behind branches, PRs, and test vectors.
8. Explain why any Core change cannot be handled by a Profile/Registry/Extension.
9. Never make a named blockchain, DID, hash, watermark, or provider a permanent Core dependency.
10. Do not use expensive multi-candidate semantic reranking as the baseline text mechanism.
11. Do not treat RID/watermark recovery as provider authentication.
12. Do not present `UNVERIFIED` as fake or human.
13. Do not present `VERIFIED` as factually true.
14. Prioritize executable test vectors and independent interoperability over adding more abstractions.

## 19. Public-standard governance principles

GCPP follows durable ideas from DNS, TLS, OAuth, and Certificate Transparency: separate protocol semantics from physical implementation; stable Core plus replaceable profiles/algorithms; separate mechanism from policy; do not trust transport when proof can be verified; allow distributed operation without one global server; allow registry coordination without operational control; make caching/offline verification important; plan algorithm agility/deprecation early; define forward-compatible extension behavior; prefer append-only correction over silent history rewriting.

The goal is not “no governance.” The goal is: **standards can be coordinated, while operational facts cannot be arbitrarily rewritten by one actor.**

## 20. Long-term vision

GCPP is not intended to become “AI Watermark 2.0.” It aims at a **Content Provenance Layer of the Internet**.

DNS answers where a name points. TLS answers who is being securely communicated with and whether communication was altered. OAuth answers who is authorized to do what. GCPP aims to answer:

> **Where did the digital content I am seeing come from, who claimed to produce it, what transformations did it undergo, how much of its original provenance relationship remains, and why can those conclusions be independently verified?**

## 21. Ready-to-use prompt for a new chat

> Continue development of `https://github.com/b8vipvip/GCPP.git`. Read `DEVELOPMENT_STATUS.md` first, followed by `spec/GCPP-CORE.md`, `spec/GCPP-DATA-MODEL.md`, `spec/GCPP-VERIFY.md`, `spec/GCPP-THREAT-MODEL.md`, and `ROADMAP.md`, then inspect Issues #2/#3/#4 and the current PR/branch state. Do not redesign the established Core or turn the project back into a blockchain/central-regulator/single-watermark scheme. Prioritize Issue #3: GCPP Internet Profile 0.1 canonical encoding, signature envelope, baseline algorithms, and byte-for-byte test vectors, then implement a minimal reference signer/verifier and use cross-implementation interoperability as the acceptance criterion.

## 22. One-sentence current status

> **GCPP has completed the structured transition from concept to a Core 0.1 public-standard Working Draft and has converted repository documentation to Chinese-first bilingual form; the next core milestone is to turn the abstract specification into an interoperable protocol through the Internet Profile, canonical bytes, machine-readable test vectors, and independent signer/verifier implementations.**
