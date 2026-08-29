#!/usr/bin/env python3
"""A0-R3 generic multi-authority coordination falsification model.

This is NOT an Agent Succession protocol implementation.
It intentionally uses generic authority-owned relationship state,
version/epoch checks, exclusivity constraints and optional atomic groups.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Decision:
    authority: str
    relationship: str
    status: str  # ACK, DENY, REISSUE_REQUIRED, UNAVAILABLE, CONFLICT
    successor: Optional[str] = None
    version: int = 0
    exclusive: bool = False


def evaluate_atomic(decisions, required_relationships, expected_successor=None):
    by_rel = {}
    for decision in decisions:
        by_rel.setdefault(decision.relationship, []).append(decision)

    for relationship in required_relationships:
        if relationship not in by_rel:
            return "UNRESOLVED"

        values = by_rel[relationship]
        if any(x.status == "CONFLICT" for x in values):
            return "CONFLICT"
        if any(x.status == "DENY" for x in values):
            return "ABORT"
        if any(x.status == "UNAVAILABLE" for x in values):
            return "UNRESOLVED"

        if any(x.exclusive for x in values):
            successors = {x.successor for x in values if x.status == "ACK"}
            if len(successors) > 1:
                return "CONFLICT"

        if expected_successor is not None:
            if not any(
                x.status == "ACK" and x.successor == expected_successor
                for x in values
            ):
                return "UNRESOLVED"

    return "COMMIT"


def evaluate_transfer(current_version, request_version, decisions, relationship, successor):
    if request_version < current_version:
        return "REJECT_STALE"

    values = [x for x in decisions if x.relationship == relationship]
    if not values:
        return "UNRESOLVED"
    if any(x.status == "CONFLICT" for x in values):
        return "CONFLICT"
    if any(x.status == "DENY" for x in values):
        return "DENY"
    if any(x.status == "UNAVAILABLE" for x in values):
        return "UNRESOLVED"
    if any(x.status == "REISSUE_REQUIRED" for x in values):
        return "REISSUE_REQUIRED"

    if any(x.exclusive for x in values):
        successors = {x.successor for x in values if x.status == "ACK"}
        if len(successors) > 1:
            return "CONFLICT"

    if any(x.status == "ACK" and x.successor == successor for x in values):
        return "TRANSFERRED"

    return "UNRESOLVED"
