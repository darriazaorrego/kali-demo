"""
Stamina economy. Strikes cost. Recovery accrues per tick.
Low stamina degrades resolution outcomes (handled in resolver).
"""
from dataclasses import dataclass


@dataclass
class Stamina:
    current: float = 100.0
    maximum: float = 100.0
    recovery_per_tick: float = 2.0

    def spend(self, amount: float) -> bool:
        if self.current < amount:
            return False
        self.current -= amount
        return True

    def recover(self) -> None:
        self.current = min(self.maximum, self.current + self.recovery_per_tick)

    @property
    def ratio(self) -> float:
        return self.current / self.maximum
