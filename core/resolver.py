"""
Action resolution. Pure function over combatant state + actions.
Determines whether an attack lands, is countered, or whiffs.
"""
from core.angles import is_counter
from core.interfaces import Action
from core.combatant import Combatant


def resolve(attacker: Combatant, defender: Combatant,
            attack: Action, defense: Action) -> dict:
    """
    Resolve one exchange. Returns an event dict describing the outcome.
    Tempo and stamina modulate effectiveness.
    """
    # Stamina spend; failed spend = whiff
    if not attacker.stamina.spend(attack.cost):
        return {"type": "whiff", "reason": "exhausted", "attacker": attacker.name}

    defender.stamina.spend(defense.cost)  # defense can attempt even at low stamina

    # Counter logic: correct defensive angle on tempo cancels the strike
    if not defense.is_strike and is_counter(defense.angle, attack.angle):
        return {
            "type": "counter",
            "attacker": attacker.name,
            "defender": defender.name,
            "attack_angle": attack.angle.name,
            "defense_angle": defense.angle.name,
        }

    # Stamina-scaled damage: tired fighters hit softer
    damage = attacker.weapon.damage(attack.angle) * attacker.stamina.ratio
    defender.health -= damage
    return {
        "type": "hit",
        "attacker": attacker.name,
        "defender": defender.name,
        "angle": attack.angle.name,
        "damage": round(damage, 1),
    }
