# Architecture

F36 is a control-plane reference architecture for deterministic multi-agent coordination.

## Flow

`case -> planner -> capability router -> specialist registry -> execution -> critic -> safety -> human approval gate`

The orchestrator owns state transitions. Agents do not silently mutate external systems. Specialist handlers are registered with declared capabilities and invoked through a bounded registry.

## State

`RunState` preserves analyses, evidence, unresolved questions, conflicts, risks, tool calls, approvals, and an ordered trace. These fields are deliberately separate so downstream evaluators can distinguish a useful result from an unresolved or unsafe result.

## Routing

Routing is based on explicit eligibility plus capability overlap with the goal. Explicit user preference wins only when the requested specialist is eligible. When multiple specialists have zero capability signal, routing blocks rather than choosing arbitrarily.

## Execution

The execution layer invokes only specialists present in the registry. Exceptions are contained and converted into blocking state rather than escaping as silent partial completion.

## Approval

Agent completion is not authorization. The final approval gate requires no unresolved questions, conflicts, or risks, and a human approval request.
