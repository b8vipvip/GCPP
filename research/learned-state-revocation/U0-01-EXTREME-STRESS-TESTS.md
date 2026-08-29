# U0-01 — 极端压力测试 / Extreme Stress Tests

> 状态：Research vectors / 非规范性

## T1 — Source Deleted, Embedding Survives

D 的源记录已 erase，但由 D 产生的 embedding/vector entry 仍可检索。

预期：`SOURCE_ERASURE_INCOMPLETE_FOR_RETRIEVAL_STATE`；需要 vector/index remedy。

## T2 — RAG Removed, Parametric Memory Remains

D 已从 RAG store 删除，但基础/微调模型仍能稳定复现 D 的敏感事实。

预期：`RAG_REMOVAL_DOES_NOT_PROVE_MODEL_UNLEARNING`。

## T3 — Model Unlearned, Cached Outputs Survive

模型 M 已完成符合定义的 unlearning，但旧 response cache / summary / export 中仍有 D。

预期：模型状态完成不代表 derivative artifacts 完成；缓存仍需独立 remedy。

## T4 — Synthetic Derivative Trains Downstream Model

D -> M1 -> synthetic dataset S -> M2。

在 D 撤销时：

- 是否 S 必须 erase？
- M2 是否必须 unlearn？

不能只由 `derivedFrom` 决定。

预期：`POLICY/PROFILE_DECISION_REQUIRED`，并保留下游通知状态。

## T5 — Diffuse Statistical Influence

D 是百万训练样本之一，对模型总体统计模式有微小影响，但无明确可恢复内容。

若任何 lineage 都强制删除，将导致无限级联。

预期：`NO_AUTOMATIC_REMEDY_FROM_LINEAGE_ALONE`；需要 materiality/threat-model/policy criterion。

## T6 — Public Disclosure Already Happened

模型过去把 D 的敏感事实公开发布到外部不可控网络。

预期：不能声称 `ERASED_FROM_WORLD`。可执行的只是停止未来处理、删除受控副本、撤回/通知 where possible，并记录 `IRREVERSIBLE_EXTERNAL_DISCLOSURE`。

## T7 — Offline Backup

D 存在于离线备份，当前无法逐项删除，但备份按 30 天轮换销毁且恢复流程会重新执行 tombstones。

预期：`DEFERRED_ERASURE_WITH_CONTROLLED_RETENTION` 或政策例外，而不是虚假 immediate erase。

## T8 — Malicious Downstream Participant Drops Revocation

A 把 D 传给 B，B 又生成 S 给 C。A 撤销 D，B 不转发。

预期：协议无法凭空控制恶意 B；需要可审计 downstream relationships / periodic validity checks / external enforcement。结果不能标记 global complete。

## T9 — Process Receipt Without Outcome Guarantee

Provider 提供“已运行 unlearning job #123”的签名 receipt，但算法只是 heuristic fine-tune。

预期：`PROCESS_EXECUTED != CERTIFIED_FORGETTING`。

## T10 — Approximate Unlearning Under Explicit Threat Model

模型通过指定 MIA/behavioral tests，但没有 counterfactual equivalence proof。

预期：允许 `VERIFIED_UNDER_TEST_PROFILE P`，禁止升级为 universal forgotten。

## T11 — Legally Retained Audit Log

业务数据必须 erasure，但最小 audit record 因法律义务需保留且访问严格限制。

预期：`PARTIAL_REMEDIATION_WITH_DECLARED_EXCEPTION`，不能把 exception 当 failure 或假装全部 erased。

## T12 — Re-Ingestion After Forgetting

D 已从 M unlearn，但后续 crawler/RAG sync 又重新摄入 D。

预期：forget set/tombstone/usage revocation 必须影响未来 ingestion；`UNLEARNING != FUTURE_REINGESTION_PREVENTION`。

## T13 — Federated / Replicated Learned State

全局模型已更新，但多个 edge/client checkpoint 仍包含旧 influence，未来可能重新聚合。

预期：需要 replica/federated scope reconciliation；global receipt 不能忽略 stale replicas。

## T14 — Unknown Downstream Universe

组织知道 B/C 两个 downstream consumer，但后来发现 D 也曾进入未知 D4。

预期：

```text
KNOWN_REMEDIATION_COMPLETE
!=
UNIVERSAL_ERASURE_COMPLETE
```

完成声明必须 scope-bounded。

## T15 — Derived Artifact Contains No Recoverable Target

D 被用于计算一个大规模匿名聚合统计 G，现有验证表明无法合理恢复/关联到 D。

预期：不能仅因历史 derivation 自动销毁 G；remedy applicability 由明确 policy/materiality criterion 决定。

## T16 — One Derivative Contains Exact Copy

另一个 synthetic artifact S2 虽然经生成模型产生，但包含 D 的逐字敏感片段。

预期：与 T15 相反，transformation 名称相同并不意味着 remedy 相同；需看 target exposure/materiality evidence。

## 候选不变量

```text
U1 SOURCE DELETION != LEARNED INFLUENCE REMOVAL
U2 REMEDY IS STATE-SPECIFIC
U3 LINEAGE != REMEDY OBLIGATION
U4 FUTURE-USE REVOCATION != PAST-STATE REMEDIATION
U5 PROCESS RECEIPT != OUTCOME GUARANTEE
U6 PROOF SCOPE MUST NOT AMPLIFY
U7 UNLEARNING != REINGESTION PREVENTION
U8 KNOWN REMEDIATION != UNIVERSAL ERASURE
U9 SOME DISCLOSURES ARE IRREVERSIBLE
U10 EXCEPTIONS / DEFERRED REMEDIATION MUST BE EXPLICIT
```

## 第一轮反证目标

尝试只用：

```text
policy decision
+ known provenance graph
+ state class
+ remedy profile
+ evidence/receipt class
+ explicit unknown/exception
```

安全分类全部 16 个场景。

如果成功，只说明 U0 可以被通用机制表达；下一轮仍需测试跨供应商 remedy vocabulary 是否真的需要独立公共框架。