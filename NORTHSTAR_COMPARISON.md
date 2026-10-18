# Claude Code vs earlier GPT-4.1 mini: scoring with targeted adjudication

Initial scorer: Codex assistant. On October 18 the user submitted excerpt-based adjudication of five flagged cases and approved Case 38 uncertainty and evidence scores of 2/2. This was not a verified full-packet review or independent validation of all 48 answers. The earlier scores remain the user-approved scores, unchanged. The scoring file was frozen and hashed before loading the Claude condition map for aggregation. Style can reveal conditions, and model identity was known.

## Main findings

All 48 Claude answers give the required core answer correctly. Only 28/48 earn full marks across the entire answer. Deductions concern unsupported additions and uncertainty, not a repeat of the earlier March 15 contradiction. This does not establish that Claude is generally better or worse.

## Matching conditions

Claude ran only raw documents and reviewed memory. Automatic extraction and retrieved reviewed memory were not rerun. Each condition contains 12 questions twice.

| Setup and scorer | Context | Full marks | Correct core answers | Correctness | Uncertainty/scope | Evidence |
|---|---|---:|---:|---:|---:|---:|
| GPT-4.1 mini · prior human scores | raw | 16/24 | 21/24 | 43/48 | 39/48 | 45/48 |
| GPT-4.1 mini · prior human scores | reviewed | 21/24 | 22/24 | 44/48 | 45/48 | 48/48 |
| Claude Code Opus 5.5 Medium · assistant + targeted adjudication | raw | 12/24 | 24/24 | 48/48 | 33/48 | 44/48 |
| Claude Code Opus 5.5 Medium · assistant + targeted adjudication | reviewed | 16/24 | 24/24 | 48/48 | 39/48 | 46/48 |

Core correctness is the rubric’s decision-correctness dimension. It is not a claim that every sentence is correct. Full marks require 2/2/2 and no serious error. Scores across runs are descriptive because reviewer and interface differ.

## Error examples

- **Historical permission improved in these outputs:** all four Claude Q05 answers correctly begin Yes for March 15, 2026; all four earlier raw/reviewed Q05 answers contained a contradictory No opening. Two Claude answers, cases 30 and 46, nevertheless assert an unsupported 2027 policy. Case 17 correctly qualifies the future year; case 28 avoids asserting it.
- **Named-case causality:** all four Claude Q11 answers preserve the unknown Cedar/Vale-to-April connection. Earlier raw answers had one serious error; earlier reviewed answers already handled this correctly.
- **Unknown authority becomes universal denial:** case 11 says “Nobody can grant an exception here”; case 26 says “No one can grant exceptions.” Source 06 names no approver and grants no waiver power through those responsibilities; it cannot establish that nobody has authority elsewhere.
- **Context matters when scoring:** case 38 says “No paid-conversion data exists,” but repeatedly limits its claims to the supplied record. The excerpt-based adjudication accepted that surrounding scope; uncertainty and evidence are now both 2/2. It is not counted as a failure.
- **Additional factual slip:** case 40 says “The pilot ran for 14 days.” The approved duration was 14 days per trial; the pilot approval covered a period through April 30.

## Final submitted severity classifications

The five flagged cases were adjudicated from excerpts and stated surrounding qualifications, not a verified reading of the full packet. Case 11 is serious; cases 26, 30 and 46 are non-serious errors; case 38 is acceptable in context. The user explicitly approved increasing Case 38 uncertainty/scope from 0 to 2 and evidence from 1 to 2. Other numeric scores and all model answers are unchanged.

Claude raw has one serious error (case 11); reviewed memory has zero under the current scoring. Across all 48 answers, the updated scores are correctness 96/96, uncertainty/scope 72/96 and evidence 90/96: 258/288 points, with 28/48 full-mark answers. These figures combine assistant scoring with targeted excerpt-based adjudication, not full independent human validation. Earlier raw/reviewed human scores retain 3 and 2 serious errors. This is not a validated cross-model ranking.

See severity-adjudication-2026-10-18.json for the decision record. The initial pre-adjudication version remains available in Git history; the original local masked score lock is unchanged.

## Startup failure and recovery

