# Experiment status — October 12, 2026

The public compiler is an early prototype. Subsequent local development has run live extractions and raw-document versus prepared-memory answer comparisons. The experimental runners and full response archives remain local and are not included in this documentation update.

## What happened

The first four-document Northstar comparison reached the correct main conclusion on six of seven questions in each condition in a provisional assistant review. Both incorrectly inferred that the earlier 14-day pilot duration continued after a later onboarding change. The generated context was larger than the originals.

Follow-ups explored uncertainty prompts, attribute-level decision records, exact citation checks and a separate model reviewer. These exposed missing uncertainty, misleading extracted records, invalid quotations and incorrect conclusions despite valid citations.

The latest local source-ID experiment used six known questions, two answer conditions and three reviewer controls: 27 successful API requests. The reviewer approved all 12 generated answers, including contradictions and unsupported conclusions. Three simple control claims were handled as expected. This does not establish reliable automatic verification.

## Why this is not a benchmark claim

The cases are small, fictional and known to the developing assistant. Human validation is pending. The latest answer generator and reviewer used the same model snapshot, gpt-4.1-mini-2025-04-14. The reviewer received full originals but not the original question. There was no human-checked bundle baseline. Questions about missing permission versus prohibition need clearer wording. Representation and prompting evolved together across runs.

The latest workflow remained retrieval-free, but its reviewer loaded full originals, so it was not memory-only end to end. None of this establishes that a knowledge format improves accuracy, saves tokens or replaces retrieval.

## Current direction

The [expanded Northstar example](COMPANY_MEMORY_EXAMPLE.md) restores all three use cases: decisions, agent onboarding and cross-document explanation. Its three draft outputs await human review. It is development material, not an unseen evaluation set.

Review these artifacts for usefulness and source fidelity before extending the compiler. Future comparisons should distinguish raw documents, a human-checked bundle and an automatically prepared bundle, and include the question in any relevance review. Earlier failures remain informative development cases rather than evidence against every company-memory architecture.
