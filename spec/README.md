# GCPP Specification Set

This directory contains the normative and pre-normative protocol documents for the Generative Content Provenance Protocol.

## Current working drafts

- `GCPP-CORE.md` — scope, invariants, layer model, abstract protocol semantics.
- `GCPP-DATA-MODEL.md` — implementation-independent object model.
- `GCPP-VERIFY.md` — verification vector, state semantics, and interoperable labels.
- `GCPP-THREAT-MODEL.md` — adversaries, non-goals, residual risk, privacy and availability threats.

## Profile documents

Profiles select replaceable technologies or media-specific behavior without changing Core semantics.

- `../profiles/GCPP-TEXT-0.1.md` — experimental plain-text provenance and robust locator profile.

## Supporting standards material

- `../registries/README.md` — initial parameter registry framework.
- `../test-vectors/README.md` — required conformance cases.
- `../governance/PROCESS.md` — standards maturity and change process.
- `../ROADMAP.md` — standards roadmap.

## Normative boundary

A document labelled **Working Draft** is not stable. The project will explicitly mark Candidate Draft and Stable Standard maturity when interoperability and security criteria are met.

The repository currently has no final Internet deployment profile. Therefore identifiers, algorithms, media types, and concrete serialization choices marked `provisional` are not permanent interoperability guarantees.

## Design rule

If a new technology can be introduced as a registry entry, adapter, carrier, evidence scheme, or deployment profile, it should not require a Core semantic change.
