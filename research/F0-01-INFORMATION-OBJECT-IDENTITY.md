# F0-01 — 信息对象与身份：第一轮反证研究 / Information Object and Identity — Round 1 Falsification Study

> 状态 / Status: **F0 Research / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 研究问题

F0 的第一个问题是：

> **公共来源协议里最小的 Information Object 到底是什么？**

如果这个问题回答错误，后面的来源关系、片段归属、转换连续性、模型血缘和 Evidence 都会建立在错误对象模型上。

本文件不寻找“别人还没有定义的对象类型”，而是尝试反驳 GCPP 当前的初始假设。

## 2. 初始假设受到的第一轮压力

此前 GCPP 暂定研究模型：

```text
Entity
Relation
Continuity
Evidence
```

第一轮研究结论是：

> **单一 `Entity` 不能充分承担 Information Object 的身份语义。**

原因不是缺少字段，而是“同一个信息对象”本身具有多个互不等价的观察层级。

### 2.1 字节相同

两个对象可以具有完全相同的字节：

```text
A bytes == B bytes
```

这只能建立某个 representation / bitstream 层面的等价。

它不能证明：

- A 是 B 的复制品；
- B 来源于 A；
- 谁先产生；
- 谁拥有内容；
- 两者是否属于同一个逻辑作品；
- 两者是否由同一生成执行产生。

IETF RFC 6920 可以用哈希命名数字对象，但同时明确指出，URI 中 authority/domain 的存在本身不证明该域与内容之间的所有权或来源关系。

因此：

```text
CONTENT_EQUALITY != PROVENANCE
HASH_MATCH != ACTOR_IDENTITY
HASH_MATCH != DERIVATION
```

### 2.2 字节不同但可被认为“内容相同”

例如：

- UTF-8 与 UTF-16 编码同一文本；
- 换行符不同；
- 图片重新编码但像素相同；
- PDF 重新保存但显示内容相同；
- 同一录音以不同无损容器表示。

此时 byte identity 已经失效，但某个更高层 projection 仍可能相等。

因此不存在脱离比较规则的全局 `same-content`。

必须先声明：

```text
under which projection / normalization / interpretation?
```

### 2.3 表达不同但被认为属于同一个逻辑作品

IFLA 的 Work / Expression / Manifestation / Item 模型长期区分：

```text
Work
  ↓ realized through
Expression
  ↓ embodied in
Manifestation
  ↓ exemplified by
Item
```

翻译可以是同一 Work 的不同 Expression；但 IFLA 同时强调，仅有事实或主题上的相似不足以判定两个表达属于同一 Work。

这说明：

> **逻辑作品身份不是由语义相似度自动推出的密码学事实。**

它通常包含领域规则、创作关系、编目或社会约定。

因此 GCPP Core 不能定义：

```text
semantic_similarity > X
=> SAME_INFORMATION_OBJECT
```

### 2.4 同一“东西”随时间发生变化

W3C PROV 已经遇到这一问题。PROV 把 Entity 定义为具有某些 fixed aspects 的东西，并明确指出：当现实对象在一段时间内相关属性发生变化时，应使用多个 Entity/state 描述，并通过事件和关系连接。

这说明：

```text
logical referent
```

与：

```text
fixed state used for provenance verification
```

不应该被强行压成同一个概念。

## 3. F0 第一项关键结论：不要定义万能 InformationObject

GCPP 当前不应创建：

```text
InformationObject {
  id
  type
  hash
  ...
}
```

然后假设它可以同时代表：

- 一篇不断修改的新闻；
- 新闻某个历史版本；
- 该版本的 PDF；
- PDF 中一段文字；
- 这段文字表达的一个主张；
- 一个模型 checkpoint；
- 一次生成执行。

这会把不同身份层级混在一起。

## 4. 新的候选分离：Subject / State / Representation

F0 Round 1 提出三个**研究角色**，目前尚未冻结为 Core primitive：

```text
Subject
State
Representation
```

### 4.1 Subject

`Subject` 表示“协议声明正在谈论的那个 referent”。

它可以是：

- 逻辑作品；
- 某个发布条目；
- 模型；
- 数据集；
- Agent 任务；
- 人；
- 组织；
- 生成执行；
- 未来未知对象。

Core 不试图定义 Subject 的完整本体论。

关键要求：

> Subject identifier 只是引用方式，不自动证明现实世界身份。

### 4.2 State

`State` 是为了验证而固定下来的某个 Subject 的状态/观察切片。

候选语义：

```text
State {
  subject_ref?
  state_context
  fixed_aspects / commitments
  temporal_context?
}
```

一个不断变化的 Subject 可以有多个 State：

```text
Article A
  ├─ State A1  10:00
  ├─ State A2  11:30 correction
  └─ State A3  15:00 update
```

来源关系和 Evidence 应尽可能绑定 State，而不是模糊绑定一个可变 Subject。

### 4.3 Representation

`Representation` 是 State 的具体编码/承载表现。

例如：

```text
State S
  ├─ UTF-8 text
  ├─ UTF-16 text
  ├─ HTML
  ├─ PDF
  └─ printed form
```

Representation 可以发生 byte-level 变化，而更高层 State 仍可能被某个 Profile 判定为保留了指定属性。

## 5. 为什么暂时不能把三者都直接冻结为 Core

这三个角色解决了很多混淆，但仍有风险：

1. `Subject` 与 `State` 的边界可能依赖使用场景；
2. 一个 Representation 本身也可以成为另一个声明的 Subject；
3. 模型 checkpoint 既可以视为 State，也可以直接视为独立 Subject；
4. Claim-level provenance 可能根本不需要完整的 Subject ontology；
5. W3C PROV 已能通过多个 Entity + specialization/alternate 表达相似思想。

