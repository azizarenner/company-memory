# Company Memory

**Turn a small collection of company documents into an evidence-linked knowledge bundle for an AI agent.**

Company Memory explores three uses of prepared company knowledge: remembering decisions, onboarding an agent, and connecting scattered knowledge. The Python prototype currently compiles decision-focused bundles; the broader use cases are illustrated in a draft worked example.

It reads complete Markdown and text files, accepts or generates a structured extraction, checks exact evidence quotes, and writes a draft [Open Knowledge Format (OKF v0.2)](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) bundle. It also assembles that bundle into one context file.

**Status:** early prototype. The [October 14 results archive](NORTHSTAR_RESULTS.md) includes a human-reviewed GPT-4.1 mini comparison and a Claude Code follow-up with provisional assistant scores. It contains fictional sources, exact task packets, unchanged answers, scores, and the recorded startup failure/recovery. Results are from one known development case; they do not establish general model or architecture superiority. Earlier experiments are documented in [experiment status](EXPERIMENT_STATUS.md).

## Explore the three use cases

Read the [complete Northstar worked example](COMPANY_MEMORY_EXAMPLE.md): ten fictional source documents, a decision history, an agent onboarding guide and an explanation connecting documents. Start with the onboarding guide’s worked request. All three outputs are assistant-prepared drafts with completed [source and usefulness checks](SOURCE_REVIEW.md). Independent human validation is pending; these are not automatically compiled or benchmarked results.

## See the original compiler example

Northstar is a fictional company. Its January proposal, February pilot approval, April review, and May decision explain why enterprise trials moved to assisted onboarding.

- [Original documents](examples/northstar/sources/)
- [Prepared extraction](examples/northstar/extraction.json) — an assistant-authored reference fixture, not output from a live API run
- [Generated decision record](examples/northstar/bundle/knowledge/decisions/trial-onboarding.md)
- [Complete context file](examples/northstar/bundle/context.md)
- [Evaluation questions](docs/evaluation.md)

The example deliberately leaves “enterprise” undefined. It also does not establish whether the pilot's 14-day duration remains in force. A useful memory preserves these gaps.

## Run the demo

Python 3.9+; no third-party runtime dependencies. From this repository directory:

```sh
python3 company_memory.py compile examples/northstar/sources \
  --extraction examples/northstar/extraction.json --out build/northstar
python3 company_memory.py check build/northstar
```

Open `build/northstar/context.md` to inspect the generated context. Outputs must be new directories so an earlier bundle cannot be silently replaced.

## Use your own files without an API key

```sh
python3 company_memory.py prepare path/to/source-folder --out build/extraction-prompt.txt
```

Give that prompt to an AI model you choose, or author the extraction yourself using [the JSON schema](extraction.schema.json). The prompt contains the complete source texts: use a model or service authorized to receive them. Save its JSON response as `build/extraction.json`, without Markdown fences, then compile:

```sh
python3 company_memory.py compile path/to/source-folder \
  --extraction build/extraction.json --out build/my-memory
```

The source hashes must still match. If the sources changed after preparing the prompt, repeat the extraction. Quote checks can require correcting the model's output before compilation succeeds.

## Optional automatic conversion

Configure `OPENAI_API_KEY` in your local environment, then supply an explicit API model that supports structured outputs:

```sh
python3 company_memory.py build path/to/source-folder \
  --model YOUR_MODEL_ID --out build/my-memory
```

This command sends all accepted source files to the OpenAI Responses API and incurs that provider's model charges. It requests `store: false`; that setting is not a general promise about provider retention policies. The key is read from the environment and is never saved in a bundle. There is no default model or automatic retry. Incomplete responses and refusals fail without producing a bundle. The published adapter has mocked transport tests. Subsequent local evaluation code has exercised live requests; those experimental code additions are not included in this documentation update.

The adapter follows [OpenAI's structured output documentation](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses). Structured output constrains the response shape, not its factual correctness.

## What you get

```text
my-memory/
  sources/                 Exact original source snapshots
  knowledge/
    index.md               Bundle entry point
    decisions/*.md         Draft concepts, history, evidence, unknowns, links
  extraction.json          Inspectable model- or human-authored extraction
  context.md               Complete knowledge bundle assembled for a prompt
  manifest.json            Source/artifact hashes and build provenance
  REVIEW.md                Items to check before use
```

Keep the entire output directory together: knowledge documents link to the sibling source snapshots. The `knowledge/` directory follows our small OKF v0.2 profile; source snapshots are supporting material outside that directory. We have not run an independent OKF conformance validator. `check` validates this tool's own output, not arbitrary OKF bundles.

## What “RAGless” means here

This prototype does not create embeddings, a vector database, fixed-size document chunks, or a runtime retrieval index. Extraction receives all accepted source files. The generated `context.md` can be loaded in full for a bounded task.

Concept pages are semantic units: the information is still organized into smaller records. OKF itself does not require retrieval-free consumption. A larger deployment may need navigation or retrieval.

Input is capped at 120,000 UTF-8 bytes. This is a predictable local size guard, not a token count or a guarantee the request fits every model. Oversized inputs fail rather than being silently truncated. Only non-hidden `.md` and `.txt` files are read; other formats are ignored. Symlink files are rejected and hidden/symlink directories are skipped. Use a dedicated source folder and inspect the manifest for coverage.

## Compare against raw files

```sh
python3 company_memory.py compare build/northstar \
  --question "Can an enterprise customer get a self-service trial?" \
  --out build/comparison
```

This creates two prompts for fresh model sessions and an unrun results record. It does not execute or score a model benchmark. Use the same model and settings, score against original sources, and include extraction/review costs. See [the evaluation plan](docs/evaluation.md).

## Limits that matter

- The model, or the person writing the extraction, decides authority, chronology, scope, and relevance. Those judgments can be wrong even when quotes match.
- Dates are validated as calendar dates; the compiler does not independently infer which date a passage means.
- Evidence does not mechanically validate titles, unknowns, completeness, or logical entailment. A human review is still needed.
- An extraction that marks a concept conflicted cannot also declare a current decision for that concept. This conservative rule may require splitting unrelated scopes into separate concepts.
- Rebuild from the full source set after changes. There is no background synchronization, incremental update engine, or automatic deletion propagation.
- Output retains source text. Do not publish real internal documents, private data, or credentials with a bundle. There is no permissions system or redaction engine.
- Integrity hashes detect accidental changes when checked against an unchanged manifest. They are not signatures or protection against a malicious editor who rewrites the manifest.
- No file content is executed as code. Prompt instructions ask models to treat documents as untrusted data, but this is not a complete prompt-injection defense.

## Development

```sh
python3 -m unittest discover -s tests -v
```

See [architecture](docs/architecture.md), [roadmap](docs/roadmap.md), and [contributing](CONTRIBUTING.md). This independent experiment is not affiliated with Google or the OKF maintainers.

## License

MIT. See [LICENSE](LICENSE). The included Northstar documents are fictional and covered by the same license.

