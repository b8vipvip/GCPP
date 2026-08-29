# GCPP 协议注册表 / GCPP Protocol Registries

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror.

## 简体中文

状态：**Initial registry framework（初始注册表框架）**

GCPP 使用 Registry 将稳定的协议语义与可替换技术分离。Registry 条目不赋予法律地位、Provider 合法性、政策批准或事实可信性。

### 1. Registry 原则

Registry 用来回答：

- 算法标识符 `X` 表示什么？
- 哪份文档定义 Normalization Profile `Y`？
- Evidence Scheme `Z` 应如何验证？

Registry **不**回答：

- 哪个 Provider 被允许运营；
- 内容是否真实或合法；
- 某个 Actor 是否应该被某个国家或平台信任；
- 未验证内容是否虚假。

Registry 治理应遵循开放规范评审流程。成熟条目应引用稳定规范，并包含安全考虑、版本规则和弃用状态。

### 2. 初始 Registry

#### 2.1 Identity Methods

| ID | 名称 | 状态 | 说明 |
|---|---|---|---|
| `identity.raw-key` | 原始公钥 / Raw public key | provisional | 直接密码学标识符 |
| `identity.domain-key` | 域绑定密钥 / Domain-bound key | provisional | 需要定义域控制证明的 Profile |
| `identity.did` | DID Adapter | provisional | 使用已注册 DID method/profile |
| `identity.x509` | X.509 Adapter | provisional | Trust Policy 保持本地化 |

#### 2.2 Signature Schemes

| ID | 名称 | 状态 |
|---|---|---|
| `sig.ed25519` | Ed25519 | provisional deployment option |
| `sig.ecdsa-p256` | ECDSA P-256 | provisional deployment option |
| `sig.future` | Future scheme placeholder | reserved |

没有任何算法是永久性的。Profile 定义某一时期哪些方案 required、optional、deprecated 或 forbidden。

#### 2.3 Content Commitment Algorithms

| ID | 名称 | 状态 |
|---|---|---|
| `hash.sha256` | SHA-256 | provisional deployment option |
| `hash.sha384` | SHA-384 | provisional deployment option |
| `hash.sha3-256` | SHA3-256 | provisional deployment option |

Core 不永久要求任何一个条目。

#### 2.4 Binding Types

| ID | 含义 |
|---|---|
| `binding.exact-bytes` | 精确字节表示 |
| `binding.normalized-text` | 对已注册文本规范化结果计算 Digest |
| `binding.segment-set` | 对可独立匹配 Segment 的 Commitment 集合 |
| `binding.chunk-tree` | 对已注册 Chunking 构造建立 Tree/Root |

#### 2.5 Event Types

| ID | 含义 |
|---|---|
| `event.generate` | AI 或软件生成事件 |
| `event.capture` | Camera/Sensor Capture |
| `event.human-edit` | 人工声明编辑 |
| `event.ai-rewrite` | AI 重写/转换 |
| `event.translate` | 翻译 |
| `event.summarize` | 摘要 |
| `event.compose` | 多父来源组合 |
| `event.render` | 渲染 |
| `event.transcode` | 媒体转码 |
| `event.publish` | 发布/分发事件 |
| `event.unknown-transform` | 已知发生转换，但类型未指定 |

#### 2.6 Evidence Types

| ID | 含义 |
|---|---|
| `evidence.signature` | 数字签名 |
| `evidence.watermark-locator` | Locator Recovery Result |
| `evidence.transparency` | Append-only/Transparency Proof |
| `evidence.timestamp` | 可信或去中心化 Timestamp Proof |
| `evidence.witness` | 独立 Witness Proof |
| `evidence.blockchain` | Blockchain/Distributed-Ledger Anchor |
| `evidence.hardware-attestation` | Hardware/TEE Attestation |
| `evidence.vc` | Verifiable Credential Adapter |
| `evidence.execution-proof` | Verifiable Execution Proof |
| `evidence.zk-proof` | Zero-Knowledge Proof Profile |

#### 2.7 Carrier Types

| ID | 含义 |
|---|---|
| `carrier.embedded` | 嵌入式 Provenance Package/Manifest |
| `carrier.sidecar` | Sidecar Proof File |
| `carrier.remote` | Remote/Resolvable Proof |
| `carrier.clipboard` | Structured Clipboard Representation |
| `carrier.document-metadata` | Document/HTML Metadata |
| `carrier.robust-locator` | In-band Robust Recovery Locator |
| `carrier.unicode-aux` | Auxiliary Unicode Carrier |

#### 2.8 Text Capacity States

| ID | 含义 |
|---|---|
| `capacity.none` | 未嵌入 in-band Locator |
| `capacity.provider-only` | 只有粗粒度 Provider/Scheme 信号 |
| `capacity.partial-locator` | 嵌入部分 Locator Fragment |
| `capacity.full-locator` | 达到完整 Locator Payload 目标 |
| `capacity.redundant-locator` | Locator 具有显著恢复冗余 |
| `capacity.low-entropy-unavailable` | 因生成自由度不足而跳过嵌入 |

### 3. Normalization Profiles

Normalization Profile 会影响密码学完整性，因此需要独立的规范文档。

初始 placeholder：

- `norm.text-plain-1`
- `norm.html-visible-text-1`
- `norm.markdown-text-1`
- `norm.json-canonical-1`

在相应规范性文档和测试向量完成前，这些标识符均为 provisional。

### 4. Registry Entry 生命周期

推荐状态：

```text
experimental -> provisional -> recommended -> deprecated -> historic
```

