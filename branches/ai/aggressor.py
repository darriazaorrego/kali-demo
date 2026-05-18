"""Aggressor: high-tempo offense, biases diagonal high strikes."""
import random
from core.angles import Angle
from core.interfaces import AIBrain, Action


class Aggressor(AIBrain):
    def __init__(self, weapon):
        self.weapon = weapon
        self._preferred = [Angle.A1, Angle.A2, Angle.A3, Angle.A4, Angle.A5]

    def decide(self, self_state, opponent_last_action):
        angle = random.choice(self._preferred)
        return Action(angle=angle, is_strike=True,
                      cost=self.weapon.cost(angle))
