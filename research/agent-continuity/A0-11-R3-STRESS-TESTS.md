# A0-11 — R3 多权威继承压力测试 / Multi-Authority Succession Stress Tests

> 状态 / Status: **Research Tests / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## R3-T1 — Multi-Issuer Fork

```text
A -> fork -> B, C
Bank acknowledges B for spend authority
License authority acknowledges C for license
```

若应用没有要求这些关系必须绑定同一 successor，则这是合法 mixed outcome，而不是协议冲突。

若应用要求一个 successor 原子承接两项关系，则现有 atomic coordination 足够表达：

```text
prepare(bank, B)
prepare(license, B)
if all prepared -> commit
else -> abort / unresolved
```

结论：**目前被 generic atomic coordination 吸收。**

## R3-T2 — Obligation Double Assignment

同一 exclusive obligation 被 counterparty 同时确认给 B 与 C：

```text
Obligation O -> B
Obligation O -> C
```

安全答案来自 obligation authority 自己的 versioned state：

```text
single current obligor
or explicit joint/several semantics
```

若没有明确 joint semantics，双重 ACK 即 conflict。

结论：**authority-side concurrency control 可吸收。**

## R3-T3 — Successor Race

B/C 同时请求继承同一个 exclusive grant。

解决方式：

```text
relationship version / epoch
compare-and-swap
fencing token
```

先成功的 transition 提升 version，旧 version 请求失败。

结论：**传统并发控制吸收。**

## R3-T4 — Provider Dies Mid-Succession

分两种情况：

### provider 只是 coordinator

可通过：

```text
replicated/durable coordinator
participant receipts
recovery protocol
choreography
```

降低单点故障。

### provider 是不可替代 relationship authority

其决定尚未作出便消失：

```text
UNRESOLVED
```

是唯一诚实结果。

没有公共协议可以事后制造其授权。

结论：**coordinator failure 可吸收；authority disappearance 不可“解决”，只能正确暴露未决。**

## R3-T5 — Reputation Split

A fork 为 B/C。

Reputation issuer 可以：

```text
reissue B
reissue C
reference predecessor history
require reassessment
deny transfer
```

但不能由 Agent 自己复制 reputation。

这属于 issuer policy + credential reissue，不要求 succession transaction protocol。

结论：**大部分被 issuer semantics 吸收。**

## R3-T6 — Merge with Conflicting Duties

```text
A owes duty X
B owes duty Y
A+B -> C
```

若 X/Y 不兼容，generic coordinator 只能报告：

```text
CONFLICT
DENY
COMPENSATE
UNRESOLVED
```

它不能决定哪个 duty 应被删除、优先或修改。

这必须由 contract/domain semantics 决定。

结论：**协调可吸收，业务冲突本身不是通用协议可自动解决的问题。**

## R3-T7 — Revocation During Succession

```text
transition request based on version 8
issuer revokes grant -> version 9
old transition tries commit
```

资源/issuer 拒绝 version 8。

结论：**versioning/fencing 吸收。**

## R3-T8 — Partial Evidence Loss

例如只保存了银行 ACK，丢失合同 authority 的结果。

若一个 atomic transition 需要两方证明：

```text
missing required receipt
=> UNRESOLVED
```

不能从“一部分成功”推出全局 committed。

结论：**durable receipt + conservative completion check 即可表达。**

## 汇总

| Vector | 当前结果 | 独立协议必要性 |
|---|---|---|
| Multi-Issuer Fork | atomic/mixed outcome 可表达 | 低 |
| Obligation Double Assignment | authority state/versioning | 低 |
| Successor Race | CAS/fencing | 低 |
| Provider dies mid-transition | coordinator 可恢复；authority 消失则 unresolved | 低 |
| Reputation Split | issuer reissue/reassess | 低 |
| Conflicting Duties | domain policy 决定 | 低 |
| Revocation During Succession | version/fencing | 低 |
| Partial Evidence Loss | durable receipt + unknown | 低 |

## 新反证

R3 发现：所谓跨域 succession 似乎可以被拆成两个已有问题：

```text
1. Who has authority to decide this relationship transition?
2. How are multiple such decisions coordinated/recovered?
```

第 1 个由 domain semantics / issuer / counterparty 决定。
第 2 个由 distributed transaction / workflow mechanisms 解决。

目前尚未发现第三个必须由 Agent-specific public protocol 解决的不可约问题。

---

# English

Eight R3 stress tests currently reduce to authority-owned relationship semantics plus generic coordination/concurrency machinery. Atomic groups can use prepare/commit; long-running transfers can use compensation; successor races and revocation races use versioning/fencing; missing indispensable authority yields unresolved rather than invented consent. No Agent-specific irreducible coordination primitive has yet survived.