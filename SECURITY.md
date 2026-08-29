# Security Policy

GCPP is a security-sensitive protocol project. Provenance failures can cause false attribution, privacy leakage, history rewriting, or dangerous overconfidence in content labels.

## Scope

Security reports may concern:

- signature or key-confusion attacks;
- canonicalization inconsistencies;
- content-binding bypasses;
- RID/watermark spoofing or transplant attacks;
- false-positive attribution;
- parser ambiguity or downgrade behavior;
- provenance graph confusion;
- privacy/linkability failures;
- transparency/history equivocation;
- revocation/key-lifecycle failures;
- conformance vectors that would cause implementations to disagree.

## Reporting

Until a dedicated private security-reporting channel is configured for the repository, avoid publishing weaponized exploit details for an unpatched implementation in a public issue. Open a minimal issue requesting a private contact path without including sensitive exploit material.

Specification-level weaknesses that do not expose an immediate implementation vulnerability can be discussed publicly through design issues.

## Security principles

A conforming implementation should assume:

- transports and resolvers can be malicious;
- metadata and sidecars can disappear;
- watermarks can be studied, copied, or removed;
- providers or provider keys can be compromised;
- external evidence systems can fail or fork;
- algorithms can become obsolete;
- users and UIs can misinterpret protocol labels.

Accordingly, GCPP uses layered evidence and exposes assurance dimensions instead of one universal trust bit.

## No truth oracle

A critical semantic safety property is that provenance does not certify factual truth. Security reviews should treat any UI/API behavior that maps `VERIFIED` to factual truth or `UNVERIFIED` to falsity as a protocol misuse with potentially serious downstream consequences.
