# GCPP Protocol Registries

Status: **Initial registry framework**

GCPP uses registries to keep stable protocol semantics separate from replaceable technologies. Registry entries do not grant legal status, provider legitimacy, policy approval, or factual trust.

## 1. Registry principles

Registries exist to answer questions such as:

- what does algorithm identifier `X` mean?
- which document defines normalization profile `Y`?
- how is evidence scheme `Z` verified?

They do **not** answer:

- which provider is allowed to operate;
- whether content is true or legal;
- whether an actor should be trusted by a specific country or platform;
- whether unverified content is fake.

Registry governance should follow an open specification-review process. Mature entries should cite a stable specification and include security considerations, versioning rules, and deprecation status.

## 2. Initial registries

### 2.1 Identity Methods

| ID | Name | Status | Notes |
|---|---|---|---|
| `identity.raw-key` | Raw public key | provisional | Direct cryptographic identifier |
| `identity.domain-key` | Domain-bound key | provisional | Requires a profile defining domain proof |
| `identity.did` | DID adapter | provisional | Uses a registered DID method/profile |
| `identity.x509` | X.509 adapter | provisional | Trust policy remains local |

### 2.2 Signature Schemes

| ID | Name | Status |
|---|---|---|
| `sig.ed25519` | Ed25519 | provisional deployment option |
| `sig.ecdsa-p256` | ECDSA P-256 | provisional deployment option |
| `sig.future` | Future scheme placeholder | reserved |

No algorithm is permanent. Profiles define which schemes are required, optional, deprecated, or forbidden at a point in time.

### 2.3 Content Commitment Algorithms

| ID | Name | Status |
|---|---|---|
| `hash.sha256` | SHA-256 | provisional deployment option |
| `hash.sha384` | SHA-384 | provisional deployment option |
| `hash.sha3-256` | SHA3-256 | provisional deployment option |

Core does not require any one entry forever.

### 2.4 Binding Types

| ID | Meaning |
|---|---|
| `binding.exact-bytes` | Exact byte representation |
| `binding.normalized-text` | Digest over a registered text normalization |
| `binding.segment-set` | Commitments over independently matchable segments |
| `binding.chunk-tree` | Tree/root over registered chunking construction |

### 2.5 Event Types

| ID | Meaning |
|---|---|
| `event.generate` | AI or software generation event |
| `event.capture` | Camera/sensor capture |
| `event.human-edit` | Human-declared edit |
| `event.ai-rewrite` | AI rewrite/transformation |
| `event.translate` | Translation |
| `event.summarize` | Summarization |
| `event.compose` | Multi-parent composition |
| `event.render` | Rendering |
| `event.transcode` | Media transcoding |
| `event.publish` | Publication/distribution event |
| `event.unknown-transform` | Transformation known to have occurred but type unspecified |

### 2.6 Evidence Types

| ID | Meaning |
|---|---|
| `evidence.signature` | Digital signature |
| `evidence.watermark-locator` | Locator recovery result |
| `evidence.transparency` | Append-only/transparency proof |
| `evidence.timestamp` | Trusted or decentralized timestamp proof |
| `evidence.witness` | Independent witness proof |
| `evidence.blockchain` | Blockchain/distributed-ledger anchor |
| `evidence.hardware-attestation` | Hardware/TEE attestation |
| `evidence.vc` | Verifiable credential adapter |
| `evidence.execution-proof` | Verifiable execution proof |
| `evidence.zk-proof` | Zero-knowledge proof profile |

### 2.7 Carrier Types

| ID | Meaning |
|---|---|
| `carrier.embedded` | Embedded provenance package/manifest |
| `carrier.sidecar` | Sidecar proof file |
| `carrier.remote` | Remote/resolvable proof |
| `carrier.clipboard` | Structured clipboard representation |
| `carrier.document-metadata` | Document/HTML metadata |
| `carrier.robust-locator` | In-band robust recovery locator |
| `carrier.unicode-aux` | Auxiliary Unicode carrier |

### 2.8 Text Capacity States

| ID | Meaning |
|---|---|
| `capacity.none` | No in-band locator embedded |
| `capacity.provider-only` | Only coarse provider/scheme signal available |
| `capacity.partial-locator` | Partial locator fragments embedded |
| `capacity.full-locator` | Full locator payload target met |
| `capacity.redundant-locator` | Locator has significant recovery redundancy |
| `capacity.low-entropy-unavailable` | Embedding skipped due to insufficient generation freedom |

## 3. Normalization profiles

Normalization profiles require dedicated specifications because they affect cryptographic integrity.

Initial placeholders:

- `norm.text-plain-1`
- `norm.html-visible-text-1`
- `norm.markdown-text-1`
- `norm.json-canonical-1`

These identifiers are provisional until the corresponding normative documents and test vectors exist.

## 4. Registry entry lifecycle

Recommended states:

```text
experimental -> provisional -> recommended -> deprecated -> historic
```

A deprecated entry remains identifiable for historical verification. Registry deprecation MUST NOT make old signed provenance records syntactically disappear.

## 5. No operational control

Maintaining a registry is standards coordination, not operational control. Registry maintainers cannot invalidate a cryptographically valid historical record merely by removing an entry. Entries needed for long-term verification should remain available as historic metadata.
