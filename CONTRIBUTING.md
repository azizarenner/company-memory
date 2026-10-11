# Contributing

Start with a reproducible issue, a fictional or public input set, expected behavior, and the actual output. Do not submit confidential company material or API keys.

Run `python3 -m unittest discover -s tests -v` before proposing a change. Add tests for meaningful new failure cases. Keep runtime dependencies minimal and distinguish compiler checks from model evaluation.

Changes to extraction structure must update the runtime schema, checked-in schema, fixtures, and documentation together. Avoid changing evidence text or source snapshots merely to make an incorrect extraction pass.

Contributions are offered under the repository's MIT license. Maintainers should review any benchmark claim against its complete protocol and recorded outputs.
