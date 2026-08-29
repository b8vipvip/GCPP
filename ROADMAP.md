# GCPP Roadmap

This roadmap is about standards maturity, not product delivery dates.

## Phase 0 — Architecture freeze for Core concepts

Goals:

- stabilize the four durable abstractions: Identity, Provenance, Integrity, Evidence;
- stabilize `GenerationID` vs `RecoveryLocator` separation;
- stabilize provenance DAG semantics;
- stabilize verification vector and presentation labels;
- freeze the rule that watermarks are discovery/recovery evidence, not final authentication;
- freeze privacy and policy-neutrality invariants.

Exit condition: no known requirement forces Core to depend on a specific blockchain, DID method, hash, signature, watermark, storage system, or AI architecture.

## Phase 1 — Canonical Internet Profile

Define a first interoperable deployment profile with concrete but replaceable choices:

- canonical serialization;
- signature envelope;
- baseline hash/commitment schemes;
- key identifiers;
- record size limits;
- deterministic canonicalization;
- error behavior;
- self-contained and sidecar proof packaging.

Exit condition: independently implemented sign/verify code produces identical signature inputs and results.

## Phase 2 — Text Integrity Profile

Define:

- `norm.text-plain-1`;
- exact normalized-text binding;
- robust segment/chunk binding;
- content-defined or structurally aware segmentation;
- authenticated coverage calculation;
- normalization conformance vectors.

Exit condition: two independent implementations agree on exact and partial integrity results after common edits.

## Phase 3 — Text Recovery Profile

Research and standardize an efficient in-band recovery locator that:

- does not require extra LLM inference passes;
- does not require large candidate semantic reranking;
- supports graceful abstention for short/low-entropy output;
- provides ECC/synchronization;
- has measured false-positive/false-negative behavior;
- is tested across languages and common copy/edit paths;
- treats recovery as discovery only.

Exit condition: a candidate scheme passes published robustness, quality, throughput, spoofing, and transplant tests.

## Phase 4 — Discovery and transport profiles

Optional profiles for:

- `.well-known` provider capability discovery;
- HTTPS record resolution;
- structured clipboard carriage;
- caching/mirroring;
- offline proof bundles.

Exit condition: transport can be replaced without changing Core verification.

## Phase 5 — Existing-standard adapters

Develop adapters for mature ecosystems where useful:

- C2PA/content credentials;
- DID/VC identity evidence;
- X.509/domain identity;
- transparency logs;
- trusted timestamping;
- media-specific watermark systems.

Exit condition: adapters preserve GCPP verification distinctions without making any one external standard mandatory.

## Phase 6 — Historical evidence profiles

Define common interfaces for append-only and time/existence evidence:

- transparency logs;
- witnesses/cross-logging;
- timestamp networks;
- blockchain/distributed-ledger anchors;
- future evidence systems.

Exit condition: verifiers can compare history assurance independently from actor signature validity.

## Phase 7 — Model assurance extensions

Optional, non-hot-path mechanisms:

- model commitments;
- selective disclosure;
- TEE/hardware attestation;
- verifiable inference;
- zero-knowledge execution proofs when practical.

Exit condition: stronger model assurance does not retroactively redefine ordinary `MODEL_DECLARED` records.

## Phase 8 — Interoperability and standardization readiness

Before a stable 1.0 claim:

- explicit specification license/IPR policy;
- independent implementations;
- complete positive/negative test vectors;
- security review;
- privacy review;
- internationalization review;
- algorithm agility/deprecation procedure;
- documented relationship to adjacent standards;
- stable registry process.

## Non-goals for the roadmap

GCPP will not attempt to build a global content-moderation authority, universal AI detector, truth oracle, mandatory blockchain, or central user-tracking registry.
