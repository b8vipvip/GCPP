# GCPP Threat Model 0.1

Status: **Working Draft**

This threat model defines the attacks GCPP intends to detect, resist, or represent accurately. It also states what the protocol cannot guarantee.

## 1. Security goals

GCPP aims to make it difficult to:

- forge a provenance claim as if signed by another actor;
- transplant a real locator or identifier into unrelated content and have it authenticate the whole subject;
- silently rewrite authenticated provenance history when independent historical evidence exists;
- erase all provenance through ordinary format conversion when a robust carrier survives;
- confuse partial provenance with whole-document provenance;
- confuse provider model declarations with independently proven model execution;
- turn absence of provenance into proof of falsity or human authorship.

## 2. Non-goals

GCPP does not guarantee:

- factual correctness of content;
- universal detection of all AI-generated content;
- survival of provenance after arbitrary rewriting, translation, re-generation, manual re-expression, or destructive editing;
- prevention of a provider intentionally making a false signed claim about its own internal model execution;
- legal attribution to a natural person;
- secrecy of content that is already public;
- enforcement of platform or national policy.

## 3. Adversary classes

### 3.1 Content editor

Can copy, paste, normalize, reformat, delete, insert, reorder, paraphrase, translate, or partially rewrite content.

### 3.2 Provenance stripper

Intentionally removes metadata, sidecars, hidden Unicode, custom clipboard MIME types, manifests, or known watermark carriers.

### 3.3 Locator transplanter

Copies a valid RID, watermark pattern, manifest reference, or provenance fragment into unrelated content.

### 3.4 Signature forger

Attempts to create a record that appears signed by a provider or actor without possession of its signing key.

### 3.5 Watermark learner

Queries a provider repeatedly to infer watermark behavior, then attempts to scrub or spoof it.

### 3.6 Malicious or compromised provider

Controls legitimate signing keys and can sign misleading model declarations or omit transparency publication.

### 3.7 Key thief

Obtains a legitimate actor signing key and signs fraudulent records until revocation or compromise is recognized.

### 3.8 History rewriter

Attempts to delete or replace earlier provenance records or checkpoints after publication.

### 3.9 Resolver attacker

Controls a server, cache, CDN, P2P node, or index used to retrieve candidate provenance records.

### 3.10 Policy manipulator

Uses valid protocol outputs to make unsupported claims such as `UNVERIFIED = FAKE` or `VERIFIED = TRUE`.

## 4. Core defenses

### Signature forgery

Defense: cryptographic record signatures with replaceable registered schemes and explicit key lifecycle semantics.

Expected result: invalid signature, not trusted attribution.

### Locator transplant

Defense: locator is discovery-only; attribution additionally requires signed record verification plus content binding/coverage.

Expected result: `LOCATOR_RECOVERED` with failed or insufficient integrity, not verified origin.

### Partial-copy inflation

Defense: partial coverage is first-class and MUST NOT be extrapolated to the entire current subject.

Expected result: `PARTIAL_PROVENANCE` with measured authenticated coverage where supported.

### Metadata stripping

Defense: multiple independent carriers MAY coexist. Text profiles can include a robust in-band locator in addition to metadata, sidecars, or clipboard payloads.

Expected result: provenance can degrade gracefully from attached proof to locator recovery instead of binary failure.

### Arbitrary rewrite

Defense: none can be guaranteed in the general case. If all information carrying provenance is removed, GCPP reports `UNVERIFIED`.

### Resolver tampering

Defense: retrieved records are not trusted based on transport. Signatures and evidence are verified locally.

Expected result: a malicious resolver can deny availability but cannot create valid provider signatures.

### Historical rewriting

Defense: optional append-only evidence, transparency logs, witness systems, timestamps, blockchains, or future evidence systems.

Expected result: history assurance is reported as a distinct dimension; lack of history evidence does not invalidate an otherwise valid signature.

### Watermark spoofing

Defense: watermarks and RIDs do not authenticate identity. Strong attribution comes from signed records and content binding.

### Provider false declaration

Defense: a normal provider signature proves the provider made the declaration, not that the declaration about internal execution is true. Stronger model assurance requires optional attestation or verifiable-execution evidence.

Expected result: `MODEL_DECLARED`, not `MODEL_EXECUTION_PROVEN`.

### Key compromise

Defense: identity profiles must support key rotation, revocation/compromise status, and historical key validation. Corrections should be append-only where possible.

## 5. Privacy threats

### Cross-generation user tracking

A stable per-user or per-device provenance identifier could become a tracking primitive. GCPP identifiers therefore MUST NOT require embedded user identity and SHOULD be unlinkable across generation events.

### Prompt guessing

Publishing deterministic hashes of low-entropy prompts can leak information through dictionary attacks. Public prompt bindings are therefore not required and should use randomized commitments when needed.

### Permanent public personal data

Append-only or blockchain evidence can make accidental personal-data publication difficult or impossible to remove. Profiles SHOULD anchor commitments rather than raw user data or raw content.

## 6. Availability threats

No online resolver, provider endpoint, log, or chain is assumed immortal. GCPP therefore supports self-contained proof bundles, sidecars, cached records, independent mirrors, and multiple evidence systems.

Availability failure MUST be represented separately from cryptographic invalidity.

## 7. Algorithm agility threats

Hash, signature, identity, watermark, and evidence algorithms can become obsolete. Registries and profiles MUST support deprecation and migration without changing Core provenance semantics.

Historical verification software SHOULD preserve algorithm identifiers and verification material needed for long-term validation.

## 8. Content-specific limits

Very short text, deterministic code, formulas, JSON, fixed-format outputs, and low-entropy generation may not have enough freedom for robust in-band watermarking without harming correctness.

Profiles MUST be allowed to declare low or zero locator capacity and fall back to attached/sidecar proof.

## 9. Safety against semantic overclaim

The protocol's presentation vocabulary is part of the security model. Implementations that turn `UNVERIFIED` into `FAKE`, or `VERIFIED` into `TRUE`, create a policy-level spoofing vulnerability even when cryptography is correct.

Conformance testing SHOULD include UI/API semantic misuse tests in addition to cryptographic vectors.

## 10. Residual risk

GCPP raises the cost of provenance forgery and makes evidence quality explicit. It cannot make information indestructible, cannot prove reality from cryptography alone, and cannot force non-participating software or local open-source models to emit provenance.

The intended outcome is graceful assurance: exact, derivative, partial, locator-only, or unverified — not an impossible promise of universal permanent tracking.
