# Architecture

## Two separate responsibilities

1. Extraction: an AI model or human reads complete source documents and creates typed JSON. This is the interpretive step: deciding what a document means, what was approved, and what remains unknown.
2. Compilation: deterministic Python validates structure, input hashes, evidence excerpts, dates, IDs, and links. It writes source snapshots, OKF draft records, context, and a review list.

Separating these responsibilities makes incorrect extraction inspectable. A successful compiler run does not certify the model's interpretation.

## Extraction contract

The top level contains a title, an exact source manifest, and concepts. Each concept has a stable slug, title, evidence-backed claims, unknowns, conflicts, and optional evidence-backed links to other concepts.

Claims are typed as current decision, historical decision, proposal, recommendation, rationale, or observation. The JSON contract lives in `extraction.schema.json`; tests ensure it matches the runtime schema. Current decisions must retain scope and effective dates in their text. All emitted concepts are draft regardless of their claims' approval status.

The compiler checks a quote as an exact Unicode substring of the original decoded source. For repeated quotes, its displayed line number points to the first occurrence. Hashes are calculated over original bytes; snapshots preserve those bytes.

## Publication of a bundle

Validate first. Create output in a temporary sibling directory. Render artifacts, calculate hashes, check the resulting bundle, then move it to the requested new directory. Existing bundles are not overwritten. This is intended for one local writer; it is not a concurrent publication service.

## Consumption

`context.md` concatenates the knowledge index and all concept pages with file labels. It includes selected evidence excerpts, not all source bodies. No tool-driven lookup is needed to consume this context, but source pointers are only checkable when the accompanying snapshots are available.

The source set size cap is independent of a model's context window. Generated context can be longer than the originals when records include provenance and review information. Compactness must be measured rather than assumed.

## Deliberate boundaries

No source mutation, automatic policy enforcement, database, semantic search, scheduled update process, enterprise access control, or authority resolver. The current tool is a research prototype for bounded document sets.