被 deprecated 的条目仍必须可以用于历史验证。Registry deprecation MUST NOT 让旧 Signed Provenance Record 在语法上“消失”。

### 5. 无运行控制权

维护 Registry 是标准协调，不是运行控制。Registry 维护者不能仅通过删除条目就使密码学上有效的历史记录失效。长期验证所需的条目应以 Historic Metadata 形式继续保留。

---

# English

Status: **Initial registry framework**

GCPP uses registries to keep stable protocol semantics separate from replaceable technologies. Registry entries do not grant legal status, provider legitimacy, policy approval, or factual trust.

## 1. Registry principles

Registries exist to answer questions such as:

- what does algorithm identifier `X` mean?
- which document defines normalization profile `Y`?
- how is evidence scheme `Z` verified?

They do **not** answer:

- which provider is allowed to operate;
- whether content is true or legal;
- whether an actor should be trusted by a specific country or platform;
- whether unverified content is fake.

Registry governance should follow an open specification-review process. Mature entries should cite a stable specification and include security considerations, versioning rules, and deprecation status.

## 2. Initial registries

### 2.1 Identity Methods

| ID | Name | Status | Notes |
|---|---|---|---|
| `identity.raw-key` | Raw public key | provisional | Direct cryptographic identifier |
| `identity.domain-key` | Domain-bound key | provisional | Requires a profile defining domain proof |
| `identity.did` | DID adapter | provisional | Uses a registered DID method/profile |
| `identity.x509` | X.509 adapter | provisional | Trust policy remains local |

### 2.2 Signature Schemes

| ID | Name | Status |
|---|---|---|
| `sig.ed25519` | Ed25519 | provisional deployment option |
| `sig.ecdsa-p256` | ECDSA P-256 | provisional deployment option |
| `sig.future` | Future scheme placeholder | reserved |

No algorithm is permanent. Profiles define which schemes are required, optional, deprecated, or forbidden at a point in time.

### 2.3 Content Commitment Algorithms

| ID | Name | Status |
|---|---|---|
| `hash.sha256` | SHA-256 | provisional deployment option |
| `hash.sha384` | SHA-384 | provisional deployment option |
| `hash.sha3-256` | SHA3-256 | provisional deployment option |

Core does not require any one entry forever.

### 2.4 Binding Types

| ID | Meaning |
|---|---|
| `binding.exact-bytes` | Exact byte representation |
| `binding.normalized-text` | Digest over a registered text normalization |
| `binding.segment-set` | Commitments over independently matchable segments |
| `binding.chunk-tree` | Tree/root over registered chunking construction |

### 2.5 Event Types

| ID | Meaning |
|---|---|
| `event.generate` | AI or software generation event |
| `event.capture` | Camera/sensor capture |
| `event.human-edit` | Human-declared edit |
| `event.ai-rewrite` | AI rewrite/transformation |
| `event.translate` | Translation |
| `event.summarize` | Summarization |
| `event.compose` | Multi-parent composition |
| `event.render` | Rendering |
| `event.transcode` | Media transcoding |
| `event.publish` | Publication/distribution event |
| `event.unknown-transform` | Transformation known to have occurred but type unspecified |

### 2.6 Evidence Types

| ID | Meaning |
|---|---|
| `evidence.signature` | Digital signature |
| `evidence.watermark-locator` | Locator recovery result |
| `evidence.transparency` | Append-only/transparency proof |
| `evidence.timestamp` | Trusted or decentralized timestamp proof |
| `evidence.witness` | Independent witness proof |
| `evidence.blockchain` | Blockchain/distributed-ledger anchor |
| `evidence.hardware-attestation` | Hardware/TEE attestation |
| `evidence.vc` | Verifiable credential adapter |
| `evidence.execution-proof` | Verifiable execution proof |
| `evidence.zk-proof` | Zero-knowledge proof profile |

### 2.7 Carrier Types

| ID | Meaning |
|---|---|
| `carrier.embedded` | Embedded provenance package/manifest |
| `carrier.sidecar` | Sidecar proof file |
| `carrier.remote` | Remote/resolvable proof |
| `carrier.clipboard` | Structured clipboard representation |
| `carrier.document-metadata` | Document/HTML metadata |
| `carrier.robust-locator` | In-band robust recovery locator |
| `carrier.unicode-aux` | Auxiliary Unicode carrier |

### 2.8 Text Capacity States

| ID | Meaning |
|---|---|
| `capacity.none` | No in-band locator embedded |
| `capacity.provider-only` | Only coarse provider/scheme signal available |
| `capacity.partial-locator` | Partial locator fragments embedded |
| `capacity.full-locator` | Full locator payload target met |
| `capacity.redundant-locator` | Locator has significant recovery redundancy |
| `capacity.low-entropy-unavailable` | Embedding skipped due to insufficient generation freedom |

## 3. Normalization profiles

Normalization profiles require dedicated specifications because they affect cryptographic integrity.

Initial placeholders:

- `norm.text-plain-1`
- `norm.html-visible-text-1`
- `norm.markdown-text-1`
- `norm.json-canonical-1`

These identifiers are provisional until the corresponding normative documents and test vectors exist.

## 4. Registry entry lifecycle

Recommended states:

```text
experimental -> provisional -> recommended -> deprecated -> historic
```

A deprecated entry remains identifiable for historical verification. Registry deprecation MUST NOT make old signed provenance records syntactically disappear.

## 5. No operational control

Maintaining a registry is standards coordination, not operational control. Registry maintainers cannot invalidate a cryptographically valid historical record merely by removing an entry. Entries needed for long-term verification should remain available as historic metadata.
