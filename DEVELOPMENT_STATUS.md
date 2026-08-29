# GCPP 开发进度与完整交接上下文

> 最后整理日期：2026-08-29  
> 文档用途：这是供后续新聊天、开发者、审阅者直接继续推进 GCPP 的长期交接文档。阅读本文件后，应当能够在不依赖此前聊天记录的情况下理解项目目标、仓库状态、架构决策、已完成工作、已确认边界、未完成任务和下一步执行顺序。

---

## 1. 项目定位

### 1.1 项目名称

**GCPP — Generative Content Provenance Protocol**  
中文：**生成式内容来源协议**。

GCPP 的目标不是做一个 AI 检测器、监管平台、区块链项目、内容数据库或单一产品，而是设计一套可以长期演进、由不同实现独立实现和互操作的**公共数字内容来源协议**。

GCPP 要标准化四个长期不会随具体技术变化而消失的抽象问题：

1. **Identity（身份）**：谁对来源声明负责？
2. **Provenance（来源/演化）**：内容由哪一次生成、编辑、转换或组合事件产生？
3. **Integrity（完整性/关联性）**：当前内容与声明中的原始内容还保持多强的可验证关系？
4. **Evidence（证据）**：凭什么相信以上身份、来源、完整性和历史声明？

协议必须能够在未来更换底层实现而不推倒 Core，例如：

- 区块链消失或不再适合；
- SHA-256 被淘汰；
- DID 被新身份体系替代；
- Ed25519 被后量子签名替代；
- 文本/图片/视频水印技术完全换代；
- Transformer / LLM 架构被新 AI 架构替代；
- 存储、传输、Transparency Log、时间戳基础设施发生变化。

只要 Identity / Provenance / Integrity / Evidence 仍然成立，GCPP 就应继续成立。

### 1.2 明确非目标

GCPP **不是**：

- AI 监管中心；
- AI 内容中央数据库；
- 全球 Provider 审批系统；
- 区块链协议；
- 统一指定某一种水印算法；
- AI / 人类二元检测器；
- 事实真相认证系统；
- 内容审查或删除系统；
- 版权裁判系统；
- 用户跟踪系统；
- 单一政府、公司或平台控制的认证服务。

协议只提供**来源事实和证据关系**，不提供政策判断。

---

## 2. 当前仓库信息

- GitHub 仓库：`b8vipvip/GCPP`
- 仓库地址：`https://github.com/b8vipvip/GCPP`
- 可见性：Public
- 默认分支：`main`
- 当前规范工作分支：`standards/gcpp-core-0.1`
- 当前公开规范 PR：**#1 — `spec: establish GCPP Core 0.1 public standards draft`**
- PR 状态：Open
- PR 当前可合并：Yes（最近检查 `mergeable=true`）
- PR Base：`main`
- PR Head：`standards/gcpp-core-0.1`
- `main` 初始化提交：`5f0f236c7c74e3eab5631f2b3b192ef8eb519d3f`
- Core 0.1 首批规范提交：`6f6038144ed007401e0b5628c7c906f6fd2f785e`
- 本交接文档在上述规范分支上继续提交，因此实际最新 HEAD 应以 GitHub 分支当前状态为准。

### 2.1 当前开放 Issues

#### Issue #2

`standards: choose specification license and contributor IPR policy`

目的：在 Candidate Draft 前明确公共标准文本许可、参考代码许可、贡献者专利/IPR 要求、第三方算法引用规则、历史版本再分发权。

这是公共标准项目必须解决的问题，不能默认套用普通软件项目许可。

#### Issue #3

`profile: define GCPP Internet Profile 0.1 canonical encoding and baseline algorithms`

目的：定义第一套真正可以互操作的具体部署 Profile，包括 canonical serialization、签名 envelope、baseline algorithms、key ID、size limits、错误处理、sidecar/self-contained packaging 等。

关键原则：这些只能属于可替换 Profile，不能倒灌成永久 Core 依赖。

