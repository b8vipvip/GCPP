# F0-04 — 最小性删除实验与验证边界模型 / Minimality Deletion Experiments and Verification-Boundary Model

> 状态 / Status: **F0 Research / Non-normative**  
> 默认语言 / Default language: **简体中文（zh-CN）**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 为什么必须继续删除

F0 前三轮已经把原始假设：

```text
Entity
Relation
Continuity
Evidence
```

修正成更 Claim-centric 的候选架构。

但“能表达”不是进入公共协议 Core 的充分条件。

如果一个已有通用图模型同样可以表达这些东西，那么 GCPP 只是重新命名已有概念。

所以本轮采用更严格标准：

> **逐个删除候选概念。删除后如果仍能无歧义表达真实痛点，该概念不应成为独立 Core primitive。**

同时加入 Prior Art 反证：

- W3C PROV 已有 Entity / Activity / Agent、qualified relations、Bundle；
- Nanopublication 已有 Assertion + assertion provenance + publication info；
- RDF 1.2 已加入 proposition / reification 方向，能够引用一个 proposition 而不把它自动断言为事实，并允许给潜在矛盾 proposition 附加 metadata。

所以：

```text
GRAPH != GCPP NOVELTY
CLAIM != GCPP NOVELTY
REIFIED RELATION != GCPP NOVELTY
PROVENANCE-OF-PROVENANCE != GCPP NOVELTY
```

F0 必须找到一个更基本的、真实行业仍缺少统一语义的层。

---

## 2. 删除实验 A：删除独立 `State` primitive

候选架构原来区分：

```text
Subject
State
Representation
```

现在尝试只保留通用 `Node/Subject`，把版本关系写成 Claim：

```text
Node A1
Claim: A1 is-version-of Article-A
Claim: A1 valid-at T1
Claim: A1 bound-by digest H1

Node A2
Claim: A2 is-version-of Article-A
Claim: A2 valid-at T2
Claim: A2 bound-by digest H2
```

### 能否表达新闻更正？

可以。

### 能否表达模型 checkpoint？

可以。

### 能否表达 mutable dataset snapshot？

可以。

### 问题

如果没有统一的 `State` 语义，独立 verifier 如何知道：

- 哪个 Node 是可变逻辑对象；
- 哪个 Node 是为了验证被冻结的状态；
- 某个 binding 到底绑定逻辑 Subject 还是某个时刻的 State；
- 两个实现是否会把同一 version relation 理解成同样的验证边界。

### 结论

`State` **不必成为一种封闭对象类型**，但“状态固定性”不能被删除。

更小的要求可能是：

> **任何可验证 Claim 必须能够指向一个明确的 Observation Boundary / State Boundary。**

因此本轮把：

```text
State as Core object type
```

降级为候选：

```text
State Boundary as Claim qualification
```

它回答：

> 这个 Claim 说的是对象的哪个固定状态？

---

## 3. 删除实验 B：删除 `Representation`

将编码/载体差异全部放到 binding Profile：

```text
Claim target = State S
Binding profile P says:
  bytes/file/text/pixels/... correspond to S
```

### UTF-8 -> UTF-16

可以由 normalization/binding profile 表达。

### PDF -> visible text

可以由 extraction/projection profile 表达。

### 图片重新编码

可以由 media binding profile 表达。

### 结论

`Representation` 目前**没有证明必须是独立 Core primitive**。

它更适合作为：

```text
binding / projection profile concern
```

保留术语用于说明，但不晋级 Core。

---

## 4. 删除实验 C：删除 `Scope`

尝试把所有 selector 都下放到 relation Profile：

```text
quoted-from-text-range
quoted-from-image-region
quoted-from-json-pointer
...
```

### 立即出现的问题

每种 relation × 每种媒体 × 每种局部范围都需要新 predicate。

例如：

```text
translated-from-paragraph
translated-from-page
translated-from-time-range
translated-from-table-cell
```

不仅词汇爆炸，而且 verifier 无法用统一方式回答：

```text
Which part of this object is actually covered?
```

### 混合文档失败

如果 Scope 不是通用 qualification，以下对象无法得到统一 Verification Vector：

```text
P1 human
P2 AI exact
P3 AI heavily edited
P4 quoted source
P5 unknown
```

### 多来源摘要失败

无法统一映射：

```text
Source scope -> Target claim/scope
```

