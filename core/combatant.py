"""
A combatant is state, not behavior. Behavior lives in AI branches.
"""
from dataclasses import dataclass, field
from core.stamina import Stamina
from core.state_machine import StateMachine
from core.interfaces import Weapon


@dataclass
class Combatant:
    name: str
    weapon: Weapon
    health: float = 100.0
    stamina: Stamina = field(default_factory=Stamina)
    fsm: StateMachine = field(default_factory=StateMachine)

    @property
    def alive(self) -> bool:
        return self.health > 0
