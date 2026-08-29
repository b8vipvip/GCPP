# C0 — AI Assurance Contracts / AI 保证契约研究

> 状态 / Status: **Fundamental falsification research — active, non-normative**  
> 分支 / Branch: `research/c0-ai-assurance-contracts`  
> 日期 / Date: 2026-08-29

## 中文

C0 不研究新的 API schema，也不把 benchmark 报告包装成协议。

研究问题是：

> 对黑盒、学习型、会升级和漂移的 AI/Agent 组件，跨供应商编排系统是否需要一种公共的运行时保证契约，使接收方能够机器判断“在什么假设下、依据什么证据、当前版本和上下文中，某项统计/行为保证仍然适用”，并在组合多个组件时安全推导系统级保证？

暂时写成：

```text
Assumptions
    ↓
Evidence-backed Guarantee
    ↓
Runtime applicability
    ↓
Composition / degradation
    ↓
Invalidation / reassessment
```

C0 首先主动尝试由既有技术完全吸收：

```text
probabilistic assume/guarantee theory
ISO/IEC 42102 capability descriptors
ISO/IEC 25059 AI quality model
IEEE P3777 Agent benchmarking
OMG SACM assurance cases
VC / JWS / COSE / attestation carriers
runtime assumption / drift monitoring
PROV / dependency metadata
SLO / error-budget practice
```

### Kill Criteria

如果上述组件加一个普通 application profile 就能安全处理所有极端场景，则：

```text
NO INDEPENDENT AI ASSURANCE CONTRACT PROTOCOL
```

只有发现一个跨行业、跨供应商、现有 assurance/contract theory 无法表达或执行的不可约 runtime semantic 才继续协议化。

## English

C0 tests whether black-box learned AI components require a new cross-vendor runtime assurance-contract primitive, or whether existing probabilistic contracts, AI quality/benchmark standards, assurance cases, attestations, runtime monitors and ordinary metadata already suffice. This is falsification research, not a protocol design effort.