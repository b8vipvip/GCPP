# GCPP 第一性原理协议研究 / GCPP Fundamental Protocol Research

> 状态 / Status: **Research Charter / 非规范性研究纲领**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 研究目的

GCPP 的下一阶段不以“比 C2PA、SPDX、CycloneDX 更早实现某个功能”为目标，也不以寻找现有标准的短期空白为研发驱动力。

GCPP 的研究顺序固定为：

```text
社会/行业长期问题
    ↓
Problem
    ↓
Abstraction
    ↓
Invariant
    ↓
Protocol Primitive
    ↓
Evidence
    ↓
Implementation / Adapter
```

现有标准只在最后一层参与实现与互操作。一个 GCPP Core 原语若只能通过“某个现有标准暂时没做”来证明存在价值，则不应进入 Core。

## 2. 核心问题从“文件来源”升级为“信息连续性”

传统 provenance 常以资产或文件为中心：

```text
Asset A -> Asset B -> Asset C
```

生成式 AI、Agent、RAG、摘要、翻译、训练、蒸馏与多人协作使真实信息流变成多源、多阶段、多变换的图：

```text
Human idea
   +
Retrieved sources
   +
Model reasoning
   +
Tool outputs
   +
Human edits
   +
Model transformations
        ↓
Information object
        ↓
summary / translation / extraction / training / regeneration
```

因此 GCPP 的长期研究对象不是“某个文件是否带有凭证”，而是：

> **信息经过生成、传播、编辑、组合、转换、训练和再生成以后，哪些来源关系仍然存在，哪些关系可以被验证，以及验证证据的边界是什么。**

本研究暂称这一问题为 **Provenance Continuity / 来源连续性**。

## 3. 五个第一性问题

### Q1 — 什么是信息对象？

协议不应永久假设信息对象一定是文件、URL、数据库记录或某种媒体容器。

研究对象需要能够涵盖：

- 完整文件；
- 文本片段；
- 图像区域；
- 音视频时间段；
- 结构化记录；
- Agent 中间结果；
- 数据集或数据集子集；
- 模型、checkpoint、adapter；
- 一次生成执行的多个输出；
- 未来尚未出现的数字对象。

目标不是立即创建通用超级对象格式，而是确定 Core 对对象身份的最小假设。

### Q2 — 什么叫两个信息对象之间存在来源关系？

来源关系不能只剩下模糊的 `derived-from`。

需要研究不同关系是否属于同一种协议原语，以及它们各自能证明什么：

```text
copied-from
quoted-from
summarized-from
translated-from
extracted-from
combined-with
generated-from
retrieved-from
reasoned-with
edited-from
trained-on
distilled-from
synthetic-data-generated-by
evaluated-by
```

这些名称目前只是研究词汇，不是正式 registry。

核心问题是：

> relation 描述“历史先后”、 “结构派生”、 “信息贡献”、 “因果影响”还是“法律归属”？

GCPP Core 必须只表达可以被证据支持的技术事实，不把版权、合法性、真实性或责任判断编码成来源事实。

### Q3 — 信息变化后，什么叫来源关系仍然连续？

这是 GCPP 下一阶段的重点问题。

连续性不是简单的：

```text
same / different
```

候选抽象包括：

```text
exact continuity
structural continuity
segment continuity
transform continuity
semantic continuity
causal influence
historical relation
unknown
```

不同连续性类型需要不同证据，不能被压缩为一个统一相似度百分比。

例如：

- 删除标点可能保持 exact-normalized continuity；
- 摘录可能保持 segment continuity；
- 翻译可能失去字节连续性但保留声明的 transform relation；
- 摘要属于多输入到新对象的有损关系；
- 模型训练只表明训练影响，不意味着单次模型输出可归属于某个训练样本。

协议必须能够明确表达“无法证明”与“证明不存在”的区别。

### Q4 — Evidence 到底证明什么？

每份 Evidence 必须声明：

```text
subject
claimed relation / property
scope
verification method
assumptions
failure modes
issuer / observer
validity / time context
```

不同证据不得自动互相升级：

```text
SIGNATURE != TRUTH
WATERMARK != IDENTITY
SIMILARITY != LINEAGE
ATTESTATION != INDEPENDENT AUDIT
REGULATORY LABEL != CRYPTOGRAPHIC PROVENANCE
ABSENCE OF EVIDENCE != EVIDENCE OF ABSENCE
```

未来的 GCPP verifier 应首先输出 Evidence Facts / Verification Vector，再由独立 Policy 层产生“可信”“合规”“允许发布”等结论。

### Q5 — 公共协议最少需要哪些长期原语？

初始研究假设为：

```text
Entity
Relation
Continuity
Evidence
```

其中：

- **Entity**：参与来源关系的对象或主体；
- **Relation**：对象之间声明的来源、变换或影响关系；
- **Continuity**：关系经过复制、编辑或转换后仍可验证到什么程度；
- **Evidence**：支持关系、连续性或身份声明的证据。

这只是研究假设。进入 GCPP Core 前必须证明它们是必要、互相独立且足够稳定的抽象。

## 4. 信息关系图，而不是单链历史

GCPP 必须假设 provenance 是 DAG 或更一般的带证据关系图，而不是只有一个 parent 的版本链。

示例：

```text
Source A ----quoted-from----\
                          \
Source B ----summarized-from---> Result X
                          /
Human C ------edited-by------/
                          \
Model D ----translated-by-----> Result Y
```

