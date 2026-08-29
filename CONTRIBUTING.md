# Contributing to GCPP

GCPP is being developed as an open public protocol. Contributions should improve interoperability, security, privacy, implementation independence, or clarity rather than optimize one vendor's product architecture.

## Before proposing a change

Please identify which layer is affected:

- Identity
- Provenance
- Integrity
- Evidence
- Verification
- Presentation
- Registry
- Deployment profile
- Test vectors

If a change can be expressed as a new algorithm, identity adapter, evidence scheme, carrier, normalization profile, transport, storage method, or deployment profile, it should normally **not** modify GCPP Core.

## Proposal content

Substantive proposals should include:

1. problem statement;
2. proposed semantics;
3. alternatives considered;
4. security considerations;
5. privacy considerations;
6. backwards/forward compatibility;
7. interoperability implications;
8. expected test-vector changes;
9. whether the change is Core, registry, or profile scope.

## Design rules

Contributions must preserve these semantic boundaries:

- provenance is not truth;
- unverified is not fake or human;
- a locator/watermark is not authentication;
- model declaration is not execution proof;
- current-content integrity is distinct from validity of a historical signed record;
- user identity is not required for public content provenance;
- policy remains outside Core verification.

## Performance-sensitive AI profiles

Baseline production profiles should avoid requirements that materially increase model inference cost, including additional LLM passes, multi-candidate full-sentence semantic reranking, per-token network operations, or per-token proof generation.

A profile may define stronger optional mechanisms, but their cost and assurance level must be explicit.

## Pull requests

Keep normative and explanatory changes clearly separated when practical. Add or update conformance cases for normative behavior changes.

Large Core changes should begin with a design issue before implementation text is treated as stable.

## Specification language

Use BCP 14 requirement keywords only for normative requirements. Avoid ambiguous uses of words such as `trusted`, `authentic`, `verified`, and `original`; specify exactly which evidence dimension is meant.

## Third-party work

Do not copy normative text, code, or patented mechanisms from third-party standards or papers unless reuse rights are clear. Prefer references, adapters, and independently written interoperability text.

## Licensing status

The repository still requires an explicit standards-document license and contributor IPR policy before formal standards maturity. That decision is tracked separately and should be resolved before external implementers are asked to rely on patent/license assurances.
