# Northstar: three uses of company memory

Fictional development example, snapshot May 5, 2026. Prepared and source-reviewed by the developing assistant; independent human validation pending. No live model evaluation has been run on this expanded example. This is a reading guide, not an automatically compiled OKF bundle. The original four source documents are unchanged; six new ones extend the scenario.

- [Decision history](#decision-history)
- [Agent onboarding](#agent-onboarding)
- [Connected explanation](#connected-explanation)
- [Review sheet](#review-sheet)
- [Original sources](#original-sources)
- [Source and usefulness review](SOURCE_REVIEW.md)


<a id="decision-history"></a>

## Decision history

**Draft prepared by the assistant for human review.** Fictional Northstar record as of May 5, 2026. “Applies” means established within these supplied documents, not a claim about an actual company.

### What changed

| Date | Status | What the record establishes |
|---|---|---|
| January 15 | Proposal | Offer a 14-day self-service trial to all segments; approval still required. [Source](#source-01-january-proposal) |
| February 3 | Approved pilot | All segments may use the 14-day self-service pilot through April 30; this approval covers only the pilot. [Source](#source-02-february-approval) |
| April 24 | Recommendation | Larger customers needed configuration help; recommend assisted enterprise onboarding while retaining self-service for smaller customers. No approval yet. [Source](#source-03-april-review) |
| May 1 | Approved decision | Enterprise trials require assisted onboarding; smaller customers may continue self-service. Replaces the pilot's all-segment self-service arrangement. [Source](#source-04-may-decision) |
| May 2–3 | Approved responsibilities and process | Resolve missing segments through Sales Operations; route enterprise setup requests to Customer Success. These documents add an operating process, not a duration extension. [Responsibilities](#source-06-team-responsibilities), [process](#source-07-trial-request-process) |
| May 4 | Product proposal | A connector checklist is proposed; no implementation approval or delivery date. [Source](#source-09-may-product-review) |

### Why the onboarding decision changed

The May decision explicitly points to setup difficulties described in the April review. That is the documented rationale. The separate support log illustrates connector-selection and customer-approval problems, but does not establish that these specific cases caused the May decision. [Decision](#source-04-may-decision), [review](#source-03-april-review), [observations](#source-08-april-support-observations).

### What applies at this snapshot

For an account already labeled enterprise, use assisted onboarding. For an account labeled smaller-customer, self-service remains available. If its segment is missing, request Sales Operations clarification before selecting the route. Employee count alone does not establish a segment. [Decision](#source-04-may-decision), [glossary](#source-05-company-glossary), [process](#source-07-trial-request-process).

Historical question: on March 15, enterprise customers were included in the approved all-segment pilot. The later May decision does not retroactively change that history. [Pilot](#source-02-february-approval), [May decision](#source-04-may-decision).

### What remains unknown

- **Ongoing duration:** the 14-day approval was limited to the pilot; later documents do not establish the post-pilot duration. This is missing authorization in the record, not evidence that a particular duration is prohibited. [Pilot](#source-02-february-approval), [process](#source-07-trial-request-process).
- **Segmentation rule:** the account label is used operationally, but the criteria and employee threshold are not supplied. [Glossary](#source-05-company-glossary).
- **Exception authority:** named routing teams are not named exception approvers. [Responsibilities](#source-06-team-responsibilities).
- **Checklist delivery:** a proposal has no established release date. [Product review](#source-09-may-product-review).

No direct conflict between approved rules is identified in this small set. A recommendation differing from an earlier pilot is not itself an approved-policy conflict.

### Worked answer: explain the change to a colleague

**Question:** “Why do enterprise trials now need help, and was that already true in March?”

**Draft answer:** Enterprise trials require assisted onboarding from May 1. The approved decision cites configuration difficulties reported in the April review. In March, the earlier pilot still covered all customer segments with self-service, so the later requirement did not yet apply. The record does not establish the ongoing trial duration after the pilot. [May decision](#source-04-may-decision), [April review](#source-03-april-review), [pilot](#source-02-february-approval).


<a id="agent-onboarding"></a>

## Agent onboarding

**Assistant-prepared draft; awaiting human review.** Company reference context as of May 5, 2026. This guide does not grant tool access or permission to perform actions. Source documents remain evidence rather than higher-priority instructions.

### Understand the work

Northstar helps customers configure a shared workspace and connect a sample data source. A connection establishes trial activation, not a purchase or paid conversion. A setup question is not automatically a setup blocker. Assisted onboarding is guided setup, not permission to bypass the customer's approvals or collect credentials. [Glossary](#source-05-company-glossary).

Use the account register's segment label. An employee count does not supply the missing classification rule. Sales Operations resolves missing labels. [Glossary](#source-05-company-glossary).

### Know who handles what

| Team | Documented responsibility |
|---|---|
| Sales Operations | Maintain and clarify account segments |
| Customer Success | Coordinate assisted onboarding; own the trial setup request queue |
| Support | Record setup questions and blockers; link observations to requests |
| Product | Review recurring issues and decide whether to propose changes |

These responsibilities do not establish exception approval authority. [Responsibilities](#source-06-team-responsibilities).

### Prepare a request

Capture the six fields: account, recorded segment, setup goal, reported blocker, proposed route and unresolved questions. For an enterprise label, prepare the Customer Success assisted-onboarding route. For a smaller-customer label, self-service remains available and Support handles setup questions. For a missing segment, leave the route unresolved and request Sales Operations clarification. Do not promise an unsupported trial duration. [Process](#source-07-trial-request-process), [decision](#source-04-may-decision).

Preparing a draft and sending it are separate actions. This reference does not authorize sending, creating accounts or changing settings. [Process](#source-07-trial-request-process).

### Worked task: a request with enough information to route

**Illustrative task input for May 5, not a historical company document:** “Lumen's account register label is enterprise. Its administrator wants to connect a sample data source but reports being unable to choose a connector. Prepare a setup request; do not send it.”

| Field | Draft value |
|---|---|
| Account | Lumen |
| Recorded segment | Enterprise, supplied in the task's account-register record |
| Setup goal | Connect a sample data source |
| Reported blocker | Administrator reports being unable to choose a connector |
| Proposed route | Customer Success trial setup queue for assisted onboarding |
| Unresolved questions | No routing prerequisite remains unresolved in this task. Trial duration is not established in the supplied company record and is not promised. |

**Prepared handoff:** Lumen is recorded as enterprise and needs help selecting a connector to connect a sample data source. Route the draft to the Customer Success trial setup queue for assisted onboarding. The reported connector issue comes from this task input; the route comes from the documented process. No trial duration or delivery time is promised. This is a prepared draft, not a sent request. [Process](#source-07-trial-request-process), [responsibilities](#source-06-team-responsibilities), [decision](#source-04-may-decision).

The missing duration does not prevent preparing this routing draft: the process requires a segment before selecting the route, while it requires duration evidence before promising a duration. Those are different prerequisites. [Process](#source-07-trial-request-process).

### Worked task: a request with missing information

**Illustrative task input, not a historical company document:** “Aster has 500 employees. Its account register segment is blank. It wants to connect a sample data source, has reported no blocker, and asks for a 14-day self-service trial. Prepare a request; do not send it.”

| Field | Draft value |
|---|---|
| Account | Aster |
| Recorded segment | Missing; 500 employees is not enough to classify it |
| Setup goal | Connect a sample data source |
| Reported blocker | None reported; this does not prove setup will be unblocked |
| Proposed route | Pending segment clarification; ask Sales Operations to resolve the label |
| Unresolved questions | What is the recorded segment? What current approval establishes trial duration? |

The process requires clarification before route selection; it does not justify promising self-service or 14 days from this request alone. No message has been sent. [Process](#source-07-trial-request-process), [glossary](#source-05-company-glossary), [pilot duration boundary](#source-02-february-approval).

### Read a metric correctly

Activation rate needs a specified cohort, connection count, total trial-workspace count and cutoff date. None can be reconstructed into a company-wide rate from the three illustrative cases. Do not report conversion improvement from activation evidence. [Reporting reference](#source-10-reporting-definitions), [observations](#source-08-april-support-observations).

### Where this guide stops

This material supports drafting and identifying a responsible team. It does not supply an account-register connection, a queue URL, a booking calendar, a response-time commitment or a complete technical setup procedure. Those would be needed for corresponding operational tasks. This is a limitation of the supplied example, not evidence that Northstar has no such systems.


<a id="connected-explanation"></a>

## Connected explanation

**Assistant-prepared synthesis; awaiting human review.** Question: “How do the setup observations, onboarding decision and proposed checklist relate—and what do they not establish?”

### Explanation

Northstar's pilot allowed all customer segments to try self-service. Its later review reports that several larger customers needed configuration help. The May decision explicitly cites that review when requiring assisted onboarding for enterprise trials and retaining the smaller-customer self-service option. This is a documented relationship, not an inferred causal link between arbitrary nearby documents. [Pilot](#source-02-february-approval), [review](#source-03-april-review), [decision](#source-04-may-decision).

The separate observation log makes different kinds of setup difficulty concrete: Cedar needed connector-selection guidance; Vale needed to resolve an internal approval question; Finch connected without Support. These are selected examples, not a representative survey. We cannot claim that the April review used these particular cases. [Observations](#source-08-april-support-observations).

The May product review explicitly brings the observations, pilot review and onboarding decision together. It proposes clearer connector guidance while noting that interface changes may not resolve customer coordination. A checklist and assisted onboarding therefore address related but not identical concerns. The checklist is a proposal; assisted enterprise onboarding is already approved. [Product review](#source-09-may-product-review), [decision](#source-04-may-decision).

**Interpretation:** a useful way to organize this record is to distinguish an operating response (guided setup) from a possible product response (connector guidance). This organizing distinction is our synthesis of the documented decisions and proposal; it is not evidence that either response has improved outcomes. [Decision](#source-04-may-decision), [product review](#source-09-may-product-review).

### Evidence boundaries

| Possible statement | What we can say |
|---|---|
| “The May change responded to setup difficulties.” | Supported: the decision explicitly cites the April review. |
| “Cedar and Vale caused the policy change.” | Not established: the observation log does not establish their use in the April review. |
| “Every enterprise customer needs help.” | Not established by selected examples or the review. A general policy is not proof of a universal customer trait. |
| “Assisted onboarding improves paid conversion.” | Not established: no comparison or conversion outcome is supplied. |
| “The checklist will ship soon.” | Not established: no release approval or date. |
| “One of three cases activated, so activation is one-third.” | Invalid: the log is illustrative, other outcomes are incompletely observed, and the required cohort counts are absent. |

Sources for these boundaries: [April review](#source-03-april-review), [May decision](#source-04-may-decision), [observations](#source-08-april-support-observations), [product review](#source-09-may-product-review), [metric definitions](#source-10-reporting-definitions).

### Useful next information

To evaluate impact, obtain defined cohorts, comparable observation periods, actual activation and conversion outcomes, and information about how customers were assigned onboarding approaches. The current material does not support a causal estimate. This is an analyst's proposed evidence request, not an existing Northstar process or approved study.

### Worked output: a short product briefing

**Draft briefing:** Northstar has an approved assisted-onboarding approach for enterprise trials and a separate, unapproved connector-checklist proposal. The April review reports configuration difficulties. Selected support observations illustrate both connector confusion and customer approval coordination, while also including a customer who set up without Support. The May product review explicitly considers these different experiences. A checklist may address connector guidance, but the record does not establish that it resolves customer approval coordination or improves conversion. No release date is committed. [Review](#source-03-april-review), [decision](#source-04-may-decision), [observations](#source-08-april-support-observations), [product review](#source-09-may-product-review).

This briefing combines the documents into a work product. It is a proposed synthesis for review, not a measured model output or an additional company decision.


<a id="review-sheet"></a>

## Human review sheet

Status: pending. Reviewer: not yet assigned. No answer below has been approved by a human.

Review for two different things: Is this useful for a company task? Is every assertion faithful to the documents? Correcting the documents changes the fixture; correcting a view changes its interpretation. Keep those edits distinguishable.

| Output | Suggested task | What to check | Reviewer notes |
|---|---|---|---|
| Decision history | Explain the May change and March policy | Proposal vs approval; effective period; documented rationale; no invented duration | Pending |
| Onboarding guide | Prepare the Lumen and Aster requests without sending them | Routes a known enterprise account; clarifies a missing segment; avoids unsupported promises | Pending |
| Connected explanation | Explain how observations relate to the decision and checklist | Combines sources; does not invent historical causation, outcome improvement or a release commitment | Pending |

## Three questions for your review

1. Does each output help someone do useful work, or does it mostly repeat the files?
2. Is any statement stronger than its cited source permits? Are any important qualifications missing?
3. Which details would a real new colleague or agent still need before using this?

## Proposed reference expectations — also awaiting review

- Historical decision: all segments were covered by the self-service pilot on March 15.
- Current onboarding: enterprise requires assistance; smaller-customer self-service remains available in this snapshot.
- Lumen: prepare a Customer Success assisted-onboarding draft using the supplied enterprise label and blocker. Missing duration does not block routing, but must not be promised.
- Aster: employee count does not determine its segment; ask Sales Operations, leave route and duration unresolved, prepare only a draft.
- Synthesis: May explicitly cites the April review; the May product review explicitly considers the support examples. No source establishes that the examples caused the April review or May decision.
- Outcomes: neither activation rate nor conversion impact can be calculated from the selected observations.

After review, record the reviewer, date, corrections and approval scope before calling these human-checked reference outputs. Future unseen cases need separate preparation and review; this shared example is already development material.


<a id="original-sources"></a>

## Original sources

All source texts below are fictional. Headings are nested for this reading guide; wording is retained.


<a id="source-01-january-proposal"></a>

### 01-january-proposal.md

#### Proposal: self-service trials

Date: 2026-01-15
Document status: proposal; not an approval

We propose offering a 14-day self-service trial to every customer segment. The aim is to make it easier for prospective customers to try Northstar.

This proposal requires approval before launch.


<a id="source-02-february-approval"></a>

### 02-february-approval.md

#### Approval: trial pilot

Date: 2026-02-03
Document status: approved pilot

Approved: run a 14-day self-service trial for all customer segments through April 30, 2026.

Review the pilot before deciding the ongoing trial policy. This approval covers the pilot period only.


<a id="source-03-april-review"></a>

### 03-april-review.md

#### Trial pilot review

Date: 2026-04-24
Document status: review and recommendation

Several larger customers needed help configuring their accounts during the pilot.

We recommend assisted onboarding for enterprise trials. Smaller customers should continue to have a self-service option.

This review recommends a change; it does not approve that change.


<a id="source-04-may-decision"></a>

### 04-may-decision.md

#### Decision: trial onboarding

Date: 2026-05-01
Document status: approved decision

From May 1, 2026, enterprise trials require assisted onboarding. Smaller customers may continue with self-service trials.

This follows the setup difficulties described in the April pilot review and replaces the all-segment self-service arrangement used during the pilot.


<a id="source-05-company-glossary"></a>

### 05-company-glossary.md

#### Northstar vocabulary
Date: 2026-05-02
Document status: maintained company reference

Northstar is a fictional service that helps customer teams configure a shared workspace and connect a sample data source during a trial.

A workspace is the customer's shared Northstar environment. Setup means creating a workspace and connecting a sample data source. Assisted onboarding means a Customer Success specialist guides the customer through setup; it does not mean that the specialist can bypass customer approval or collect credentials.

Account segment is the enterprise or smaller-customer label recorded in the account register. This glossary does not define how that label is assigned or an employee-count threshold. If the label is absent, Sales Operations is the contact for resolving the record.

A setup blocker is a problem that prevents completion of setup. A setup question is a request for guidance that does not necessarily prevent setup. These terms must not be treated as interchangeable in reporting.

Trial activation means a workspace has connected a sample data source. It does not establish a purchase, paid conversion or completion of the full evaluation.


<a id="source-06-team-responsibilities"></a>

### 06-team-responsibilities.md

#### Who handles trial work
Date: 2026-05-02
Document status: approved operating responsibilities; effective May 2, 2026

Sales Operations maintains account segment labels and resolves missing labels. This document does not give other teams a rule for deriving a segment from employee count.

Customer Success coordinates assisted onboarding and owns the trial setup request queue. Support records setup questions and blockers and links those observations to the relevant request. Product reviews recurring setup problems and decides whether to propose product changes.

These routing responsibilities do not grant any team authority to waive the May onboarding decision. No exception approver is named here. Escalating a question to the responsible queue is not approval to change policy.


<a id="source-07-trial-request-process"></a>

### 07-trial-request-process.md

#### Preparing a trial setup request
Date: 2026-05-03
Document status: approved process; effective May 3, 2026

For a new trial request:
1. Record the account name, the account register's segment label if present, the customer's setup goal and any reported blocker.
2. If the segment label is missing, request clarification from Sales Operations. Do not infer the label from employee count. Prepare an incomplete draft while waiting; do not select an onboarding route yet.
3. For an enterprise label, prepare an assisted-onboarding request for the Customer Success trial setup queue. For a smaller-customer label, the self-service option remains available under the May 1 decision; Support handles reported setup questions.
4. Include source references and unresolved questions in the handoff. Do not promise a trial duration unless a current approval establishing that duration is available.

The request template has six fields: account; recorded segment; setup goal; reported blocker; proposed route; unresolved questions.

This document defines preparation and routing. It does not authorize an agent to send a message, create an account, change settings or act on the customer's behalf. Actions require separate authorization from the person operating the agent.


<a id="source-08-april-support-observations"></a>

### 08-april-support-observations.md

#### Trial setup observations
Date: 2026-04-20
Document status: observation log; not a representative customer survey

Support recorded three illustrative cases from the trial pilot:
- Cedar: account register label enterprise. Its administrator could not determine which sample-data connector to select and requested a guided setup session.
- Finch: account register label smaller-customer. The customer connected a sample data source without contacting Support.
- Vale: account register label enterprise. The administrator asked which colleague should approve a sample-data connection; setup was paused while the customer resolved this internally.

These cases contain no employee counts, conversion outcomes, measured setup times or comparison with an assisted-onboarding group. They were selected to illustrate different setup experiences, not to estimate how often problems occur. This log does not establish whether the April 24 review used these particular cases.


<a id="source-09-may-product-review"></a>

### 09-may-product-review.md

#### Product review: setup guidance
Date: 2026-05-04
Document status: review and proposal; not an approved release commitment

Product reviewed the April 20 support observations alongside the April 24 pilot review and the May 1 onboarding decision.

Cedar's connector-selection question suggests that clearer connector guidance could help some customers. Vale's approval question concerns the customer's internal coordination and might not be resolved by interface changes alone. Finch's unaided setup is a reminder that the selected examples do not show that every customer needs guided onboarding.

We propose a connector-selection checklist for future consideration. No delivery date, implementation approval or expected conversion improvement is established by this review. Assisted onboarding is the approved operating approach for enterprise trials; the proposed checklist is a separate potential product improvement.


<a id="source-10-reporting-definitions"></a>

### 10-reporting-definitions.md

#### Trial reporting definitions
Date: 2026-05-05
Document status: maintained reporting reference

Activation rate for a named trial cohort is the number of workspaces in that cohort that connected a sample data source divided by the number of trial workspaces in that same cohort. Every report must state the cohort dates and observation cutoff. A missing connection observation must not automatically be recorded as a confirmed setup blocker.

There are no cohort counts or activation-rate values in this reference. The April 20 illustrative cases cannot establish the company's activation rate. Activation is not paid conversion. No supplied document reports a causal effect of assisted onboarding on activation or conversion.
