#!/usr/bin/env python3
"""A0-R2 succession falsification harness.

Research prototype only. This deliberately uses generic relationship authority
acknowledgement plus fencing semantics instead of defining an Agent Continuity
wire protocol.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import sys
from typing import Any


ROOT = Path(__file__).resolve().parent


@dataclass
class Relationship:
    rid: str
    kind: str
    holder: str
    authority: str
    epoch: int = 0
    exclusive: bool = False
    transferable: bool = True
    provider_scoped: bool = False


def transfer(
    rel: Relationship,
    successors: list[str],
    acknowledger: str | None,
    assigned: list[str],
) -> str:
    """Evaluate conservative relationship succession.

    A predecessor declaration alone cannot transfer an externally-defined
    relationship. The relationship authority must acknowledge it.
    """
    if acknowledger != rel.authority:
        return "UNRESOLVED_NO_AUTHORITY_ACK"

    if rel.exclusive and len(assigned) > 1:
        return "REJECT_AUTHORITY_MULTIPLICATION"

    if any(successor not in successors for successor in assigned):
        return "REJECT_UNKNOWN_SUCCESSOR"

    if not rel.transferable and assigned:
        return "REISSUE_REQUIRED"

    if not assigned:
        return "TERMINATED_OR_UNASSIGNED"

    return "TRANSFERRED"


def fenced_action(current_epoch: int, presented_epoch: int) -> str:
    """Reject stale rollback/fork instances at the resource boundary."""
    return "ACCEPT" if presented_epoch >= current_epoch else "REJECT_STALE_EPOCH"


def evaluate(vector: dict[str, Any]) -> str:
    operation = vector["operation"]

    if operation == "transfer":
        rel = Relationship(**vector["relationship"])
        return transfer(
            rel,
            vector["successors"],
            vector.get("acknowledger"),
            vector.get("assigned", []),
        )

    if operation == "fenced_action":
        return fenced_action(vector["current_epoch"], vector["presented_epoch"])

    raise ValueError(f"unknown operation: {operation}")


def main() -> int:
    payload = json.loads((ROOT / "r2_vectors.json").read_text(encoding="utf-8"))

    rows: list[dict[str, Any]] = []
    passed = 0

    for vector in payload["vectors"]:
        actual = evaluate(vector)
        ok = actual == vector["expected"]
        passed += int(ok)
        rows.append(
            {
                "id": vector["id"],
                "expected": vector["expected"],
                "actual": actual,
                "pass": ok,
            }
        )

    report = {
        "status": "research-prototype",
        "model": "relationship-authority + fencing",
        "passed": passed,
        "total": len(rows),
        "vectors": rows,
        "interpretation": (
            "Passing vectors only demonstrates that conservative succession "
            "safety can be modeled with generic relationship authority and "
            "fencing semantics. It does not establish a need for a new Agent "
            "Continuity protocol."
        ),
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
