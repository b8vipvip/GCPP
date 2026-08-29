# GCPP 模型血缘与蒸馏来源语义 0.1 / GCPP Model Lineage and Distillation Provenance 0.1

> 状态 / Status: **Exploration / Pre-normative Working Draft**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 为什么需要单独的 Model Lineage

内容来源与模型训练来源不是同一问题。

```text
OUTPUT_PROVENANCE
= 这一次输出是谁生成/签名的？

MODEL_LINEAGE
= 这个模型的能力、训练数据或教师信号来自哪里？
```

C2PA/GCPP 对某次输出进行有效签名，只能证明这次输出的来源声明。它不能自动证明模型训练过程中是否使用了其他模型输出、推理轨迹、偏好数据或蒸馏教师。

因此：

```text
OUTPUT_PROVENANCE != TRAINING_LINEAGE
```

## 2. 蒸馏场景

典型抽象：

```text
Teacher Model A
   ↓ generates
Synthetic Dataset / Reasoning Traces
   ↓ training/distillation
Student Model B
   ↓ generates
New Output C
```

`Output C` 可以由 B 合法签名，并拥有自己的 Content Credential；这不意味着 A 对 C 进行了签名，也不意味着 A 的原始输出 Manifest 应直接“转移”到 C。

需要额外的 `ModelLineage` 证据来表达 A → B 的训练影响。

## 3. 为什么普通内容标识通常不会继承到 Student Model

资产级来源机制通常绑定的是一个具体输出资产：

- 文件元数据；
- C2PA Manifest/Claim；
- 对具体资产的 Hash/Hard Binding；
- 可恢复该资产 Manifest 的 Soft Binding。

训练系统从教师输出中学习 token/feature/behavior 时，通常并不会把这些外部资产容器字段变成 Student 权重中的可验证来源链。

即使教师输出包含可检测文本水印，Student 是否继承该统计信号取决于水印方案、训练流程、数据混合和后续优化；这不是普通数字签名能够保证的。

## 4. Assurance Levels

GCPP 建议将模型血缘证据分层，而不是简单输出“抄袭/未抄袭”。

```text
LINEAGE_NONE
LINEAGE_DECLARED
LINEAGE_DATASET_COMMITTED
LINEAGE_TEACHER_ATTESTED
LINEAGE_WATERMARK_INDICATED
LINEAGE_INDEPENDENTLY_VERIFIED
```

### LINEAGE_DECLARED

Provider 自己声明使用了某个教师模型、数据来源或蒸馏流程。

### LINEAGE_DATASET_COMMITTED

存在对训练/蒸馏数据集合的承诺（commitment），可在授权情况下选择性披露或审计。

### LINEAGE_TEACHER_ATTESTED

教师 Provider、数据提供方或可信执行环境为某项训练关系提供证明。

### LINEAGE_WATERMARK_INDICATED

在 Student 行为中检测到与某种“可经蒸馏继承”的 watermark/fingerprint 一致的统计证据。该状态只是证据，不应单独等同侵权或确定血缘。

### LINEAGE_INDEPENDENTLY_VERIFIED

多个独立证据共同支持某种训练/蒸馏关系，具体门槛由 Profile 定义。

## 5. ModelLineage 抽象

```text
ModelLineageClaim {
  subject_model
  relation_type
  source_model_or_dataset?
  dataset_commitment?
  time_range?
  evidence[]
  disclosure_policy?
  extensions[]
}
```

`relation_type` 可以包括：

```text
trained-on
fine-tuned-from
teacher-distilled-from
preference-optimized-from
synthetic-data-generated-by
reasoning-traces-generated-by
unknown-influence
```

## 6. 隐私和商业秘密

协议不应要求公开完整训练集、Prompt、教师输出或内部模型路由。

可使用：

- dataset commitment；
- Merkle root；
- selective disclosure；
- confidential audit；
- TEE attestation；
- future ZK evidence。

目标是在“完全不披露”与“公开全部训练数据”之间提供可验证中间层。

## 7. Watermark 与蒸馏

研究表明，一些 LLM watermark 可能在训练后以统计方式遗留到 Student 模型（常称 radioactivity），因此可以作为未经授权蒸馏的检测信号之一；也有研究表明，这类继承并非不可消除，且在对抗环境下存在明显局限。

因此 GCPP 的原则是：

```text
DISTILLATION_WATERMARK = EVIDENCE
DISTILLATION_WATERMARK != CRYPTOGRAPHIC PROOF
```

本规范不定义或提供规避、清除来源水印的操作流程。

## 8. 与 C2PA 的关系

C2PA 可以承载模型 Content Credential、Ingredient、Assertion 与相关 provenance 信息。GCPP Model Lineage 的目标不是替代 C2PA Manifest，而是定义一组生成式 AI 训练关系和 assurance semantics，并尽量映射为 C2PA assertions/ingredients 或未来 AI/ML profile。

## 9. 安全边界

- Provider 自声明并不自动成为独立事实；
- 没有 lineage proof 不等于没有蒸馏；
- 检测到相似行为不等于证明数据盗用；
- 模型输出签名不证明训练数据来源清白；
- 模型血缘证明不应暴露用户个人数据或商业机密。

---

# English

## 1. Separate output provenance from model lineage

`OUTPUT_PROVENANCE` asks who generated/signed one output. `MODEL_LINEAGE` asks which teacher models, synthetic datasets, reasoning traces, or prior models influenced training. A valid credential for a student's new output does not prove anything by itself about the student's training lineage.

## 2. Lineage assurance

GCPP proposes layered states rather than a plagiarism boolean:

```text
LINEAGE_NONE
LINEAGE_DECLARED
LINEAGE_DATASET_COMMITTED
LINEAGE_TEACHER_ATTESTED
LINEAGE_WATERMARK_INDICATED
LINEAGE_INDEPENDENTLY_VERIFIED
```

## 3. Distillation watermark evidence

Some research shows watermark signals can be inherited by student models through distillation, while other work demonstrates that such radioactivity is not universally robust under adversarial processing. GCPP therefore treats distillation-resistant watermarking as evidence, not as a cryptographic proof of lineage.

## 4. C2PA relationship

C2PA can carry model credentials, ingredients, and assertions. GCPP Model Lineage defines generative-AI-specific training relationships and assurance semantics that should map onto C2PA mechanisms where possible rather than create a competing manifest system.
