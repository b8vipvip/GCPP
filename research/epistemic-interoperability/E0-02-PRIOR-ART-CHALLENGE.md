# E0-02 — Prior Art Challenge / 现有理论反证

> 状态：Research only / 非规范性

## 1. W3C URW3 已经研究过“Web 不确定性互操作”

W3C Uncertainty Reasoning for the World Wide Web Incubator Group 在 2008 年已经明确提出：Web 系统需要表达和交换 uncertainty；报告覆盖 probability、fuzzy sets、belief functions、random sets、rough sets，并提出了 uncertainty ontology。

因此：

```text
uncertainty as first-class metadata
```

不是 E0 创新。

## 2. ISO/IEC TS 25223 正在做 AI uncertainty quantification

ISO/IEC JTC 1/SC 42 已有在研项目，目标包括 AI uncertainty quantification 的术语、方法特征、生命周期 guidance/requirements。

因此：

```text
AI uncertainty terminology / UQ guidance
```

也不是应由 E0 抢先定义的领域。

## 3. Expert aggregation 早就知道“相关专家 != 独立证据”

几十年的 expert judgment / forecast aggregation 研究都指出，专家判断间的 dependence/correlation 会导致共同信息被重复计算；简单平均或错误独立性假设会失真。

因此：

```text
DEPENDENT EXPERTS MUST NOT BE COUNTED AS INDEPENDENT
```

不是 AI 新理论。

## 4. Dempster-Shafer 等 evidence theory 也处理 dependence

经典 evidence combination 中，独立性假设本身就是核心限制；已有研究专门讨论 dependent evidence、discounting、outer/inner dependence。

因此 E0 不应创造新的“AI evidence math”。

## 5. Bayesian / probabilistic models 已能表示依赖

若完整 joint distribution / graphical model / covariance / copula 等信息可得，统计理论已有大量方法建模 source dependence。

问题不是数学不存在，而可能是：

> 远程 AI system 没有一个跨实现可解释的方式，让接收方知道应该用哪种数学假设。

## 6. Calibration / conformal prediction 已提供更强语义

Conformal prediction 可以在明确假设下给出 coverage guarantee；但 guarantee 依赖 exchangeability 等条件。分布漂移后，标称 coverage 不再天然成立。

这支持候选不变量：

```text
GUARANTEE WITHOUT ASSUMPTION CONTEXT IS UNSAFE TO TRANSFER
```

但 conformal prediction 本身不需要 E0 重造。

## 7. 2026 多 Agent 研究给出的新压力

近期研究观察到：

- sycophantic consensus / correlated errors 让多个 Agent 一致但共同错误；
- 相同 structured evidence 可以显著提高 consensus，同时仍保留高共识错误；
- 单个错误 testimony 能被诚实 Agent 采用、继续传播，并在原始欺骗者离开后持续存在；
- confidence 可能严重 miscalibrated，相关误差会使基于 confidence 的审计策略失效；
- multi-agent trajectory 的 uncertainty 与单次输出 uncertainty 不同。

这些不是新的概率论，但说明 agentic communication 使依赖关系动态产生：

```text
Agent A independent at t0
A speaks to B
B updates from A
A and B are no longer independent in the same sense at t1
```

这类动态 epistemic dependency 是 E0 最值得攻击的点。

## 8. 强反证路线

E0 下一步优先尝试只使用：

```text
RDF/PROV or ordinary dependency graph
+
existing uncertainty vocabulary
+
method identifier
+
calibration metadata
+
statistical aggregation chosen by receiver
```

实现所有安全行为。

若成功，则最多需要 profile/schema，不需要新协议。

## 9. 当前可能的独立缺口（尚未证明）

暂时只保留：

### Dynamic Epistemic Dependency Interchange

系统需要表达的可能不是静态：

```text
source=A
```

而是：

```text
Judgment J2
  consumed J1
  consumed Evidence E
  shares base model family F
  shares retrieval artifact R
  confidence method C
  calibration domain D
```

然后接收方判断：

```text
Can J1 and J2 be combined as independent evidence?
```

如果这种需求可由 generic provenance 完整承担，则继续 Kill。

## English summary

Prior art already covers uncertainty representation, AI UQ, expert dependence, evidence theory, Bayesian aggregation, and calibrated prediction. E0's only remaining hypothesis is an interoperability gap around *dynamic epistemic dependency*: the information needed by a receiver to know whether remote AI judgments are statistically or evidentially safe to combine.