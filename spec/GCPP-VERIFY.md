# GCPP Verification Semantics 0.1

Status: **Working Draft**

This document defines how conforming verifiers interpret GCPP claims and evidence. It is intentionally policy-neutral.

## 1. Verification is a vector, not a verdict

A verifier MUST compute independent dimensions before deriving a human-readable label. A single boolean result is insufficient for GCPP conformance.

Minimum dimensions:

```text
actor_authentication
record_signature
model_assurance
exact_integrity
partial_integrity
authenticated_coverage
locator_state
lineage_state
historical_evidence
unsupported_critical_features
```

## 2. Common state vocabulary

Unless a registered profile defines a more specific vocabulary, dimensions SHOULD use:

- `VALID`
- `INVALID`
- `UNVERIFIED`
- `UNSUPPORTED`
- `NOT_PRESENT`
- `PARTIAL`

Model assurance uses:

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

Locator state uses:

- `LOCATOR_NOT_PRESENT`
- `LOCATOR_DETECTED`
- `LOCATOR_PARTIAL`
- `LOCATOR_RECOVERED`
- `LOCATOR_AMBIGUOUS`

## 3. Verification order

A verifier SHOULD follow this logical order:

1. Parse the record and reject structurally malformed mandatory fields.
2. Evaluate unknown critical extensions.
3. Resolve or load actor verification material.
4. Verify the provenance-record signature.
5. Evaluate actor identity evidence separately from signature validity.
6. Evaluate exact content bindings against the presented subject.
7. Evaluate partial or segment bindings when available.
8. Evaluate parent references and provenance DAG consistency.
9. Evaluate watermark/locator recovery as discovery evidence only.
10. Evaluate historical evidence such as timestamps, transparency inclusion, witnesses, or anchors.
11. Evaluate optional execution/attestation evidence.
12. Emit a `VerificationVector`.
13. Derive a presentation label without changing the underlying vector.

## 4. Signature semantics

A valid record signature establishes that the holder of the relevant signing key signed the canonical record. It does not, by itself, establish:

- legal identity;
- factual truth;
- model execution correctness;
- user identity;
- historical timestamp;
- current-content identity.

Those require separate evidence dimensions.

## 5. Identity semantics

`actor_authentication = VALID` means the verifier's selected identity method and local trust policy support the actor binding.

A verifier MUST expose the identity method and SHOULD expose the basis of trust. It MUST NOT silently turn a provider-controlled key into a stronger real-world identity claim than the available evidence supports.

## 6. Exact integrity

`exact_integrity = VALID` means at least one profile-designated exact content binding matches the presented content under the specified normalization profile.

`exact_integrity = INVALID` means the presented content does not exactly match that binding. It does not invalidate a valid signature over the historical record and does not erase partial provenance.

## 7. Partial integrity and coverage

When segment/chunk evidence exists, a verifier SHOULD calculate authenticated coverage over a profile-defined denominator.

Coverage MUST identify only material that can be bound to authenticated provenance. It MUST NOT extrapolate from a small surviving fragment to the entire document.

If only 5% of a current document is authenticated to a source generation, the verifier MUST NOT label the whole document as an original output of that source.

## 8. Locator semantics

A watermark or locator can help recover a candidate RID or record reference. The following rule is normative:

> A recovered locator is never sufficient for actor or generation attribution.

Attribution requires at least a valid signed record and a sufficient content relationship under the relevant profile.

A locator transplanted into unrelated content SHOULD result in `LOCATOR_RECOVERED` plus failed/insufficient content binding, not a verified attribution.

## 9. Historical evidence

Historical evidence is evaluated independently from signature validity.

Examples:

- signed transparency checkpoint;
- inclusion/consistency proof;
- timestamp proof;
- witness quorum;
- blockchain or distributed-ledger anchor;
- hardware append-only log.

A record can have a valid provider signature and no historical evidence. In that case the verifier MUST report that distinction rather than failing the entire provenance record.

## 10. Lineage

A verifier MUST support multiple parents and detect obvious cycles in the provenance DAG.

A child event does not retroactively alter the validity of a parent record. Missing parents MAY reduce lineage assurance but MUST NOT automatically invalidate an otherwise valid signed child record.

## 11. Derived presentation labels

The following labels are RECOMMENDED for interoperable user interfaces.

### VERIFIED_ORIGINAL

Minimum conditions:

- record signature valid;
- actor authentication valid under the selected trust policy;
- exact content binding valid;
- no unresolved critical feature affects the claim.

Historical evidence and model assurance SHOULD be shown separately and are not implicitly upgraded by this label.

### VERIFIED_DERIVATIVE

Use when:

- a valid signed provenance path exists;
- the current content is not an exact match to the original source event;
- the current subject has a verified derivation relationship or substantial authenticated partial relationship.

### PARTIAL_PROVENANCE

Use when only part of the current content can be cryptographically or structurally bound to one or more valid provenance records.

The UI SHOULD show authenticated coverage when meaningful.

### LOCATOR_ONLY

Use when a recovery carrier or watermark indicates provenance material but authentication or content binding is insufficient or unavailable.

### UNVERIFIED

Use when GCPP cannot establish sufficient provenance.

Normative interpretation:

```text
UNVERIFIED != HUMAN
UNVERIFIED != FAKE
UNVERIFIED != ILLEGAL
UNVERIFIED != LOW_QUALITY
```

## 12. Truth separation

No GCPP label means that content is factually correct. UIs and APIs MUST keep provenance state separate from fact-checking, moderation, copyright, plagiarism, academic-integrity, or legal-status systems.

Normative interpretation:

```text
VERIFIED != TRUE
```

## 13. Local policy

Different applications MAY apply different trust policies to actor identity, acceptable algorithms, evidence age, or required historical assurance. The raw verification vector SHOULD remain available so that local policy does not masquerade as protocol fact.

## 14. Diagnostics

A verifier SHOULD provide machine-readable diagnostics for failures such as:

- malformed record;
- unsupported critical extension;
- invalid signature;
- unresolved actor key;
- exact content mismatch;
- insufficient partial coverage;
- ambiguous locator;
- broken lineage reference;
- stale/revoked verification key;
- historical evidence unavailable;
- evidence proof invalid.

Diagnostics MUST avoid declaring content fake solely because provenance verification failed.
