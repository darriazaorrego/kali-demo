"""
The 12-angle system: Kali's universal vocabulary.
Every strike, parry, and intercept reduces to one of these vectors.
"""
from enum import IntEnum


class Angle(IntEnum):
    A1 = 1   # forehand high (left temple)
    A2 = 2   # backhand high (right temple)
    A3 = 3   # forehand mid (left ribs)
    A4 = 4   # backhand mid (right ribs)
    A5 = 5   # thrust centerline
    A6 = 6   # forehand low thrust
    A7 = 7   # backhand low thrust
    A8 = 8   # forehand knee
    A9 = 9   # backhand knee
    A10 = 10 # forehand vertical (crown)
    A11 = 11 # backhand vertical
    A12 = 12 # rising thrust


# Counter relationships: which angle naturally defangs which.
# Used by AI and resolver for tempo-based interception.
COUNTERS = {
    Angle.A1: (Angle.A2, Angle.A5),
    Angle.A2: (Angle.A1, Angle.A5),
    Angle.A3: (Angle.A4, Angle.A6),
    Angle.A4: (Angle.A3, Angle.A7),
    Angle.A5: (Angle.A1, Angle.A2),
    Angle.A6: (Angle.A3, Angle.A8),
    Angle.A7: (Angle.A4, Angle.A9),
    Angle.A8: (Angle.A6,),
    Angle.A9: (Angle.A7,),
    Angle.A10: (Angle.A5,),
    Angle.A11: (Angle.A5,),
    Angle.A12: (Angle.A10, Angle.A11),
}


def is_counter(defense: Angle, attack: Angle) -> bool:
    """True if `defense` is a recognized counter to `attack`."""
    return defense in COUNTERS.get(attack, ())
