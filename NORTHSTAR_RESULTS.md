# Northstar company-memory results

**Reviewed memory produced more fully supported answers than original documents in both tested model setups.** Remaining errors show why memory representation and answer generation need separate checks.

This study uses ten fictional company documents and twelve questions about policy history, onboarding, authority, and unresolved information. Each question was asked twice per context condition.

## Results

| Context | GPT-4.1 mini full marks | Opus 5.5 in Claude Code full marks |
|---|---:|---:|
| Original documents | 16/24 | 12/24 |
| Reviewed memory | 21/24 | 16/24 |
| Automatic memory | 13/24 | Not tested in this run |
| Retrieved reviewed records | 20/24 | Not tested in this run |

Full marks require 2/2 for correctness, uncertainty/scope, and evidence, with no serious error. The original-document and reviewed-memory conditions produced 43/48 correct core answers for GPT and 48/48 for Claude. A correct core answer can still lose full marks through unsupported additions.

The comparison concerns context preparation within each setup. Model interfaces and scoring processes differ; [methods and review scope](docs/evaluation-methods.md) explain the study design.

## What the answers revealed

- **Historical applicability:** some GPT answers denied March self-service authorization before correctly explaining that the February pilot permitted it.
- **Unresolved authority:** Claude's “Nobody can grant an exception here” went beyond a source that named no exception approver.
- **Evidence versus interpretation:** accurate quotations did not consistently prevent contradictory or overly certain conclusions.

The next experiments address updates, context sharing, permissions, and cost. See the [roadmap](docs/roadmap.md).

## Inspect the evidence

- [Comparison and individual score explanations](NORTHSTAR_COMPARISON.md)
- [Evaluation methods and scoring history](docs/evaluation-methods.md)
- [Northstar sources and worked examples](COMPANY_MEMORY_EXAMPLE.md)
- [Download the complete evidence archive](northstar-results-2026-10-14.zip)

The archive contains the following directories:

| Path | Contents |
|---|---|
| `sources/` | Ten fictional source documents |
| `reference/` | Approved question/answer key, reviewed memory, automatic memory |
| `gpt-4.1-mini/` | 96 original answers, scores, and exact task packets |
| `claude-code/` | 48 original answers, scores, task packets, case mapping, and attempt records |
| `MANIFEST.json` | SHA-256 digests for released files |

The October 18 scoring update is included. Model answers remain unchanged. The archive contains selected research fields and excludes credentials, local paths, session identifiers, and raw application transcripts. The [methods page](docs/evaluation-methods.md#publication-and-provenance) describes publication checks.

Archive SHA-256: `d80863bb2149376755483f2f221d40da912579bf4d7717a53766371c3037dbbc`.
