# GCPP 路线图 / GCPP Roadmap

> 默认语言：简体中文（zh-CN） / Default language: Simplified Chinese (zh-CN)

# 简体中文

## 总原则

GCPP 路线图不再以“先补齐 C2PA/SPDX/CycloneDX 的功能空白”为主线，也不以成为更早、更全的标准为目标。

后续研发采用：

```text
Problem
-> Abstraction
-> Invariant
-> Protocol Primitive
-> Evidence
-> Implementation / Adapter
```

只有经过真实问题验证、跨实现仍有意义的概念，才可能进入 Core。

## Phase F0 — 第一性原理研究

目标：回答五个基础问题。

1. 什么是协议层最小的 `Information Object`？
2. 什么叫两个对象之间存在可验证来源关系？
3. 信息转换以后，什么叫来源关系仍然连续？
4. 不同 Evidence 能证明什么、不能证明什么？
5. 最小公共协议原语是什么？

当前研究假设：

```text
Entity
Relation
Continuity
Evidence
```

退出条件：每个候选原语都能通过 `research/FUNDAMENTAL-PROTOCOL-RESEARCH.md` 中的 Core 晋级测试。

## Phase F1 — Information Relation Model

研究来源图，而不是单链历史。

需要解决：

- 多 parent / 多 contributor；
- copy / quote / extract / summarize / translate / combine 等不同关系的技术语义；
- 历史关系、信息贡献与因果影响的边界；
- relation 的 subject / object / scope；
- relation 是否可直接验证，还是只能由声明和证据共同支持；
- 冲突 relation 与 unknown relation。

硬约束：不把版权、侵权、真实性、责任或合法性编码成 relation 技术事实。

## Phase F2 — Provenance Continuity Model

研究内容在变化后仍能保持何种可验证关系。

候选研究维度：

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

需要特别研究：

- copy/paste；
- 删除/插入/替换；
- 拼接；
- 翻译；
- 摘要；
- 多轮 AI rewrite；
- 人工与 AI 混合编辑；
- 多输入生成；
- 训练/蒸馏这种非资产级影响关系。

退出条件：能够明确区分“关系已验证”“部分验证”“只有声明”“未知”“证据冲突”“无法从当前证据判断”。

## Phase F3 — Evidence Semantics

建立 Evidence capability / limitation 模型。

至少覆盖：

- digital signature；
- exact hash binding；
- soft binding / watermark；
- fingerprint / similarity；
- timestamp / transparency receipt；
- identity credential；
- process attestation；
- hardware / execution attestation；
- dataset commitment；
- confidential audit；
- probabilistic lineage indication；
- future evidence。

每类 Evidence 必须定义：

```text
what it proves
what it does not prove
scope
assumptions
failure modes
issuer / observer
validity / time context
```

## Phase F4 — Partial / Mixed / Conflict / Time

把真实世界的不完整性作为一等状态。

研究：

- authenticated coverage；
- 多来源片段；
- transformed coverage；
- unattributed regions；
- conflicting claims；
- evidence supersession；
- revocation / correction；
- temporal validity；
- historical evidence 与 current state 的区别。

## Phase F5 — Privacy-preserving Provenance

目标：允许：

```text
prove relation
without disclosing all underlying data
```

研究承载方案包括 commitment、selective disclosure、confidential audit、TEE、ZK、transparency receipt 等，但 Core 不绑定任何一种。

重点场景：

- 私有训练集；
- 企业 Agent；
- 医疗/法律/科研；
- 商业秘密；
- 用户 prompt / account 数据；
- 模型蒸馏授权证明。

## Phase F6 — Real-world Problem Validation

不允许只用理想化示例验证协议。

至少选择以下真实行业场景建立 problem corpus：

1. 新闻转载、摘要、引用与纠错；
2. 科研论文、数据、计算结果与结论链；
3. AI Agent 多工具、多模型、多资料决策过程；
4. 人类 + AI 混合文档；
5. 模型训练、合成数据、蒸馏与评测；
6. 内容平台跨平台传播与来源丢失；
7. 代码生成、人工修改与依赖来源；
8. 跨法域 AI 标识与凭证验证。