#### Issue #4

`text: benchmark a low-overhead robust RecoveryLocator profile`

目的：把当前文本来源架构约束转化为可测量的低开销 RID/RecoveryLocator 水印候选方案。

硬约束：不得要求额外 LLM 推理、大规模候选句重排、逐 token 网络/区块链/ZK 请求。

---

## 3. 当前标准成熟度

当前阶段：

**GCPP Core 0.1 — Working Draft**

尚未达到：

- Candidate Draft；
- Proposed Standard；
- Stable 1.0；
- 可宣称跨实现互操作；
- 可宣称已有生产级 Text Profile。

当前真正完成的是：

> 已从概念讨论进入公共协议架构和规范文本阶段，并建立了公开 PR、威胁模型、验证语义、Text Profile 约束、注册表框架、测试向量规划和标准治理流程。

---

## 4. 已确认的最高层架构

### 4.1 五层逻辑模型

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

物理实现层不属于 Core：

```text
Database / HTTP / P2P / Local File / Cloud
Transparency Log / Timestamp / Blockchain / Future System
```

### 4.2 Core 必须保持的“无关性”

GCPP Core 必须是：

- Storage-Agnostic；
- Transport-Agnostic；
- Identity-Agnostic；
- Algorithm-Agnostic；
- Watermark-Agnostic；
- Evidence/Anchor-Agnostic；
- Model-Agnostic；
- Platform-Agnostic；
- Policy-Neutral。

任何具体 SHA、签名、DID、区块链、水印、数据库、Provider Discovery 实现只能进入 Registry / Profile / Adapter，不能成为 Core 的永久要求。

---

## 5. 已确认的核心对象与关键设计决策

### 5.1 Actor / Identity

`Actor` 是做出来源声明的主体，可以是：

- AI Provider；
- AI 模型服务；
- Human；
- Organization；
- Editing Tool；
- Camera / Recorder；
- Autonomous Agent；
- Hardware Device。

核心抽象：

```text
ActorIdentifier {
  method
  identifier
}
```

Core 不绑定 DID/X.509/raw key/domain key。

必须区分：

- **Cryptographic Identity**：谁控制并使用了某个密钥/标识；
- **Real-world Identity Claim**：这个密钥是否对应现实世界某个品牌/公司/组织。

密码学不能凭空证明“某个公钥就是 OpenAI”，现实身份需要 domain control、VC、第三方 attestation、历史 key continuity 等独立 Evidence。

### 5.2 Provenance Event

协议基本单位是**内容状态变化事件**，而不是文件。

事件包括但不限于：

- GENERATED；
- HUMAN_EDITED；
- AI_REWRITTEN；
- TRANSLATED；
- SUMMARIZED；
- COMPOSED；
- RENDERED；
- TRANSCODED；
- PUBLISHED；
- CAPTURED；
- FUTURE / REGISTERED EVENT TYPE。

来源结构是 **DAG**，不是单 parent 链，因为一个内容可能由多来源组合。

### 5.3 GenerationID（GID）与 RecoveryLocator（RID）必须分离

这是当前最重要的协议决策之一。

**GID**：真正标识某一次具体生成事件的高熵、不可从用户身份推导的唯一标识。

**RID / RecoveryLocator**：为了跨纯文本复制、metadata 丢失后恢复 provenance 使用的短 locator。

RID：

- 不是身份凭证；
- 可以比 GID 短；
- 可以部分恢复；
- 可以碰撞；
- 可以指向多个候选记录；
- 只能用于 discovery/recovery；
- 必须继续验证 Signed Record + Content Binding 才能做归属判断。

此设计解决了短文本无法稳定承载完整 GID/签名的问题，也阻止系统把“检测到水印”误当成“已认证 Provider”。

### 5.4 Provenance Record

当前抽象记录结构：

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

序列化格式尚未写死，由 Internet Profile 决定。

