# GCPP Text Profile 0.1

Status: **Experimental Working Draft**  
Profile goal: robust provenance recovery for plain text while preserving model throughput and text quality.

## 1. Purpose

Plain text is a difficult provenance medium because copy/paste commonly strips document metadata and sidecar state. This profile defines a layered carrier strategy that can degrade gracefully when metadata is lost.

This profile does not claim universal AI detection and does not promise watermark survival after arbitrary rewriting.

## 2. Performance invariant

A production-conforming text provenance carrier SHOULD NOT require:

- an additional LLM inference pass;
- a second model call;
- generation of multiple full sentence candidates for semantic reranking;
- embedding-model calls on every sentence;
- per-token network requests;
- per-token ledger/blockchain operations;
- per-token zero-knowledge proof generation.

The preferred in-band path is a lightweight sampling/logit transformation that does not materially alter the main model forward pass.

If a watermarking scheme cannot meet the provider's correctness or latency requirements for a given output, the profile permits the in-band carrier to be absent and requires the capability state to say so explicitly.

## 3. Layered carrier model

Text provenance SHOULD use multiple independent carriers when available:

1. **Attached proof** — full signed provenance object bundled with content.
2. **Structured clipboard carrier** — for supporting applications.
3. **Document/HTML metadata** — for rich formats.
4. **Robust in-band locator** — a short locator encoded through generation choices.
5. **Auxiliary Unicode carrier** — optional convenience channel only.

No single carrier is mandatory in every environment.

## 4. GID and RID separation

The full `GenerationID` is the authoritative event identifier. It is not required to fit inside the visible text.

The in-band text watermark carries a compact `RecoveryLocator` (RID) or fragments that can be used to discover candidate signed records.

RID properties:

- shorter than or independent from the GID;
- may be error-corrected and interleaved;
- may resolve to multiple candidates;
- not sufficient for authentication;
- not required to be globally unique on its own.

This avoids unrealistic claims that a four-character answer can invisibly carry a full cryptographic identity with strong edit robustness.

## 5. Locator watermark abstraction

A registered text-locator scheme defines:

```text
TextLocatorScheme {
  scheme_id
  version
  payload_capacity
  synchronization_method
  error_correction_method
  detector_parameters
  generation_constraints
}
```

The scheme MAY operate on token sampling, lexical choices, punctuation choices, or future efficient in-band mechanisms, but Core does not prescribe one algorithm.

## 6. Quality and correctness

A text-locator scheme MUST allow the generator to abstain from embedding when constraints would materially harm correctness, safety, deterministic formatting, code execution, mathematical output, structured data validity, or provider-defined generation quality.

The record SHOULD communicate a capacity state such as:

- `NONE`
- `PROVIDER_ONLY`
- `PARTIAL_LOCATOR`
- `FULL_LOCATOR`
- `REDUNDANT_LOCATOR`
- `UNAVAILABLE_LOW_ENTROPY`

These states describe carrier capacity, not provenance validity.

## 7. Low-entropy outputs

Examples that often require fallback behavior:

- very short answers;
- exact quotations where transformation is not permitted;
- source code;
- JSON/XML with strict schemas;
- formulas;
- deterministic or temperature-zero output;
- fixed legal/medical text requiring exact wording;
- constrained decoding with very few valid tokens.

For such outputs, attached proof, clipboard proof, or sidecar proof can provide full provenance even when no robust in-band locator is embedded.

## 8. Error correction and synchronization

A robust locator scheme SHOULD be designed for deletion, insertion, and substitution rather than only bit flips.

Registered schemes may use:

- block error-correcting codes;
- interleaving;
- rateless/fountain-style coding;
- synchronization strings;
- edit-distance codes;
- repeated independent locator fragments;
- future coding constructions.

The exact construction is profile-registered and replaceable.

## 9. Recovery

A verifier processing plain text SHOULD:

1. inspect attached/clipboard/metadata carriers if present;
2. normalize only as allowed by the detector scheme;
3. attempt registered robust locator detection;
4. recover zero or more RID candidates plus confidence/diagnostics;
5. resolve candidate signed provenance records from any available source;
6. verify record signatures;
7. compare the current text against exact and partial content bindings;
8. attribute only content supported by valid bindings.

A high watermark confidence cannot override an invalid signature or content mismatch.

## 10. Copy/paste behavior

Supporting software MAY place provenance in a custom clipboard representation such as:

```text
application/gcpp-provenance+cbor
```

alongside ordinary representations such as `text/plain` and `text/html`.

A receiving application that understands the GCPP clipboard profile can preserve the full signed proof. A non-supporting application can drop the structured representation while leaving visible text intact; the in-band locator remains the fallback when present.

The media type above is provisional and MUST NOT be represented as an officially registered IANA type until such registration exists.

## 11. Unicode auxiliary carrier

Zero-width characters, variation selectors, special spaces, or equivalent Unicode mechanisms MAY be used as an auxiliary carrier.

They MUST NOT be the only mechanism behind a robustness claim because normalizers and sanitizers can remove them without changing visible text.

An implementation MUST NOT treat deletion of the auxiliary Unicode carrier as proof of malicious stripping.

## 12. Text normalization

Text integrity and watermark detection use separate normalization concerns.

A `TEXT-PLAIN` integrity profile SHOULD define at least:

- Unicode normalization form;
- line-ending normalization;
- treatment of trailing spaces;
- treatment of BOM/control characters;
- whether visually invisible characters are preserved or removed;
- language-independent encoding requirements.

Normalization rules MUST be explicit and versioned.

## 13. Exact and partial text binding

A provider SHOULD create an exact normalized-text binding and MAY create segment/chunk commitments for partial attribution.

Segment boundaries SHOULD resist catastrophic shift after one early insertion. Content-defined, paragraph-aware, sentence-aware, or future robust segmentation profiles can be registered.

Coverage calculations MUST use a defined denominator and MUST NOT infer that unmatched text belongs to the source generation.

## 14. Edit outcomes

Illustrative behavior:

- formatting/font change: attached or normalized binding may remain valid;
- ordinary cross-software copy: robust locator may survive;
- small word edits: locator/ECC may survive, exact digest fails;
- deleted paragraphs: partial binding may authenticate surviving segments;
- inserted unrelated text: only matched segments are attributed;
- moderate paraphrase: scheme-dependent; no Core guarantee;
- translation/back-translation: expected recovery degradation;
- full rewrite/re-generation: provenance may become unrecoverable.

The last state is reported as `UNVERIFIED`, not `HUMAN`.

## 15. Anti-transplant rule

A RID or detectable watermark transplanted into unrelated text MUST NOT authenticate the unrelated text.

The verifier must require a valid signed record and sufficient content relationship. A transplanted locator should produce `LOCATOR_ONLY` or a diagnostic indicating locator/content inconsistency.

## 16. Scheme evaluation

Before a text-locator scheme is recommended for an Internet deployment profile, it SHOULD be evaluated for:

- output-quality regression;
- latency and throughput overhead;
- cross-language behavior;
- short-text capacity;
- low-entropy failure behavior;
- false positive rate;
- false negative rate;
- deletion/insertion/substitution robustness;
- paraphrase/translation robustness;
- spoofing and watermark-stealing resistance;
- detector-key compromise consequences.

Benchmarks MUST distinguish recovery performance from cryptographic attribution performance.

## 17. Future evolution

Semantic methods may be registered later if they become sufficiently low-cost, but expensive multi-candidate semantic reranking is intentionally not part of the baseline GCPP Text Profile.
