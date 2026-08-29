# GCPP 开发进度与完整交接上下文 / GCPP Development Status and Full Handoff Context

> **默认语言：简体中文（zh-CN）**，英文摘要在后。  
> **Default language: Simplified Chinese (zh-CN)**, followed by an English summary.  
> 最后更新 / Last updated: **2026-08-29**

# 简体中文

## 1. 当前一句话状态

> **GCPP 正从 0.2 的“C2PA 兼容生成式来源扩展/Profile”进一步进入第一性原理架构研究阶段：不再围绕 C2PA/SPDX/CycloneDX 的短期功能空白做标准竞赛，而是研究信息关系、来源连续性、Evidence 边界和可长期存在的最小协议原语。**

## 2. 仓库状态

- 仓库：`b8vipvip/GCPP`
- 默认分支：`main`
- 0.2 架构重构 PR：**#5**，已合并；
- 0.2 merge commit：`29195b94ec87a3603f8fb0c61db3cef7cc5c9200`；
- 当前第一性原理研究分支：`research/fundamental-protocol-architecture`；
- 本阶段目标：更新研究纲领、Core 架构纪律、Roadmap 和现有标准边界后合并回 `main`。

## 3. 为什么再次调整方向

0.2 已正确完成第一轮收敛：GCPP 不再重新发明 C2PA 的 Manifest、Claim、Hard/Soft Binding 等成熟能力。

新的研究结论进一步指出：

> 不能把“其他标准暂时没做什么”当成 GCPP 的长期研发方向。

否则 GCPP 会陷入：

```text
external standard releases feature
        ↓
GCPP searches next gap
        ↓
repeat
```

这种模式无法产生稳定的公共协议价值。

因此研发方法改为：

```text
真实长期问题
-> Abstraction
-> Invariant
-> Protocol Primitive
-> Evidence
-> Implementation / Adapter
```

## 4. 当前核心研究问题

GCPP 研究问题从：

```text
Who generated this file?
```

提升为：

```text
What information relationships survive transformation?
What evidence can verify those relationships?
What exactly does each item of evidence prove?
```

暂称这一长期问题为：

**Provenance Continuity / 来源连续性**。

## 5. 当前第一性原理研究假设

候选最小模型：

```text
Entity
Relation
Continuity
Evidence
```

含义：

- `Entity`：参与来源关系的主体或信息对象；
- `Relation`：对象之间的来源、转换、贡献或影响关系；
- `Continuity`：经过复制、编辑、转换后关系还可以验证到什么程度；
- `Evidence`：支持某个关系、身份、连续性或其他事实的证据。

注意：这仍是 **research hypothesis**，尚未正式冻结为 GCPP 0.3 Core。

## 6. 与旧 Core 模型的关系

0.2 使用：

```text
Identity
Provenance
Integrity
Evidence
```

下一阶段需要比较：

```text
Identity / Provenance / Integrity / Evidence
```

与：

```text
Entity / Relation / Continuity / Evidence
```

之间的抽象能力。

当前重点问题：

- `Identity` 是否只是 Entity 的可验证属性；
- `Provenance` 是否应该表达成 evidence-backed relation graph；
- `Integrity` 是否不足以涵盖翻译、摘要、片段继承等 transformation；
- `Continuity` 是否能够更一般地表达 exact / segment / transform / historical 等状态。