47/48 first attempts completed. Case 42 failed before answering and was later rerun once after VS Code restarted. Its recovery is shown separately and never substituted for the original failure. It received 2/1/1 = 4/6, with no primary operational serious error.

- Excluding recovery, Claude raw: 12/23 full marks; dimension sums 46, 32, 43 out of 46 each.
- Excluding recovery, Claude reviewed: 16/24 full marks; dimension sums 48, 39, 46 out of 48 each.

The incomplete raw denominator is not an equally balanced 24-answer set; report the startup failure independently from answer quality.

## What this changes for the article

The useful result is a shift in failure mode: correct remembered facts did not force reliable answers in the earlier run; the Claude Code run resolved the tested historical permission correctly, yet added unsupported claims beyond the question. Both context representation and answer generation need evaluation. Longer answers created more opportunities for these observed errors, but this run does not establish verbosity as their cause.

## Limits

One fictional known case, two repeats, no held-out companies. Claude Code uses its own system instructions, settings and context wrappers; it is not matched to the earlier API’s temperature and 1,200-token output cap. Claude scores combine assistant judgments with targeted excerpt-based adjudication, while previous scores were human-approved; scoring all answers with one independent blinded reviewer would be needed for a stronger ranking. Raw/reviewed only means this says nothing new about Claude extraction quality or whether the automatic bundle would succeed with Claude. No model or provider superiority claim is warranted.

## Individual scores

C = core decision correctness, U = uncertainty/scope, E = evidence, each 0–2. Serious error reflects the current scoring, including the five submitted excerpt-based adjudications.

