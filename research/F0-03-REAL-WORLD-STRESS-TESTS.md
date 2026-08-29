# F0-03 — 真实行业场景压力测试 / Real-World Architecture Stress Tests

> 状态 / Status: **F0 Research / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 目的

F0 不通过“概念听起来合理”决定 Core。

候选架构必须面对真实行业场景，并允许被场景反驳。

本轮测试的候选模型：

```text
Subject / State
Claim
Relation proposition
Scope / Projection qualification
Evidence
Assessment
Policy outside Core
```

本文件不证明该模型最终正确，只记录第一轮压力测试结果。

## 2. Test A — 完全复制但来源未知

### 场景

文件 B 与文件 A 字节完全相同，但无法知道谁先产生。

### 可观察事实

```text
bytes(A) == bytes(B)
```

### 不能推出

```text
B derived-from A
A derived-from B
same author
same generation event
same legal owner
```

### 协议要求

必须分离：

```text
state/representation equality
historical provenance
actor identity
```

### F0 结果

**通过。** `Claim + Evidence` 模型可以表达 equality evidence，同时保持 derivation unknown。

---

## 3. Test B — 编码变化但内容保持

### 场景

同一文本从 UTF-8 转 UTF-16，并改变换行风格。

### 问题

byte hash 完全变化，但在某个 normalization profile 下文本内容可以相等。

### 协议要求

```text
comparison criterion / projection
```

必须成为 continuity claim 的限定条件。

### F0 结果

**原四元组失败，新模型通过。** 裸 `Continuity(A,B)` 不足；需要 `projection_profile`。

---

## 4. Test C — 新闻文章更正

### 场景

10:00 发布 Article A；11:30 修改错误数字；15:00 增补新的采访内容。

平台仍使用同一个 URL。

### 必须回答

- URL 指的是逻辑 Article 还是当前版本？
- 10:00 的签名能否验证 15:00 内容？
- 哪条旧 claim 已被更正？
- 历史版本能否继续验证？

### 协议要求

```text
mutable Subject
multiple immutable/fixed States
supersede / correction Claims
temporal context
```

### F0 结果

**支持 Subject / State 分离。** 一个 URL/Subject identifier 不足以承担 state identity。

---

## 5. Test D — 翻译

### 场景

英文原文 A 由翻译者或 AI 翻译成中文 B。

### 可以有的 Evidence

- 翻译服务签名 execution record；
- input/output binding；
- human translator attestation；
- later independent quality assessment。

### 不同 Claim

```text
B was-produced-by translating A
B preserves proposition P from A
B is a faithful translation of A
```

三个 Claim 不等价。

### F0 结果

**证明 Historical Dependency 与 semantic preservation 必须分离。**

“翻译发生过”可以被 process evidence 强验证；“语义完全保真”不能由同一签名自动推出。

---

## 6. Test E — 多来源摘要

### 场景

Agent 阅读 100 个来源并生成一份报告。

### 失败的对象级表示

```text
Report derived-from Source1..Source100
```

它无法回答：

- 哪个来源支持哪条主张；
- 某来源只是被检索到还是实际使用；
- 哪个来源与报告存在冲突；
- 哪个主张没有来源；
- 报告中哪些句子来自模型推断而非来源原文。

### 协议要求

```text
claim-level provenance
scope / claim selector
support / contradict relation
retrieved != used != supports
```

### 现实痛点验证

2026 年关于 Deep Research Agent auditability 的研究把 claim-evidence tracing、provenance coverage、contradiction transparency 视为核心审计问题；LLM Agent execution provenance 研究也将 retrieved evidence、tool output、memory、intermediate claim 和 final answer 的关系列为开放问题。

### F0 结果

**Claim 必须是一等对象的证据增强。**

---

## 7. Test F — 人类 + AI 混合文档

### 场景

一份合同草稿：

- P1-P3 人工原创；
- P4 AI 起草后人工重写 60%；
- P5 引用法规；
- P6 使用另一个模型翻译；
- P7 来源未知。

### 错误表示

```text
Document = AI_GENERATED
```

或：

```text
Document = HUMAN
```

都丢失关键信息。

### 协议要求

```text
partial provenance
mixed provenance
scope-qualified claims
unknown as first-class state
```

### F0 结果

**Scope 是强候选 Core requirement。**

具体 selector encoding 可以属于媒体/Profile，但 relation 能被 scope 限定应属于抽象模型能力。

---

## 8. Test G — 语义相同但独立创作

### 场景

两个模型分别回答“水在标准大气压下约 100°C 沸腾”。

输出高度相似甚至完全相同。

### 错误推断

```text
similarity => copied/distilled/derived
```

### 协议要求

semantic similarity 只能成为某种 measurement Evidence：

```text
algorithm M observed score x
```

不能自行升级为 historical relation。

