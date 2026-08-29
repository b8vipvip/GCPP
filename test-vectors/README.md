# GCPP Conformance Test Vectors

Status: **Initial test plan**

This directory defines interoperability cases that every GCPP verifier should eventually be able to evaluate consistently. Concrete serialized fixtures will be added after the first Internet deployment profile fixes canonical encoding and baseline algorithms.

## 1. Purpose

Test vectors are part of the standards contract. They prevent two implementations from interpreting the same provenance record differently.

Vectors MUST include negative and ambiguous cases, not only valid originals.

## 2. Required Core cases

### TV-CORE-001 — valid original

Inputs:

- structurally valid signed record;
- trusted actor verification material under the chosen test policy;
- exact subject binding matches;
- no unknown critical extension.

Expected presentation label: `VERIFIED_ORIGINAL`.

Expected vector highlights:

```text
record_signature = VALID
actor_authentication = VALID
exact_integrity = VALID
```

### TV-CORE-002 — one-byte or one-character modification

Record signature remains valid over the historical record, but current exact content binding fails.

Expected: MUST NOT be `VERIFIED_ORIGINAL`.

If no partial binding exists, current-content attribution is insufficient even though the historical record is authentic.

### TV-CORE-003 — valid derivative with parent

A signed child record refers to a valid parent and binds to the current subject.

Expected: `VERIFIED_DERIVATIVE` when the transformation relationship validates.

### TV-CORE-004 — partial copy

Only selected source segments appear in a larger current document.

Expected: `PARTIAL_PROVENANCE`; authenticated coverage must not include unmatched text.

### TV-CORE-005 — forged signature

Record syntax and content binding appear plausible but signature is invalid.

Expected:

```text
record_signature = INVALID
```

No verified actor attribution.

### TV-CORE-006 — recovered RID, unrelated content

A valid RID/watermark locator from generation A is inserted into unrelated content B.

Expected:

```text
locator_state = LOCATOR_RECOVERED
exact_integrity != VALID
```

Presentation MUST NOT attribute all of B to A. Expected label is `LOCATOR_ONLY` or an equivalent insufficient-attribution state.

### TV-CORE-007 — ambiguous RID

RID resolves to multiple signed records.

Expected:

```text
locator_state = LOCATOR_AMBIGUOUS
```

Content bindings may disambiguate. Without sufficient binding, no generation attribution.

### TV-CORE-008 — unknown non-critical extension

Expected: Core verification continues; extension is reported unsupported.

### TV-CORE-009 — unknown critical extension

Expected: affected claim is `UNSUPPORTED`; content is not labeled fake.

### TV-CORE-010 — provider signature valid, no history evidence

Expected:

```text
record_signature = VALID
historical_evidence = NOT_PRESENT
```

The verifier must not conflate these dimensions.

### TV-CORE-011 — invalid transparency/anchor evidence

Provider signature and content binding valid, optional historical proof invalid.

Expected: provenance authentication and historical assurance reported separately.

### TV-CORE-012 — revoked/compromised current key, valid historical key

The generation predates key compromise and the profile provides historical key validity evidence.

Expected: historical verification follows the key-lifecycle profile rather than treating every old record as automatically invalid.

### TV-CORE-013 — cycle in provenance graph

Expected: lineage invalid/diagnostic cycle detected. Individual independently signed records can retain their own signature states.

### TV-CORE-014 — missing parent

Child signature valid but one parent record unavailable.

Expected: availability/missing-lineage diagnostic rather than forged-content conclusion.

### TV-CORE-015 — provider model declaration only

Valid provider signature claims model `M` but no execution attestation exists.

Expected:

```text
model_assurance = MODEL_DECLARED
```

MUST NOT become `MODEL_EXECUTION_PROVEN`.

## 3. Text-profile cases

### TV-TEXT-001 — rich copy preserves full proof

Clipboard includes plain text plus structured GCPP provenance carrier. Expected full proof resolution without watermark dependence.

### TV-TEXT-002 — plain-text copy strips metadata

Only visible text survives. Robust locator is recovered and then authenticated through signed record plus content binding.

### TV-TEXT-003 — Unicode auxiliary carrier stripped

Visible text and robust locator remain. Expected: auxiliary carrier loss does not imply malicious tampering.

### TV-TEXT-004 — small substitutions

Exact normalized-text digest fails; registered locator scheme recovers RID; segment evidence identifies surviving content.

Expected label depends on authenticated coverage, normally `VERIFIED_DERIVATIVE` or `PARTIAL_PROVENANCE`.

### TV-TEXT-005 — paragraph deletion

Surviving segments authenticate; deleted material is absent.

Expected: coverage calculated only over current authenticated material according to the profile-defined denominator.

### TV-TEXT-006 — unrelated insertion

Original AI text remains as one portion of a larger document.

Expected: inserted content remains unauthenticated; no whole-document attribution.

### TV-TEXT-007 — low-entropy code output

Record declares `capacity.low-entropy-unavailable`; attached proof is valid.

Expected: provenance can still be `VERIFIED_ORIGINAL` without an in-band locator.

### TV-TEXT-008 — very short text

No full RID capacity. Metadata/attached proof absent.

Expected: `UNVERIFIED` or coarse carrier state according to the selected profile; MUST NOT infer human authorship.

### TV-TEXT-009 — full paraphrase/re-generation

No sufficient carrier or content binding survives.

Expected: `UNVERIFIED`.

## 4. Privacy cases

### TV-PRIV-001 — generation identifier inspection

GID must not encode account ID, IP address, device ID, or geographic location.

### TV-PRIV-002 — raw prompt absent

Baseline public record contains no raw prompt.

### TV-PRIV-003 — randomized input commitment

Enterprise profile binds an input using randomized commitment; public record does not disclose the input.

## 5. Presentation-semantic cases

Conformance tests SHOULD check API/UI labels in addition to cryptography.

Forbidden semantic mappings include:

```text
UNVERIFIED -> "human-written"
UNVERIFIED -> "fake"
VERIFIED -> "true"
LOCATOR_RECOVERED -> "generated by provider X"
```

without the additional evidence required by GCPP-VERIFY.

## 6. Future fixture format

Once the first canonical serialization profile is selected, each machine-readable vector should contain:

```text
id
profile
input_content
records
evidence
trust_policy
expected_verification_vector
expected_label
notes
```

Fixtures should be deterministic and usable across languages.
