from __future__ import annotations

from typing import Iterable


def can_approve(unresolved_questions: Iterable[str], conflicts: Iterable[str], risks: Iterable[str]) -> bool:
    return not any([list(unresolved_questions), list(conflicts), list(risks)])
