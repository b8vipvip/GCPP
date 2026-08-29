# E0-04 — 第一轮研究结论 / First-Round Findings

> 状态 / Status: Research Findings / 非规范性

## 1. 第一轮没有证明需要新协议

12 个首轮压力测试全部可以用普通：

```text
dependency metadata
calibration metadata
measure semantics
conservative downgrade rules
```

安全分类。

因此当前没有理由定义：

```text
Epistemic Token
Confidence Protocol
AI Belief Ledger
Epistemic Blockchain
```

## 2. 被大幅降级的候选

以下内容本身不是 E0 独立创新：

```text
uncertainty representation
confidence serialization
expert dependence math
Bayesian aggregation
Dempster-Shafer dependence handling
calibration metadata
conformal guarantees
ordinary dependency DAG
```

## 3. 真正剩下的困难转向“可观测性”

如果 aggregator 已经知道：

```text
J2 consumed J1
J1/J2 share RAG artifact R
J1/J2 share model family F
confidence type = calibrated_probability
calibration domain = D
```

那么很多安全行为非常直接。

真正困难的是：现实中这些信息往往不可得、不可验证或不能公开：

- 模型供应商不愿公开底层 model lineage；
- 两个 API 可能共享基础模型而 verifier 不知道；
- 蒸馏/微调导致 error correlation，但不存在精确 lineage disclosure；
- shared pretraining data 几乎不可完整声明；
- proprietary RAG/source graph 可能涉及商业秘密或隐私；
- 两个不同方法的 error modes 是否“足够独立”通常需要经验数据而不是静态声明；
- Agent 在对话中被另一个 Agent 影响后，依赖关系是动态产生的。

因此候选问题从：

```text
How do we aggregate AI confidence?
```

缩小为：

> **How can a receiver obtain enough trustworthy information about epistemic dependence to avoid false independence assumptions, without requiring full disclosure of proprietary model/data internals?**

暂名：

```text
Epistemic Dependency Observability
```

## 4. 这仍然可能被现有机制吸收

可能的吸收路线：

```text
PROV / dependency graph
+
verifiable credentials / attestations
+
privacy-preserving disclosure / ZK where useful
+
benchmark-based empirical correlation certificates
+
receiver-side conservative policy
```

如果这些已有组件足够，那么 E0 最终也只需要 interoperability profile / test suite。

## 5. 第二轮必须攻击的问题

E0-R2 不再测试“已知 dependency 时如何聚合”，而测试 dependency 不完全可见：

```text
R2-T1 Hidden shared base model
R2-T2 Hidden distillation lineage
R2-T3 Shared pretraining but different vendors
R2-T4 Private RAG source overlap
R2-T5 Dynamic persuasion dependence
R2-T6 Claimed independence without evidence
R2-T7 Empirical correlation certificate drift
R2-T8 Privacy-preserving dependence disclosure
R2-T9 Malicious omission of dependency
R2-T10 Unknown dependency graph with high-stakes decision
R2-T11 Dependency discovered after action
R2-T12 Cross-domain calibration certificate portability
```

## 6. 当前生死问题

如果安全系统只需：

```text
when dependency is unknown -> don't assume independence
```

那么这虽然正确，却可能过于保守，不需要新公共标准。

E0 必须证明一个更强的现实需求：

> 在不暴露完整商业秘密/训练数据/内部推理的前提下，跨供应商系统仍需要一种可互操作、可验证的有限 dependency disclosure，使得接收方可以获得比“全部 UNKNOWN”更有用、同时又不产生虚假独立性的安全决策。

如果做不到，或者已有 attestation/VC/privacy technology 可自然承担，E0 应终止。

## English summary

The first E0 round does not justify a new protocol. Ordinary metadata is sufficient when dependency and calibration facts are known. The surviving research question is **Epistemic Dependency Observability**: whether heterogeneous AI providers can disclose enough trustworthy information about shared evidence, model lineage, derivation and calibration dependence to prevent false independence assumptions without exposing proprietary internals.