# GCPP

**Generative Content Provenance Protocol** — an implementation-agnostic, policy-neutral public protocol for verifiable digital content provenance.

GCPP standardizes four durable questions:

- **Identity** — who made the provenance claim?
- **Provenance** — what generation or transformation event occurred?
- **Integrity** — how does the current content relate to the claimed source content?
- **Evidence** — what verifiable evidence supports those claims?

GCPP deliberately does **not** require a particular blockchain, database, identity system, hash algorithm, watermark algorithm, AI architecture, provider, government, or verification service.

The repository is being organized as an open standards project. The first normative draft will live under `spec/` and will distinguish stable protocol semantics from replaceable deployment profiles.

## Design invariants

1. Provenance is not truth: `VERIFIED` never means factually true.
2. Absence of provenance is not falsity: `UNVERIFIED` never means human, fake, illegal, or low quality.
3. Watermarks are discovery/recovery evidence, not final authentication.
4. User identity is not required for content provenance.
5. Verification must not depend on one central online verifier.
6. Storage, transport, identity, algorithms, watermarking, evidence systems, AI architectures, and policy are replaceable.
7. Modified content must not be reduced to a binary AI/non-AI label; partial provenance is first-class.
8. Protocol mechanisms report evidence and relationships; policy decisions remain outside GCPP.

## Status

Early public standards draft. Interfaces and semantics are expected to change until GCPP Core reaches a stable version.
