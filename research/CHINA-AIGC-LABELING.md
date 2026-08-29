# 中国人工智能生成合成内容标识体系研究 / China AIGC Labeling Ecosystem Research

> 状态 / Status: **Informative Research Note — 非规范性研究文档**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 1. 结论摘要

截至 2026 年，中国主流生成式 AI 平台公开遵循的核心体系并不是 C2PA，而是中国自己的法定/标准化标识体系：

- 《人工智能生成合成内容标识办法》；
- 强制性国家标准 **GB 45438—2025《网络安全技术 人工智能生成合成内容标识方法》**；
- TC260 配套的服务提供者编码规则、不同文件类型的元数据隐式标识实践指南、安全防护指南与检测指南。

公开平台条款显示，DeepSeek、Kimi、豆包、腾讯混元等均明确提及按照上述中国法律法规和国家标准添加 AI 生成标识。公开资料中暂未发现这些平台把 C2PA 作为其中国业务统一法定来源协议的证据。

## 2. 中国体系的三层结构

### 2.1 显式标识

用户可以直接看到，例如：

- 文本/对话界面“AI 生成”提示；
- 图片角标或可见水印；
- 音频提示；
- 视频画面提示。

### 2.2 文件元数据隐式标识

GB 45438—2025 要求文件元数据包含人工智能生成属性、生成服务提供者、内容制作编号、传播服务提供者、传播编号等信息。

标准公开文本给出了类似以下结构：

```json
{
  "AIGC": {
    "Label": "...",
    "ContentProducer": "...",
    "ProduceID": "...",
    "ReservedCode1": "...",
    "ContentPropagator": "...",
    "PropagateID": "...",
    "ReservedCode2": "..."
  }
}
```

其中 `ProduceID` 是生成服务提供者为具体内容分配的唯一编号；`ContentProducer` 可以记录服务提供者名称或编码。

### 2.3 可选数字水印/安全防护

中国《标识办法》鼓励使用数字水印等隐式标识技术，但法定基础仍以显式标识与文件元数据隐式标识为核心。

因此当前中国体系更接近：

```text
Visible Label
+
AIGC File Metadata
+
Optional Digital Watermark
+
Platform Detection / Declaration
```

而不是：

```text
C2PA Signed Manifest
+
C2PA Trust List
+
Hard/Soft Binding
```

## 3. Provider 编码

TC260 的服务提供者编码指南定义了 27 位服务提供者编码结构，包括：

- 2 位标识格式定义码；
- 20 位主体标识码；
- 5 位服务扩展码。

该编码用于文件元数据隐式标识中的服务提供者身份表达。

## 4. 主流平台公开情况

### DeepSeek

DeepSeek 用户协议明确说明平台已按照《人工智能生成合成内容标识办法》和 GB 45438—2025 等要求对模型生成内容添加标识；其开放平台协议也要求 API 使用方对生成文本进行标识。

### Kimi

Kimi 模型使用协议明确描述“显式标识 + 隐式标识”，并称隐式标识按国家规范嵌入生成内容文件数据。

### 豆包

豆包用户协议明确说明可根据法规对 AI 生成文本、图片、音频、视频添加显式标识和文件元数据隐式标识。

### 腾讯混元

腾讯云大模型条款公开说明生成/合成内容文件元数据会加入隐式标识，包括生成属性、服务提供者名称或编码、内容编号等；混元生图/生视频同时支持显式 AI 水印。

## 5. 与 C2PA 的主要区别

中国 GB 45438 体系主要回答：

> 内容是否属于/可能/疑似 AI 生成，以及哪个生成/传播服务提供者和编号与其关联。

C2PA 更强调：

> 谁签署了内容来源 Claim、内容是否与 Manifest 绑定、发生了哪些 Action/Ingredient 关系，以及凭证能否通过签名链验证。

因此二者不是完全相同的问题空间。

简化比较：

| 维度 | 中国 GB 45438 体系 | C2PA |
|---|---|---|
| 法律/监管定位 | 中国强制标准与监管配套 | 全球开放行业标准 |
| 显式 AI 标签 | 核心要求 | 可通过 assertions/UI 表达，但非核心等价物 |
| 文件元数据 AIGC 字段 | 核心 | 使用 Manifest/Assertions |
| Provider 内容编号 | 明确要求 | 可通过标识/assertion 表达 |
| 数字签名来源链 | 不是当前核心结构 | 核心能力 |
| Hard Binding | 预留/安全防护可扩展 | 核心 |
| Soft Binding/Manifest recovery | 可通过水印创新扩展 | 已标准化框架 |
| Trust List | 没有 C2PA 同构机制 | C2PA Trust List |
| AI/ML provenance | 主要是输出标识 | 可表达更完整 provenance |

## 6. 对 GCPP 的意义

GCPP 不应该选边站在“中国体系”或“C2PA”之一，而应该设计 Adapter：

```text
GB 45438 / AIGC Metadata Adapter
                ↘
                 GCPP Verification Semantics
                ↗
C2PA Content Credentials Adapter
```

这样：

- 中国平台可以保留法定 `AIGC` 字段；
- 同一资产可额外拥有 C2PA Claim/Signature；
- GCPP RID 可以作为 C2PA soft binding 或中国预留安全防护字段的补充证据；
- Verifier 可以同时报告 regulatory label 与 cryptographic provenance，不把二者混成一个状态。

## 7. 参考资料

- 中国国家互联网信息办公室：《人工智能生成合成内容标识办法》；
- GB 45438—2025《网络安全技术 人工智能生成合成内容标识方法》；
- TC260 服务提供者编码规则；
- TC260 文件元数据隐式标识实践指南；
- DeepSeek、Kimi、豆包、腾讯混元公开用户协议/服务条款。

---

# English

## Summary

As of 2026, the publicly documented baseline for major Chinese generative-AI services is not C2PA. It is China's own regulatory and standards stack: the Measures for Labeling AI-Generated Synthetic Content, mandatory national standard GB 45438—2025, and supporting TC260 implementation guides.

The architecture centers on visible labels, `AIGC` file-metadata fields containing generation status/provider/content identifiers, optional digital watermarks, and platform-side detection/declaration workflows.

Public terms from DeepSeek, Kimi, Doubao, and Tencent Hunyuan explicitly reference compliance with the Chinese labeling rules/standards. This research did not find public evidence that C2PA is the uniform legally required provenance protocol for those Chinese services.

## GCPP implication

GCPP should define both a C2PA adapter and a GB 45438/AIGC metadata adapter. Regulatory AI labeling and cryptographic provenance are different dimensions and should be reported separately.
