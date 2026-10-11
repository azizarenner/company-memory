# Roadmap: three company-memory problems

## 1. Remembering decisions — prototype implemented

Inputs: complete text documents. Outputs: draft decisions, history, evidence, unknowns, conflict entries, and full context.

Next evidence: live extraction, unseen decision examples, independent review, and a raw-files comparison. Do not claim success beyond the verified compiler behavior.

## 2. Onboarding an agent — design stage

Extend the content model with vocabulary, process descriptions, role boundaries, and task-specific context. Distinguish source knowledge from operational instructions. Test whether an agent can use a metric correctly without inventing its definition.

Completion criterion: an agent performs a bounded onboarding task using the bundle and cites definitions correctly; compare against the raw material.

## 3. Connecting scattered knowledge — design stage

Evidence-backed relationships are supported in the prototype, but automatic cross-document synthesis is not independently evaluated. Explore links between decisions, customer constraints, processes, and metrics. Preserve conflicting definitions and source-specific terminology.

Completion criterion: held-out multi-document questions answered with correct reasoning and citations, including cases where no defensible connection exists.

## Later, only with evidence of need

PDF conversion, incremental rebuilds, explicit approval workflows, permission-aware packaging, signed bundles, evaluation automation, and alternative model adapters. A larger corpus may require selective navigation or retrieval; that is a design decision, not a failure to honor a slogan.
