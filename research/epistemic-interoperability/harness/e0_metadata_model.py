"""E0 research prototype.

This is NOT an Epistemic Interoperability protocol implementation.
It intentionally uses ordinary metadata and conservative classification
rules to test whether the first E0 safety vectors require any new primitive.
"""


def classify(d):
    if d.get("late_dependency_discovered"):
        return "ALLOW_ASSESSMENT_DOWNGRADE"
    measure_types = d.get("measure_types", [])
    if len(measure_types) >= 2 and len(set(measure_types)) > 1:
        return "INCOMPARABLE_MEASURES"
    if d.get("calibration_domain") and d.get("current_domain") and d["calibration_domain"] != d["current_domain"]:
        return "OUT_OF_CALIBRATION_DOMAIN"
    if d.get("distribution_shift_detected") and d.get("has_old_calibration"):
        return "DOWNGRADE_OR_RECALIBRATE"
    if d.get("measure_type") == "self_confidence" and not d.get("external_calibration"):
        return "UNVERIFIED_SELF_REPORT"
    if d.get("dependency_metadata_complete") is False:
        return "DO_NOT_ASSUME_INDEPENDENCE"
    if d.get("consumes_prior_judgment") and not d.get("new_external_evidence"):
        return "REDUNDANT_OR_DEPENDENT_SUPPORT"
    if d.get("consensus_changed") and not d.get("new_external_evidence"):
        return "NO_AUTOMATIC_EVIDENCE_GAIN"
    if d.get("same_model") and d.get("evidence_independence_asserted") and len(set(d.get("evidence_ids", []))) > 1:
        return "MODEL_DEPENDENCE_DOES_NOT_ERASE_EVIDENCE_DIVERSITY"
    if d.get("same_evidence") and d.get("different_methods") and d.get("method_error_modes_independent_evidence"):
        return "DEPENDENT_BUT_POSSIBLY_NONZERO_MARGINAL_SUPPORT"
    if d.get("different_models") and d.get("same_evidence"):
        return "DEPENDENT_SUPPORT"
    if d.get("same_model") and d.get("same_evidence") and not d.get("explicit_independence"):
        return "NO_CONFIDENCE_AMPLIFICATION"
    return "UNKNOWN"
