# GPTAuto v0.2 — GCPP

## 中文（默认）

本仓库内嵌 GPTAuto v0.2。GitHub 工程任务默认采用最终目标驱动协议：

    GOAL → PLAN / DoD → EXECUTE selected Dynamic Gates → VERIFY DoD → DONE

用户无需每次额外声明“使用 GPTAuto”，只需说明最终目标。Commit、PR、CI、Merge、Release、Deploy 是否必要由任务专属 DoD 决定。默认分支为 `main`。项目自身 CI/Build/Release（若存在）作为动态 Gate 能力使用；旧的通用 Actions Governor / Policy Check / Recovery / Housekeeping 不属于本集成。

只有权限/凭据缺失、重大产品决策歧义、未授权高风险破坏操作、修复预算耗尽或不可修复平台条件才进入 BLOCKED。

## English

GCPP embeds GPTAuto v0.2 and uses goal-bound GitHub engineering semantics by default. Users state the final outcome; GPTAuto derives task-specific DoD and Dynamic Gates, executes only the required gates, verifies evidence, and then enters DONE.
