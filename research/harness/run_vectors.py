#!/usr/bin/env python3
"""F0 semantic-safety falsification harness.

This is a research runner, not a GCPP protocol implementation.
It intentionally reuses RDF/SPARQL instead of defining a GCPP rule language.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from rdflib import Graph


ROOT = Path(__file__).resolve().parent


def load_rules(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [chunk.strip() for chunk in text.split("---RULE---") if chunk.strip()]


def apply_rules(graph: Graph, rules: list[str], max_rounds: int = 16) -> int:
    """Apply SPARQL CONSTRUCT rules to a fixed point.

    Returns the number of evaluation rounds. A missing rule means no positive
    inference is invented; this is deliberate for the F0 non-amplification test.
    """
    for round_no in range(max_rounds):
        before = len(graph)
        for rule in rules:
            result = graph.query(rule)
            result_graph = getattr(result, "graph", None)
            if result_graph is not None:
                for triple in result_graph:
                    graph.add(triple)
        if len(graph) == before:
            return round_no + 1
    raise RuntimeError("rule evaluation did not reach a fixed point")


def turtle_prefixes_to_sparql(prefixes: str) -> str:
    return prefixes.replace("@prefix ", "PREFIX ").replace(" .\n", "\n")


def ask(graph: Graph, prefixes: str, query: str) -> bool:
    result = graph.query(turtle_prefixes_to_sparql(prefixes) + query)
    return bool(result.askAnswer)


def main() -> int:
    payload = json.loads((ROOT / "vectors.json").read_text(encoding="utf-8"))
    rules = load_rules(ROOT / "rules.rq")
    prefixes = payload["prefixes"]

    passed = 0
    rows = []

    for vector in payload["vectors"]:
        graph = Graph()
        graph.parse(data=prefixes + vector["input"], format="turtle")

        rounds = apply_rules(graph, rules)
        query_true = ask(graph, prefixes, vector["ask"])
        actual = vector["true_result"] if query_true else vector["false_result"]
        ok = actual == vector["expected"]
        passed += int(ok)

        rows.append(
            {
                "vector_id": vector["id"],
                "expected": vector["expected"],
                "actual": actual,
                "pass": ok,
                "triples": len(graph),
                "rule_rounds": rounds,
            }
        )

    report = {"passed": passed, "total": len(rows), "vectors": rows}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