### 结论

`Scope` 本身不必是某个固定 selector 语法，但：

> **Scope-qualification capability 无法被删除。**

这成为 F0 Round 2 第一个强 Core 候选不变量：

```text
EVERY CLAIM MAY BE SCOPE-QUALIFIED
EVERY ASSESSMENT MUST REPORT VERIFIED SCOPE WHEN SCOPE MATTERS
```

Core 只规定 Scope 的角色；具体 selector 交给 Profile。

---

## 5. 删除实验 D：删除 `Event / Activity`

尝试把 Event 当成普通 Node：

```text
Node Run-42
Claim: Run-42 has-role generation-execution
Claim: Run-42 used Input-A
Claim: Run-42 used Model-M
Claim: Run-42 generated Output-B
Claim: Run-42 began-at T1
Claim: Run-42 ended-at T2
```

### 表达能力

从纯信息建模角度看，**可以表达**。

所以不需要再创造一套与 `Node` 平行的 Event container。

### 但语义约束不能消失

如果一个 Node 声明自己扮演 Event/Activity role，则某些 Profile 可能需要约束：

```text
input existed before use
output generation occurred within event interval
generation follows relevant usage
same execution ID cannot mean two incompatible intervals
```

W3C PROV 已有成熟时间约束，因此 GCPP 不应重新发明通用 Activity ontology。

### 结论

`Event` **可约化为 Node + Event Role + Claims**。

GCPP Core 不需要新的 Event primitive。

如果将来 Generation Execution 有特殊要求，应作为 Profile，而不是重建通用 process model。

---

## 6. 删除实验 E：删除 `Continuity`

这是本轮最重要的实验。

尝试完全不存：

```text
Continuity = X
```

只保存：

```text
Historical Relation
Preservation / Transformation Claim
Source Scope
Target Scope
Projection / Facet
Evidence
Assessment
```

### 翻译

```text
Claim 1: B produced-by translation-event E using A
Claim 2: B.scope P preserves A.scope Q under translation-fidelity-profile F
Evidence 1: execution record
Evidence 2: independent translation assessment
```

无须独立 Continuity primitive。

### 摘要

```text
Claim: target claim C is-supported-by source spans S1,S2
Claim: summary event used documents D1..Dn
```

无须 Continuity scalar。

### 精确复制

```text
Claim: B representation equals A under byte-exact profile
```

无须 Continuity scalar。

### 模型训练

```text
Claim: training-run E used dataset D
```

不能也不应该自动产生 content continuity。

### 结论

> **`Continuity` 目前已被成功从最小 Core primitive 集中删除。**

但 Provenance Continuity 仍然保留为 GCPP 的**研究问题和派生查询概念**：

```text
ContinuityView
  = derive from verified historical relations
  + preservation claims
  + scopes
  + projection profiles
  + evidence assessments
```

这比把 Continuity 写成一个字段更严格。

---

## 7. 删除实验 F：删除独立 `Assessment`

尝试把 verifier 输出本身表示成另一个 Claim：

```text
Claim V1:
  verifier X states that Claim C1 is supported
  under verification profile P
  using Evidence E1,E2
  at time T
```

### 从抽象信息模型看

可以。

因此：

```text
Assessment object
```

不是不可约 primitive。

### 但互操作 API 仍需要 Assessment role

消费者需要稳定读取：

```text
claim assessed
verifier
verification profile
result
verified scope
assumptions
limitations
time
```

### 结论

`Assessment` 可以是：

> **一种具有规范字段的 Claim role / output profile。**

无需成为与 Claim 平行的超类。

这与 IETF RATS 的分层精神兼容：raw Evidence 可以高度平台相关，而 verifier result 应具有清晰、可消费的语义。

---

## 8. 删除实验 G：删除独立 `Evidence` primitive

尝试把 Evidence 只视为 Node：

```text
Node E1 = signature artifact
Node E2 = attestation artifact
Node E3 = watermark observation
```

然后通过 Claim：

```text
E1 supports C1 under profile P
```

### 形式上可以

所以 `Evidence` 也未必需要是一种底层容器。

### 但 Evidence Role 无法删除

协议必须知道某引用：

- 是主张本身；
- 是支持主张的证据；
- 是 verifier 的评价；
- 还是普通输入对象。

更重要的是 Evidence Profile 必须声明 proof boundary。

### 结论

