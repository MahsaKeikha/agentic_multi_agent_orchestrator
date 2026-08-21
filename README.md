# F36 Agentic Multi Agent Orchestrator

A standalone reference implementation for coordinating specialized AI agents through explicit routing, shared state, tool access, reusable skills, safety gates, and observable execution.

## Architecture

This repository exposes actual implementation files directly under `AGENTS/`, `TOOLS/`, and `SKILLS/`. The orchestrator coordinates independent specialists rather than hiding all behavior inside one prompt.

## Core goals

- explicit agent roles
- deterministic routing and handoffs
- shared state and evidence tracking
- tool invocation boundaries
- reusable skills
- human approval gates
- traceable execution
- reproducible tests

## Maturity

Reference implementation. Production use requires domain validation, security review, integration testing, and operational evidence.

## AI Engineering Handbook Series

Companion books by Mahsa Keikha:

- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

## License

MIT
