# GCPP Verification Semantics 0.2 / GCPP 验证语义 0.2

> 状态 / Status: **Working Draft**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 验证是向量，不是单一结论

GCPP 0.2 的 Verifier 必须把“当前输出来源”“模型执行保证”“模型训练血缘”“监管标识”分开计算。

最小 Verification Vector：

```text
output_provenance
actor_authentication
record_signature
exact_integrity
partial_integrity
authenticated_coverage?
locator_state
lineage_state
historical_evidence
model_assurance
model_lineage_assurance
regulatory_label_state
unsupported_critical_features[]
diagnostics[]
```

## 2. C2PA 基础验证

在 C2PA-based Profile 中：

- C2PA Claim Signature 负责基础 record signature；
- Hard Binding 负责 exact/cryptographic content binding；
- Soft Binding 可负责 durable discovery/near-match；
- Actions/Ingredients 提供资产 lineage；
- Manifest Repository 可提供被分离凭证的恢复。

GCPP-aware Verifier 在 C2PA 验证结果之上增加生成式语义，不改变基础 C2PA validity。

## 3. Output Provenance

推荐展示标签：

- `VERIFIED_ORIGINAL`
- `VERIFIED_DERIVATIVE`
- `PARTIAL_PROVENANCE`
- `LOCATOR_ONLY`
- `UNVERIFIED`

`VERIFIED_ORIGINAL` 至少要求签名与 exact binding 满足所选 Profile。

`PARTIAL_PROVENANCE` 必须只覆盖能够认证的片段，不能从小片段外推全文。

## 4. Model Assurance

```text
MODEL_NONE
MODEL_DECLARED
MODEL_ATTESTED
MODEL_EXECUTION_PROVEN
```

Provider 对 Manifest/Assertion 的签名最多直接证明“Provider 做出了模型声明”，即 `MODEL_DECLARED`。更高状态需要额外 attestation / execution evidence。

## 5. Model Lineage Assurance

```text
LINEAGE_NONE
LINEAGE_DECLARED
LINEAGE_DATASET_COMMITTED
LINEAGE_TEACHER_ATTESTED
LINEAGE_WATERMARK_INDICATED
LINEAGE_INDEPENDENTLY_VERIFIED
```

这些状态不能被压缩成“抄袭/未抄袭”。

特别是：

```text
OUTPUT_PROVENANCE = VERIFIED
```

不代表：

```text
MODEL_LINEAGE = VERIFIED
```

## 6. Regulatory Label State

对于中国 GB 45438 Adapter 等监管 Profile，Verifier 可以独立输出：

```text
REGULATORY_LABEL_NOT_PRESENT
REGULATORY_LABEL_PRESENT
REGULATORY_LABEL_MALFORMED
REGULATORY_LABEL_INCONSISTENT
REGULATORY_LABEL_UNSUPPORTED
```

监管元数据存在并不自动建立 C2PA cryptographic provenance；C2PA Claim 有效也不自动满足某一国家的显式标识义务。

## 7. Locator 语义

`RecoveryLocator` / watermark 只用于 discovery。

```text
LOCATOR_NOT_PRESENT
LOCATOR_DETECTED
LOCATOR_PARTIAL
LOCATOR_RECOVERED
LOCATOR_AMBIGUOUS
```

任何 locator 状态都不能单独建立 Provider attribution。

## 8. 永久边界

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
LOCATOR_RECOVERED != PROVIDER_AUTHENTICATED
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
MODEL_LINEAGE_UNKNOWN != NO_DISTILLATION
OUTPUT_PROVENANCE != MODEL_LINEAGE
```

## 9. 本地政策

应用可以设置不同的 Trust List、identity policy、algorithm policy、regulatory policy，但原始 Verification Vector 应可见，不能把本地政策判断伪装成协议事实。

---

# English

GCPP 0.2 verification is a multidimensional vector. A C2PA-based profile uses C2PA signed claims, hard/soft bindings, actions/ingredients, and manifest repositories for base asset provenance. GCPP adds generative-specific dimensions for partial attribution, model assurance, model training/distillation lineage, and jurisdictional regulatory-label state.

Permanent distinctions include:

```text
VERIFIED != TRUE
UNVERIFIED != FAKE
UNVERIFIED != HUMAN
LOCATOR_RECOVERED != PROVIDER_AUTHENTICATED
MODEL_DECLARED != MODEL_EXECUTION_PROVEN
MODEL_LINEAGE_UNKNOWN != NO_DISTILLATION
OUTPUT_PROVENANCE != MODEL_LINEAGE
```
