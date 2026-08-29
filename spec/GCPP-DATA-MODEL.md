# GCPP Data Model 0.1

Status: **Working Draft**

This document defines the abstract data model used by GCPP Core. It deliberately does not prescribe JSON, CBOR, protobuf, ASN.1, blockchain storage, HTTP transport, or any other physical representation.

## 1. Primitive design rules

All protocol objects MUST be explicitly versioned or interpreted through a versioned profile.

Identifiers used for events and generations SHOULD be opaque and high entropy. They MUST NOT encode a user's account, IP address, device identifier, geographic location, or raw prompt.

Algorithm identifiers, identity methods, evidence schemes, normalization profiles, event types, and carrier types are registry-controlled symbolic or numeric values.

## 2. ActorIdentifier

```text
ActorIdentifier {
  method: RegistryID
  identifier: BytesOrString
}
```

The `method` defines how `identifier` is interpreted and how verification material is resolved. Core does not require online resolution.

## 3. Event

```text
Event {
  id: OpaqueID
  type: RegistryID
  time?: TimeClaim
}
```

`time` is a claim until supported by an evidence scheme that provides stronger temporal assurance.

A generation event SHOULD use a generation-specific opaque identifier. Other transformation events MAY use equivalent opaque event identifiers.

## 4. Subject

```text
Subject {
  media_type: MediaType
  bindings: [ContentBinding, ...]
}
```

A subject MUST contain at least one content binding for an authenticated provenance claim to bind to concrete content.

## 5. ContentBinding

```text
ContentBinding {
  binding_type: RegistryID
  algorithm: RegistryID
  normalization_profile: RegistryID
  value: Bytes
  parameters?: Map
}
```

Examples of `binding_type` include exact digest, normalized-text digest, segment commitment set, content-defined chunk tree, or a future robust integrity construction.

The same subject MAY carry multiple bindings over different representations.

## 6. ModelClaim

```text
ModelClaim {
  public_model_id: String
  model_family?: String
  model_commitment?: Commitment
  extensions?: [Extension, ...]
}
```

`public_model_id` is the provider's public declaration. `model_commitment` can commit to internal model build or routing information without revealing it.

Presence of `ModelClaim` alone MUST NOT be interpreted as execution proof.

## 7. ParentReference

```text
ParentReference {
  event_id?: OpaqueID
  record_commitment?: Commitment
  relation_type: RegistryID
  subject_selector?: Selector
}
```

A record MAY have zero or more parents. Implementations MUST support multiple parents so composition and multi-source transformations can be represented.

## 8. CarrierDescriptor

```text
CarrierDescriptor {
  carrier_type: RegistryID
  scheme: RegistryID
  locator?: BytesOrString
  parameters?: Map
}
```

A carrier identifies how the record or a recovery locator can accompany or be recovered from content. Carrier validity is not equivalent to provenance validity.

## 9. RecoveryLocator

```text
RecoveryLocator {
  scheme: RegistryID
  value: Bytes
  confidence?: Number
  fragments?: [Bytes, ...]
}
```

A recovery locator is discovery material. It MAY resolve to zero, one, or many candidate records. A verifier MUST authenticate candidate records separately.

## 10. Evidence

```text
Evidence {
  evidence_type: RegistryID
  scheme: RegistryID
  subject: EvidenceSubject
  proof: BytesOrStructuredValue
  parameters?: Map
}
```

`subject` identifies exactly what the proof covers. Evidence types MUST specify canonical verification rules in their registered scheme specifications.

## 11. Extension

```text
Extension {
  id: RegistryID
  critical: Boolean
  value: StructuredValue
}
```

Unknown non-critical extensions are ignored for Core claim evaluation but reported. Unknown critical extensions cause the affected claim to be `UNSUPPORTED` rather than `INVALID` unless the enclosing profile states otherwise.

## 12. ProvenanceRecord

```text
ProvenanceRecord {
  version: Version
  event: Event
  actor: ActorIdentifier
  subject: Subject
  model_claim?: ModelClaim
  parents: [ParentReference, ...]
  carriers: [CarrierDescriptor, ...]
  evidence: [Evidence, ...]
  extensions: [Extension, ...]
}
```

Records are logical claim sets. A deployment profile defines canonical serialization and signature envelopes.

## 13. SignedProvenance

```text
SignedProvenance {
  record: ProvenanceRecord
  signer: ActorIdentifier
  signature_scheme: RegistryID
  signature: Bytes
  signature_parameters?: Map
}
```

The signature input MUST be the profile-defined canonical encoding of the complete record plus any required domain-separation context.

Profiles MUST define algorithm substitution and key-identifier behavior unambiguously.

## 14. VerificationVector

```text
VerificationVector {
  actor_authentication
  record_signature
  model_assurance
  exact_integrity
  partial_integrity
  authenticated_coverage?
  locator_state
  lineage_state
  historical_evidence
  unsupported_critical_features[]
  diagnostics[]
}
```

Each field is independently evaluated. Presentation labels are derived from this structure; they are not stored as authoritative truth in the record.

## 15. Canonicalization boundary

Canonicalization is security-critical. GCPP Core deliberately keeps canonical encodings and media normalization in profiles, but every profile MUST define them precisely enough that two conforming implementations generate identical signature inputs and content-binding inputs for the same logical value.

## 16. Media normalization

Normalization profiles SHOULD be representation-specific. For text, profiles can define Unicode normalization, line-ending handling, whitespace rules, control-character treatment, and markup extraction. For binary media, normalization can be identity (raw bytes) or an explicitly defined canonical representation.

Normalization MUST NOT silently erase semantically relevant information unless the profile explicitly defines that tradeoff.

## 17. Evolution

New fields should normally be introduced as registered extensions or profile updates. Core object meaning should change only with a major protocol revision.
