# A0-15 — R4 终极攻击压力测试 / Ultimate Stress Tests

> 状态 / Status: **Research / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## R4-T1 — Visible Authority Equivocation

同一 authority、同一 exclusive relationship、同一有效版本，对两个 successor 签发冲突决定：

```text
Q: R -> B
Q: R -> C
```

若两份签名均可见：

```text
CONFLICT_SIGNED_EQUIVOCATION
```

不需要猜谁是真 successor。

## R4-T2 — Isolated Equivocation

V1 只看到：

```text
Q: R -> B
```

V2 只看到：

```text
Q: R -> C
```

两者签名都合法。

单个 verifier 的安全结论只能是：

```text
LOCALLY_VALID_GLOBALLY_UNKNOWN
```

除非存在 gossip / witness / transparency cross-check / consensus。

## R4-T3 — Unknown Authority Set

已知：

```text
Bank ACK
Contract ACK
```

但系统无法证明这就是完整 relationship-authority universe。

禁止：

```text
GLOBAL_SUCCESSION_COMPLETE
```

允许：

```text
COMPLETE_WITHIN_DECLARED_SCOPE(S,R,E)
```

否则：

```text
INCOMPLETE_UNKNOWN_AUTHORITY_SET
```

## R4-T4 — Dynamic Authority Set / Policy Epoch

transition 在 policy epoch 7 准备；commit 前 authority membership / trust policy 更新到 epoch 8。

旧决定不得无条件 commit：

```text
REJECT_STALE_POLICY_EPOCH
```

## R4-T5 — No Shared Clock

Authority A 时间戳 10:01，Authority B 时间戳 09:59，不足以建立全局顺序。

如业务需要 ordering，应依赖：

```text
version
epoch
causal reference
consensus sequence
```

而不是隐式 wall-clock ordering。

预期：

```text
ORDER_BY_VERSION_NOT_WALLCLOCK
```

若没有可验证顺序材料：

```text
ORDER_UNRESOLVED
```

## R4-T6 — Network Partition

需要 3 个 mandatory authority ACK，但分区期间只得到 2 个。

安全优先：

```text
PENDING_PRESERVE_SAFETY
```

不能为了 continuity liveness 自动降低 quorum。

## R4-T7 — Malicious Coordinator

Coordinator 声称：

```text
COMMITTED
```

但缺少 mandatory participant 的签名 receipt。

若 participant-signed evidence 是 completion 条件：

```text
NO_FALSE_COMMIT
```

Coordinator 可以阻塞/审查，但不能伪造缺失 authority decision。

## R4-T8 — Transparency Split View

Transparency service 向两个观察者发布不一致的 signed tree heads / histories。

单一 inclusion proof 不足以证明全局一致视图。

预期：

```text
SPLIT_VIEW_REQUIRES_GOSSIP_OR_WITNESS
```

如果两份不一致 signed view 被比较，则产生可验证 misbehavior evidence。

## R4-T9 — Different Verifier Trust Policies

Verifier V1 接受 Authority Q；V2 不接受 Q。

同一合法 credential：

```text
V1 -> ACCEPT
V2 -> REJECT / UNKNOWN
```

这是：

```text
POLICY_DIVERGENCE_NOT_PROTOCOL_CONFLICT
```

公共协议不应强迫所有 relying party 拥有相同 trust policy。

## R4-T10 — Late-Discovered Relationship

系统曾对已知集合声明：

```text
succession complete for {R1,R2}
```

后来发现先前未知 R3。

正确解释：

```text
PRIOR_COMPLETION_WAS_SCOPE_LIMITED
```

而不是历史声明“失效”，更不是宣称原先具有 universal completeness。

## R4-T11 — Finite Byzantine Authority Committee

若业务明确有固定 committee：

```text
n = 4
f = 1
```

并采用 BFT policy：

```text
2f+1 = 3 matching decisions
```

则 generic quorum/BFT 可以决定 committee-level outcome。

预期：

```text
QUORUM_ACCEPT
```

该机制不是 Agent-specific。

## R4-T12 — Indispensable Authority Gone

唯一能够转让关系 R 的 authority Q 永久消失，且此前没有 recovery delegation。

正确结果：

```text
UNRESOLVED_NO_AUTHORITY
```

禁止新协议自行生成：

```text
SUCCESSOR_VERIFIED
```

## 跨向量安全属性

R4 只保留以下通用安全要求：

```text
SIGNED != TRUSTED
LOCAL_VALIDITY != GLOBAL_NON-EQUIVOCATION
KNOWN_SET != COMPLETE_UNIVERSE
WALL_CLOCK != CAUSAL_ORDER
PARTITION MAY BLOCK LIVENESS
COORDINATOR != AUTHORITY
TRANSPARENCY RECEIPT != GLOBAL CONSISTENCY BY ITSELF
POLICY DIVERGENCE != PROTOCOL FAILURE
NO AUTHORITY => NO TRANSFER
```

这些目前均未证明为 AI Agent 特有原语。

---

# English

R4 defines twelve ultimate Byzantine/open-world vectors: visible and isolated equivocation, unknown/dynamic authority sets, no shared clock, partitions, malicious coordinators, transparency split views, verifier-policy divergence, late-discovered relationships, finite Byzantine committees, and permanently unavailable indispensable authorities. The expected safe outcomes deliberately include UNKNOWN, PENDING and UNRESOLVED.