### 5.5 Model Claim 是“声明”，不是天然执行证明

当前至少区分：

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

Provider 普通数字签名最多可以直接建立 `MODEL_DECLARED`。

如果将来需要证明真实执行模型，可选使用：

- TEE/hardware attestation；
- verifiable inference；
- ZK execution proof；
- 未来其他执行证明。

这些不允许成为第一代主推理热路径的强制要求。

### 5.6 Content Binding 不绑定具体 Hash

抽象：

```text
ContentBinding {
  binding_type
  algorithm
  normalization_profile
  value
}
```

一个 subject 可以同时具有多个 bindings：

- raw bytes；
- normalized visible text；
- structured representation；
- chunk/segment commitments。

**Full hash mismatch 不能自动抹掉 partial provenance。**

### 5.7 Exact Integrity 与 Partial Integrity 必须分开

修改一个字符就会使完整 Hash 不匹配，因此必须支持：

- exact content binding；
- segment/chunk binding；
- authenticated coverage；
- unknown/new content coverage；
- lineage-based derivative validation。

攻击者不能通过保留一小段带真实来源的信息，把整篇伪造文章认证为同一来源。

### 5.8 Evidence 是可插拔接口

抽象：

```text
Evidence {
  evidence_type
  scheme
  subject
  proof
  parameters?
}
```

可实现为：

- Digital Signature；
- Watermark Recovery；
- Transparency Inclusion；
- Timestamp Proof；
- Witness Proof；
- Blockchain Anchor；
- Verifiable Credential；
- Hardware Attestation；
- Execution Proof；
- Future Evidence。

**区块链只是 Evidence 的一种物理实现，不是协议核心。**

### 5.9 Carrier 与 Proof 分离

Carrier 只负责搬运 provenance 或 locator，例如：

- embedded manifest；
- sidecar；
- clipboard MIME；
- document metadata；
- robust watermark；
- remote reference。

Carrier 本身不可信。Proof 可以从任意不可信传输源取得，只要签名和绑定可验证。

核心原则：

> **Proof is authoritative; transport is not.**

---

## 6. 验证语义已经确认

GCPP 不输出单一 AI / Human boolean，而输出结构化 **Verification Vector**。

至少包括：

- actor authentication state；
- record signature state；
- model assurance state；
- exact integrity state；
- partial integrity / coverage；
- locator/watermark state；
- lineage state；
- historical evidence state；
- unsupported critical features。

在此基础上才映射为展示标签：

### `VERIFIED_ORIGINAL`

来源身份和签名有效，当前内容与声明中的内容精确绑定匹配。

### `VERIFIED_DERIVATIVE`

来源有效、lineage 可验证，但当前内容已经修改/转换。

### `PARTIAL_PROVENANCE`

只有部分当前内容能够与某来源建立认证关系，必须报告 coverage，不可扩大到全文归属。

### `LOCATOR_ONLY`

发现水印/RID/locator，但缺少完整认证证据或绑定验证，只能表示“发现来源线索”。

### `UNVERIFIED`

没有足够的 GCPP 来源证明。

以下三个语义边界已经固定，后续不得轻易破坏：

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
```

另外：

```text
WATERMARK != AUTHENTICATION
```

GCPP 永远不应该把来源认证直接解释为事实正确、合法、优质、非作弊或应该传播。

---

## 7. 文本来源方案当前结论

纯文本是 GCPP 最有区别化价值、也是最困难的场景。

目标：即使 HTML/metadata/custom clipboard information 丢失，普通复制粘贴和部分编辑之后仍尽量恢复 RID，再通过外部 Signed Record 做真正认证。

### 7.1 当前 Text Profile 硬性能约束

Baseline **不得要求**：

- 额外 LLM inference pass；
- 第二次模型调用；
- 每句话生成大量完整候选再 rerank；
- 大规模语义候选重排；
- 每 token 网络调用；
- 每 token 区块链/日志调用；
- 每 token ZK proof。

主生成热路径最多允许类似：

```text
Transformer forward
    ↓