每条边可以拥有独立 Evidence 和 Continuity 状态。

Verifier 不应因为图中某条边验证失败而把整个对象简单标记为 `FAKE` 或 `HUMAN`。

## 5. Partial / Mixed Provenance 是正常状态

未来内容大量由混合来源组成，因此：

```text
PARTIAL != ERROR
MIXED != UNTRUSTED
TRANSFORMED != UNVERIFIED
```

GCPP 应研究如何表达：

- 哪些片段具有 exact binding；
- 哪些片段具有 transform relation；
- 哪些片段只有历史声明；
- 哪些片段没有来源证据；
- 多个来源如何在同一对象中并存。

`authenticated coverage` 应被视为一种验证结果，而不是强行要求所有对象达到 100%。

## 6. 隐私与选择性披露是协议基本要求

真实的 provenance 系统不能要求公开完整训练数据、raw prompt、用户身份、内部工具调用或商业秘密。

Core 研究必须允许：

```text
prove relation
without disclosing all underlying data
```

可由 Profile 使用的技术包括但不限于：

- commitment；
- selective disclosure；
- confidential audit；
- trusted execution attestation；
- zero-knowledge proof；
- transparency receipt；
- future evidence systems。

GCPP Core 不绑定上述任何一种技术。

## 7. 长期技术独立性

以下技术均不得成为 GCPP Core 永恒前提：

```text
C2PA
SPDX
CycloneDX
DID / VC
X.509
SHA-2
blockchain
specific watermark
specific transparency log
specific AI architecture
specific national regulation
```

它们可以作为 2026 年的优秀实现、Adapter 或 Evidence carrier。

GCPP 的长期语义必须能够在这些技术被替换后继续成立。

## 8. 与现有标准的关系

GCPP 不与成熟标准进行功能竞赛。

当已有标准可以承载某项事实时，GCPP 优先建立映射，而不是重新定义对象格式：

```text
C2PA          -> content credentials / signatures / bindings / asset history
SPDX/CDX      -> software, AI and dataset supply-chain description
VC            -> identity / authorization credentials
in-toto       -> process attestations
SCITT/logs    -> transparency / registration evidence
GB 45438      -> Chinese regulatory AIGC labeling
future specs  -> future implementation layers
```

GCPP 的研究价值只来自更底层、跨实现仍成立的问题，而不是“某标准暂时缺少一个字段”。

## 9. 研究验证标准

任何候选 GCPP Core 原语进入规范前都必须回答：

1. 它解决的现实问题是什么？
2. 该问题是否跨平台、跨模型、跨法域长期存在？
3. 为什么已有一般概念不足以表达？
4. 如果 C2PA/SPDX/CycloneDX 明天加入类似字段，该原语是否仍有意义？
5. 它是否依赖某个具体算法或厂商？
6. 它能否被至少两种完全不同的证据技术实现？
7. 它是否把事实与政策/法律判断混在一起？
8. 它能否支持 unknown / partial / conflicting evidence？
9. 它是否要求不必要的个人数据或商业秘密？
10. 独立实现是否可能得到一致验证结果？

若第 4 项答案为“否”，该候选更适合作为 Adapter/Profile，而不是 Core。

## 10. 下一阶段研究任务

在继续定义 Internet Profile assertion 之前，优先完成：

1. `Information Object` 最小抽象研究；
2. `Relation` 类型系统与事实/政策边界研究；
3. `Provenance Continuity` 形式模型；
4. Evidence capability / limitation model；
5. Partial / Mixed provenance verification semantics；
6. provenance graph 的冲突、未知、撤销与时间语义；
7. privacy-preserving evidence model；
8. 使用真实行业案例验证上述原语，而不是只做理论示例。

## 11. 成功标准

GCPP 的成功不定义为：

- 比其他标准更早发布；
- assertion 数量更多；
- 支持更多算法；
- 创建自己的加密容器；
- 让所有行业迁移到 GCPP 专有格式。

成功定义为：

> **GCPP 找到一组足够小、足够稳定、能够解决真实信息来源连续性问题的公共协议原语，并且这些原语可以由多个现有和未来标准独立承载与验证。**

---

# English

## Research charter

GCPP must not be driven by a race to implement features before C2PA, SPDX, CycloneDX, or other standards. Its research order is:

```text
real long-term problem
-> abstraction
-> invariant
-> protocol primitive
-> evidence
-> implementation / adapter
```

Existing standards belong primarily to the implementation and interoperability layer.

The principal research question is **provenance continuity**: after information is generated, copied, edited, combined, translated, summarized, trained on, distilled, or regenerated, which source relationships still exist, which can be verified, and what exactly does each item of evidence prove?

The current first-principles hypothesis is that a durable protocol may need four minimal concepts:

```text
Entity
Relation
Continuity
Evidence
```

This is a research hypothesis, not yet a normative Core model.

GCPP should model provenance as an evidence-backed relation graph, treat partial and mixed provenance as normal states, preserve strict separation between facts and policy/legal conclusions, support privacy-preserving evidence, and remain independent of any particular credential format, hash, watermark, PKI, ledger, AI architecture, or national regulation.

A proposed Core primitive must remain meaningful even if an existing standard later adds a similar field. Otherwise it belongs in an Adapter or Profile rather than Core.