`Evidence` 可以约化成：

```text
Node + Evidence Role + Evidence Profile
```

但 **Evidence role 与 proof-boundary contract** 不可删除。

---

## 9. 一个危险结果：最小模型可能退化成“Node + Claim”

经过删除以后，形式上几乎所有内容都可以写成：

```text
Node
Claim
```

例如：

- State = Node with state role；
- Event = Node with event role；
- Evidence = Node with evidence role；
- Assessment = Claim with assessment role；
- relation = Claim proposition；
- identity equivalence = Claim；
- retraction = Claim about Claim。

这看起来非常小，但也暴露一个问题：

> **如果 GCPP 只做到这里，它就基本退化成一个通用 reified statement graph。**

而 RDF 1.2、Nanopublications、PROV 等已经覆盖大量这种能力。

因此 F0 必须停止把“节点和声明”本身当作新架构价值。

---

## 10. 从对象模型转向“Verification Boundary Model”

F0 Round 2 的核心发现是：

> **AI 时代来源系统最难统一的可能不是‘有什么对象’，而是‘一个可验证声明到底覆盖到哪里、在什么解释下成立、由什么证据支持、证据能证明到哪一步’。**

因此提出新的研究中心：

# Verification Boundary / 验证边界

一个 provenance Claim 的机器可验证含义至少受到以下边界约束：

```text
Target Boundary
Scope Boundary
Projection Boundary
Temporal Boundary
Evidence Boundary
Authority Boundary
Inference Boundary
```

---

## 11. Target Boundary

回答：

> Claim 到底谈论哪个固定对象/状态？

必须防止：

- mutable URL 指向变化内容；
- model name 不区分 checkpoint；
- dataset name 不区分 snapshot；
- `document` 同时指逻辑作品和某文件实例。

候选要求：

```text
claim_target MUST be resolvable to a profile-defined state boundary
```

这里不要求全球统一 ID，也不要求目标一定 content-addressed。

---

## 12. Scope Boundary

回答：

> Claim 覆盖 target/source 的哪一部分？

例如：

```text
whole object
text span
image region
time range
JSON subtree
dataset subset
model component
individual proposition
```

Scope selector 本身由 Profile 定义。

Core 只要求：

```text
partial != whole
unknown scope != whole scope
```

---

## 13. Projection Boundary

回答：

> 比较或保持的是对象的哪种可观察性质？

例如：

```text
raw bytes
normalized text
pixel content
layout
selected structure
logical claim set
profile-defined transform property
```

这直接解决“同一个信息到底是什么”的伪问题。

协议不问绝对：

```text
Are A and B the same information?
```

而问：

```text
Does relation/property P hold
between A.scope and B.scope
under projection/profile π?
```

---

## 14. Temporal Boundary

至少需要区分：

```text
event time
claimed occurrence time
claim issuance time
evidence observation time
assessment time
validity interval / freshness context
```

这些时间不能被一个 `timestamp` 字段压平。

例如：

- 2020 年发生的生成事件可以在 2026 年才被重新证明；
- 2026 年签出的 retraction 不会让 2020 年原 Claim 从历史上消失；
- 在线 attestation 的 freshness 与历史档案签名的时间语义完全不同。

---

## 15. Evidence Boundary

回答：

> 这个 Evidence 到底能支持哪类 proposition、哪些 scope、基于哪些假设？

要求 Evidence Profile 声明至少：

```text
supported_claim_family
observable
scope semantics
verification procedure
assumptions
known failure modes
freshness semantics
negative-evidence semantics
```

关键不变量：

```text
SIGNATURE VALIDITY != CLAIM TRUTH
SIGNAL DETECTION != ACTOR AUTHENTICATION
SIMILARITY != HISTORICAL DERIVATION
ATTESTATION != UNIVERSAL FACT
```

---

## 16. Authority Boundary

回答：

> 谁有资格对什么作出什么类型的 Claim？

这里不是建立全球审批中心。

而是区分：

```text
self-assertion
first-party attestation
counterparty attestation
independent observation
independent audit
registry assertion
court/regulator statement
```

它们可能全部密码学有效，但 epistemic role 不同。

Core 不判断谁“最终正确”，但不能把这些 Claim origin 压成同一个 `signed=true`。

---

## 17. Inference Boundary

回答：

