# GCPP 架构原则 / GCPP Architectural Principles

> 状态 / Status: **Architectural Direction / 架构方向文档**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 目的

本文件定义 GCPP 后续研究和规范工作的架构纪律。它不直接定义 wire format，也不把当前研究假设提前升级为稳定 Core。

## 2. 第一性原理优先

GCPP 的规范工作 **MUST** 从真实长期问题出发，而不是从其他标准当前缺失的能力出发。

规范提案的推荐顺序为：

```text
Problem
-> Abstraction
-> Invariant
-> Protocol Primitive
-> Evidence
-> Profile / Adapter / Implementation
```

以下理由本身不足以让一个对象进入 GCPP Core：

- C2PA 当前没有该字段；
- SPDX 当前没有该关系；
- CycloneDX 当前没有该对象；
- 某厂商尚未实现某种能力；
- 可以比另一个标准更早发布。

## 3. 不进行标准时间竞赛

GCPP **MUST NOT** 以抢占标准发布时间、功能数量或命名空间为研发目标。

如果成熟标准可以表达同一技术事实，GCPP **SHOULD**：

1. 直接复用；或
2. 建立 Adapter；或
3. 只定义跨标准的验证语义。

只有当一个问题在不同底层标准和算法之间仍然成立时，才有资格成为 GCPP Core 候选。

## 4. 核心研究对象：关系与连续性

GCPP 下一阶段重点研究：

```text
Entity
Relation
Continuity
Evidence
```

这些概念目前是研究模型，不是最终规范承诺。

### Entity

可以参与来源关系的主体或信息对象。

### Relation

描述对象之间可被声明和验证的来源、转换、贡献或影响关系。

### Continuity

描述关系经过复制、编辑、截取、组合、翻译、总结、训练或其他转换后仍能验证到什么程度。

### Evidence

支持某个 identity、relation、continuity 或其他技术事实的证据，并明确其证明边界。

## 5. 图优先，而不是单链优先

GCPP **MUST** 假设真实来源结构可能具有：

- 多个 parent；
- 多个 contributor；
- 多次 transformation；
- 冲突声明；
- 部分可验证边；
- unknown 边；
- 不同时间产生的证据。

因此来源历史不应被强制压缩为单一线性版本链。

## 6. Partial / Mixed / Unknown 是一等状态

符合 GCPP 方向的 verifier **MUST NOT** 将以下状态自动视为异常：

```text
PARTIAL
MIXED
TRANSFORMED
UNKNOWN
CONFLICTING_EVIDENCE
```

协议应尽可能报告已知事实，而不是为了得到单个结论而丢弃不完整性。

## 7. Evidence 不得越权

Evidence **MUST** 明确自己能证明什么。

固定边界包括：

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
SIMILARITY != PROVENANCE
OUTPUT_PROVENANCE != MODEL_LINEAGE
REGULATORY_LABEL != CRYPTOGRAPHIC_IDENTITY
ABSENCE_OF_EVIDENCE != EVIDENCE_OF_ABSENCE
```

一个 verifier 可以报告 evidence vector，但法律、版权、合规、真实性、作弊或内容质量判断属于独立 Policy / Application 层。

## 8. 隐私最小化

Public provenance **MUST NOT** 默认要求：

- 用户账号；
- 手机号或邮箱；
- IP 地址；
- 设备指纹；
- raw prompt；
- 完整私有训练数据；
- 内部商业秘密。

Profile 可以使用 commitment、selective disclosure、confidential audit、TEE、ZK 或未来技术提供更强证据，但 Core 只定义所需语义，不强制技术。

## 9. 算法与承载层独立

以下均属于可替换实现层，而不是 GCPP Core 永恒依赖：

```text
C2PA
SPDX
CycloneDX
VC / DID
X.509
in-toto
SCITT
hash families
watermark families
blockchains
transparency logs
AI architectures
regulatory regimes
```

Profile **MAY** 在某一时期要求具体技术以获得互操作性，但必须声明版本、迁移和弃用行为。

## 10. GCPP 与现有标准的长期关系

GCPP 的目标不是成为所有事实的唯一容器。

推荐架构：

```text
GCPP Core semantics
        |
        +-- C2PA Adapter
        +-- SPDX / CycloneDX Adapter
        +-- VC / Identity Adapter
        +-- in-toto / Attestation Adapter
        +-- SCITT / Transparency Adapter
        +-- Regulatory Adapters
        +-- Future adapters
```

GCPP verifier 的价值来自跨承载层一致解释技术事实，而不是强迫所有生态采用一套新的存储格式。

## 11. Core 晋级测试

任何候选 Core primitive **SHOULD** 通过以下测试：

- 解决真实且长期存在的问题；
- 不依赖单一厂商；
- 不依赖单一算法；
- 即使其他标准明天加入相似字段，仍然有独立语义价值；
- 可以由两个以上不同技术体系提供 Evidence；
- 能表达 unknown / partial / conflicting 状态；
- 不把事实层和政策层混合；
- 不要求不必要的敏感信息；
- 可以被独立实现并产生一致验证结果。

否则应放入 Research、Profile 或 Adapter，而不是 Core。

## 12. 研发优先级

在上述研究基础完成前，GCPP **SHOULD NOT** 为了扩充规范表面面积而快速增加大量 assertion。

当前优先级为：

1. 信息对象最小抽象；
2. 来源 Relation 模型；
3. Provenance Continuity 模型；
4. Evidence capability / limitation 模型；
5. Partial / Mixed provenance；
6. 时间、冲突、撤销与未知语义；
7. 隐私保护证明；
8. 使用真实行业案例验证抽象；
9. 再决定哪些内容进入 Core、Profile 或 Adapter。

---

# English

GCPP must be driven by first-principles problems rather than feature races with C2PA, SPDX, CycloneDX, or other standards.

The preferred research sequence is:

```text
Problem
-> Abstraction
-> Invariant
-> Protocol Primitive
-> Evidence
-> Profile / Adapter / Implementation
```

The current research model focuses on `Entity`, `Relation`, `Continuity`, and `Evidence`. Provenance must be graph-capable, partial/mixed/unknown states must be first-class, evidence must never exceed its proof boundary, privacy must be minimized, and Core semantics must remain independent from any specific credential container, PKI, hash, watermark, ledger, AI architecture, or regulation.

GCPP should reuse or adapt existing standards whenever they already encode a technical fact. A candidate belongs in Core only if its meaning remains useful across implementations and remains meaningful even if another standard later adds a similar field.
