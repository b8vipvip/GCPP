# A0-14 — Byzantine / Open-World Prior Art Challenge

> 状态 / Status: **Research / 非规范性**  
> 日期 / Date: **2026-08-29**

# 简体中文

## 1. 透明性与双签

RFC 9162 Certificate Transparency 已经提供：

- append-only Merkle log；
- inclusion proof；
- consistency proof；
- signed tree heads；
- audit / monitor；
- 对 inconsistent views 的检测讨论。

关键结论：

```text
valid signature != honest issuer
```

如果 issuer / log equivocate，透明性机制的目标不是阻止所有恶意行为，而是让冲突可被审计与举证。

RFC 9943 SCITT 又把这一模式推广到 content-agnostic signed statements：

```text
Signed Statement
+ Transparency Service
+ Receipt
+ Verifiable Data Structure
```

因此“succession statement 需要不可抵赖、可审计、可发现冲突”本身并不需要新的 Agent log protocol。

## 2. Byzantine agreement

PBFT 等经典工作已经处理：

```text
malicious nodes
arbitrary behavior
asynchronous network
quorum agreement
```

对于一个已知、有限的 authority committee，如果 succession 的业务语义真的要求 committee-level consensus，则这是标准 BFT / state-machine-replication 问题。

A0 不应重新定义 Byzantine consensus。

## 3. 异步环境中的 liveness 边界

FLP 证明：纯异步分布式系统中，即使只有一个故障进程，也无法保证所有合法执行都终止达成 consensus。

对 Agent succession 的含义不是“发明一个更强协议”，而是：

```text
SAFETY MAY REQUIRE NON-COMPLETION
```

即系统必须允许：

```text
PENDING
UNKNOWN
UNRESOLVED
```

而不是为了给用户一个 continuity answer 强行 commit。

## 4. 凭证与 trust policy

W3C Verifiable Credentials 2.0 已经提供 issuer / subject / verifier / status 等通用模型。

它可以承载：

- transfer acknowledgement；
- reissue decision；
- successor claim；
- authority membership claim；
- policy-epoch claim；
- negative/deny decision。

但 VC 不替 verifier 决定“信谁”。这正好符合 R4：

```text
cryptographic validity != trust policy acceptance
```

不同 verifier 可以对同一组有效 credential 得出不同 policy outcome，这不是协议冲突。

## 5. OAuth / replay / sender binding

RFC 9700 等 OAuth 安全实践已经覆盖 replay prevention、sender-constrained token、rotation 等问题。

因此 forked / restored Agent 使用旧授权材料的问题，继续属于 authorization/resource-server enforcement，而不是 R4 独立问题。

## 6. 2026 Agent 标准工作的方向

2026 年 IETF 的多个 AI Agent 草案正在把 OAuth/WIMSE/现有凭证机制用于 Agent authentication / authorization，而不是假设所有 Agent 安全都必须由全新协议解决。

这进一步提高 A0 的创新门槛：Agent-specific 协议只有在通用机制无法表达某个稳定安全不变量时才有必要。

## 7. Prior-art challenge 后的剩余问题

R4 只剩三个理论挑战：

### 7.1 隔离视图

如果 Authority Q 同时签：

```text
R -> B
R -> C
```

Verifier V1 只看到第一份，V2 只看到第二份。

单一 verifier 无法从本地证据推导出隐藏冲突。

需要：

```text
gossip
witness
transparency cross-check
consensus
```

或保持：

```text
LOCALLY_VALID_GLOBALLY_UNKNOWN
```

这不是 AI-specific。

### 7.2 authority universe 未知

若参与 succession 的 authority 集合不是 closed world，则：

```text
all known relationships completed
```

不能推出：

```text
all relationships completed
```

因此只能做 scope-bounded completion。

### 7.3 不可替代 authority 消失

如果唯一有权转移关系的 authority 永久消失且此前未委托 recovery authority，则任何协议都不能生成缺失授权。

正确状态仍是：

```text
UNRESOLVED
```

## 8. 当前 prior-art 判定

截至 R4，本轮未发现以下必要性：

```text
new Agent-specific consensus
new Agent transparency log
new Agent credential container
new Agent trust engine
new Agent global clock
```

A0 的最后机会仅剩：能否找到一个无法分解为上述成熟问题的 Agent-specific safety property。

---

# English

R4 prior-art analysis finds that equivocation, transparent audit, Byzantine agreement, asynchronous liveness limits, signed credentials, trust policy divergence, replay prevention and stale-instance enforcement already have mature generic foundations. The only remaining challenge is whether long-lived Agent succession introduces a genuinely irreducible safety property beyond those foundations.