### F0 结果

**证明 similarity 与 provenance 必须正交。**

---

## 9. Test H — 模型训练与单次输出

### 场景

Dataset D 被用于训练 Model M；M 生成 Output O。

### 可以成立

```text
D used-in-training-of M
M generated O
```

### 不能自动成立

```text
O derived-from every item in D
O preserves item d42
```

即使某训练样本对模型参数有因果影响，也不等于可以把每次输出归属给该样本。

### 协议要求

```text
training lineage
output provenance
content continuity
```

三个域必须分开。

### F0 结果

**支持 `OUTPUT_PROVENANCE != MODEL_LINEAGE`，并进一步证明 lineage relation 也不能自动传播到下游 output。**

---

## 10. Test I — 蒸馏水印证据

### 场景

Student Model 中检测到与 Teacher watermark/profile 一致的统计信号。

### 可记录

```text
Evidence E:
  method = watermark-profile-X
  observation = positive
  score = x
```

### 不可自动输出

```text
Teacher A definitely distilled into B
illegal distillation
copyright infringement
```

### 协议要求

```text
Evidence
Assessment
Policy/legal interpretation
```

必须分层。

### F0 结果

**Evidence -> Assessment -> Policy 分离通过。**

---

## 11. Test J — 来源凭证被剥离但 RID 可恢复

### 场景

文本经过平台复制后 metadata / manifest attachment 丢失，但内容内 signal 恢复出 RID。

### RID 可以证明什么？

只证明：

```text
candidate record locator recovered
```

还需要：

```text
resolve record
verify signature
verify state/content binding
verify applicable scope
```

才能建立 attribution。

### F0 结果

**Identifier / Binding / Locator 分离通过。**

此前 GID/RID 设计应被视为这个更一般原则的一个实例。

---

## 12. Test K — 两套冲突来源凭证

### 场景

两个签名主体都声明自己生成了同一份可见内容。

两份签名都 cryptographically valid。

### 错误处理

```text
signature valid => provenance true
```

### 正确结构

```text
Claim C1 + Evidence E1
Claim C2 + Evidence E2
Assessment A1
Assessment A2
conflict remains visible
```

可能需要额外：

- timestamp / transparency；
- generation execution evidence；
- authoritative registry；
- source-side records。

### F0 结果

**证明 Claim 必须与 cryptographic validity 分离；valid signatures can support contradictory claims.**

---

## 13. Test L — 科研数据到结论

### 场景

Raw Data D 经清洗、统计模型、过滤、人工解释后得到论文结论 Claim C。

### 问题

只保存：

```text
Paper derived-from Dataset D
```

无法审计：

- 哪个处理版本；
- 哪些记录被排除；
- 哪个软件参数；
- 哪个统计结果直接支持 C；
- 哪一步发生错误。

数据库 provenance 研究早已区分 why-provenance、where-provenance 与 how/provenance-polynomial 等不同问题，这说明“来源”本身不是一个单关系问题。

### 协议要求

```text
process / event provenance
claim-level support
multi-stage derivation
scope
evidence of execution
```

### F0 结果

**Activity/Event 仍是强候选。** 不能在 F0 过早把 process node 从模型中删除。

---

## 14. Test M — Agent 工具调用与错误传播

### 场景

Agent：

```text
Search -> Web page -> parser -> calculator -> memory -> LLM -> final claim
```

最终数字错误。

### 审计问题

- 网页数据就错了？
- parser 解析错？
- calculator 参数错？
- memory 取错版本？
- LLM 在最后转述错？

### 协议要求

```text
execution event graph
input/output state binding
claim-level evidence chain
intermediate artifacts
selective disclosure
```

### F0 结果

**Object-level content credential 不足以单独解决 agent auditability。**

这可能是 GCPP 未来产生真实社会价值的重要场景之一，但 F0 仍需要验证能否通过通用 Claim/Event/Evidence 模型解决，而不是创建 Agent 专用 Core。

---

## 15. Test N — 隐私敏感来源

### 场景

医疗模型或企业 Agent 必须证明：

```text
approved dataset/version was used
```

但不能公开患者数据、完整训练集或商业秘密。

### 协议要求

Claim 应允许 Evidence 是：

- commitment；
- selective disclosure；
- confidential auditor result；
- TEE attestation；
- ZK proof；
- future mechanism。

### F0 结果

**Core 必须描述“证明什么”，而不能要求固定 Evidence payload。**

这与 IETF RATS 的 architecture lesson 一致：Evidence 可以高度平台特定，而 interoperable assessment/result 往往更重要。

---

# 16. 第一轮矩阵

