#!/usr/bin/env python3
"""A0-R4 research evaluator.

This is intentionally NOT an Agent Continuity protocol implementation.
It only checks whether conservative R4 outcomes can be expressed using generic
signed-evidence, version/epoch, quorum and open-world safety semantics.
"""

import json
from pathlib import Path


def evaluate(v):
    t = v["type"]

    if t == "equivocation_visible":
        if v["exclusive"] and v["all_signatures_valid"] and len(set(v["successors"])) > 1:
            return "CONFLICT_SIGNED_EQUIVOCATION"

    if t == "equivocation_isolated":
        return "LOCALLY_VALID_GLOBALLY_UNKNOWN"

    if t == "unknown_authority_set":
        return (
            "EVALUATE_CLOSED_SET"
            if v["closed_world_authority_set"]
            else "INCOMPLETE_UNKNOWN_AUTHORITY_SET"
        )

    if t == "dynamic_authority_epoch":
        return (
            "REJECT_STALE_POLICY_EPOCH"
            if v["decision_epoch"] < v["current_epoch"]
            else "EVALUATE"
        )

    if t == "no_shared_clock":
        return (
            "ORDER_BY_VERSION_NOT_WALLCLOCK"
            if v["has_monotonic_version"]
            else "ORDER_UNRESOLVED"
        )

    if t == "network_partition":
        return (
            "COMMIT"
            if v["acks_seen"] >= v["required_acks"]
            else "PENDING_PRESERVE_SAFETY"
        )

    if t == "malicious_coordinator":
        if v["participant_signatures_required"] and not v["has_required_participant_signatures"]:
            return "NO_FALSE_COMMIT"
        return "COMMIT"

    if t == "split_view_log":
        return (
            "SPLIT_VIEW_REQUIRES_GOSSIP_OR_WITNESS"
            if v["inconsistent_signed_tree_heads"]
            else "NO_SPLIT_VIEW_EVIDENCE"
        )

    if t == "different_trust_policies":
        return "POLICY_DIVERGENCE_NOT_PROTOCOL_CONFLICT"

    if t == "late_discovered_relationship":
        return "PRIOR_COMPLETION_WAS_SCOPE_LIMITED"

    if t == "bft_quorum":
        n = v["n"]
        f = v["f"]
        signatures = v["matching_signatures"]
        return "QUORUM_ACCEPT" if n >= 3 * f + 1 and signatures >= 2 * f + 1 else "NO_QUORUM"

    if t == "indispensable_authority_gone":
        return "UNRESOLVED_NO_AUTHORITY"

    raise ValueError(f"unknown vector type: {t}")


def main():
    base = Path(__file__).resolve().parent
    data = json.loads((base / "r4_vectors.json").read_text(encoding="utf-8"))
    out = []
    passed = 0
    for vector in data["vectors"]:
        actual = evaluate(vector)
        ok = actual == vector["expected"]
        passed += int(ok)
        out.append({
            "id": vector["id"],
            "expected": vector["expected"],
            "actual": actual,
            "pass": ok,
        })

    result = {
        "status": "research-prototype",
        "date": "2026-08-29",
        "model": "generic signed-evidence + epoch/version + quorum + open-world conservative semantics",
        "passed": passed,
        "total": len(out),
        "vectors": out,
        "interpretation": (
            "Matching vectors shows only that the tested R4 safety outcomes can be expressed "
            "without an Agent-specific wire protocol. It does not implement cryptography, "
            "transparency gossip, BFT consensus, authority discovery or cross-implementation interoperability."
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
