# Northstar company-memory results — October 14, 2026

One fictional, known development case. This release contains the complete ten-document corpus, approved reference memory and answer key, exact question/context packets, unchanged answer text, scores and scoring explanations. It is an evidence archive, not a new release of the local experimental runners or a production reliability claim.

## Results

| Context | GPT-4.1 mini: human-scored full marks | Claude Code: assistant scores + targeted adjudication |
|---|---:|---:|
| Raw documents | 16/24 | 12/24 |
| Reviewed memory | 21/24 | 16/24 |
| Automatic memory | 13/24 | Not run |
| Retrieved reviewed records | 20/24 | Not run |

Full marks require 2/2/2 for correctness, uncertainty/scope and evidence, with no serious error. Claude gave the required core answer in all 48 responses but added unsupported claims in some explanations. Previous matching raw/reviewed core answers were correct in 43/48 responses. Reviewer and application differences prevent treating this as a controlled model ranking.

[Full comparison and individual score explanations](NORTHSTAR_COMPARISON.md). October 18 adjudication classified case 11 as serious, cases 26/30/46 as non-serious, and case 38 as acceptable in context. Case 38 uncertainty and evidence were explicitly revised to 2/2. Claude now has 28/48 full-mark answers and one serious error under the current scoring. This targeted review was excerpt-based, not verified full-packet validation.

## Methods and limitations

- GPT-4.1 mini snapshot: gpt-4.1-mini-2025-04-14, temperature 0, answer output cap 1,200 tokens. Twelve questions, two repetitions, four conditions: 96 answers plus one automatic extraction. Human scores were locked before condition labels were revealed. BM25 retrieved three complete reviewed records.
- Claude Code in VS Code: displayed Opus 5.5 Medium; transcripts identify claude-opus-5-5. Twelve questions, two repetitions, raw and reviewed context only. Fresh conversations, complete prompt text verified, zero tool calls. Default application instructions and output limits were not matched to the API experiment. VS Code sometimes enclosed pasted text in pasted_content tags; exported prompt files contain the exact task packet, without application wrappers.
- Claude: 47/48 first attempts completed. Case 42 timed out before answering, then completed on a separately labelled recovery attempt after restart. Excluding recovery: raw 12/23 full marks, reviewed 16/24. Do not count the recovery as a first-attempt success.
- Claude scores were assigned by the developing assistant, then revised by user-submitted excerpt-based adjudication of five flagged cases. The full 48-answer set has not been independently human-validated. The condition map was opened after provisional scores were locked, but style can reveal condition; model identity was known. The earlier human scores were not changed.
- The source case and questions were already known development material. Repetitions are not independent companies. These tests evaluate answers, not autonomous actions over time.

## Files

- sources/: unchanged fictional source texts.
- reference/: approved question/answer key, reviewed memory and automatic memory. Approval metadata identifies a role rather than a personal name.
- gpt-4.1-mini/: 96 unchanged answer strings with human scores, and deduplicated exact instruction/context requests.
- claude-code/: 48 unchanged answer strings with revised scores and the adjudication record, deduplicated input packets, case mapping, attempt record, scoring method and comparison.
- MANIFEST.json: SHA-256 digests for the released files.

## Privacy and provenance

This is an allowlisted export. It excludes credentials and environment files, local filesystem paths, usernames in local metadata, session/conversation identifiers, provider request/response identifiers, account/subscription details, UI snapshots, raw application transcripts, hidden application context, transport logs, and machine timestamps. Only model answer text and task-relevant research fields were selected from the transcripts; answer text was not rewritten. The local originals remain private and unchanged. A package scan checks common secret patterns and private metadata, and answer hashes are checked against the local originals. This is not a promise that an automated scan detects every possible secret.

The Substack draft is kept separate. Existing public examples remain historical documentation; this release does not imply that every earlier worked guide or prototype feature has been validated.

Download the [complete evidence archive](northstar-results-2026-10-14.zip). Paths listed above are inside the archive. Updated October 18, 2026.

Archive SHA-256: `d80863bb2149376755483f2f221d40da912579bf4d7717a53766371c3037dbbc`.
