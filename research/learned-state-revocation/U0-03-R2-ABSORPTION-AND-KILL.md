# U0-03 — R2 Absorption / Kill Decision

> 状态 / Status: **Research finding / 非规范性**

## 1. R2 结论

U0 指向一个真实且日益重要的问题：AI 系统的 erasure/remediation 必须覆盖 heterogeneous learned state，而不能只删源记录。

但当前证据仍不支持独立公共协议。

```text
INDEPENDENT U0 WIRE PROTOCOL / POLICY LANGUAGE:
NOT JUSTIFIED
```

## 2. 现有机制已经形成可行分解

```text
Revocation / right / obligation
    -> ODRL / DPV / Gaia-X DUA

Known derivative discovery
    -> PROV / ordinary lineage

AI state classification
    -> DPV AI / domain metadata

State-specific remedy semantics
    -> ODRL Profile extension
       (e.g. unlearn, rebuild-index, invalidate-cache)

Model-level forgetting evidence
    -> certified removal / proof-of-unlearning / evaluation profile

Evidence carrier
    -> VC / JWS / COSE / attestation

Cascading downstream obligation
    -> Gaia-X DUA / usage-control policy propagation

Completion
    -> scoped receipts + UNKNOWN / exception / deferred states
```

ODRL 的 Profile mechanism 明确允许社区增加新的 Action、Constraint 和语义，因此“AI unlearning/remedy action vocabulary”天然可以作为 Profile，而不是新 policy language。

## 3. 保留的重要安全原则

```text
SOURCE DELETION != LEARNED INFLUENCE REMOVAL
ONE REVOCATION TRIGGER != ONE UNIVERSAL REMEDY
LINEAGE != AUTOMATIC REMEDY OBLIGATION
PROCESS RECEIPT != FORGETTING OUTCOME PROOF
RAG REMOVAL != PARAMETRIC UNLEARNING
MODEL UNLEARNING != DERIVATIVE CLEANUP
UNLEARNING != REINGESTION PREVENTION
KNOWN REMEDIATION != UNIVERSAL ERASURE
```

## 4. 为什么不继续协议化

剩余困难主要是：

- machine-unlearning 算法质量；
- forgetting verification 的科学有效性；
- policy 对 material influence / exception 的定义；
- provider 是否诚实执行；
- unknown downstream discovery；
- irreversible public disclosure。

这些问题不能通过增加一个新的网络协议原语解决。

## 5. 推荐归宿

如未来继续使用 U0 成果，应优先作为：

```text
ODRL/DPV AI Learned-State Remedy Profile
unlearning evidence vocabulary
adversarial erasure conformance corpus
cross-standard mapping
```

并贡献给既有 data-space/privacy/AI-governance 生态，而不是建立独立协议栈。
