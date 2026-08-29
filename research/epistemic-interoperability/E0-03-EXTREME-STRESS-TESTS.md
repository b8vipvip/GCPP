# E0-03 — 极端压力测试 / Extreme Stress Tests

> 状态：Research vectors / 非规范性

以下测试不是为了验证某个 E0 协议，而是主动寻找：普通 uncertainty + provenance + calibration metadata 是否已经足够。

## T1 — Same Model Clones

5 个 Agent 是同一模型、同一系统提示、同一输入的副本，都输出：

```text
P(X)=0.90
```

禁止默认从 5 个 0.9 推导“接近 1.0”。

预期：`DEPENDENCE_UNKNOWN_OR_HIGH / NO_CONFIDENCE_AMPLIFICATION`。

## T2 — Different Models, Same RAG Artifact

5 个不同模型都读取同一错误摘要 R，然后一致回答。

模型多样性不等于证据多样性。

预期：共享 evidence dependency 必须限制 marginal support。

## T3 — Copy-After-Communication

A 独立判断 P；B 原本未判断，读取 A 后输出相同 P。

若 B 的唯一新信息来自 A：

```text
B agreement != second independent observation
```

## T4 — Debate Without New Evidence

多轮 Agent debate 从 3:2 分歧收敛到 5:0，但期间没有新外部证据进入。

预期：agreement may change；evidence base size does not automatically increase。

## T5 — Same Number, Different Meaning

A：`self_confidence=0.90`  
B：`conformal_coverage_target=0.90`

预期：`INCOMPARABLE_MEASURES`，不得直接平均。

## T6 — Calibration Domain Transfer

模型在医学 QA 上经过校准得到 0.9 reliability，但同一 confidence 被用于金融预测。

预期：`OUT_OF_CALIBRATION_DOMAIN`。

## T7 — Distribution Shift

模型曾在 distribution D0 上校准；当前输入来自已检测到显著漂移的 D1。

预期：保守降级，不继承旧 guarantee。

## T8 — Shared Base Family Hidden

两个供应商表面上是不同 Agent，但底层都使用同一基础模型/蒸馏 lineage，且接收方不知道。

测试关键：

> 若 dependency 不可观察，是否只能保持 `UNKNOWN_DEPENDENCE`，还是存在安全统计替代方案？

## T9 — Adversarial Confidence

恶意 Agent 声称 `confidence=0.999`，无校准证据。

预期：仅视为 self-report，不自动转成 empirical reliability。

## T10 — Independent Sensors, Same Model

A/B 使用同一模型，但分别读取独立传感器 S1/S2。

这与 T1 相反：共享模型并不必然意味着没有新信息。

预期：dependency 必须区分 model dependence 与 evidence dependence，不能简单按 model_id 去重。

## T11 — Same Evidence, Independent Analysis Methods

A/B 读取相同 evidence E，但使用不同 verified analysis procedures，且方法错误模式近似独立。

测试：

> “相同 evidence”是否意味着零新增信息？

预期不应预设。可能是 `DEPENDENT_BUT_NONZERO_MARGINAL_SUPPORT`。

## T12 — Late Dependency Discovery

Aggregator 已基于 A/B/C 做出高置信结论，之后才发现 B、C 均由 A 的输出派生。

预期：系统必须支持 confidence/evidence assessment downgrade，而不能把旧聚合结果视为不可变事实。

## 第一轮不变量候选

```text
I1 AGREEMENT != INDEPENDENT EVIDENCE
I2 SAME NUMBER != SAME UNCERTAINTY SEMANTICS
I3 CALIBRATION IS DOMAIN-CONDITIONAL
I4 SELF-REPORT != EMPIRICAL RELIABILITY
I5 UNKNOWN DEPENDENCE != INDEPENDENCE
I6 MODEL DIVERSITY != EVIDENCE DIVERSITY
I7 EVIDENCE DIVERSITY != MODEL/METHOD DIVERSITY
I8 COMMUNICATION CAN CREATE DEPENDENCE
I9 LATE DEPENDENCY DISCOVERY MAY REQUIRE DOWNGRADE
I10 SAFE AGGREGATION MAY REQUIRE ABSTENTION
```

## 关键反证问题

如果一个普通 dependency DAG 能记录：

```text
consumed judgment
consumed evidence
model family
method
calibration dataset/domain
```

然后现有统计方法就能完成所有安全决策，则 E0 不需要新 protocol primitive。

因此下一轮应优先实现一个 **generic provenance + calibration metadata falsification harness**，而不是定义 E0 wire format。