> 哪些内容是 Evidence 直接观察，哪些是 verifier 推导，哪些是 Policy 解释？

例如：

```text
Observed:
  watermark signal score = 0.97

Inferred under Profile P:
  evidence supports possible teacher influence

Policy decision:
  investigate license compliance
```

三者必须可区分。

所以：

```text
OBSERVATION != INFERENCE
INFERENCE != POLICY
```

---

## 18. GCPP 的潜在原创问题被重新定义

此时 GCPP 的问题不再是：

```text
How do we build a provenance graph?
```

也不再是：

```text
How do we make claims about claims?
```

而是：

> **How can independently implemented provenance systems preserve and exchange the verification boundaries of claims across copying, transformation, aggregation, AI execution and partial disclosure?**

中文：

> **不同系统如何在复制、转换、聚合、AI 执行和选择性披露之后，仍然不丢失一个来源声明的验证边界？**

这开始接近一个未被简单 graph/credential container 自动解决的行业痛点。

---

## 19. 为什么这比“来源连续性字段”更有社会价值

当边界丢失时，会发生典型错误：

### Scope escalation

“这两段有来源”被显示成“整篇有来源”。

### Identity escalation

“一个 ID 被解析到 Provider”被显示成“Provider 已认证”。

### Evidence escalation

“检测到水印”被显示成“来源已密码学证明”。

### Lineage escalation

“训练使用了 Dataset D”被显示成“输出 O 来自 D”。

### Semantic escalation

“语义相似”被显示成“发生了复制/蒸馏”。

### Time escalation

“过去曾有效”被显示成“当前仍有效”。

### Authority escalation

“Provider 自己声明”被显示成“独立机构验证”。

这些错误都不是缺少更多 provenance 字段，而是：

> **Claim 的验证边界在跨系统传播时丢失。**

---

## 20. 新的最小候选，不再以对象数量定义

F0 Round 2 建议暂时停止寻找“4 个或 5 个名词 primitive”。

改为寻找**不可删除的语义约束**。

当前强候选：

```text
1. Claims are not facts by default.
2. Every verifiable claim has an explicit target/state boundary.
3. Claims may be scope-qualified; partial never silently becomes whole.
4. Equality/preservation is always relative to a projection/profile.
5. Evidence has an explicit proof boundary.
6. Observation, inference, assessment and policy are distinguishable.
7. Claim origin/authority role is explicit.
8. Temporal meanings are not collapsed into one timestamp.
9. Unsupported/unknown is not false.
10. Conflicting valid claims can coexist without destructive overwrite.
```

这组约束比 `Entity/Relation/Continuity/Evidence` 更可能成为真正长期稳定的 Core。

---

## 21. Graph 结构的新结论：不能要求全局 DAG

此前 provenance 常被画成 DAG。

F0 Round 2 发现必须区分：

```text
Process / causal subgraph
```

与：

```text
Claim / evidence / correction graph
```

### Process causal subgraph

在具有可信时间语义时，某些 Profile 可以要求因果无环。

### Claim graph

可以合法出现：

- Claim about Claim；
- Claim challenging another Claim；
- later Claim retracting an earlier Claim；
- mutual dispute；
- cross-reference；
- assessment of assessment。

所以它是 general directed labeled multigraph，不能被 Core 强制成 DAG。

这是一个重要修正：

```text
PROVENANCE DATA AS A WHOLE != DAG
```

只有某些被严格定义的 derivation/process projection 可能是 DAG。

---

## 22. Negative Evidence 的边界

`没有看到证据` 与 `有证据证明不存在` 必须严格分离。

要支持：

```text
EVIDENCE_OF_ABSENCE
```

Evidence Profile 必须说明：

- 检查过的搜索空间；
- 检测方法；
- 覆盖率/完备性假设；
- detection sensitivity；
- 时间窗口；
- 失败条件。

否则 verifier 只能返回：

```text
NOT OBSERVED / UNKNOWN
```

而不能：

```text
ABSENT
```

---

## 23. Retraction / Correction 不删除历史

候选原则：

```text
RETRACTION IS A NEW CLAIM ABOUT AN OLD CLAIM
CORRECTION DOES NOT ERASE HISTORICAL EXISTENCE
```

这样长期审计才能回答：

- 谁什么时候说过什么；
- 什么时候更正；
- 当时哪些 Evidence 可用；
- 后来为什么改变 Assessment。

