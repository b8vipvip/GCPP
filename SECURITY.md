# 安全策略 / Security Policy

> **默认语言：简体中文（zh-CN）**。中文完整版本在前，英文完整镜像在后。
>
> **Default language: Simplified Chinese (zh-CN).** The complete Chinese version appears first, followed by the complete English mirror.

## 简体中文

GCPP 是一个安全敏感的协议项目。来源证明失败可能导致错误归属、隐私泄露、历史重写，或让用户对内容标签产生危险的过度信任。

### 范围

安全报告可以涉及：

- 签名或 key-confusion 攻击；
- canonicalization 不一致；
- content-binding 绕过；
- RID/watermark spoofing 或 transplant 攻击；
- false-positive attribution；
- parser 歧义或 downgrade 行为；
- provenance graph 混淆；
- privacy/linkability 失败；
- transparency/history equivocation；
- revocation/key-lifecycle 失败；
- 会导致不同实现产生不同结论的 conformance vectors 问题。

### 报告方式

在仓库配置专门的私密安全报告通道之前，不要在公开 Issue 中发布针对尚未修复实现的可武器化漏洞细节。可以创建一个不包含敏感漏洞材料的最小 Issue，请求建立私密联系渠道。

不会立即暴露具体实现漏洞的规范级弱点，可以通过公开设计 Issue 讨论。

### 安全原则

符合规范的实现应假设：

- transport 和 resolver 可能是恶意的；
- metadata 和 sidecar 可能消失；
- watermark 可能被研究、复制或删除；
- Provider 或 Provider key 可能被攻破；
- 外部 Evidence System 可能失效或分叉；
- 算法可能过时；
- 用户和 UI 可能错误理解协议标签。

因此，GCPP 使用分层证据并暴露多个 assurance dimension，而不是提供一个通用的单一 trust bit。

### 不是真相裁判

一个关键语义安全属性是：provenance 不认证 factual truth。安全审查应把任何将 `VERIFIED` 映射为“事实为真”，或把 `UNVERIFIED` 映射为“虚假”的 UI/API 行为视为协议误用；这种误用可能造成严重下游后果。

---

# English

GCPP is a security-sensitive protocol project. Provenance failures can cause false attribution, privacy leakage, history rewriting, or dangerous overconfidence in content labels.

## Scope

Security reports may concern:

- signature or key-confusion attacks;
- canonicalization inconsistencies;
- content-binding bypasses;
- RID/watermark spoofing or transplant attacks;
- false-positive attribution;
- parser ambiguity or downgrade behavior;
- provenance graph confusion;
- privacy/linkability failures;
- transparency/history equivocation;
- revocation/key-lifecycle failures;
- conformance vectors that would cause implementations to disagree.

## Reporting

Until a dedicated private security-reporting channel is configured for the repository, avoid publishing weaponized exploit details for an unpatched implementation in a public issue. Open a minimal issue requesting a private contact path without including sensitive exploit material.

Specification-level weaknesses that do not expose an immediate implementation vulnerability can be discussed publicly through design issues.

## Security principles

A conforming implementation should assume:

- transports and resolvers can be malicious;
- metadata and sidecars can disappear;
- watermarks can be studied, copied, or removed;
- providers or provider keys can be compromised;
- external evidence systems can fail or fork;
- algorithms can become obsolete;
- users and UIs can misinterpret protocol labels.

Accordingly, GCPP uses layered evidence and exposes assurance dimensions instead of one universal trust bit.

## No truth oracle

A critical semantic safety property is that provenance does not certify factual truth. Security reviews should treat any UI/API behavior that maps `VERIFIED` to factual truth or `UNVERIFIED` to falsity as a protocol misuse with potentially serious downstream consequences.