logits
    ↓
lightweight locator/watermark processor
    ↓
sampling
    ↓
token
```

旁路可以做 streaming binding、chunk state、ECC state，生成结束后再 finalize/sign。

### 7.2 低熵/短文本必须允许 abstain

以下内容不应为了强行塞水印而破坏质量：

- 极短文本；
- deterministic output；
- code；
- JSON/structured data；
- 数学公式；
- temperature≈0 / 低可选 token 场景。

这些场景允许通过：

- attached proof；
- sidecar；
- clipboard provenance；
- signed record；

来保持来源，而不是强制 in-band watermark。

### 7.3 RID 水印只是恢复层

预期逻辑：

```text
plain text
  ↓
RID recovery
  ↓
candidate provenance records
  ↓
signature verification
  ↓
content binding / partial coverage
  ↓
attribution result
```

RID 被移植/伪造时，内容绑定必须阻断错误归属。

### 7.4 目前仍未确定具体水印算法

当前仓库只有**Text Profile 约束和评估目标**，没有声称已经选定生产级方案。

Issue #4 后续必须通过 benchmark 决定是否有候选方案满足：

- throughput/latency；
- quality regression；
- false positive / false negative；
- 多语言；
- deletion/insertion/substitution；
- copy/paste/normalization；
- paraphrase/translation degradation；
- spoofing/watermark stealing；
- RID transplant；
- ECC/synchronization recovery curve。

---

## 8. Canonicalization / Integrity 的关键未完成问题

文本来源协议能否实现跨实现互操作，Canonicalization 是非常关键的部分。

必须标准化：

- UTF-8 / encoding handling；
- Unicode normalization；
- line ending；
- whitespace；
- control characters；
- visible text extraction；
- HTML / Markdown / JSON 等结构化表示；
- chunking boundaries；
- normalization profile IDs。

不能让不同 Verifier 自己理解“规范化文本”，否则同一内容会产生不同 commitment。

未来需要注册类似：

```text
norm.text-plain-1
norm.html-visible-1
norm.markdown-text-1
norm.json-canonical-1
```

以及相应 test vectors。

---

## 9. 历史不可抵赖/Transparency 的当前结论

GCPP Core **不要求区块链**。

真正抽象需求是：

> 是否存在额外 Evidence 能证明某份 commitment 在某个时间以前已经存在，并降低 Provider 无痕重写历史的能力？

可实现为：

- CT-style append-only transparency log；
- independent witness / cross logging；
- timestamp service/network；
- blockchain/distributed ledger；
- federated append-only log；
- future evidence system。

因此需要区分：

- Actor Signature Assurance；
- Historical Evidence Assurance。

没有 transparency/anchor 时，签名仍然可以是 valid，但 `History Assurance` 可以是 NONE。

区块链未来可以作为某个部署 Profile 的可选 Anchor，但 Core 不依赖它。

---

## 10. 隐私边界已经确认

Public GCPP provenance 默认**不得要求**：

- 用户姓名；
- ChatGPT/平台账号 ID；
- email；
- phone；
- IP；
- device ID；
- geolocation；
- raw prompt；
- session ID。

Generation ID 必须每次生成独立、不可预测、不编码用户信息，避免变成跨内容用户 tracking identifier。

Prompt 默认不进入 public provenance。

如果企业内部审计确实要绑定输入，应使用 salted/randomized commitment + selective disclosure，而不是公开 raw prompt 或稳定用户 ID。

---

## 11. Provider / 模型平台接受度相关已确认原则

GCPP 不能成为模型输出延迟来源。

因此：

- 不在 token path 等待外部服务；
- 不等待区块链/Transparency confirmation 才返回内容；
- 不要求重型语义 reranking；
- 不强制 ZKML/TEE 成为第一代 requirement；
- Generation Record finalize/sign 可在 generation completion 阶段完成；
- historical evidence 可批处理/异步生成；
- internal routing/checkpoint 不默认公开。

Provider 可以只公开 public model ID；内部实际模型/route 如需更强保证，可通过 commitment / selective disclosure / attestation 扩展。

协议给模型平台的价值包括：

- 防止第三方伪造其 AI 输出；
- 能证明“该内容没有可验证的本平台来源”；
- 品牌防伪；
- 企业审计；
- 跨平台、跨国家统一来源接口；
- 更清晰的责任边界。

代价包括签名、密钥、日志、水印、兼容性和可能增加可追责性，因此协议必须保持低开销、隐私保护和实现可替换。

---

## 12. 当前关键文件

### 根目录

#### `README.md`

仓库入口、项目定位、八条 Design Invariants。

#### `ROADMAP.md`

标准成熟度路线，当前规划 Phase 0–8：

- Phase 0 Core architecture freeze；
- Phase 1 Canonical Internet Profile；
- Phase 2 Text Integrity Profile；
- Phase 3 Text Recovery Profile；
- Phase 4 Discovery/transport profiles；
- Phase 5 Existing-standard adapters；
- Phase 6 Historical evidence profiles；
- Phase 7 Model assurance extensions；
- Phase 8 Interoperability / standardization readiness。

#### `CONTRIBUTING.md`

贡献和标准讨论要求。

#### `SECURITY.md`

安全报告和协议安全边界。

#### `DEVELOPMENT_STATUS.md`

即本文件，作为新聊天/新开发者的持续交接入口。

### `spec/`

#### `spec/README.md`

规范模块索引和阅读入口。

#### `spec/GCPP-CORE.md`

当前最重要的规范文件。定义 Scope、Architectural Invariants、Actor、Event、GID/RID、Record、Model Claim、Content Binding、Evidence、Carrier、Extensions、Privacy、History 和核心输出要求。

#### `spec/GCPP-DATA-MODEL.md`

抽象数据模型；不绑定具体 serialization。

#### `spec/GCPP-VERIFY.md`

Verification Vector 和展示标签语义，阻止来源证明被误用成 truth/fake 判定。

#### `spec/GCPP-THREAT-MODEL.md`

当前已覆盖主要威胁：

- watermark/RID spoofing；
- RID transplant；
- partial-copy attribution inflation；
- metadata stripping；
- provider/key compromise；
- history rewriting；
- malicious resolver/transport；
- privacy correlation；
- availability / disappearance；
- model-claim overstatement。

### `profiles/`

#### `profiles/GCPP-TEXT-0.1.md`

实验性低开销 Text Profile 约束；特别禁止影响模型效率的大量候选语义 rerank 路线作为 baseline。

### `registries/`

#### `registries/README.md`

Registry 框架。后续预计包括：

- identity methods；
- signature algorithms；
- content commitment/hash algorithms；
- normalization profiles；
- event types；
- evidence methods；
- carrier/watermark schemes；
- extension IDs。

Registry 只协调编号和语义，不是运营/监管中心。

### `test-vectors/`

#### `test-vectors/README.md`

Conformance 测试计划，包括 valid/invalid signature、partial copy、transplant、revocation、unknown extension、low entropy 等场景。

### `governance/`

#### `governance/PROCESS.md`

开放标准治理流程。目标不是 DAO 投票或单公司决定，而是 public proposal / review / reference implementations / interoperability / security review 的标准演进方式。

---

## 13. 已确认不能再退回的设计不变量

后续新聊天开发时，除非有非常强的新证据并明确修改规范，不应破坏以下原则：

1. **Provenance ≠ Truth**。
2. **UNVERIFIED ≠ FAKE / HUMAN / ILLEGAL / LOW QUALITY**。
3. **Watermark / RID ≠ Authentication**。
4. 用户身份不是 public provenance 的必要字段。
5. 验证不能依赖唯一中央在线 verifier。
6. Core 不能永久绑定单一 storage / transport / identity / hash / signature / watermark / ledger / model architecture。
7. Partial provenance 必须是一等状态，不能退化成 AI / non-AI boolean。
8. Policy decisions 必须位于 GCPP 之外。
9. GID 与 RID 必须分离。
10. Model claim 必须区分 declared / attested / execution-proven。
11. Physical infrastructure 是实现，不是协议本体。
12. 未来技术替换优先通过 Registry/Profile/Extension，而不是修改 Core 语义。

---

## 14. 当前已确认的问题 / 风险

### 14.1 文本水印不存在“不可删除”的绝对方案

彻底重写、翻译回译、人工重新表达或大量内容替换后，in-band 来源信号可能消失。

GCPP 的现实目标不是“永远无法删除”，而是：

> 将删除来源的成本从清 metadata 提高到需要实质性改变内容，并在仍保留足够原内容时恢复 locator 和 partial provenance。

### 14.2 短文本容量不足

`谢谢。` 等短文本不可能同时稳定承载 128+ bit GID、签名和高冗余 ECC。

因此 GID/RID 分离，并允许 short/low-entropy abstention。

### 14.3 Provider 签名不能证明 Provider 没撒谎

签名证明的是“谁声明了什么”，不是自动证明“真实机器确实执行了该模型”。

第一代只安全地声称 `MODEL_DECLARED`；更强证明留给可选 Evidence。

### 14.4 真实世界品牌身份不可能完全由密码学凭空得出

公钥可以证明 key continuity/control，但“它是不是现实中的 OpenAI/Google”需要 domain proof、VC、attestation、组织证明等外部 Evidence。

### 14.5 区块链不是必要条件

区块链会带来交易成本、拥堵、治理、分叉、链停机等复杂度。

协议需要的是抽象 evidence / append-only history / time existence proof，不是 Ethereum 等具体基础设施。

### 14.6 规范本身仍缺少真正可执行的 canonical bytes

当前 Core/Data Model 是抽象层，还没有确定第一套 deterministic canonical serialization，因此还不能生成真正跨实现 byte-for-byte 一致的 signature test vectors。

这是下一阶段最高优先级任务。

### 14.7 许可/IPR 尚未确定

没有明确 specification license、reference implementation license、contributor patent/IPR policy 前，不应宣称成熟公共标准。

---

## 15. 未完成任务（按优先级）

### P0 — 必须先完成

#### 15.1 完成 GCPP Internet Profile 0.1

对应 Issue #3。

需要决定但保持可替换：

- canonical serialization；
- canonical signing input / domain separation；
- baseline signature algorithms；
- baseline content commitment algorithm；
- key ID format；
- extension encoding；
- size / depth / recursion limits；
- duplicate field handling；
- unknown fields；
- canonical ordering；
- self-contained proof packaging；
- sidecar proof packaging；
- downgrade/deprecation behavior。

**成功标准**：两个独立实现对同一 abstract record 生成完全相同的 signing bytes 和 verify result。

#### 15.2 生成真正 machine-readable test vectors

至少包括：

- valid original；
- tampered record；
- invalid signature；
- exact content mismatch；
- valid derivative；
- partial provenance；
- RID transplant；
- unknown non-critical extension；
- unknown critical extension；
- historical evidence absent；
- revoked/rotated key scenario。

#### 15.3 建立最小 reference Signer + Verifier

目标不是做平台产品，而是验证规范能否落地。

建议先实现：

```text
parse record
→ canonical encode
→ sign
→ verify signature
→ verify binding
→ build Verification Vector
→ map presentation label
```

至少应有两个独立实现或两种语言，才能证明没有把实现细节误当规范。

### P1 — 紧接 P0

#### 15.4 Text Integrity Profile

定义 `norm.text-plain-1` 和 chunking/coverage 规则。

先解决**不依赖水印**的文本 exact/partial integrity，再研究 RecoveryLocator。

#### 15.5 Text Recovery benchmark

对应 Issue #4。

先 benchmark，再标准化，不能先选某个学术算法再强行写入协议。

#### 15.6 Clipboard / Sidecar carrier profile

定义例如：

```text
application/gcpp-provenance+...
```

以及 clipboard、document、sidecar 的承载规则。

### P2 — 标准生态

#### 15.7 C2PA Adapter

GCPP 不应重复发明成熟图片/视频 manifest/provenance，重点定义与 C2PA 的互操作映射。

#### 15.8 DID / VC / X.509 identity adapters

保持 Identity Core 抽象，同时实现现实可用适配器。

#### 15.9 Transparency / Timestamp / Witness evidence adapters

参考 Certificate Transparency 的 append-only Merkle 设计，但不绑定单一网络。

### P3 — 后续高级能力

#### 15.10 Model assurance extensions

- model commitment；
- selective disclosure；
- TEE attestation；
- verifiable inference；
- ZKML（只有在成本现实可接受时）。

这些不得阻塞 Core / Internet Profile / Text Integrity 的推进。

---

## 16. 下一步推荐执行顺序

新聊天进入仓库后，建议严格按照以下顺序：

### Step 1 — 先读取状态，不重复重新设计

读取：

1. `DEVELOPMENT_STATUS.md`
2. `spec/GCPP-CORE.md`
3. `spec/GCPP-DATA-MODEL.md`
4. `spec/GCPP-VERIFY.md`
5. `spec/GCPP-THREAT-MODEL.md`
6. `ROADMAP.md`
7. Issues #2/#3/#4
8. PR #1 状态和 review comments

不要重新把协议退回“区块链 AI 水印项目”的方向。

### Step 2 — 优先推进 Issue #3 / Internet Profile 0.1

这是当前从“标准文本”迈向“可独立实现”的关键瓶颈。

需要先研究并选择一套 2026 年现实可用但明确可替换的 canonical encoding/signing baseline。

推荐原则：

- deterministic；
- 有成熟库；
- 跨语言；
- 不依赖 JSON key ordering 的模糊实现；
- 支持 extensions；
- 能生成稳定 byte vectors；
- 易于未来算法迁移。

在做决定前，需比较 deterministic CBOR / canonical JSON 类方案及其标准化成熟度，而不是凭偏好直接选。

### Step 3 — 写 canonical signing test vectors

规范不能只说“canonical”，必须把输入对象和最终签名字节明确到 hex。

至少做：

```text
abstract object
→ canonical bytes
→ digest
→ signature
→ expected verification vector
```

### Step 4 — 实现最小 reference verifier

只实现 Core + Internet Profile，不碰大型平台集成。

### Step 5 — 独立实现互操作测试

最好第二个实现使用不同语言/库。

如果两个实现结果不一致，应首先修规范，而不是写兼容 hack。

### Step 6 — 再推进 Text Integrity，然后才是 Text Watermark

顺序必须是：

```text
Canonical Text
→ Exact Binding
→ Partial/Chunk Binding
→ Coverage
→ Recovery Locator Watermark
```

不能把水印放在完整性定义之前。

---

## 17. 对下一位开发者/新聊天的明确指令

如果新聊天收到“继续开发 GCPP”，应执行：

1. 检查 `b8vipvip/GCPP` 当前仓库状态；
2. 读取本文件和 PR #1；
3. 检查 Issues #2/#3/#4 是否已有新讨论；
4. 检查 PR #1 是否有 review comments / CI / conflicts；
5. 不重复已经确定的 Core 架构；
6. 优先推进 Issue #3 Internet Profile 0.1；
7. 所有重大规范变化使用独立 branch + PR；
8. Core 变化必须说明为什么不能通过 Profile/Registry/Extension 解决；
9. 不把任何具体区块链、DID、Hash、水印、Provider 写成永久核心依赖；
10. 不使用会明显拖慢模型推理的大量候选语义重排作为 Text Profile baseline；
11. 不把 watermark recovery 当 provider authentication；
12. 不把 `UNVERIFIED` 呈现为 fake/human；
13. 不把 `VERIFIED` 呈现为 factually true；
14. 优先建立可执行 test vectors 和独立实现互操作性，而不是继续增加抽象概念数量。

---

## 18. 当前 PR #1 合并策略

PR #1 当前的价值是建立 GCPP Core 0.1 的公开审阅基线。

建议在合并前至少检查：

- 是否存在明显把实现细节写死进 Core 的地方；
- GID/RID 边界是否清楚；
- Verification labels 是否有错误扩张解释；
- Privacy invariants 是否足够；
- Threat Model 是否漏掉会破坏架构的高风险攻击；
- Text Profile 是否坚持低开销边界；
- README/ROADMAP 与 Core 是否一致。

PR #1 可以在 Core 架构稳定后合并；不必等待 Issue #2/#3/#4 全部完成，因为它们属于后续成熟阶段。但在进入 Candidate Draft 之前，Issue #2 和 Internet Profile 的核心选择必须解决。

---

## 19. 公共标准治理原则

GCPP 应学习 DNS/TLS/OAuth/CT 等长期公共协议的思想：

- 协议语义与物理实现分离；
- 稳定 Core + 可替换算法/Profile；
- 机制与政策分离；
- 数据来源 transport 不必可信，proof 必须可验证；
- 分布式运行，不要求全球唯一服务器；
- 可以有 Registry/标准协调，但不赋予其运营控制权；
- caching/offline verification 应成为重要能力；
- algorithm agility 和 deprecation 必须从第一版考虑；
- forward compatibility 必须有 explicit extension behavior；
- append-only correction 优先于 silent history rewrite。

目标不是“完全没有任何治理”，而是：

> **标准可以被协调，但运行事实不能由某个单一机构任意改写。**

---

## 20. 最终愿景

GCPP 最终不是“AI Watermark 2.0”，而是尝试定义：

> **Content Provenance Layer of the Internet — 互联网内容来源层。**

DNS 回答：名字指向哪里。  
TLS 回答：正在和谁安全通信、通信是否被篡改。  
OAuth 回答：谁被授权做什么。  
GCPP 希望回答：

> **“我现在看到的数字内容从哪里来、由谁声明产生、经历过什么变化、当前内容还保留多少原始来源关系，以及这些结论凭什么可以被独立验证？”**

这一愿景只有在 GCPP 不依赖今天某一种具体技术时才有长期意义。

---

## 21. 新聊天可直接使用的启动提示

可以直接把下面这段作为下一聊天的工作指令：

> 继续开发 GitHub 仓库 `https://github.com/b8vipvip/GCPP.git`。先读取仓库根目录 `DEVELOPMENT_STATUS.md`，再读取 `spec/GCPP-CORE.md`、`spec/GCPP-DATA-MODEL.md`、`spec/GCPP-VERIFY.md`、`spec/GCPP-THREAT-MODEL.md`、`ROADMAP.md`，并检查 PR #1 与 Issues #2/#3/#4 的最新状态。不要重新设计已确认的 Core，也不要把协议退回区块链/中央监管/单一水印方案。优先推进 Issue #3：GCPP Internet Profile 0.1 的 canonical encoding、signature envelope、baseline algorithms 和 byte-for-byte test vectors，然后实现最小 reference signer/verifier，并以跨实现互操作作为验收标准。所有重大规范修改通过独立 branch + PR 推进。

---

## 22. 当前一句话状态

> **GCPP 已完成从概念到 Core 0.1 公共标准 Working Draft 的第一次结构化落库；下一核心里程碑不是继续扩写理念，而是通过 Internet Profile + canonical bytes + machine-readable test vectors + 独立 signer/verifier，把抽象规范变成真正可互操作的协议。**
