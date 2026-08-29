# 蒸馏与来源继承研究 / Distillation and Provenance Inheritance Research

> 状态 / Status: **Informative Research Note — 非规范性研究文档**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 先纠正一个容易误解的说法

不能笼统断言“当前中国很多模型都是通过蒸馏美国前沿模型发展起来的”。

公开事实是：

- 蒸馏本身是整个 AI 行业普遍使用的合法技术；
- DeepSeek 等中国模型曾受到 OpenAI 等方面关于未经授权蒸馏的公开指控；
- 这些指控与所有中国模型、所有训练阶段或所有能力来源不能等同；
- 在缺乏独立可审计训练血缘证据时，不应把指控表述成对整个行业的既定事实。

因此 GCPP 研究的目标不是判断某个国家“是否抄袭”，而是解决：

> **任何 Provider 的模型训练/蒸馏来源目前都缺乏一个跨平台、可验证、可选择披露的公共血缘协议。**

## 2. 为什么 C2PA/GB 45438 标识不会自然继承到 Student Model

资产级来源凭证主要绑定具体输出资产。

### C2PA

典型绑定对象：

```text
Specific Asset
+
C2PA Manifest
+
Claim Signature
+
Hard/Soft Binding
```

### 中国 GB 45438

典型绑定对象：

```text
Specific Generated File
+
AIGC Metadata
  ├── ContentProducer
  ├── ProduceID
  └── ...
```

当教师输出被用于训练时，Student 学的是 token 分布、目标答案、推理行为、偏好信号或其他可优化表示。外部文件容器中的 Manifest、X.509 签名、`AIGC` metadata 字段本身不会自动变成可验证的 Student 权重来源链。

所以很多时候所谓“来源被洗掉”，实际更准确的描述是：

> **现有来源协议没有设计成训练血缘协议，因此资产凭证在进入训练过程时就跨越了协议边界。**

## 3. 不需要主动“清洗”，来源也可能自然断裂

典型过程：

```text
Teacher API output
      ↓
text/data extraction
      ↓
training corpus representation
      ↓
optimization
      ↓
Student weights
      ↓
new sampling
      ↓
Student output
```

教师资产的外部 Manifest 或文件 metadata 并不会因“知识迁移”自动复制到 Student 新输出。

Student 的新输出如果符合中国法规，可以写入 Student Provider 自己的：

```text
ContentProducer = Student Provider
ProduceID = new identifier
```

如果使用 C2PA，也会由 Student Provider 对新资产签署新的 Manifest。

这两个行为都只能说明：

> “谁生成了当前新资产”。

不能说明：

> “模型能力从哪里学来”。

## 4. 文本 token watermark 是否会继承？

与 metadata 不同，部分 LLM watermark 是直接作用于输出 token 统计分布，因此有可能在 Student 使用大量教师输出训练后留下统计“radioactivity”。

已有研究表明：

- 一些 watermark 能通过 distillation 留下可探测信号；
- 专门的 distillation-resistant / radioactive watermark 可以用于模型窃取检测；
- 但这种信号不是传统数字签名，且在数据混合、再训练、模型变换或对抗处理下并非不可消除；
- 2025–2026 的研究进一步表明，现有 watermark 对未经授权蒸馏的鲁棒性仍然是开放问题。

因此：

```text
Inherited Watermark Signal
        = probabilistic evidence
        != signed training lineage
```

本研究不提供去除、规避或中和此类水印的操作性步骤。

## 5. 为什么数字签名不能解决蒸馏

假设教师输出 A 有合法签名：

```text
Sign_Teacher(Hash(A))
```

Student 训练后生成新文本 B：

```text
B != A
```

教师对 A 的签名不能验证 B，因为数字签名绑定的是原始 Claim/Asset，而不是“语义知识”。

这不是签名机制失败，而是证明对象不同。

## 6. 当前真正缺失的是 Model Training Lineage

需要新增的是：

```text
Model B
  ↓
which datasets?
which synthetic generators?
which teacher models?
which reasoning traces?
which fine-tuning ancestors?
which evidence supports those claims?
```

而不是继续加强某一个具体输出文件的 metadata。

## 7. GCPP 应新增的血缘证据

建议包括：

- `source_model` / `teacher_model` 标识；
- `synthetic-data-generated-by` 关系；
- dataset Merkle commitment；
- authorized distillation credential；
- teacher-provider attestation；
- training-run attestation；
- distillation-watermark evidence；
- selective disclosure；
- independent audit evidence。

重要的是：这些都属于不同 assurance 级别，不能都显示成一个绿色“Verified”。

## 8. 中国标识体系的盲点

GB 45438—2025 的 `ContentProducer` / `ProduceID` 非常适合表示“当前输出是谁制作的”，但并不要求公开：

- 模型训练使用了哪些教师模型；
- 是否使用国外 API 输出蒸馏；
- 训练语料中哪些是 synthetic data；
- 模型能力是否来自某个上游模型。

因此即使一个模型完全符合 GB 45438，也不能据此推出其 training lineage 已经得到验证。

同样，C2PA 对一个新输出的有效 Manifest 也不能推出 Student 的训练来源清白。

## 9. 对 GCPP 定位的影响

这说明 GCPP 真正值得新增的不是第三套通用 Manifest，而是两条生成式 AI 特有链路：

```text
Asset Provenance
C2PA / GB45438 adapter
        │
        └── 当前输出来源

Model Lineage
GCPP model-lineage profile
        │
        └── 训练 / 蒸馏 / synthetic-data 来源
```

最终 Verifier 应同时显示：

```text
Output provenance: VERIFIED / PARTIAL / ...
Model lineage assurance: DECLARED / COMMITTED / ATTESTED / INDICATED / VERIFIED
```

## 10. 研究边界

GCPP 不把模型相似性、benchmark 相似、语言风格相似或单一 watermark detector 结果直接解释为未经授权蒸馏。

训练血缘属于高风险归因问题，需要多证据、可复核、可审计的 assurance model。

---

# English

## Summary

It is inaccurate to generalize that most Chinese models are simply distilled from U.S. frontier models. Distillation is widely used across the AI industry, and some Chinese providers—most notably DeepSeek—have faced public allegations from OpenAI regarding unauthorized distillation. Those allegations should not be generalized to every Chinese model or treated as fully audited lineage facts.

The protocol problem is broader: current asset-provenance systems such as C2PA and China's GB 45438 primarily bind provenance to specific generated assets. Their manifests, signatures, and file metadata do not automatically become verifiable lineage inside student model weights.

Some token-level LLM watermarks can leave statistical "radioactivity" through distillation, but research also shows such inheritance is not universally robust. GCPP should treat such signals as probabilistic lineage evidence, not as cryptographic proof.

The missing layer is a public **Model Training Lineage** profile capable of expressing teacher models, synthetic-data generators, dataset commitments, authorized distillation credentials, attestations, selective disclosure, and independent audit evidence.