| Case | Q | Context | Attempt | C | U | E | Serious error | Review note |
|---|---|---|---:|---:|---:|---:|---|---|
| case-01 | Q03 | reviewed | 1 | 2 | 2 | 2 | No | Recorded April setup difficulties correctly explain the May decision. The named-case caveat is immediately qualified by the source; no causal or outcome claim is invented. |
| case-02 | Q06 | raw | 1 | 2 | 1 | 2 | No | Core recommendation/approval distinction is correct. The added “Gap between April 30 and May 1” invents a calendar coverage uncertainty: through April 30 and from May 1 are consecutive dates. Actual rollout would be a different question. |
| case-03 | Q03 | raw | 1 | 2 | 2 | 2 | No | Correct documented rationale; selected cases remain illustrative, their use by April unresolved, and conversion benefit unproven. Supported glossary detail is not penalized. |
| case-04 | Q11 | reviewed | 1 | 2 | 2 | 2 | No | The opening No is immediately qualified as lack of support, and the body explicitly says Unknown. Unlike earlier A010/A020, it does not categorically deny case involvement. Proposal documents never being operative by themselves is accepted. |
| case-05 | Q08 | raw | 1 | 2 | 2 | 2 | No | Correctly leaves the route undecided, directs missing labels to Sales Operations and requires an incomplete draft. References support the procedure. “Only Sales Operations” is read as the designated process contact, not a universal claim about authority. |
| case-06 | Q08 | reviewed | 1 | 2 | 2 | 2 | No | Correct missing-segment procedure; explicitly preserves duration and exception-authority uncertainty. |
| case-07 | Q11 | raw | 1 | 2 | 2 | 2 | No | Correctly preserves the unresolved case-to-review link and the documented review-to-decision rationale. Later review is not treated as proof that earlier consideration never occurred. |
| case-08 | Q11 | reviewed | 1 | 2 | 2 | 2 | No | Correct evidence-bounded denial of the asserted causal chain. Explicitly identifies the case-to-review connection as unknown. |
| case-09 | Q02 | reviewed | 1 | 2 | 2 | 2 | No | Self-service is permitted, not mandatory; assisted help is not declared forbidden. Segment and duration caveats are supported. |
| case-10 | Q04 | reviewed | 1 | 2 | 1 | 2 | No | Core answer is correct, but “the February 3 approval launched trials” conflates authorization with actual launch. The record authorizes a pilot and later describes it operating, without establishing its launch date. |
| case-11 | Q07 | raw | 1 | 2 | 0 | 1 | Yes | October 18 excerpt-based adjudication: Categorical denial of exception authority can foreclose escalation relevant to the duration question; later uncertainty does not adequately qualify it. |
| case-12 | Q09 | raw | 1 | 2 | 2 | 2 | No | Correctly states no supplied authorization for Customer Success and treats existence of exceptions and an approver as unresolved. |
| case-13 | Q06 | reviewed | 1 | 2 | 2 | 2 | No | Correct recommendation versus approval sequence and historical applicability, with explicit unresolved fields. |
| case-14 | Q09 | reviewed | 1 | 2 | 1 | 2 | No | Core waiver answer is carefully bounded, including possible authority elsewhere. Added “No length after April 30 has been approved” needs “in the supplied record,” consistent with the prior A011 qualification. |
| case-15 | Q10 | reviewed | 1 | 2 | 2 | 2 | No | Correct proposal status, no established delivery approval, and no supersession of enterprise assistance. Read as a source-bounded status report; no assertion that delivery never happened. |
| case-16 | Q04 | raw | 1 | 2 | 2 | 2 | No | Correct distinction between January proposal and February pilot approval, preserving scope and subsequent May decision. |
| case-17 | Q05 | raw | 1 | 2 | 2 | 2 | No | Correct Yes for March 15, 2026; distinguishes authorized access from demonstrated operation. The 2027 discussion explicitly says future policy cannot be confirmed, unlike cases 30/46. |
| case-18 | Q01 | reviewed | 1 | 2 | 2 | 2 | No | Correct enterprise route and date; duration and exception authority remain unresolved. Recommended handoff is not represented as an executed action. |
| case-19 | Q11 | raw | 1 | 2 | 2 | 2 | No | Explicitly labels the named-case connection Unknown and correctly identifies the May-to-April link as a stated basis, without denying earlier consideration. |
| case-20 | Q12 | reviewed | 1 | 2 | 2 | 2 | No | No conversion improvement established, with effect explicitly unknown. “Reported anywhere” is interpreted in its immediate supplied-source framing; no claim of zero effect. |
| case-21 | Q09 | raw | 1 | 2 | 2 | 2 | No | Correctly denies established Customer Success waiver authority while leaving exception processes and approvers unresolved. |
| case-22 | Q01 | raw | 1 | 2 | 1 | 2 | No | Correct route. “No approved exception path exists” exceeds “no path is established in these sources.” Later no-document qualification softens it; score as a scope omission, consistent with prior waiver cases. |
| case-23 | Q01 | raw | 1 | 2 | 1 | 2 | No | Correct route. “No one named in the sources can grant an exception” claims inability, where source 06 only establishes that these responsibilities grant no authority. Later uncertainty warrants a qualification rather than a primary-route error. |
| case-24 | Q10 | raw | 1 | 2 | 1 | 2 | No | Correct checklist status and continuing assisted route. “Routing teams can’t approve such a change” extends source 06’s non-grant of onboarding-waiver authority to a categorical claim about product/change approval powers. |
| case-25 | Q07 | reviewed | 1 | 2 | 1 | 2 | No | Correct refusal to promise a duration. “No later approval sets a trial length” needs an explicit supplied-record limit; the closing section does preserve the underlying unknown. |
| case-26 | Q02 | raw | 1 | 2 | 0 | 1 | No | October 18 excerpt-based adjudication: Unsupported exception restriction needs correction but leaves the ordinary smaller-customer onboarding route intact. |
| case-27 | Q01 | reviewed | 1 | 2 | 1 | 2 | No | Correct enterprise route. “No approved length exists after April 30” is broader than no current approval being established in the supplied record. |
| case-28 | Q05 | reviewed | 1 | 2 | 2 | 2 | No | Correct historical Yes, temporal precedence, and authorization/actual-operation distinction. Does not apply the May rule retroactively or assert a future-year policy. |
| case-29 | Q02 | reviewed | 1 | 2 | 2 | 2 | No | Correct optional self-service and explicitly avoids forbidding assisted help. Duration and waiver caveats remain evidence-bounded. |
| case-30 | Q05 | raw | 1 | 2 | 0 | 1 | No | October 18 excerpt-based adjudication: Historical answer is correct; future policy claim needs an explicit unchanged-policy assumption. |
| case-31 | Q04 | raw | 1 | 2 | 2 | 2 | No | Correct proposal/approval sequence and limited pilot scope; no unsupported ongoing duration commitment. |
| case-32 | Q02 | raw | 1 | 2 | 2 | 2 | No | Correctly permits smaller-customer self-service, preserves uncertainty about offering assisted help, and makes no claim that assistance is forbidden. |
| case-33 | Q07 | raw | 1 | 2 | 1 | 2 | No | Correct duration refusal. “No one named in the sources can approve an exception” and the draft’s “duration has not been approved” need evidentiary qualification; absence of a named approver is not proof of inability. |
| case-34 | Q03 | raw | 1 | 2 | 1 | 2 | No | Correct rationale and named-case uncertainty. Added “routing teams can’t waive the decision” should be limited to the authority established by the supplied responsibilities, not all possible authority. |
| case-35 | Q04 | reviewed | 1 | 2 | 2 | 2 | No | Correct January non-authorization and February time-limited approval. The recency aside is unnecessary but not a material contrary policy claim. |
| case-36 | Q12 | raw | 1 | 2 | 1 | 2 | No | Correct absence of demonstrated conversion improvement. “Neither has been measured or reported” asserts no measurement occurred; the sources only establish no supplied measurements/results. The product-review expectation also should stay scoped to its proposal. |
| case-37 | Q08 | reviewed | 1 | 2 | 2 | 2 | No | Correct missing-segment handling, incomplete draft, undecided route, and qualified uncertainty about approvers elsewhere. |
| case-38 | Q12 | raw | 1 | 2 | 2 | 2 | No | October 18 excerpt-based adjudication: Repeated supplied-context qualifications adequately scope the isolated statement that no data exists; wording improvement remains appropriate. |
| case-39 | Q06 | reviewed | 1 | 2 | 1 | 2 | No | Correct April recommendation/May approval distinction. Added “No current approval sets a length” requires “in the supplied record,” consistent with prior duration deductions. |
| case-40 | Q03 | reviewed | 1 | 2 | 1 | 1 | No | Correct rationale and causal uncertainty. “The pilot ran for 14 days” misstates pilot duration: 14 days was each trial’s approved duration, while the pilot approval ran through April 30. This ancillary factual error needs correction. |
| case-41 | Q08 | raw | 1 | 2 | 2 | 2 | No | Correctly leaves route unset, directs the missing label to Sales Operations, and preserves action authorization and duration boundaries. |
| case-42 | Q10 | raw | 2 | 2 | 1 | 1 | No | Recovery attempt. Correct proposal status and continuing assisted policy. “It was never meant to replace assisted onboarding” claims historical intent beyond the record’s statement that it is a separate potential improvement. Also avoid converting Product’s documented proposal role into exhaustive approval-power limits. |
| case-43 | Q10 | reviewed | 1 | 2 | 2 | 2 | No | Correct current proposal status, no established implementation approval/delivery date, and no precedence over the May decision. Later explicit source limits resolve the introductory shorthand. |
| case-44 | Q09 | reviewed | 1 | 2 | 1 | 2 | No | Correct supplied-source waiver boundary and explicit possibility of an approver elsewhere. The closing “It can’t approve the exception” becomes categorical again; apply the same minor scope deduction as earlier A021. |
| case-45 | Q07 | reviewed | 1 | 2 | 2 | 2 | No | Correct refusal to promise 14 days, preserves actual post-pilot duration as unknown and asks for a current approval. No invented replacement duration. |
| case-46 | Q05 | reviewed | 1 | 2 | 0 | 1 | No | October 18 excerpt-based adjudication: Same principle as case 30; assumptions heading and waiver uncertainty do not explicitly qualify policy continuity. |
| case-47 | Q12 | reviewed | 1 | 2 | 2 | 2 | No | Correctly states no established paid-conversion improvement, distinguishes activation, and leaves the causal effect unknown rather than zero. |
| case-48 | Q06 | raw | 1 | 2 | 1 | 2 | No | Correct April recommendation/May decision sequence. The added unresolved “gap between April 30 and May 1” creates unnecessary coverage uncertainty despite consecutive effective dates; implementation continuity is a separate question. |
