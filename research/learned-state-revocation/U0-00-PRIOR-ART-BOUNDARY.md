# U0-00 — Prior Art Boundary / 现有工作边界

> 状态：Research only / 非规范性

## 1. 数据删除/擦除语义已有成熟 vocabularies

W3C DPV 已区分：

```text
Delete   — 逻辑删除，可能可恢复
Destruct — 处理到不再存在/不可修复
Erase    — 从存在中移除，不可检索
```

并包含 DataDeletionPolicy / DataErasurePolicy 等概念。

因此 U0 不创造“erase”这个概念。

## 2. 跨组织 usage-control 与 cascading revocation 已存在

IDS/ODRL 可表达：

```text
use data then delete
attach policy when distributing to third party
runtime usage enforcement
post-condition deletion
```

Gaia-X Data Usage Agreement 更直接具有：

```text
Cascading Agreement and Right to Oblivion
```

允许数据被组成新 Data Product 后递归控制 usage agreement 和 revocation。

因此：

```text
revocation notification propagation
```

本身也不是 U0 创新。

## 3. 单模型 machine unlearning / certified removal 已有理论

Certified removal 把“移除训练数据影响”定义为：更新后的模型与从未见过该数据、重新训练得到的模型在定义意义上不可区分。

后续研究已有 cryptographic/verifiable unlearning：证明模型更新流程、forget item 不在新训练集、被忘记项不会重新加入等。

所以 U0 不创造 unlearning algorithm / proof-of-unlearning cryptography。

## 4. 当前断层位于“同一撤销义务，不同状态需要不同 remedy”

现实 AI 系统中，同一信息可能同时存在于：

```text
source record
backup/log
exact copy
embedding
vector index
retrieval cache
summary/generated artifact
adapter/fine-tune
model weights
federated state
synthetic dataset
downstream model
public output
```

这些状态的“忘记”操作并不同构：

```text
raw row          -> erase/destruct
embedding        -> delete vector + rebuild affected index state
cache            -> invalidate/delete
RAG source       -> remove retrieval accessibility
adapter          -> unlearn/retrain/replace
model weights    -> certified/approximate unlearning or retraining
synthetic output -> policy-dependent delete/retract/quarantine
public disclosure-> cannot make history unhappen; only stop future processing/retract where possible
backup           -> scheduled erasure / cryptographic deletion / retention exception
```

所以：

```text
ONE REVOCATION TRIGGER != ONE UNIVERSAL REMEDY
```

## 5. 关键问题之一：provenance relation 不等于 remedy obligation

若：

```text
X derivedFrom D
```

不能自动推出：

```text
D revoked => X MUST be erased
```

否则会造成无限或荒谬级联：一个训练样本理论上影响整个模型，模型又影响海量输出。

是否需要 remedy 取决于：

```text
legal/policy basis
processing purpose
transformation type
recoverability / leakage risk
material influence criterion
applicable threat model
retention exception
```

因此 U0 必须把：

```text
lineage discovery
```

与：

```text
remedy applicability decision
```

分离。

## 6. 关键问题之二：proof scope 不可放大

```text
source_deleted
```

不能显示为：

```text
system_forgotten
```

```text
RAG_index_removed
```

不能显示为：

```text
model_weights_unlearned
```

```text
unlearning_process_executed
```

也不必然等于：

```text
counterfactual_forgetting_guaranteed
```

候选原则：

```text
ERASURE RECEIPT MUST BE STATE- AND GUARANTEE-SCOPED
```

## 7. 当前最有希望的 U0 缺口

不是 transport，而可能是一个跨标准的 **Revocation Remedy Semantics**：

```text
Revocation Trigger
    ↓
Known Derivative Discovery
    ↓
Remedy Applicability per state/profile
    ↓
State-specific Remedy
    ↓
Evidence / Receipt
    ↓
Downstream obligation propagation
    ↓
Scoped completion / unresolved / exception
```

但它仍可能被：

```text
Gaia-X/ODRL policy
+
PROV graph
+
DPV vocabulary
+
state-specific unlearning profiles
+
generic credentials/receipts
```

完全吸收。

U0 必须主动尝试证明这一吸收路线足够。