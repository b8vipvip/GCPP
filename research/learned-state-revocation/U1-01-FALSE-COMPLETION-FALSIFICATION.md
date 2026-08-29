# U1-01 — False-Completion Falsification / 虚假完成语义反证

> 状态 / Status: **Research experiment / 非规范性**  
> 日期 / Date: 2026-08-29

## 1. 研究问题

U1 第一轮不测试 unlearning 算法，而测试：

> 两个系统都诚实报告了自己做过的 remediation，但下游是否会因为把不同 guarantee 当成等价而产生 **false completion**？

最小安全策略：

```text
NO EXPLICIT SEMANTIC ENTAILMENT
=>
NO GUARANTEE UPGRADE
```

## 2. 12 个反例

### T1 — Retrieval Exclusion -> System-wide Forgetting

```text
retrieval_exclusion
↛
system_wide_forgetting
```

### T2 — Behavioral Suppression -> Parametric Unlearning

```text
behavioral_suppression
↛
parametric_influence_removal
```

### T3 — Process Executed -> Outcome Verified

```text
process_executed
↛
outcome_verified
```

### T4 — Model Remediated -> All Derivatives Remediated

```text
model_state_remediated
↛
all_derivatives_remediated
```

### T5 — Benchmark Forgetting -> Retraining Equivalence

```text
benchmark_profile_forgetting
↛
retraining_equivalence
```

### T6 — Source Erasure -> Re-ingestion Prevention

```text
source_erasure
↛
future_reingestion_prevented
```

### T7 — Pre-Transformation Proof -> Post-Transformation Proof

```text
pre_transform_verified
↛
post_transform_verified
```

### T8 — Known Scope Complete -> Universal Complete

```text
known_scope_complete
↛
universal_complete
```

### T9 — Partial + Exception -> Full Erasure

```text
partial_with_exception
↛
fully_erased_no_exception
```

### T10 — Internal Cleanup -> Reverse External Disclosure

```text
internal_cleanup_complete
↛
external_disclosure_reversed
```

### T11 — Exact Copy -> Erasure Applicable

这是首轮唯一显式允许的正向规则示例：

```text
exact_copy_detected
=>
erasure_applicable
```

但这里只表示 remedy applicability，不表示已经完成 erasure。

### T12 — Correction Obligation -> Deletion Obligation

```text
correction_obligation
↛
deletion_obligation
```

## 3. 首轮可执行结果

使用一个刻意极小的 entailment model：

- 默认无规则即不升级 guarantee；
- 仅加入研究用正向规则 `exact_copy_detected -> erasure_applicable`；
- 不实现新 policy language / protocol。

结果：

```text
12 / 12 matched expected
```

## 4. 这对 U1 是正面还是负面？

两面都是。

### 对“新复杂协议”不利

说明不需要全新的交易状态机、ledger 或 transport。

### 对“公共语义框架”反而提供支持

因为真正需要共同理解的可能就是一组稳定的：

```text
remediation objective classes
non-equivalence rules
allowed entailment rules
proof-scope requirements
invalidation/recheck rules
```

它们可以映射到 ODRL/DPV/PROV/VC，但如果每个供应商自己定义，`forgotten / deleted / unlearned / suppressed / retracted` 会继续互相冒充。

## 5. 下一轮必须证明的不是表达能力

ODRL Profile / RDF 显然可以“表达字段”。这不足以 Kill framework。

U1-R2 必须问：

> 是否存在真实跨供应商互操作场景，使得没有共同 remediation semantics 时，两个 schema-valid、各自 truthful 的系统仍会系统性产生安全/合规误判？

如果只是文档命名不统一，做 vocabulary 即可。

如果不同 guarantee 之间的错误替代会直接造成：

- 撤销义务被错误判定完成；
- 下游停止继续 remediation；
- 不再触发 recheck；
- 用户/监管方收到过强 deletion claim；
- 未来 re-ingestion 被遗漏；

则存在框架级 conformance 价值。
