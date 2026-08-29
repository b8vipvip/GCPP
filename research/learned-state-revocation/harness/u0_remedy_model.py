"""U0 research prototype — NOT a revocation/unlearning protocol.

The model tests whether state-specific remedy classes and conservative scope
semantics are sufficient to classify first-round learned-state revocation cases.
"""


RESULTS = {
    "source_deleted_embedding_survives": "RETRIEVAL_REMEDY_REQUIRED",
    "rag_removed_parametric_remains": "MODEL_STATE_NOT_PROVEN_FORGOTTEN",
    "model_unlearned_cache_survives": "DERIVATIVE_REMEDIATION_INCOMPLETE",
    "synthetic_downstream": "POLICY_PROFILE_DECISION_REQUIRED",
    "diffuse_influence": "NO_AUTOMATIC_REMEDY_FROM_LINEAGE_ALONE",
    "public_disclosure": "IRREVERSIBLE_EXTERNAL_DISCLOSURE",
    "offline_backup": "DEFERRED_ERASURE_WITH_CONTROLLED_RETENTION",
    "malicious_downstream": "GLOBAL_COMPLETION_UNRESOLVED",
    "process_receipt": "PROCESS_EXECUTED_NOT_OUTCOME_CERTIFIED",
    "approx_unlearning": "VERIFIED_UNDER_TEST_PROFILE_ONLY",
    "legal_audit_retention": "PARTIAL_REMEDIATION_WITH_DECLARED_EXCEPTION",
    "reingestion": "FUTURE_INGESTION_BLOCK_REQUIRED",
    "federated_stale_replicas": "REPLICA_RECONCILIATION_REQUIRED",
    "unknown_downstream": "KNOWN_SCOPE_COMPLETE_UNIVERSAL_UNKNOWN",
    "anonymous_aggregate": "NO_AUTOMATIC_REMEDY_FROM_DERIVATION",
    "exact_copy_synthetic": "ERASURE_REMEDY_REQUIRED",
}


def classify(case):
    return RESULTS[case]
