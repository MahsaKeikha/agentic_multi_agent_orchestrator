# Extending F36

Add a specialist by registering a unique name, explicit capabilities, and a handler in a `SpecialistRegistry`. Prefer deterministic handlers for tests and adapters around external services for production integrations.

A new specialist should include:

- a clear mission and input/output contract;
- capabilities used by the router;
- failure behavior;
- tests for successful routing and invocation;
- tests for malformed input and handler failure;
- safety notes if outputs could influence consequential actions.

Do not bypass the registry by importing and calling specialists directly from the orchestrator. Do not let a specialist set final approval state.