| 场景 | Subject/State | Claim | Scope | Event | Evidence/Assessment split | Continuity relative to facet |
|---|---:|---:|---:|---:|---:|---:|
| Exact copy | useful | required | optional | optional | required | required |
| Re-encoding | required | required | optional | useful | required | **required** |
| News correction | **required** | **required** | useful | useful | required | required |
| Translation | required | **required** | useful | **strong** | **required** | **required** |
| Multi-source summary | required | **required** | **required** | strong | **required** | **required** |
| Human+AI mixed doc | required | **required** | **required** | useful | **required** | required |
| Similar independent text | useful | **required** | optional | unknown | **required** | **required** |
| Model training | required | **required** | dataset scope | **strong** | **required** | separates from lineage |
| RID recovery | required | required | required | optional | **required** | required |
| Conflicting credentials | useful | **required** | optional | useful | **required** | optional |
| Scientific claim | required | **required** | **required** | **strong** | **required** | required |
| Agent execution | required | **required** | **required** | **strong** | **required** | required |
| Privacy-sensitive proof | required | **required** | **required** | useful | **required** | context-dependent |

## 17. 第一轮结构性结论

### 17.1 Claim 的必要性高于 Continuity 作为独立 primitive

所有冲突、修正、审计、claim-level support 场景都要求 Claim 一等化。

### 17.2 Scope 很可能是 Core capability

不是说 Core 必须定义所有 selector，而是：

> **任何 provenance relation/claim 都必须能够说明它适用于哪个范围。**

### 17.3 Continuity 更像 qualified claim / query result

它不是一个脱离 projection、scope、relation 和 Evidence 的对象。

### 17.4 Activity/Event 尚不能删除

训练、Agent、科研工作流、翻译执行都表明 process node 有真实价值。

下一轮需要比较：

```text
Event as first-class Core role
```

与：

```text
Event represented as a generic Subject + typed Claims
```

哪种更小、更稳定。

### 17.5 Assessment 是互操作价值的候选核心

不同 Evidence 技术可能永远高度异构。

真正跨厂商有价值的可能不是统一所有 raw Evidence，而是统一：

```text
what claim was assessed
what evidence profile was used
what scope was verified
what result was obtained
what assumptions / limitations apply
```

这需要继续验证。

## 18. F0 下一轮实验

### F0-R2.1 — State minimality

尝试删除 `State`，只使用 Subject + Claim，观察上述场景是否仍能无歧义表达。

### F0-R2.2 — Scope minimality

尝试把 Scope 全部下放到 Profile，观察 Core 是否还能保证 partial/mixed provenance 的互操作语义。

### F0-R2.3 — Event reducibility

尝试把 Event 作为 generic Subject 表达，与独立 Event primitive 比较。

### F0-R2.4 — Continuity reducibility

尝试完全删除 Continuity primitive，仅使用：

```text
historical relation
+
preservation claim
+
scope
+
projection
+
evidence
```

如果表达能力不下降，则 Continuity 应保留为上层查询/展示概念而非 Core primitive。

### F0-R2.5 — Claim conflict algebra

定义至少：

```text
supports
challenges
contradicts
supersedes
retracts
```

并验证它们是否属于 Core 还是 registry/profile。

## 19. 参考资料 / References

- W3C PROV-DM: https://www.w3.org/TR/prov-dm/
- W3C PROV Constraints: https://www.w3.org/TR/prov-constraints/
- IFLA Library Reference Model: https://repository.ifla.org/handle/20.500.14598/40
- PREMIS v3.0: https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf
- RFC 6920: https://www.rfc-editor.org/rfc/rfc6920.html
- RFC 9334: https://www.rfc-editor.org/rfc/rfc9334.html
- Nanopublications: https://nanopub.net/
- Why and Where: A Characterization of Data Provenance: https://www.cis.upenn.edu/~sanjeev/papers/icdt01_data_provenance.pdf
- Provenance Semirings: https://repository.upenn.edu/bitstreams/b598c0a7-0d24-4162-8279-5f51a17d29c2/download
- From Fluent to Verifiable: Claim-Level Auditability for Deep Research Agents: https://arxiv.org/abs/2602.13855
- From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents: https://arxiv.org/abs/2606.04990

---

# English

This document stress-tests the F0 candidate architecture against exact copying, transcoding, news corrections, translation, multi-source summarization, mixed human/AI documents, independently similar content, model training, watermark evidence, RID recovery, conflicting credentials, scientific workflows, agent execution, and privacy-sensitive provenance.

The first-round result is that a first-class `Claim` is more fundamental than a standalone `Continuity` primitive. Scope qualification appears necessary for partial and mixed provenance. Continuity appears reducible to historical relation + preservation claim + scope + projection/facet + evidence. Activity/Event remains a strong candidate because training, agent execution, scientific workflows, and transformation pipelines require process-level explanations.

The next round will explicitly try to delete State, Scope, Event, and Continuity one at a time. Any concept that can be removed without losing required semantics should not become a GCPP Core primitive.
