"""
Abstract contracts that branches must satisfy.
Core depends on these; never on concrete branch classes.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from core.angles import Angle


@dataclass
class Action:
    angle: Angle
    is_strike: bool   # False = parry/intercept
    cost: float       # stamina cost


class Weapon(ABC):
    """A weapon defines reach, cost profile, and damage by angle."""

    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def damage(self, angle: Angle) -> float: ...

    @abstractmethod
    def cost(self, angle: Angle) -> float: ...


class AIBrain(ABC):
    """An AI brain decides the next action given perceived state."""

    @abstractmethod
    def decide(self, self_state, opponent_last_action: Action | None) -> Action: ...
