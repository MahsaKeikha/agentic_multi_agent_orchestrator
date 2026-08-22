# Contributing

Contributions should improve substantive multi-agent behavior, evaluation, reproducibility, documentation, or safety rather than only adding folders or role names.

Before opening a pull request:

1. install with `python -m pip install -e '.[dev]'`;
2. run `pytest -q`;
3. run `python run.py`;
4. add or update tests for behavioral changes;
5. document new agents, specialists, tools, state fields, or safety boundaries;
6. avoid committing secrets, credentials, generated caches, or private data.

Pull requests should explain the problem, design choice, failure modes, tests, and any safety implications.
