"""Knife: lower cost, thrust-biased, lethal at close range."""
from core.angles import Angle
from core.interfaces import Weapon


class Knife(Weapon):
    @property
    def name(self) -> str:
        return "knife"

    def damage(self, angle: Angle) -> float:
        thrusts = {Angle.A5, Angle.A6, Angle.A7, Angle.A12}
        return 18.0 if angle in thrusts else 11.0

    def cost(self, angle: Angle) -> float:
        return 5.0
