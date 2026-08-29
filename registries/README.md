# GCPP Protocol Registries 0.2 / GCPP 协议注册表 0.2

> 状态 / Status: **Initial Registry Framework**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

GCPP 注册表用于协调生成式扩展语义，不用于替代 C2PA 自己的算法列表、Trust List 或 IANA 等既有注册体系。

## 1. Registry 原则

- C2PA 已注册/标准化的通用能力 **SHOULD** 直接引用，不创建重复 ID；
- GCPP Registry 主要登记生成式专用 semantics/profile；
- Registry entry 不代表法律许可、Provider 合法性、事实真实性或平台信任；
- Deprecated/Historic entry 必须保留用于历史验证。

## 2. Generative Event Types

| ID | 含义 |
|---|---|
| `gcpp.event.generate` | AI/软件生成事件 |
| `gcpp.event.ai-rewrite` | AI 重写 |
| `gcpp.event.summarize` | AI 摘要 |
| `gcpp.event.translate` | 翻译 |
| `gcpp.event.compose` | 多来源组合 |

## 3. Model Lineage Relations

| ID | 含义 |
|---|---|
| `gcpp.lineage.trained-on` | 训练使用某数据源 |
| `gcpp.lineage.fine-tuned-from` | 从模型/权重继续训练 |
| `gcpp.lineage.teacher-distilled-from` | 教师蒸馏关系 |
| `gcpp.lineage.synthetic-data-generated-by` | 合成训练数据生成者 |
| `gcpp.lineage.reasoning-traces-generated-by` | 推理轨迹来源 |
| `gcpp.lineage.preference-optimized-from` | 偏好优化数据来源 |
| `gcpp.lineage.unknown-influence` | 已知存在影响但类型未知 |

## 4. Model Lineage Evidence Types

| ID | 含义 |
|---|---|
| `gcpp.evidence.dataset-commitment` | 数据集 commitment |
| `gcpp.evidence.training-run-attestation` | 训练运行证明 |
| `gcpp.evidence.teacher-attestation` | 教师/数据提供方 attestation |
| `gcpp.evidence.distillation-watermark` | 可经蒸馏继承的 watermark indication |
| `gcpp.evidence.independent-audit` | 独立审计证据 |
| `gcpp.evidence.selective-disclosure` | 选择性披露证明 |

## 5. Text Locator Schemes

初始 placeholder：

```text
gcpp.text.locator.experimental-1
```

任何推荐 scheme 必须有公开 benchmark，并明确是否适合作为 C2PA Soft Binding Algorithm 候选。

## 6. Normalization Profiles

```text
gcpp.norm.text-plain-1
gcpp.norm.html-visible-1
gcpp.norm.markdown-text-1
```

这些 ID 在 normative 文档和 machine-readable vectors 完成前保持 provisional。

## 7. Regulatory Adapters

| ID | 含义 |
|---|---|
| `gcpp.regulatory.cn-gb45438-2025` | 中国 GB 45438—2025 AIGC 标识 Adapter |
| `gcpp.regulatory.future` | 未来地区/国家 Profile |

监管 Adapter 解析监管字段，但不自动建立 cryptographic provenance。

## 8. External Standards Adapters

| ID | 目标 |
|---|---|
| `gcpp.adapter.c2pa-2x` | C2PA 2.x Content Credentials |
| `gcpp.adapter.did` | DID identity |
| `gcpp.adapter.vc` | Verifiable Credentials |
| `gcpp.adapter.x509` | X.509 identity/trust |

具体版本兼容范围由 Profile 决定。

## 9. Assurance vocabularies

### Model assurance

```text
MODEL_NONE
MODEL_DECLARED
MODEL_ATTESTED
MODEL_EXECUTION_PROVEN
```

### Model lineage assurance

```text
LINEAGE_NONE
LINEAGE_DECLARED
LINEAGE_DATASET_COMMITTED
LINEAGE_TEACHER_ATTESTED
LINEAGE_WATERMARK_INDICATED
LINEAGE_INDEPENDENTLY_VERIFIED
```

---

# English

GCPP registries coordinate generative-specific semantics and profiles. They do not duplicate C2PA algorithm lists or Trust Lists where existing registries already suffice.

New 0.2 registry areas include generative event types, model-lineage relationship types, training-lineage evidence, durable text locator schemes, regulatory adapters such as China GB 45438—2025, and external-standard adapters such as C2PA, DID/VC, and X.509.
