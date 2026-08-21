# F36 Agentic Multi Agent Orchestrator

A standalone reference implementation for coordinating specialized AI agents through explicit routing, shared state, tool access, reusable skills, safety gates, and observable execution.

## Direct agent links

- [Planner Agent](AGENTS/planner_agent.py)
- [Router Agent](AGENTS/router_agent.py)
- [Execution Agent](AGENTS/execution_agent.py)
- [Critic Agent](AGENTS/critic_agent.py)
- [Safety Agent](AGENTS/safety_agent.py)

## Core implementation

- [All agents](AGENTS/)
- [All tools](TOOLS/)
- [All skills](SKILLS/)
- [Orchestration](orchestration/)
- [Safety](safety/)
- [Observability](observability/)
- [Schemas](schemas/)
- [Tests](tests/)

## Execution

```bash
python run.py
pytest -q
```

## Maturity

Reference implementation. Production use requires domain validation, security review, integration testing, and operational evidence.

## AI Engineering Handbook Series

Companion books by Mahsa Keikha:

- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

## License

MIT
