#!/usr/bin/env python3
"""Run A0-R3 multi-authority succession falsification vectors."""

import json
from pathlib import Path

from r3_coordination_model import Decision, evaluate_atomic, evaluate_transfer

ROOT = Path(__file__).resolve().parent


def parse_decision(payload):
    return Decision(
        authority=payload["authority"],
        relationship=payload["relationship"],
        status=payload["status"],
        successor=payload.get("successor"),
        version=payload.get("version", 0),
        exclusive=payload.get("exclusive", False),
    )


def main():
    payload = json.loads((ROOT / "r3_vectors.json").read_text(encoding="utf-8"))
    rows = []
    passed = 0

    for vector in payload["vectors"]:
        decisions = [parse_decision(x) for x in vector["decisions"]]

        if vector["mode"] == "atomic":
            actual = evaluate_atomic(
                decisions,
                vector["required_relationships"],
                vector.get("expected_successor"),
            )
        elif vector["mode"] == "transfer":
            actual = evaluate_transfer(
                vector["current_version"],
                vector["request_version"],
                decisions,
                vector["relationship"],
                vector["successor"],
            )
        else:
            raise ValueError(f"unknown mode: {vector['mode']}")

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

    report = {"passed": passed, "total": len(rows), "vectors": rows}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed == len(rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