退出条件：候选原语能解决多个场景中的共同问题，而不是为单一案例定制。

## Phase P0 — Core Candidate Selection

只有完成 F0–F6 的研究后，才决定哪些概念进入下一版 Core。

候选可能包括：

```text
Entity
Relation
Continuity
Evidence
Evidence-backed Provenance Graph
Verification Vector
```

是否保留、改名、拆分或删除，由研究结果决定。

## Phase P1 — Existing Standards as Adapters

对成熟标准做互操作映射，而不是功能竞赛：

- C2PA；
- SPDX；
- CycloneDX；
- VC / DID / X.509；
- in-toto / attestation；
- SCITT / transparency systems；
- GB 45438；
- 其他监管或未来标准。

原则：已有事实表示优先复用；GCPP 只定义必要的跨标准语义。

## Phase P2 — Experimental Profiles

现有研究方向保留，但重新接受 Core/Profile/Adapter 分类审查：

### Durable Text / RecoveryLocator

继续 benchmark 低开销文本恢复机制，但成功标准是解决“来源信息在传播后丢失”的真实问题，而不是开发 GCPP 专有水印。

如果现有或未来算法表现更好，GCPP 应直接支持其作为 Evidence/Profile。

### Generation Execution

研究一次生成执行与多个输出之间是否存在独立于资产 ID 的长期语义需求。若无法证明，则不进入 Core。

### Model / Distillation Lineage

重点研究 teacher influence、synthetic-data、reasoning traces、授权证据、训练运行证明、独立审计和 probabilistic evidence。

普通 AI BOM、模型依赖、数据集清单等已有标准能够表达的内容不重复定义。

### Regulatory Adapters

继续研究中国 GB 45438 等法域要求，但监管标签与来源事实保持分离。

## Phase P3 — Reference Verification

当 Core Candidate 足够稳定后实现：

```text
multiple evidence inputs
        ↓
GCPP semantic normalization
        ↓
relation / continuity verification
        ↓
Verification Vector
        ↓
independent Policy layer
```

要求：

- machine-readable schema；
- test vectors；
- deterministic interpretation；
- conflicting evidence handling；
- no single global verifier dependency。

## Phase P4 — Interoperability and Public Standard Maturity

进入候选公共标准前至少需要：

- 清晰 specification license / contributor IPR policy；
- reference implementation；
- 至少两个独立实现；
- security/privacy review；
- algorithm agility / deprecation；
- versioned registries；
- reproducible conformance suite；
- 至少一个非项目作者控制的真实集成。

## 明确非目标

GCPP 不构建：

- 第二套 C2PA；
- 第二套 SPDX / CycloneDX；
- AI 功能竞赛清单；
- 全球 AI 审批中心；
- 通用 AI 检测器；
- 真相裁判；
- 版权/侵权自动裁判；
- 强制区块链；
- 用户追踪系统；
- 单一全球 verifier；
- 依赖某家 AI 厂商的专有协议。

---

# English

GCPP is moving to a first-principles research roadmap rather than a feature race with existing standards.

The research sequence is:

```text
Problem
-> Abstraction
-> Invariant
-> Protocol Primitive
-> Evidence
-> Implementation / Adapter
```

The fundamental phases study information objects, evidence-backed relations, provenance continuity under transformation, evidence capabilities and limitations, partial/mixed/conflicting/time semantics, privacy-preserving proofs, and validation against real industry problems.

Only after that research should GCPP select Core candidates. C2PA, SPDX, CycloneDX, identity systems, attestation systems, transparency systems, and regulations are treated primarily as interoperable implementation/adaptation layers rather than competitors.

Durable text recovery, generation execution, model/distillation lineage, and regulatory adapters remain active research directions, but each must justify whether it belongs in Core, a Profile, an Adapter, or only an implementation experiment.
