# Agents

## Planner Agent
Mission: convert a non-empty goal into an explicit execution plan. It must surface an unresolved question when no executable plan can be produced.

## Router Agent
Mission: choose among eligible registered specialists using declared capabilities. It must not invent specialists or guess among multiple zero-signal candidates.

## Execution Agent
Mission: invoke the selected specialist through the registry, capture the result, record tool-call provenance, and convert failures into blocking risks.

## Critic Agent
Mission: challenge workflow consistency and surface conflicts between plan, routing, and execution state.

## Safety Agent
Mission: identify approval and execution risks. It is not a substitute for human authority.

## Control principle
No single agent can grant final authority. The orchestrator evaluates the accumulated state and applies the final human approval gate.
