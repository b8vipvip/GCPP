# GCPP

**Generative Content Provenance Protocol** — an implementation-agnostic, policy-neutral public protocol for verifiable digital-content provenance.

GCPP is being designed as a public protocol layer, not as a blockchain project, central registry, AI detector, or government verification service.

## The four durable questions

GCPP standardizes:

- **Identity** — who made the provenance claim?
- **Provenance** — what generation or transformation events produced the content?
- **Integrity** — how does the current content relate to the content bound by those events?
- **Evidence** — what verifiable evidence supports those claims?

Everything else is replaceable implementation detail.

## Architectural stance

GCPP Core is intended to remain:

- storage-agnostic;
- transport-agnostic;
- identity-system-agnostic;
- cryptographic-algorithm-agile;
- watermark-agnostic;
- evidence/anchor-system-agnostic;
- AI-model-architecture-agnostic;
- platform-agnostic;
- policy-neutral.

A blockchain can carry historical evidence, but GCPP does not require a blockchain. DID can implement identity, but GCPP does not require DID. SHA-256 or Ed25519 can appear in an Internet profile, but they are not permanent Core assumptions.

## Non-negotiable semantics

1. `VERIFIED` provenance does **not** mean factually true.
2. `UNVERIFIED` does **not** mean human, fake, illegal, or low quality.
3. A watermark or RID is discovery/recovery evidence, **not authentication**.
4. User identity is not required for public content provenance.
5. Verification must be possible without one globally privileged online verifier.
6. Partial and modified provenance are first-class states.
7. Model declaration is not automatically proof of actual model execution.
8. Policy decisions remain outside the protocol's cryptographic result.

## Current specification set

Start here: [`spec/README.md`](spec/README.md)

- [`spec/GCPP-CORE.md`](spec/GCPP-CORE.md) — core semantics and invariants.
- [`spec/GCPP-DATA-MODEL.md`](spec/GCPP-DATA-MODEL.md) — abstract protocol objects.
- [`spec/GCPP-VERIFY.md`](spec/GCPP-VERIFY.md) — verification vector and result semantics.
- [`spec/GCPP-THREAT-MODEL.md`](spec/GCPP-THREAT-MODEL.md) — attacks, non-goals, and residual risks.
- [`profiles/GCPP-TEXT-0.1.md`](profiles/GCPP-TEXT-0.1.md) — experimental low-overhead plain-text provenance profile.
- [`registries/README.md`](registries/README.md) — extensible protocol registries.
- [`test-vectors/README.md`](test-vectors/README.md) — conformance test plan.
- [`governance/PROCESS.md`](governance/PROCESS.md) — open standards process.
- [`ROADMAP.md`](ROADMAP.md) — route from architecture draft to interoperable standard.

## Text provenance direction

The baseline text profile intentionally avoids high-cost mechanisms such as additional LLM passes or large multi-candidate semantic reranking.

The preferred architecture is:

```text
main model forward pass
        -> lightweight sampling/logit locator carrier
        -> token output

parallel / post-generation:
        -> content bindings
        -> signed provenance record
        -> optional external historical evidence
```

The full generation identity does not need to be hidden inside short text. GCPP separates:

- **GenerationID (GID)** — authoritative event identity;
- **RecoveryLocator (RID)** — compact, recoverable discovery value.

A recovered RID must still resolve to a signed record and pass content-binding verification before attribution.

## Status

The repository is in **Working Draft** stage. Current text is deliberately not advertised as a stable 1.0 standard.

Before formal standards maturity, GCPP still needs a public IPR/specification licensing policy, a concrete canonical Internet deployment profile, machine-readable test fixtures, independent implementations, and external security/privacy review.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Substantive protocol changes should preserve implementation independence and include security, privacy, interoperability, and test-vector considerations.
