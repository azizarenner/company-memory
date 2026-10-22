# Experiment history

For the completed October 14 study and October 18 scoring update, start with [Northstar results](NORTHSTAR_RESULTS.md). The notes below cover earlier development experiments and explain how the evaluation evolved.

## Initial decision-memory experiments

The first four-document Northstar comparison reached the correct main conclusion on six of seven questions in each condition under provisional assistant scoring. Both conditions incorrectly carried a 14-day pilot duration forward after a later onboarding change. The generated context was larger than the source documents.

Follow-ups explored explicit uncertainty, attribute-level records, exact citation checks, and a separate model reviewer. They exposed extraction errors, invalid quotations, and incorrect conclusions despite valid citations.

## Reviewer experiment

A source-ID experiment used six known questions, two answer conditions, and three reviewer controls: 27 successful API requests. The reviewer approved all twelve generated answers, including contradictions and unsupported conclusions, while handling three simple control claims as expected.

The answer generator and reviewer used the same GPT-4.1 mini snapshot. The reviewer received the original sources but not the question. Prompts and representations changed between these early runs, and a reviewed-memory baseline had not yet been introduced. These findings informed the subsequent fixed comparison.

## Completed Northstar comparison

The October 14 study introduced an approved reference memory and answer key, four GPT context conditions, and a Claude follow-up on original documents and reviewed memory. The [results archive](NORTHSTAR_RESULTS.md) publishes inputs, unchanged answers, scores, and review records. [Evaluation methods](docs/evaluation-methods.md) describe the setup and review scope.

## Next phase

The [roadmap](docs/roadmap.md) extends this work to changing policies, shared context, access changes, unseen tasks, and total cost per successful task.
