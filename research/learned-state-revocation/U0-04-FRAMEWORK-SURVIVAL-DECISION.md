# U0-04 — Framework Survival Decision / 框架层存活判定

> 状态 / Status: **Research Decision / 非规范性**  
> 日期 / Date: 2026-08-29

## 1. 需要修正的不是 R2 结论，而是研究门槛的解释

U0-R2 已正确证明：

```text
INDEPENDENT U0 WIRE PROTOCOL / POLICY LANGUAGE:
NOT JUSTIFIED
```

这个结论保持不变。

但项目最初寻找的目标并不限定为新 transport / token / ledger；目标是寻找：

> **未来 AI 的系统性难题，是否必须依赖一个跨组织公共框架或协议语义才能可靠解决。**

按这个更准确的门槛，U0 仍然存在一个尚未被现有标准自然统一的框架级问题。

## 2. 为什么 U0 与普通 ODRL Profile 不完全等价

现有标准分别提供：

```text
DPV                  -> privacy/delete/erase vocabulary
ODRL / Gaia-X DUA    -> rights, duties, downstream usage/revocation
PROV                 -> known derivation relationships
Machine Unlearning   -> model-specific influence-removal methods
PoU / certified removal -> specific forgetting evidence
VC/JWS/COSE          -> generic evidence carriers
```

但它们并没有共同定义一个跨 AI 系统的答案：

```text
Given obligation O over target information D,
for each affected AI state S,
what remediation objective applies,
what evidence is sufficient,
and what may a verifier safely conclude?
```

## 3. 最新研究进一步确认“forget”不是一个统一操作

2026 年 machine-unlearning 研究正在显著分化：

- model weights、adapters、RAG/index、federated state、graph/temporal state 的删除保证不同；
- post-transformation（如 quantization、redeployment）可能使先前 forgetting 证据失效，需要重新验证；
- “unlearning” 一词本身正在被批评为过度使用，因为 retraining-equivalence、suppression、editing、refusal 等目标不是同一种保证；
- proof-of-unlearning 可以证明特定算法/数据集条件，但不能自动证明整个 AI application 的所有状态均已 remediation。

因此公共框架的价值可能不是创造新的 unlearning algorithm，而是阻止 **guarantee semantic collapse**。

## 4. 新的核心问题：Remediation Objective Interoperability

同一个上层触发：

```text
DELETE / ERASE / REVOKE / CORRECT / STOP FUTURE USE
```

进入不同状态后可能对应：

```text
Raw record       -> erase/destruct
Embedding        -> delete + index reconciliation
RAG cache        -> invalidate/delete
Knowledge store  -> remove + prevent re-ingestion
Adapter          -> unlearn/retrain/replace
Model weights    -> certified / approximate unlearning under profile
Synthetic data   -> delete/retract/quarantine depending policy/materiality
Downstream model -> notify + evaluate/remediate under downstream profile
Public output    -> retract where possible; irreversible disclosure remains
Backup           -> deferred erasure / retention exception
```

一个公共框架需要描述的是这些**不同保证之间的边界**，而不是统一成 `forgotten=true`。

## 5. 当前最强候选不变量

```text
R1 ONE REVOCATION TRIGGER != ONE UNIVERSAL REMEDY
R2 REMEDY OBJECTIVE MUST BE STATE-CLASS SPECIFIC
R3 PROCESS COMPLETION != OUTCOME GUARANTEE
R4 OUTCOME GUARANTEE MUST NAME ITS THREAT / TEST / REFERENCE MODEL
R5 REMEDIATION OF ONE STATE != REMEDIATION OF ALL DERIVATIVES
R6 FUTURE-USE BLOCK != PAST-INFLUENCE REMOVAL
R7 RETRAINING-EQUIVALENCE != BEHAVIORAL SUPPRESSION
R8 KNOWN-SCOPE COMPLETION != UNIVERSAL FORGETTING
R9 POST-TRANSFORMATION MAY INVALIDATE PRIOR FORGETTING EVIDENCE
R10 IRREVERSIBLE DISCLOSURE MUST REMAIN REPRESENTABLE
```

## 6. Framework Survival Criterion

U0 只继续为公共框架候选，不再考虑自有 transport。

下一阶段必须证明：

1. 至少三个不同 AI state classes 对同一 erasure obligation 需要不可互换的 completion semantics；
2. 现有标准若各自独立使用，会产生可复现的 false-completion / guarantee-confusion；
3. 一个统一的 remediation objective + evidence contract 能机器阻止这些误判；
4. 该 contract 可以复用 ODRL/DPV/PROV/VC，而不依赖某个供应商；
5. 该问题在 privacy、copyright、安全纠错、知识撤回等多个领域重复出现。

若这些条件不成立，则 U0 最终仍降级成普通 Profile。
