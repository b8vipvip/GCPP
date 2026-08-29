# U0 — Learned-State Revocation / 学习态撤销与遗忘互操作

> 状态 / Status: **Fundamental research — active, non-normative**  
> 分支 / Branch: `research/u0-learned-state-revocation`  
> 日期 / Date: 2026-08-29

## 中文

U0 研究的不是新的 machine-unlearning 算法，也不是新的数据删除 RPC。

核心问题：

> 当一条数据、授权或“允许继续使用其影响”的依据被撤销后，该撤销如何跨越异构 AI 派生状态传播，并被翻译成每种状态真正适用的补救动作（remedy），同时让下游能够验证“完成了什么、没有证明什么”？

典型派生链：

```text
Raw Data D
  ↓
copy / log
  ↓
embedding / vector index
  ↓
RAG cache / summary
  ↓
fine-tune / adapter
  ↓
model weights
  ↓
synthetic data
  ↓
downstream model
  ↓
public / external output
```

这些状态不能用一个 `DELETE=true` 统一处理。

候选安全边界：

```text
SOURCE DELETION != LEARNED INFLUENCE REMOVAL
RAG REMOVAL != PARAMETRIC UNLEARNING
MODEL UNLEARNING != DOWNSTREAM DERIVATIVE ERASURE
PROCESS RECEIPT != FORGETTING OUTCOME PROOF
DERIVED_FROM != AUTOMATIC ERASURE OBLIGATION
REVOCATION OF FUTURE USE != REVERSAL OF PAST DISCLOSURE
KNOWN DERIVATIVES != COMPLETE DERIVATIVE UNIVERSE
```

### U0 先尝试复用

```text
W3C DPV delete / erase / erasure policy
ODRL / IDS usage control
Gaia-X Data Usage Agreement + cascading right to oblivion
W3C PROV / lineage graph
ISO/IEC 8183 AI data lifecycle
machine unlearning / certified removal
proof-of-unlearning / attestation / VC / JWS / COSE
privacy-preserving proof mechanisms
```

### Kill Criteria

如果上述机制只需一个小型应用 Profile 即可：

1. 找到受影响的已知派生节点；
2. 按节点类型选择 remedy；
3. 收集对应 evidence/receipt；
4. 处理 UNKNOWN / exception / irreversible disclosure；
5. 向下游传播义务；

则不建立独立 U0 wire protocol。

只有当“学习态”产生一种现有 usage-control、provenance 和 unlearning 机制无法共同表达的稳定跨行业语义缺口时，才继续协议化。

## English

U0 studies interoperability of revocation and forgetting obligations across heterogeneous learned states. It does not invent an unlearning algorithm. The question is whether a revocation can be safely translated into state-specific remedies—delete, invalidate, rebuild, unlearn, retrain, quarantine, notify, retract—across raw data, retrieval state, learned parameters, synthetic derivatives and downstream models without making false claims of complete forgetting.