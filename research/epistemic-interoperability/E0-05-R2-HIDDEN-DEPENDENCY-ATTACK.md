# E0-05 — R2 Hidden Dependency / Observability Attack

> 状态 / Status: **Research only / 非规范性**  
> 日期 / Date: 2026-08-29

## 1. R2 要攻击的不是“已知依赖”

E0 第一轮已经证明：如果接收方知道 model/evidence/judgment/calibration dependency，普通 metadata + receiver policy 足以阻止最明显的 confidence amplification。

R2 因此只攻击：

```text
hidden shared base model
hidden distillation lineage
shared pretraining overlap
private RAG overlap
dynamic persuasion dependence
unsupported independence claims
correlation certificate drift
privacy-preserving disclosure
malicious dependency omission
high-stakes unknown dependence
late dependency discovery
cross-domain calibration portability
```

## 2. 最重要的理论转向：不需要证明“绝对独立”

统计独立不是一个脱离上下文的静态对象属性。

它至少相对于：

```text
random variables
condition set
task distribution
time window
measurement procedure
error event definition
```

成立。

因此一个通用声明：

```text
Agent A is independent from Agent B
```

几乎没有安全语义。

更安全的是有限声明，例如：

```text
Under benchmark B,
for task family D,
during interval T,
error-indicator correlation(A,B) <= rho,
measured by method M,
with sample/evaluation metadata V.
```

或：

```text
Evidence acquisition paths E1/E2 are attested disjoint
within declared source universe S.
```

这些是 scoped claims，而不是 universal independence。

## 3. Hidden common cause 不可由协议凭空消除

若两个供应商秘密共享：

```text
base model
training corpus
RAG provider
distillation ancestor
```

且没有任何可观察/可审计证据暴露这一点，则接收方不能从输出本身推导“没有共同原因”。

因此候选安全默认：

```text
ABSENCE OF DEPENDENCY EVIDENCE
!=
EVIDENCE OF INDEPENDENCE
```

以及：

```text
UNKNOWN_DEPENDENCE
=>
NO AUTOMATIC INDEPENDENCE BONUS
```

协议无法制造供应商未提供、也无法观测的真相。

## 4. 统计 prior art 对 E0 很不利

Robust forecast aggregation 的已有结果表明：若 aggregator 对 information structure 几乎一无所知，存在无法获得良好聚合性能的负面结果；要获得更好性能必须加入结构假设或额外信息。

这意味着：

```text
unknown information structure
```

本身不是 E0 可“修复”的协议 bug。

正确系统要么：

1. 获得更多关于 information structure 的可信信息；
2. 使用更保守的 robust aggregation；
3. abstain / 不提升置信；
4. 在后续真实反馈中学习相关性。

## 5. Privacy 并没有自动创造新协议空白

如果某个 provider/auditor 已经能够计算一个私有 predicate，例如：

```text
source_overlap <= threshold
model_family_hash != other_model_family_hash
benchmark_error_correlation <= rho
training_snapshot belongs_to certified cohort C
```

那么选择性披露 credential、零知识证明、普通签名 attestation 都可以作为通用载体。

这解决的是：

```text
prove a defined predicate without revealing all inputs
```

而不是：

```text
magically discover whether the predicate is true
```

因此 E0 不应重造 VC/ZK/attestation。

## 6. 动态依赖也可以首先作为普通 provenance 处理

若 B 在时刻 t 读取了 A 的判断：

```text
A:J1 -> B consumes J1 -> B:J2
```

那么通信本身就形成可记录的 derivation/dependency edge。

只要 orchestrator/transport 记录 message consumption，普通 provenance graph 已可表达：

```text
J2 derived using J1
```

这足以禁止将 J1/J2 默认视为两份完全独立观察。

因此“communication creates dependence”也不是独立 wire primitive。

## 7. 真正剩下的可能价值：bounded dependency assurance

若 E0 最后还有价值，可能不是：

```text
independent=true/false
```

而是帮助不同系统互操作如下**有限保证**：

```text
Dependency Claim
  subject judgments/models/evidence
  dependency dimension
  scope/domain
  measurement/attestation method
  bound/class
  evaluator/issuer
  validity interval
  evidence/reference
  unknown/withheld dimensions
```

但这仍然可能只是：

```text
schema/profile over VC/PROV/RATS
```

而不是新协议。

## 8. R2 Kill Criteria

如果以下组合足以：

```text
PROV / ordinary dependency graph
+
scoped correlation/calibration claims
+
VC/COSE/JWS/RATS attestation
+
selective disclosure / ZK where justified
+
receiver-side robust policy
```

则停止 E0 独立 wire-protocol 方向。

下一步只应继续研究一个问题：

> 不同供应商是否真的需要一个共享的 **epistemic assurance vocabulary/profile** 才能让这些有限依赖保证被机器正确解释，还是现有 generic schemas + domain profiles 已经足够？
