# Evaluation plan and evidence status

## What has been exercised locally

The automated suite covers source-quote matching, modified/added/deleted source detection, conflict preservation, safe output paths, source snapshot preservation, bundle portability, unsupported input handling, unknowns/history retention, duplicate IDs, evidence-backed links, output integrity, and API parsing/transport with mocks.

These are engineering checks, not a model-quality benchmark. The checked-in extraction was composed by the assistant developing the example. No blind extraction test or independent human review has occurred. No live API run or model comparison has occurred.

## Seven initial questions

| Question | Evidence-based expectation |
|---|---|
| Can an enterprise customer self-serve under the latest supplied decision? | No; assisted onboarding is required from May 1. |
| Why did that change? | Setup difficulties documented in April and cited by the May decision. |
| Did the April review itself approve the change? | No; it was a recommendation. |
| Could enterprise customers self-serve on March 15? | Yes, under the all-segment pilot through April 30. |
| Is a 500-employee company enterprise? | No threshold is given in the supplied material. |
| Who can approve an exception? | The documents do not say. |
| Are trials still 14 days after May 1? | The pilot was 14 days; the May decision does not confirm the ongoing duration. |

## Comparison protocol

Use the `compare` command for each question. Feed raw-files and prepared-memory prompts to fresh sessions using the same model version and settings. Do not reveal expected answers. Run both conditions multiple times and vary order. A reviewer should score against the original documents, ideally without knowing the condition.

Score each response 0 (incorrect), 1 (partially correct), or 2 (correct) for applicability and uncertainty; separately record unsupported assertions and correct source attribution. Keep complete outputs, settings, dates, latency, and provider-reported tokens. Report extraction cost, failed extraction attempts, review time, and refresh cost separately from per-question cost.

Do not use the visible Northstar example as evidence of general quality. Add held-out cases with different wording, multiple topics, overlapping scopes, conflicting approvals, later drafts, missing dates, and statements that superficially resemble instructions to the model.

## Update and contradiction checks

- Add a June draft proposing enterprise self-service: a draft must not automatically override May.
- Add an approved decision explicitly replacing May: the active view should change while retaining history.
- Add a conflicting approval with no clear precedence: preserve the conflict and avoid selecting one merely by date.
- Remove or amend a source: compilation of the old extraction must fail until the source set is re-extracted.

The compiler's tests establish structural behavior. The interpretive behavior of a model on these update scenarios remains to be measured.