是否要求 append-only 存储由 Adapter/registry 决定，Core 只定义非破坏性语义。

---

## 24. 多 verifier 不应自动合并成一个信任分数

两个 verifier 可以使用：

- 不同 Evidence；
- 不同算法版本；
- 不同信任根；
- 不同时间；
- 不同阈值。

所以 Core 应允许多个 Assessment Claim 并存。

```text
aggregate_trust_score
```

属于 Policy/Profile，不属于事实层 Core。

---

## 25. F0 Round 2 当前架构草图

```text
                    ┌─────────────────┐
                    │   Referent/Node │
                    └────────┬────────┘
                             │
                     target / argument
                             │
                    ┌────────▼────────┐
                    │      Claim      │
                    │ proposition     │
                    │ boundaries      │
                    │ origin/context  │
                    └────────┬────────┘
                             │ references
             ┌───────────────┼────────────────┐
             │               │                │
      Evidence-role     Event-role       Claim-role nodes
          Nodes             Nodes             ...
             │
             ▼ appraisal
     Assessment-role Claim(s)
             │
             ▼
       Local Policy / UI
```

真正的 Core 候选不是这些方框的具体类层次，而是：

```text
Boundary-preserving claim semantics
```

---

## 26. 下一轮：F0-R3

F0 下一轮不再继续增加名词，而要证明 `Verification Boundary Model` 是否真的解决真实系统互操作失败。

重点：

1. 定义 `BoundaryDescriptor` 的最小抽象，避免变成万能 metadata bag；
2. 证明 7 类 boundary 是否独立，尝试继续合并/删除；
3. 研究 transformation composition：A->B->C 时边界如何组合，哪些不能传递；
4. 研究 provenance laundering：中间系统如何通过删 Scope/Projection/Evidence 边界把弱证据升级成强声明；
5. 研究 information loss：边界字段被删除后 verifier 应如何降级，而不是猜测；
6. 研究 selective disclosure：隐藏 Evidence payload 时如何仍保留 proof boundary；
7. 建立跨 C2PA / PROV / VC / attestation / regulatory metadata 的 lossless/lossy mapping 判据；
8. 用真实新闻、Agent、科研、训练和混合文档数据进行互操作测试。

---

## 27. 参考资料 / References

- W3C PROV-O: https://www.w3.org/TR/prov-o/
- W3C PROV-DM: https://www.w3.org/TR/prov-dm/
- W3C RDF 1.2 work (proposition/reification): https://w3c.github.io/rdf-schema/spec/
- Nanopublications: https://nanopub.net/
- IETF RFC 9334 — RATS Architecture: https://www.rfc-editor.org/rfc/rfc9334.html
- RFC 6920 — Naming Things with Hashes: https://www.rfc-editor.org/rfc/rfc6920.html
- PREMIS v3.0: https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf
- IFLA Library Reference Model: https://repository.ifla.org/handle/20.500.14598/40

---

# English

## Round 2 finding

Primitive deletion shows that `State`, `Representation`, `Event`, `Evidence`, and `Assessment` do not all need to be independent Core object classes. Many can be represented as roles over generic referents/nodes and first-class claims. `Continuity` itself can be removed from the minimal stored model and reconstructed as a derived view over historical relations, preservation/transformation claims, scopes, projection profiles, and evidence assessments.

However, reducing everything to `Node + Claim` is not a satisfactory GCPP architecture: RDF 1.2, W3C PROV, Nanopublications and related systems already provide general statement/reification/provenance mechanisms.

The stronger F0 finding is therefore a shift from an object-centric model to a **Verification Boundary Model**. A verifiable provenance claim must preserve its target/state boundary, scope boundary, projection boundary, temporal boundary, evidence proof boundary, authority/origin boundary, and inference boundary. The exact number and decomposition of these boundaries remain research questions.

The long-term problem becomes: how can provenance claims move across systems, transformations, AI executions, aggregation and selective disclosure without silently widening their verification boundary?

This explains several real failure classes: partial provenance becoming whole-document provenance, a detected watermark becoming authentication, training lineage becoming output attribution, similarity becoming derivation, stale evidence becoming current evidence, or first-party assertions becoming independent verification.

The next round will try to minimize the boundary set further and formalize composition, downgrade behavior, provenance laundering resistance, selective disclosure, and lossless/lossy mappings across existing carrier standards.