所以当前正确动作不是发明三个强类型对象，而是确认**协议必须区分不同引用语义**。

## 6. F0 第二项关键结论：Identifier / Binding / Locator 必须分离

此前 GCPP 的 GID / RID 分离其实暴露了一个更一般的原则。

### 6.1 Reference Identifier

用于“指哪个对象/状态”。

它可以是：

- URI；
- UUID；
- DOI；
- provider-issued ID；
- DID URL；
- content-addressed ID；
- 本地 opaque ID。

但：

```text
IDENTIFIER != IDENTITY PROOF
```

### 6.2 Binding / Commitment

用于证明某个引用与某个可观察 State/Representation 之间的关系。

可能实现：

- cryptographic digest；
- Merkle commitment；
- signature-bound claim；
- C2PA hard binding；
- hardware measurement；
- future proof system。

因此：

```text
REFERENCE != BINDING
```

### 6.3 Locator

用于发现/检索候选记录或 Evidence。

例如：

- URL；
- Manifest Repository key；
- GCPP RID；
- content discovery fingerprint；
- database index。

因此：

```text
LOCATOR != REFERENCE IDENTITY
LOCATOR != AUTHENTICATION
```

### 6.4 三者可以共享相同字节，但语义必须不同

一个 hash 在某个系统中可以同时用于：

- reference；
- binding；
- lookup key。

但协议不能因为字段值相同就把三种语义合并。

## 7. F0 第三项关键结论：不存在无条件的“same information”

任意对象等价判断必须相对于一个 criterion/profile：

```text
Equivalent(A, B | Criterion)
```

候选 Criterion 可以包括：

```text
byte-exact
canonical-representation
normalized-text
pixel-equivalent
segment-equivalent
logical-work-equivalent
profile-defined-equivalent
```

但最后两类通常不能仅凭算法自动证明。

因此 Core 应避免一个裸的：

```text
sameAs
```

除非它明确携带：

- 谁作出该 claim；
- 按什么 criterion；
- 对哪些 scope；
- 有什么 Evidence。

## 8. 与数字保存研究的交叉验证

数字保存领域长期使用 `significant properties` / `essential characteristics` 来回答：

> 经过格式迁移后，到底哪些属性必须保留，才能认为保存仍然成功？

PREMIS 明确指出这些属性可能包括内容、外观、结构、行为、上下文，并且哪些属性“重要”可能由具体 repository / business requirement 决定。

这为 GCPP 提供一个重要反证：

> **Continuity 不能脱离“观察什么属性/Facet”而有绝对含义。**

这将在 F0-02 中继续推导。

## 9. 候选 Core 不变量

以下规则已经比具体对象类型更稳定，建议进入下一轮验证：

```text
IDENTIFIER != IDENTITY PROOF
REFERENCE != BINDING
LOCATOR != AUTHENTICATION
CONTENT EQUALITY != PROVENANCE
SEMANTIC SIMILARITY != DERIVATION
LOGICAL IDENTITY != BYTE IDENTITY
MUTABLE SUBJECT != IMMUTABLE STATE
```

## 10. F0 当前候选信息模型

不是规范，只用于后续反证：

```text
SubjectRef
    │
    ├── StateRef(s)
    │      │
    │      └── RepresentationRef(s)
    │
    └── Claims about Subject/State
```

身份关系本身也应该允许成为 Claim：

```text
Claim:
  State B is a revision-state of Subject A
```

而不是由 Core verifier 假设为客观事实。

## 11. 下一轮必须回答的问题

1. `State` 是否真的需要成为独立 primitive，还是可以由 immutable Claim target 替代？
2. Representation 是否属于 Core，还是仅仅属于 binding Profile？
3. 一个 Subject 被多个组织独立命名时，如何表达 same-referent 而不制造全球身份中心？
4. 部分内容 selector 是否应该直接绑定 State？
5. 对 streaming / mutable dataset / live Agent memory，State 如何冻结？
6. 是否需要 `StateContext` 或 `View` 来声明“固定了哪些 aspects”？
7. 哪些 identity relation 可以自动验证，哪些只能由可信主体声明？

## 12. 参考资料 / References

- W3C PROV-DM Recommendation: https://www.w3.org/TR/prov-dm/
- W3C PROV Constraints: https://www.w3.org/TR/prov-constraints/
- IFLA Library Reference Model: https://repository.ifla.org/handle/20.500.14598/40
- PREMIS Data Dictionary v3.0: https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf
- RFC 6920 — Naming Things with Hashes: https://www.rfc-editor.org/rfc/rfc6920.html
- RFC 3444 — Information Models vs Data Models: https://www.rfc-editor.org/rfc/rfc3444.html

---

# English

## Round 1 finding

F0 rejects the idea that a single universal `Entity` can safely carry all information-object identity semantics.

A protocol must distinguish at least the **roles** of a logical referent, a fixed state used for provenance claims, and a concrete representation. These roles are currently called `Subject`, `State`, and `Representation`; they are research concepts, not frozen Core classes.

A second foundational separation is:

```text
Reference Identifier
Binding / Commitment
Locator
```

An identifier names or refers; a binding establishes a verifiable relationship to a state or representation; a locator helps discover a record. The same bytes may implement more than one role, but the semantics must remain distinct.

There is no unconditional protocol-level notion of “same information.” Equivalence is always relative to a declared criterion, projection, normalization, or domain rule. Byte equality does not prove derivation, semantic similarity does not prove provenance, and logical-work identity is not the same as representation identity.

The next F0 round must determine whether `State` deserves a Core primitive, how scope/selectors attach to states, and how identity claims can remain decentralized and evidence-backed.
