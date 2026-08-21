# Safety

F36 treats agent output as decision support, not authority.

## Mandatory boundaries

- Human approval remains enabled for consequential completion.
- Missing or ambiguous routing blocks execution.
- Specialist exceptions are contained and block approval.
- Unresolved questions, conflicts, or risks block approval.
- Agents cannot invoke unregistered specialists.
- Tool and specialist calls are recorded for review.

## Threat model

F36 is designed to demonstrate resistance to silent fallback, arbitrary routing, untracked execution, and approval bypass. It does not claim to solve model-level prompt injection, sandbox escape, network security, or identity/access management for production deployments. Those require deployment-specific controls.

## Reporting

Security-sensitive issues should follow `SECURITY.md` rather than public exploit disclosure.
