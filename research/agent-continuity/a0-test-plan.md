# A0 Executable Test Plan / A0 可执行测试计划

> 状态 / Status: **Planned experiment surface / 非规范性**

A0 下一步把 13 个极端场景转成可执行 lifecycle-safety vectors，而不是继续只写概念文档。

## 统一输入模型（研究用）

每个 vector 至少包含：

```text
pre_state
transition
explicit_grants
explicit_revocations
external_effects
open_obligations
post_state_claims
expected_safe_inheritance
expected_violations
```

## 第一批 violation classes

```text
AUTHORITY_MULTIPLICATION
REVOKED_RIGHT_RESURRECTION
SPENT_RIGHT_RESURRECTION
EXTERNAL_EFFECT_REPLAY_RISK
IMPLICIT_PRIVILEGE_UNION
OBLIGATION_LOSS
REPUTATION_CLONING
UNPROVEN_SUCCESSOR
FALSE_FULL_CONTINUITY
STALE_INSTANCE_BINDING
```

## 首批 executable 场景优先级

### P0

1. `fork_authority_budget`
2. `rollback_revoked_capability`
3. `rollback_duplicate_payment`
4. `merge_privilege_union`
5. `provider_shutdown_successor`
6. `partial_state_loss_authority_suspend`

### P1

7. `key_rotation_legitimate_successor`
8. `memory_clone_not_identity`
9. `principal_transfer_scoped_authority`
10. `obligation_assignment_on_fork`
11. `reputation_non_cloning`
12. `runtime_migration_attestation_reset`
13. `model_replacement_assurance_reset`

## Falsification criterion

如果这些 vectors 可以完全由一个现成的 capability engine + event log + ordinary identity records 表达，并且不同实现自然得到同样结果：

> 不创建新的 Agent Continuity rule language。

如果不同系统在 lifecycle transition 上缺少共同语义，才进一步研究最小公共 transition contract。
