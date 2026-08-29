"""E0-R2 research prototype.

No E0 protocol is implemented here. The model tests whether hidden-dependency
cases can be handled conservatively using generic scoped claims, attestations,
provenance and receiver policy.
"""


def classify(v):
    if v.get("late_dependency_discovered"):
        return "REASSESS_AND_DOWNGRADE"
    if v.get("calibration_domain") and v.get("current_domain") and v["calibration_domain"] != v["current_domain"]:
        return "OUT_OF_SCOPE_RECALIBRATE"
    if v.get("correlation_certificate") and v.get("certificate_drifted"):
        return "STALE_CERT_DOWNGRADE"
    if v.get("verified_overlap_bound") is not None:
        return "BOUNDED_DEPENDENCE_DISCLOSURE"
    if v.get("consumed_peer_judgment"):
        return "DYNAMIC_DEPENDENCE"
    if v.get("independence_claim") and not v.get("independence_evidence"):
        return "UNVERIFIED_INDEPENDENCE_CLAIM"
    if v.get("dependency_omitted") or v.get("hidden_shared_factor") or v.get("dependency_unknown"):
        return "UNKNOWN_DEPENDENCE_NO_AMPLIFICATION"
    if v.get("high_stakes") and not v.get("dependence_assurance"):
        return "ABSTAIN_OR_SINGLE_SOURCE_BOUND"
    return "UNKNOWN"
