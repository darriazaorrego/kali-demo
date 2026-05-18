"""
Counter-fighter: prefers defensive intercepts, strikes on the half-beat
after a successful parry. Demonstrates the AIBrain contract.
"""
import random
from core.angles import Angle, COUNTERS
from core.interfaces import AIBrain, Action


class CounterFighter(AIBrain):
    def __init__(self, weapon):
        self.weapon = weapon
        self._last_parried = False

    def decide(self, self_state, opponent_last_action):
        # If we just parried, strike back on the gap
        if self._last_parried:
            self._last_parried = False
            angle = random.choice(list(Angle))
            return Action(angle=angle, is_strike=True,
                          cost=self.weapon.cost(angle))

        # Otherwise, attempt a counter to opponent's last attack
        if opponent_last_action and opponent_last_action.is_strike:
            options = COUNTERS.get(opponent_last_action.angle, (Angle.A5,))
            angle = options[0]
            self._last_parried = True
            return Action(angle=angle, is_strike=False, cost=3.0)

        # Default: probing strike
        angle = Angle.A1
        return Action(angle=angle, is_strike=True,
                      cost=self.weapon.cost(angle))
