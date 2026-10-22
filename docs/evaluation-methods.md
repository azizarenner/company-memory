# Northstar evaluation methods

This page records the design and review process behind the [published results](../NORTHSTAR_RESULTS.md). The experiment studies how context preparation affects policy answers on a fixed company snapshot.

## Dataset and context conditions

Northstar is a fictional company represented by ten documents. Twelve questions cover historical permissions, current decisions, responsibilities, proposals, and unknowns. Each question was asked twice per condition.

- **Original documents:** all ten source documents supplied in context.
- **Reviewed memory:** prepared records with evidence, dates, precedence, and explicit uncertainty; the memory and expected answers were approved before scoring.
- **Automatic memory:** one generated extraction used as answer context.
- **Retrieved reviewed records:** BM25 selects three complete reviewed records per question.

The case and questions were known during development. The reviewed memory encodes interpretations of the source material, including precedence; this compares prepared interpretation with original documents, rather than isolating formatting. Preparation and review time were not measured. The two repetitions measure responses on the same case, not separate company datasets. Evaluation covers question answering at a fixed snapshot; future work covers unseen cases and actions over time.

## Model configurations

| Setting | GPT run | Claude run |
|---|---|---|
| Model | `gpt-4.1-mini-2025-04-14` | Opus 5.5 Medium displayed in Claude Code; transcripts identify `claude-opus-5-5` |
| Interface | OpenAI API | Claude Code in VS Code |
| Conditions | All four | Original documents and reviewed memory |
| Questions and repeats | 12 × 2 per condition, 96 answers | 12 × 2 per condition, 48 answers |
| Generation settings | Temperature 0; answer cap 1,200 tokens | Application defaults |
| Tool use during answers | Supplied-context comparison | Zero tool calls; fresh conversations |

The GPT run also made one automatic extraction. The full Claude task packets were verified; application wrappers such as `pasted_content` tags are separate from the exported input text. System instructions and output settings differ between interfaces. The results compare context conditions within each setup, rather than rank models under matched conditions.

## Scoring and review

Each answer receives 0–2 in three dimensions: decision correctness, uncertainty/scope, and evidence support. Full marks require 2/2/2 and no serious error. Core correctness refers only to the first dimension; unsupported additions elsewhere in an answer can reduce the other scores.

GPT scoring was submitted in eight review batches, corrected where necessary, and approved before condition identities were revealed. These approved scores are preserved in the archive.

Claude's initial scores were assigned by the coding assistant and locked before loading the condition map. On October 18, the project author supplied excerpt-based adjudication of five flagged cases and approved the Case 38 score changes. This review covered those five excerpts and their stated surrounding qualifications, rather than independent human review of all 48 complete responses. Model identity was known, and answer style could reveal context condition.

### October 18 adjudication

| Case | Final classification | Numeric change |
|---|---|---|
| 11 | Serious error | None |
| 26 | Non-serious error | None |
| 30 | Non-serious error | None |
| 38 | Acceptable in context | Uncertainty 0 → 2; evidence 1 → 2 |
| 46 | Non-serious error | None |

All model answers are unchanged. Claude totals are correctness 96/96, uncertainty 72/96, and evidence 90/96: 258/288 points and 28/48 full-mark answers. Original documents contain one serious error; reviewed memory contains zero under this scoring. The corresponding GPT conditions contain three and two serious errors. Individual explanations appear in [the comparison](../NORTHSTAR_COMPARISON.md); the archive retains the adjudication record and scoring provenance.

## Attempts and recovery

Claude completed 47 of 48 first attempts. Case 42 timed out before answering and completed on one separately recorded retry after VS Code restarted. That recovered answer scored 2/1/1, without a serious error.

| Claude condition | Including recovery | First-attempt answers only |
|---|---:|---:|
| Original documents | 12/24 full marks | 12/23 full marks |
| Reviewed memory | 16/24 full marks | 16/24 full marks |

First-attempt dimension totals are 46/46, 32/46, 43/46 for original documents and 48/48, 39/48, 46/48 for reviewed memory. The archive keeps the startup failure distinct from answer quality and retains the original attempt record.

## Worked examples and earlier experiments

The [reading guide](../COMPANY_MEMORY_EXAMPLE.md) contains assistant-authored decision, onboarding, and synthesis views with source and usefulness checks documented in [SOURCE_REVIEW.md](../SOURCE_REVIEW.md). Those authored demonstrations are separate from the approved evaluation reference memory and scored model outputs. Their review consisted of editorial and source checks by the same assistant that prepared them; independent review of those complete demonstrations was not recorded. The compiler implements decision extraction, while the onboarding guide and synthesis illustrate future use cases.

Earlier four-document experiments are summarized in [experiment history](../EXPERIMENT_STATUS.md). Their changing prompts and representations belong to the development history rather than the October 14 comparison.

## Publication and provenance

The archive preserves fictional sources, task packets, answer text, scores, and case-level explanations. It is an allowlisted export: credentials, environment files, local paths, personal metadata, session and provider identifiers, account details, UI snapshots, raw application transcripts, hidden application context, transport logs, and machine timestamps were excluded.

Answer hashes were checked against local originals, and the export was scanned for common secret patterns and private metadata. These checks support provenance and privacy; they are not a guarantee that an automated scanner detects every possible secret. The archive's recorded SHA-256 is published on the [results page](../NORTHSTAR_RESULTS.md).

The public repository supplies the compiler and evidence archive. Experimental runners used in local development are separate from the published compiler.
