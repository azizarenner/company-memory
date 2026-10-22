# Company Memory roadmap

The project explores three uses of persistent company context: remembering decisions, onboarding agents, and connecting scattered knowledge.

## Completed foundations

- A Python compiler for evidence-linked decision bundles, with source snapshots, quote checks, hashes, and a complete context file.
- A [worked Northstar example](../COMPANY_MEMORY_EXAMPLE.md) covering decision history, onboarding, and cross-document explanation.
- A [published study](../NORTHSTAR_RESULTS.md) comparing original documents and prepared memory, with source material, unchanged answers, and scores.

## Next experiments

### Update policies without losing history

Change an approval and test both current and historical questions. Track effective dates, supersession, and which derived records need rebuilding.

### Share context between agents

Compare handoffs containing task state, evidence references, and unresolved fields. Keep working observations distinguishable from approved company knowledge.

### Propagate access changes

Test how revoked access or deleted sources affect derived memory and task context. Permission handling is a planned capability; the current compiler is designed for a local source folder.

### Compare representations and retrieval

Evaluate files, structured records, and graph relationships against the same tasks. Compare complete-context loading with retrieval where collection size warrants it.

### Measure reliability and total cost

Use unseen cases and a consistent review process. Measure extraction quality separately from answer quality, and include preparation, updates, retrieval, generation, verification, and retries in cost per successful task.

## Implementation focus

Decision extraction is implemented. Automatic onboarding-guide generation and cross-document synthesis are future extensions illustrated by the current authored examples. Incremental updates and permissions will require additions to the compiler architecture.
