"""
Combat phases driven by range and engagement, not by input.
Transitions are requested by the resolver based on action outcomes.
"""
from enum import Enum


class CombatState(Enum):
    DISENGAGED = "disengaged"
    LARGO      = "largo"     # long range
    MEDIO      = "medio"     # mid range
    CORTO      = "corto"     # close range
    TRAPPING   = "trapping"  # limb control
    RECOVERY   = "recovery"


# Legal transitions. Anything not listed is rejected.
TRANSITIONS = {
    CombatState.DISENGAGED: {CombatState.LARGO},
    CombatState.LARGO:      {CombatState.MEDIO, CombatState.DISENGAGED, CombatState.RECOVERY},
    CombatState.MEDIO:      {CombatState.LARGO, CombatState.CORTO, CombatState.RECOVERY},
    CombatState.CORTO:      {CombatState.MEDIO, CombatState.TRAPPING, CombatState.RECOVERY},
    CombatState.TRAPPING:   {CombatState.CORTO, CombatState.RECOVERY},
    CombatState.RECOVERY:   {CombatState.DISENGAGED, CombatState.LARGO},
}


class StateMachine:
    def __init__(self, initial: CombatState = CombatState.DISENGAGED):
        self.state = initial

    def can_transition(self, target: CombatState) -> bool:
        return target in TRANSITIONS[self.state]

    def transition(self, target: CombatState) -> bool:
        if self.can_transition(target):
            self.state = target
            return True
        return False
