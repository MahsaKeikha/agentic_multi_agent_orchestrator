# Evaluation

F36 evaluation focuses on control-plane behavior rather than model quality.

## Required behavioral cases

- capability-based routing selects the strongest eligible specialist;
- explicit preference works only for an eligible registered specialist;
- ambiguous zero-signal routing blocks instead of guessing;
- selected specialists are actually invoked;
- specialist failures are contained and recorded as blockers;
- evidence and tool-call provenance are emitted after successful execution;
- final approval requires both a clean state and explicit human approval;
- disabling the human-approval requirement is itself a blocker;
- traces contain the relevant agents, tool invocation, and approval-gate event.

## Reproducibility

The default registry uses deterministic offline specialist handlers so core tests do not require network access, API keys, or a hosted LLM.

## L3 requirement

L3 Gold Standard should require passing CI, published benchmark results, and independent reproduction beyond the repository author's own test run.
