# U0-02 — R1 研究结论 / First-Round Findings

> 状态 / Status: **Research Findings / 非规范性**

## 1. R1 没有证明需要新 wire protocol

16 个首轮场景都可以先用通用的：

```text
policy decision
state classification
known dependency/provenance
state-specific remedy profile
scoped evidence/receipt
UNKNOWN / exception / deferred state
```

做出安全分类。

因此当前不应创建：

```text
Unlearning Blockchain
Forget Token
Global Erasure Certificate
AI Deletion Transport
```

## 2. 但 U0 与 A0/E0/C0 的残余结构不同

A0 最终可被分布式系统/关系 authority 分解；E0 可被 uncertainty/provenance/attestation 分解；C0 可被 contract/runtime-assurance 理论分解。

U0 目前出现的是两个成熟体系之间的**语义断层**：

```text
Usage / Rights / Revocation Layer
ODRL / DPV / Gaia-X / GDPR notification

               ?

Learned-State Remedy Layer
retrieval deletion / cache invalidation /
unlearning / retraining / certified removal /
replica reconciliation / downstream cleanup
```

上层能够说：

```text
“这个用途不再被允许 / 应执行 erasure”
```

下层必须回答：

```text
“对这个具体 AI state，什么动作才算满足这个义务？”
```

## 3. `delete` 对 learned state 不是充分语义

ODRL 的 `delete` 对 Asset 有成熟语义；DPV 也区分 delete/erase/destruct。

但：

```text
model weights
adapter
embedding index
RAG memory
synthetic dataset
federated checkpoints
```

不是同一种“copy”。

例如：

```text
Delete(source record)
```

不会自动执行：

```text
Unlearn(model)
```

反过来：

```text
CertifiedUnlearn(model)
```

也不会自动清除旧 cache/public export。

所以一个通用完成状态：

```text
forgotten=true
```

目前是不安全的。

## 4. 第一轮最强候选抽象：Remedy Contract

暂时只作为研究草图：

```text
Remedy Contract
  trigger / obligation
  target state class
  target subject/data scope
  applicable policy/profile
  required remedy class
  acceptable evidence class
  completion condition
  exception / deferred condition
  downstream propagation rule
  validity / re-ingestion prevention
```

重点不是新容器，而是：

> 相同撤销义务在不同 learned state 上如何得到可互操作、不可过度声明的 fulfillment semantics。

## 5. 为什么这仍可能只是 Profile

现有生态已经有足够多可重用原语：

```text
ODRL actions/policies
DPV privacy/AI vocabulary
Gaia-X DUA cascading revocation
PROV lineage
VC/JWS/COSE attestations
machine-unlearning certificates
proof-of-unlearning research
```

所以 U0-R2 必须尝试直接映射，而不是发明语法。

### 如果可以映射为

```text
ODRL/DPV obligation
+
PROV target graph
+
AI-remedy vocabulary extension
+
generic evidence credential
```

那么最合理结局是向 DPV/ODRL/Gaia-X 等上游贡献 AI learned-state remedy profile，而不是独立协议。

## 6. R2 生死问题

> **现有 policy/provenance/credential 体系，增加少量 AI-specific remedy vocabulary 后，是否已经足够表达“撤销义务 → learned-state remedy → state-scoped proof → downstream completion”？**

如果 YES：kill U0 independent protocol/framework。

如果 NO：必须明确指出缺失的是哪个不可由扩展 vocabulary/profile 表达的跨系统执行语义。
