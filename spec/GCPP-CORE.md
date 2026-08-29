# GCPP Core 0.1

Status: **Working Draft**  
Intended track: public, implementation-agnostic provenance standard.

## 1. Scope

GCPP defines interoperable semantics for verifiable digital-content provenance. It standardizes four durable questions:

1. **Identity** — which actor made a provenance claim?
2. **Provenance** — which generation or transformation events produced the current subject?
3. **Integrity** — how does the current subject relate to the content bound by those events?
4. **Evidence** — which verifiable artifacts support the identity, event, integrity, and history claims?

GCPP does not define factual truth, legality, quality, authorship policy, copyright ownership, moderation outcomes, or whether unverified content is human-created.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described by BCP 14 when, and only when, they appear in all capitals.

## 2. Architectural invariants

A conforming GCPP Core implementation MUST preserve these invariants:

- `VERIFIED` provenance MUST NOT be presented as factual truth.
- `UNVERIFIED` provenance MUST NOT be presented as proof that content is human, fake, illegal, malicious, or low quality.
- A watermark or recoverable locator MUST NOT by itself authenticate an actor or generation event.
- Public provenance MUST NOT require a user account identifier, IP address, device identifier, email address, phone number, or raw prompt.
- Core verification MUST NOT require one globally privileged online verification service.
- GCPP Core MUST remain independent of any single storage system, transport protocol, identity system, hash function, signature algorithm, watermark algorithm, evidence ledger, AI architecture, provider, platform, government, or jurisdiction.
- Partial and transformed provenance MUST be first-class states; implementations MUST NOT collapse every result to an AI/non-AI boolean.
- Policy decisions MUST remain outside the GCPP cryptographic verification result.

## 3. Layer model

GCPP separates five logical layers:

1. **Identity** — actors, identifiers, verification methods, key history.
2. **Provenance** — events and their parent relationships.
3. **Evidence** — signatures, watermarks, transparency proofs, timestamps, attestations, and future proof types.
4. **Verification** — deterministic evaluation of the available claims and evidence.
5. **Presentation** — human-readable labels derived from the verification vector.

Physical infrastructure such as databases, blockchains, transparency logs, P2P stores, HTTP endpoints, local files, or cloud systems is outside GCPP Core.

## 4. Actor

An `Actor` is an entity that makes a provenance claim. Examples include an AI provider, organization, human author, editing application, camera, autonomous agent, or hardware device.

An actor is identified by an abstract identifier:

```text
ActorIdentifier {
  method
  identifier
}
```

GCPP Core does not mandate DID, X.509, domain keys, raw public keys, or any future identity method. Identity methods are registered and versioned independently.

A verifier MUST distinguish cryptographic control of an identifier from claims about a real-world legal or brand identity.

## 5. Provenance event

A `ProvenanceEvent` represents one asserted content-state transition. Event types are registry values and can include generation, human edit, AI rewrite, translation, summarization, composition, rendering, transcoding, publication, capture, or future transformations.

Events form a directed acyclic graph (DAG). Multiple parents MUST be supported.

Each event has an opaque event identifier. AI generation events SHOULD use a high-entropy, non-user-derived `GenerationID`.

## 6. Generation identity and recovery locator

A `GenerationID` identifies one asserted generation event.

A `RecoveryLocator` (RID) is a compact discovery value that MAY be embedded in a robust carrier such as a text watermark. The RID:

- MUST NOT be treated as authentication;
- MAY be shorter than the GenerationID;
- MAY be partial or collision-prone;
- MAY resolve to multiple candidate records;
- MUST be followed by signature and content-binding verification before attribution.

This separation prevents short or low-entropy content from being forced to carry a complete cryptographic identity.

## 7. Provenance record

The abstract GCPP record contains:

```text
ProvenanceRecord {
  version
  event {
    id
    type
    time?
  }
  actor {
    identifier
  }
  subject {
    media_type
    bindings[]
  }
  model_claim?
  parents[]
  carriers[]
  evidence[]
  extensions[]
}
```

Serialization is defined by deployment profiles, not by Core. A signature is computed over a profile-defined canonical encoding of the record.

## 8. Model claim

A model claim is an assertion, not automatically a proof of model execution.

```text
ModelClaim {
  public_model_id
  model_family?
  model_commitment?
}
```

Verification MUST distinguish at least:

- `MODEL_NONE`
- `MODEL_DECLARED`
- `MODEL_ATTESTED`
- `MODEL_EXECUTION_PROVEN`

A provider signature can establish `MODEL_DECLARED`. Stronger states require additional registered evidence such as hardware attestation or verifiable execution proof.

## 9. Content binding

A record MUST be able to bind to content without hard-coding a single hash function or representation.

```text
ContentBinding {
  binding_type
  algorithm
  normalization_profile
  value
}
```

A subject MAY carry multiple bindings, for example raw bytes, normalized visible text, structured document form, or chunk/segment commitments.

Exact and partial integrity are distinct concepts. Full-content digest mismatch MUST NOT by itself erase otherwise valid partial provenance.

## 10. Evidence

Evidence is extensible:

```text
Evidence {
  evidence_type
  scheme
  subject
  proof
  parameters?
}
```

Evidence types can include digital signatures, watermark recovery, transparency inclusion, timestamps, witness proofs, blockchain anchors, hardware attestation, verifiable credentials, execution proofs, or future schemes.

GCPP Core does not privilege blockchain or any other evidence substrate.

## 11. Carriers

A carrier transports provenance or a locator. Examples include embedded manifests, sidecar files, custom clipboard formats, document metadata, robust watermarks, external references, and future mechanisms.

A carrier MUST NOT be confused with the proof it transports. A record obtained through an untrusted transport can still verify if its signatures and bindings are valid.

## 12. Extensions

Records MUST support extensions. Extensions are either critical or non-critical.

- Unknown non-critical extensions MUST be safely ignored for Core verification while being reported as unsupported.
- Unknown critical extensions MUST cause the affected claim to be reported as unsupported, not fake.

## 13. Privacy

Public GCPP records SHOULD minimize correlatable information. Generation identifiers SHOULD be unlinkable across users and sessions. Raw prompts and user-account identifiers are out of scope for public provenance and MUST NOT be required by Core.

If an input must be bound for enterprise or audit use, profiles SHOULD use salted or randomized commitments and selective disclosure rather than publishing raw prompts or stable user identifiers.

## 14. History and correction

GCPP favors append-only correction over silent history rewriting. Revocation, key compromise, supersession, or corrected claims SHOULD be represented by additional records or evidence that preserve the original record.

## 15. Verification output

Core verification produces a structured vector rather than one boolean. At minimum it reports:

- actor authentication state;
- record signature state;
- model assurance state;
- exact integrity state;
- partial integrity/coverage state when available;
- locator/watermark state;
- lineage state;
- historical evidence state;
- unsupported critical features.

Presentation labels such as `VERIFIED_ORIGINAL`, `VERIFIED_DERIVATIVE`, `PARTIAL_PROVENANCE`, `LOCATOR_ONLY`, and `UNVERIFIED` are derived from that vector according to GCPP-VERIFY.

## 16. Protocol independence

No conforming GCPP Core specification may require one named blockchain, one named provider registry, one centralized resolver, one watermark algorithm, or one model architecture as a permanent protocol dependency.

Replaceable mechanisms belong in registries and profiles. Core semantics change only when the meaning of provenance itself must change.
