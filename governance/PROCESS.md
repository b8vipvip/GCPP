# GCPP Standards Process

Status: **Draft governance process**

GCPP is intended to be an open technical standard rather than a product specification controlled by one implementation. This document separates standards coordination from operational control.

## 1. Goals

The process should optimize for:

- technically precise, implementation-independent specifications;
- public review and archived design rationale;
- interoperable independent implementations;
- security and privacy review before stabilization;
- algorithm and infrastructure agility;
- long-term availability of historic registry information;
- no privileged power to rewrite signed provenance history.

## 2. Specification maturity

Documents progress through:

1. **Exploration** — problem statement and alternatives; not normative.
2. **Working Draft** — concrete protocol text; expected to change.
3. **Candidate Draft** — semantics frozen enough for multiple implementations and test vectors.
4. **Proposed Standard** — interoperability and security evidence available.
5. **Stable Standard** — mature, versioned public specification.
6. **Historic** — superseded but retained for verification of old records.

A document's maturity is independent from the maturity of any particular software implementation.

## 3. Change mechanism

Substantive changes SHOULD be proposed through a public issue and pull request. The proposal should state:

- problem being solved;
- affected protocol layer;
- whether Core semantics change;
- privacy impact;
- security impact;
- interoperability impact;
- backwards compatibility;
- alternative approaches;
- test-vector implications.

Changes that can be handled through registries or profiles SHOULD NOT modify GCPP Core.

## 4. Core change bar

Core changes have a deliberately high bar. A Core change is justified when the meaning of identity, provenance, integrity, evidence, or verification cannot be expressed through existing extension/profile mechanisms.

A new hash, watermark, blockchain, identity system, AI architecture, serialization, transport, or storage method is normally **not** a Core change.

## 5. Registry changes

Registry additions require a stable public specification sufficient for interoperable implementation. Recommended or security-sensitive entries should receive expert review.

Registry maintainers coordinate identifiers; they do not certify providers, decide legal policy, or determine content truth.

Historic/deprecated algorithm entries remain documented so old provenance can be interpreted.

## 6. Interoperability requirement

Before a document advances beyond Candidate Draft, there SHOULD be at least two independent implementations or one implementation plus independently generated/verified test vectors demonstrating the key semantics.

Core advancement requires test coverage for negative cases, not only happy paths.

## 7. Security and privacy review

Candidate drafts require documented review of:

- signature substitution/confusion;
- canonicalization ambiguity;
- identifier correlation;
- locator transplant/spoofing;
- partial-provenance inflation;
- key compromise and revocation;
- history equivocation;
- downgrade/algorithm agility;
- parser robustness;
- privacy leakage in public or append-only evidence.

## 8. Consensus

The project should seek rough technical consensus rather than token-weighted voting or ownership-weighted voting. Maintainers are expected to summarize unresolved objections and rationale when merging major normative changes.

Consensus on protocol text does not give maintainers operational control over provider logs, verifiers, networks, evidence systems, or signed records.

## 9. Reference implementations

Reference implementations are non-authoritative. If code and normative specification disagree, the specification and published test vectors govern until the specification is corrected.

No conforming verifier may require access to a project-operated central service merely because the reference implementation does.

## 10. Profiles

Deployment profiles can choose concrete technologies for interoperability at a given time, for example a canonical serialization, signature algorithm set, HTTP discovery mechanism, or text-locator scheme.

Profiles MUST state which choices are temporary deployment requirements rather than permanent Core assumptions.

## 11. Compatibility

Unknown non-critical extensions should remain forward compatible. Major versions are reserved for semantic incompatibility.

Algorithm and registry evolution should normally occur without a Core major-version change.

## 12. IPR and licensing

Before GCPP claims formal standards maturity, the project MUST adopt an explicit specification copyright/license and contributor IPR policy suitable for open implementation.

Until that policy is selected, contributors should avoid incorporating text or patented mechanisms from third parties without clear rights and attribution.

## 13. Relationship to other standards

GCPP should reuse or adapt established work where possible rather than duplicate it. Candidate integration areas include content-credential formats, decentralized or certificate-based identity, verifiable credentials, transparency logs, timestamp protocols, and media-specific watermark standards.

Adapters must preserve GCPP's semantic distinctions, especially `provenance != truth`, `unverified != fake`, and `locator != authentication`.
