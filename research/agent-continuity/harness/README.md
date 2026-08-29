# A0-R2 Succession Falsification Harness / A0-R2 继承反证 Harness

> 状态 / Status: **Research Prototype / 非规范性实验**  
> 日期 / Date: **2026-08-29**

## 目的

这个 Harness 不实现 Agent Continuity Protocol。

它故意使用极小的通用机制测试：

```text
relationship authority acknowledgement
+
monotonic fencing epoch
```

是否已经足以表达 A0-R2 的关键安全默认。

如果可以，则这些安全性质不能被用来证明需要新的 wire protocol。

## 当前模型

每个 external relationship 暂时建模为：

```text
relationship {
  id
  kind
  holder
  authority
  epoch
  exclusive
  transferable
}
```

其中 `authority` 是有权决定该 relationship 是否可转移/重发/终止的外部主体或域。

### 转移默认

```text
no authority acknowledgement
=> UNRESOLVED_NO_AUTHORITY_ACK
```

不是：

```text
predecessor names successor
=> relationship transferred
```

### 独占关系

```text
exclusive relationship
+
assigned to >1 successors
=> REJECT_AUTHORITY_MULTIPLICATION
```

### 不可转移评价

例如 reputation：

```text
transferable = false
=> REISSUE_REQUIRED
```

即使原 evaluator 愿意承认 successor，也应该生成对新 subject 的新 assessment，而不是复制旧状态。

### Rollback / stale instance

```text
presented_epoch < authoritative_current_epoch
=> REJECT_STALE_EPOCH
```

这是普通 fencing semantics，不是 A0 自有 primitive。

## V0.1 vectors

```text
R2-V1  fork without authority acknowledgement
R2-V2  duplicate exclusive grant to two fork children
R2-V3  rollback stale epoch
R2-V4  merge without fresh privilege acknowledgement
R2-V5  obligation must not silently disappear
R2-V6  obligation explicitly acknowledged to successor
R2-V7  reputation requires reissue
R2-V8  provider-scoped grant after provider shutdown remains unresolved
```

第一轮结果：

```text
passed: 8
 total: 8
```

## 运行

```bash
python research/agent-continuity/harness/r2_transition_model.py
```

仅依赖 Python 标准库。

## 解释边界

8/8 只说明：

> 当前这组保守 succession safety rules 可以用通用 external-authority + fencing 模型表达。

它**不证明**：

- 一个新公共协议已经必要；
- relationship authority 模型已经足够；
- 真实 OAuth / VC / ODRL / A2A systems 会自动互操作；
- 多 issuer 并发 succession 已解决；
- provider shutdown 后 trust recovery 已解决。

下一轮应该尝试使用真实现有 artifacts/profile 表达相同 vectors，而不是增加 A0 自有语法。

## 文件

```text
README.md
r2_transition_model.py
r2_vectors.json
r2_result-v0.1.json
```

## Kill Criteria

如果 R3 能直接使用：

```text
JWS / COSE / VC transition event
OAuth / capability reissuance
ODRL duty records
VC/status/reputation reissuance
ordinary durable receipts
```

实现 multi-issuer fork/merge/provider-exit，并且只需要通用 profile conventions，则应停止开发独立 Agent Continuity wire protocol。