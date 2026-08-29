# F0 Semantic-Safety Falsification Harness / F0 语义安全反证 Harness

> 状态 / Status: **Research Prototype / 非规范性实验**  
> 默认语言 / Default language: **简体中文（zh-CN）**

# 简体中文

## 目的

这个 Harness 的目的不是实现“GCPP 协议”，而是反过来验证：

> **GCPP 当前提出的 provenance semantic-safety 问题，是否可以直接使用成熟标准机制表达和执行，从而证明我们不需要自建图模型、规则语言或 Manifest。**

当前第一版使用：

```text
RDF
+
SPARQL CONSTRUCT
+
SPARQL ASK
```

Python 仅负责：

- 加载 RDF test vector；
- 迭代执行 SPARQL `CONSTRUCT` 规则直到 fixed point；
- 使用 `ASK` 查询测试目标 Claim 是否可被保守推导；
- 对照 expected result 输出机器可读报告。

当前**没有 GCPP 自有规则语言**。

## 为什么第一版没有直接使用 SHACL 1.2

F0 理论研究认为 SHACL 1.2 Core / Rules 是很合适的后续实验 substrate。

当前执行环境已经存在：

```text
rdflib 7.5.0
```

但没有 SHACL evaluator，且实验运行环境无法联网安装新的 Python package。因此 V0.1 先使用标准 RDF/SPARQL 完成第一引擎验证。

这个环境限制不得被解释成“需要开发 GCPP 自有规则引擎”。

Issue #12 的退出条件仍要求后续加入**第二个独立 evaluator**，优先尝试 SHACL 1.2 / SHACL Rules 实现。

## 当前 vectors

```text
V1  Scope laundering                         -> NOT_ENTAILED
V2  Safe weakening                           -> ENTAILED
V3  Watermark -> actor authentication        -> NOT_ENTAILED
V4  Model lineage -> output attribution      -> NOT_ENTAILED
V5  Unchecked expected evidence layer        -> COVERAGE_INCOMPLETE
V6  Cross-layer exclusive-origin conflict    -> CONFLICT
V7  Unknown profile -> generic derivation     -> UNKNOWN
V8  Past validity -> current validity         -> NOT_ENTAILED
V9  Normalized equality -> byte equality      -> NOT_ENTAILED
V10 Partial generation -> existential whole   -> ENTAILED only by explicit rule
```

## 运行

要求：

```text
Python >= 3.10
rdflib >= 7.0
```

运行：

```bash
python research/harness/run_vectors.py
```

程序退出码：

```text
0 = all vectors matched expected result
1 = at least one vector disagreed
```

## 当前本地实验结果

2026-08-29 第一轮：

```text
passed: 10
total:  10
```

详见：

- `result-v0.1.json`

注意：

> **10/10 不是 GCPP 假设得到最终证明。**

它只说明第一组极小规则和反例在一个 RDF/SPARQL evaluator 中可复现。

当前还没有满足：

- 第二个独立 evaluator；
- SHACL 1.2 实现；
- C2PA/PROV/VC 等真实 Adapter 输入；
- media-specific Scope selector；
- adversarial profile；
- large corpus；
- formal proof of conservative entailment；
- performance / complexity evaluation。

## 核心实验原则

Harness 必须保持以下纪律：

```text
NO RULE => NO INHERITED POSITIVE VERIFICATION
UNKNOWN PROFILE => UNKNOWN / DOWNGRADE
MISSING QUALIFIER => NEVER SILENTLY WIDEN
NEGATIVE CLAIM => REQUIRES EXPLICIT CLOSED-WORLD/COVERAGE BASIS
```

`rules.rq` 中出现的规则只是当前 test profile 的显式保守规则，不是 GCPP Core ontology。

例如 V10 明确加入：

```text
paragraph generated-by M
+
paragraph part-of document
=> document contains-some-generated-content-by M
```

但没有加入：

```text
paragraph generated-by M
=> whole document generated-by M
```

所以 V1 必须保持 `NOT_ENTAILED`。

## 文件

```text
research/harness/
├── README.md
├── requirements.txt
├── rules.rq
├── vectors.json
├── run_vectors.py
└── result-v0.1.json
```

## 下一步

1. 加入第二个独立 evaluator；
2. 优先建立 SHACL 1.2 equivalent profiles；
3. 将 vectors 拆成 machine-readable fixture 目录；
4. 为每个 vector 增加安全理由和边界说明；
5. 加入真实 C2PA / watermark / regulatory / PROV mapping fixtures；
6. 测试 Adapter 字段全部合法、但 verification semantics 仍发生 amplification 的场景；
7. 如果成熟标准工具已经完整解决这些要求，就停止扩大 GCPP Core。

---

# English

This is a **falsification harness**, not a GCPP protocol implementation.

The purpose is to test whether GCPP's emerging provenance semantic-safety properties can be expressed and executed using mature standards machinery instead of inventing a GCPP graph, rule language, or manifest format.

V0.1 uses RDF plus SPARQL `CONSTRUCT`/`ASK`. A Python runner applies explicit conservative rules to a fixed point and evaluates positive and negative test goals. Ten initial vectors currently pass in one RDFLib-based evaluator.

This does **not** satisfy the F0 exit criteria. A second independent evaluator is still required, preferably using SHACL 1.2 / SHACL Rules. Missing or unknown semantics must always downgrade rather than silently inherit positive verification.
