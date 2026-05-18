"""Single stick: balanced reach, moderate cost, mid-range bias."""
from core.angles import Angle
from core.interfaces import Weapon


class SingleStick(Weapon):
    @property
    def name(self) -> str:
        return "single_stick"

    def damage(self, angle: Angle) -> float:
        # Diagonal strikes carry more force than thrusts with a stick
        diagonal = {Angle.A1, Angle.A2, Angle.A3, Angle.A4}
        return 14.0 if angle in diagonal else 9.0

    def cost(self, angle: Angle) -> float:
        return 8.0
