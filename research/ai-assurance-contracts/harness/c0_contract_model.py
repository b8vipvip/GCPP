"""C0 research prototype — NOT a protocol implementation.

Tests whether generic contract metadata and conservative applicability checks
are sufficient for first-round AI assurance-contract safety vectors.
"""


def classify(v):
    if v.get("benchmark_contaminated"):
        return "EVIDENCE_INVALIDATED_REASSESS_REQUIRED"
    if v.get("late_assumption_violation"):
        return "POSTHOC_INVALIDATION_EXTERNAL_EFFECT_REMAINS"
    if v.get("exact_component_state") != v.get("assured_component_state"):
        return "CONTRACT_STALE_REASSESS_REQUIRED"
    if v.get("prompt_tool_state_changed"):
        return "COMPONENT_STATE_CHANGED_REASSESS_REQUIRED"
    if v.get("runtime_domain") and v.get("assured_domain") and v["runtime_domain"] != v["assured_domain"]:
        return "ASSUMPTION_VIOLATED"
    if v.get("dependency_changed"):
        return "DEPENDENCY_ASSUMPTION_VIOLATED"
    if v.get("required_assumptions", 0) > v.get("verified_assumptions", 0):
        return "ASSUMPTION_UNVERIFIED_GUARANTEE_NOT_ESTABLISHED"
    if v.get("metric_semantics_compatible") is False:
        return "METRIC_INCOMPARABLE"
    if v.get("guarantee_scope") and v.get("use_scope") and v["guarantee_scope"] != v["use_scope"]:
        return "GUARANTEE_SCOPE_MISMATCH"
    if v.get("self_evaluated") and not v.get("independent_evidence"):
        return "EVIDENCE_SELF_ASSERTED"
    if v.get("compose") and not v.get("composition_rule_valid"):
        return "NO_VALID_COMPOSITION_RULE"
    if v.get("compose") and v.get("composition_rule_valid"):
        return "COMPOSE_USING_DECLARED_RULE"
    return "GUARANTEE_APPLICABLE"
