# GCPP Threat Model 0.2 / GCPP 威胁模型 0.2

> 状态 / Status: **Working Draft**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 安全目标

GCPP 0.2 重点抵抗或准确表示：

- 伪造某 Actor/Provider 的来源声明；
- 将真实 RID/watermark/Manifest reference 嫁接到无关内容；
- 将 partial provenance 夸大成全文来源；
- 把 `MODEL_DECLARED` 误报成真实执行证明；
- 把当前输出来源误当成训练/蒸馏血缘；
- 把 regulatory label 当成 cryptographic authentication；
- 把 `UNVERIFIED` 误报成 Fake/Human；
- 在存在独立历史证据时无痕重写来源记录。

## 2. 新增核心威胁：Training-lineage laundering

攻击者或 Provider 可能对 Student 模型的新输出合法签名，并据此暗示：

> “因为当前输出是由 Student Provider 签名，所以 Student 的训练来源也已被证明独立。”

这是错误推理。

防御：Verifier 必须分离：

```text
output_provenance
model_lineage_assurance
```

有效 C2PA/GCPP 输出凭证不能自动提升 `model_lineage_assurance`。

## 3. 监管标签混淆

中国 GB 45438 `AIGC` metadata、显式 AI 标签等可以证明/声明监管标识状态，但并非等价于 C2PA Claim Signature。

攻击面包括：

- 将自填 `ContentProducer` 误当成已认证 Provider identity；
- 将存在 `ProduceID` 误当成完整 cryptographic provenance；
- 将 C2PA 有效签名误当成自动满足某地区显式标识法规。

防御：`regulatory_label_state` 独立于 `actor_authentication` 和 `record_signature`。

## 4. Distillation watermark 过度归因

可经蒸馏继承的 watermark/radioactivity 可能是有价值的 IP/lineage evidence，但：

- false positive/negative 仍需评估；
- 数据混合与后续训练会影响信号；
- 对抗环境下并非绝对稳健；
- 不能单独证明法律意义上的侵权或某次具体 API 调用。

因此检测到信号最多进入：

```text
LINEAGE_WATERMARK_INDICATED
```

除非 Profile 要求的其他独立证据同时满足。

## 5. Asset-level attacks

### Signature forgery

使用 C2PA Claim Signature 或其他注册签名机制验证；失败不得归属 Actor。

### Locator transplant

RID 仅用于 discovery。必须继续验证 Manifest/record signature 与 content relationship。

### Partial-copy inflation

authenticated coverage 必须只计算能够绑定的材料。

### Metadata stripping

允许 embedded manifest、sidecar、C2PA soft binding、RID、clipboard 等多层 carrier。普通 metadata 丢失不应被自动认定恶意。

### Arbitrary rewrite

如果所有可恢复 provenance 信息都被破坏，协议只能输出 `UNVERIFIED`，不能保证永久追踪。

## 6. Model-level attacks

### Provider false model declaration

签名证明 Provider 做过声明，不证明声明真实。更高 assurance 需要 attestation/verifiable execution。

### Hidden training sources

没有 `ModelLineageClaim` 或 lineage evidence 时，Verifier 只能报告 `LINEAGE_NONE/UNKNOWN`，不能推断“没有蒸馏”。

### False lineage accusation

模型行为相似、benchmark 相似、语言风格相似或单一 detector 结果不能被协议直接升级为 `LINEAGE_INDEPENDENTLY_VERIFIED`。

## 7. Privacy threats

- GID/RID 不得编码用户账号/IP/设备；
- public model-lineage proof 不应要求公开完整训练集；
- dataset commitment 应优先使用 commitment/selective disclosure；
- manifest repository 查询可能产生隐私泄漏，应支持 client-side computation/consent 等保护。

## 8. Availability and agility

C2PA repository、Provider endpoint、Transparency Log、链、Registry 都可能停止服务。验证材料应尽量支持缓存、镜像、sidecar/self-contained bundle 与历史算法标识。

## 9. 永久安全语义

```text
PROVENANCE != TRUTH
UNVERIFIED != FAKE
WATERMARK != AUTHENTICATION
OUTPUT_PROVENANCE != MODEL_LINEAGE
REGULATORY_LABEL != CRYPTOGRAPHIC_IDENTITY
WATERMARK_INDICATION != LEGAL_PROOF_OF_DISTILLATION
```

---

# English

GCPP Threat Model 0.2 adds two major risks: **training-lineage laundering** (using a valid student-output credential to imply clean/independent training lineage) and **regulatory-label confusion** (treating jurisdictional metadata as cryptographic actor authentication).

Distillation-radioactivity watermarks are useful evidence but remain probabilistic and must not be treated as standalone legal or cryptographic proof of unauthorized distillation.