## 7. 已固定的架构纪律

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
WATERMARK != AUTHENTICATION
SIMILARITY != PROVENANCE
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
OUTPUT_PROVENANCE != MODEL_LINEAGE
REGULATORY_LABEL != CRYPTOGRAPHIC_IDENTITY
ABSENCE_OF_EVIDENCE != EVIDENCE_OF_ABSENCE
```

同时新增：

- GCPP **不进行标准发布时间竞赛**；
- “现有标准没有某字段”不足以创建 Core primitive；
- partial / mixed / transformed / unknown / conflicting evidence 都是一等状态；
- Core 不绑定 C2PA、SPDX、CycloneDX、PKI、Hash、水印、区块链、AI 架构或监管体系；
- 事实层与 Policy / 法律 / 版权 / 真实性判断严格分离；
- Public provenance 默认不得要求用户账号、IP、设备指纹、raw prompt 或完整私有训练数据。

## 8. 新增关键文件

### Fundamental research

- `research/FUNDAMENTAL-PROTOCOL-RESEARCH.md`
  - 第一性原理研究纲领；
  - 五个基础问题；
  - Provenance Continuity；
  - Core 晋级测试；
  - 真实行业验证要求。

### Architecture

- `spec/GCPP-ARCHITECTURAL-PRINCIPLES.md`
  - Problem-first 研发纪律；
  - 不做标准时间竞赛；
  - Entity / Relation / Continuity / Evidence 研究模型；
  - graph-first provenance；
  - partial/mixed/unknown；
  - Evidence 不越权；
  - privacy / algorithm independence。

## 9. 已同步修改的文件

- `README.md`
  - 项目首页从“生成式来源扩展集合”改为“公共协议研究项目”；
  - 明确 Provenance Continuity 研究问题；
  - 明确现有标准位于 Adapter/Implementation 层。

- `spec/GCPP-CORE.md`
  - 状态改为 Fundamental Architecture Review；
  - 旧 Core 与新研究模型并行比较；
  - GID、Model Assurance、Lineage level 等重新进入证据化复审；
  - 引入 evidence-backed relation graph 和 Continuity 研究。

- `spec/GCPP-C2PA-ALIGNMENT.md`
  - 从 `C2PA-first research direction` 改成 `C2PA as important current adapter/evidence carrier`；
  - C2PA 功能边界不再决定 GCPP research agenda。

- `ROADMAP.md`
  - 重新组织为 F0–F6 第一性原理研究阶段 + P0–P4 协议化/互操作阶段；
  - Durable Text、Generation Execution、Model Lineage、监管 Adapter 保留为需要重新分类验证的实验方向。

## 10. 现有方向的处理

### Durable Text / RecoveryLocator

继续保留，但目标从“开发 GCPP 自有文本水印”改为：

> 解决 provenance carrier 在真实传播、复制、平台净化和编辑后丢失的恢复问题。

如果其他算法更好，GCPP 直接作为 Profile/Evidence 接入。

### GenerationID

进入复审。

如果只是另一个 Asset UUID，则删除 Core 候选；如果真实多输出/streaming/Agent 场景需要独立 `Generation Execution Identity`，再通过案例证明。

### Model Assurance

线性等级改为 Presentation/Policy convenience 的候选。

底层优先研究正交 Evidence Vector。

### Model Lineage

继续保持：

```text
OUTPUT_PROVENANCE != MODEL_LINEAGE
```

重点从通用 `trained-on/fine-tuned-from` 转向：

- teacher distillation；
- synthetic-data generation；
- reasoning traces；
- preference/evaluation signal；
- dataset commitment；
- training-run attestation；
- teacher attestation；
- authorization evidence；
- watermark indication；
- independent/confidential audit。

普通 AI BOM / 数据集清单 / 依赖描述优先映射 SPDX/CycloneDX/C2PA 等已有体系。

### Regulatory adapters

继续推进，但监管标识只作为 regulatory observation / evidence，不升级为 cryptographic provenance 或真实性结论。

## 11. 当前 P0 研究任务

### P0.1 — Information Object

回答什么东西才是最小可参与 provenance relation 的 Entity。

### P0.2 — Relation Model

区分：

```text
historical relation
structural derivation
information contribution
causal influence
```

并验证 copy / quote / summarize / translate / combine / train / distill 等关系是否需要统一原语或不同语义。

### P0.3 — Provenance Continuity

研究：

```text
exact
structural
segment
transform
semantic
causal
historical
unknown
```

这些维度是否真正必要、如何证明、哪些不能被协议客观验证。

### P0.4 — Evidence Capability / Limitation

为 signature、hash、watermark、similarity、attestation、commitment、audit 等建立“能证明 / 不能证明”矩阵。

### P0.5 — Real-world problem corpus

建立真实行业案例，不只用理想化 demo：

- 新闻；
- 科研；
- Agent；
- 混合文档；
- 训练/蒸馏；
- 内容平台传播；
- 代码；
- 跨法域监管。

## 12. 当前 Issues

历史 Issues 仍需根据新架构重新解释：

- **#2** — specification license / contributor IPR policy：继续有效，公共标准必要条件；
- **#3** — C2PA-based Internet Profile：降级为实现/互操作 Profile，不再决定 Core 方向；
- **#4** — RecoveryLocator benchmark：继续作为实验研究；
- **#6** — GB 45438 Adapter：继续作为监管 Adapter；
- **#7** — Model Lineage：继续，但需从线性 assurance level 转向 Evidence Vector，并减少与通用 AI BOM 重复。

建议后续新增独立 Fundamental Research Issues，而不是继续把所有研究塞进 #3/#7。

## 13. 下一阶段执行顺序

```text
F0 First-principles questions
        ↓
F1 Relation model
        ↓
F2 Continuity model
        ↓
F3 Evidence semantics
        ↓
F4 Partial / conflict / time
        ↓
F5 Privacy-preserving provenance
        ↓
F6 Real-world validation
        ↓
Core candidate selection
        ↓
Adapters / Profiles / Reference verifier
```

不要在 F0–F3 尚未建立稳定抽象前，为扩充规范表面面积而大量增加 assertion。

## 14. 新聊天启动提示

> 继续研究和开发 `https://github.com/b8vipvip/GCPP.git`。先读取 `DEVELOPMENT_STATUS.md`、`research/FUNDAMENTAL-PROTOCOL-RESEARCH.md`、`spec/GCPP-ARCHITECTURAL-PRINCIPLES.md`、`spec/GCPP-CORE.md` 和 `ROADMAP.md`。当前 GCPP 已明确不与 C2PA/SPDX/CycloneDX 做功能和发布时间竞赛。使用 Problem -> Abstraction -> Invariant -> Protocol Primitive -> Evidence -> Implementation/Adapter 的研究方法。优先研究 Information Object、Relation、Provenance Continuity、Evidence capability/limitation 和真实行业 problem corpus；现有标准作为 Adapter/Evidence carrier，而不是研究议程来源。

---

# English

GCPP has entered a first-principles architecture research phase beyond the 0.2 C2PA-compatible profile realignment.

The project is no longer driven by temporary feature gaps in C2PA, SPDX, CycloneDX, or other standards. The research order is now:

```text
real long-term problem
-> abstraction
-> invariant
-> protocol primitive
-> evidence
-> implementation / adapter
```

The principal research topic is **provenance continuity**, with a current hypothesis of `Entity / Relation / Continuity / Evidence`. This model is not yet frozen as a future Core.

The immediate tasks are information-object abstraction, relation semantics, continuity under transformation, evidence capability/limitation modeling, partial/mixed/conflicting/time semantics, privacy-preserving provenance, and validation against real industry cases.
