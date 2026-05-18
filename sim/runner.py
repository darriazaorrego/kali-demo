"""
Minimal harness. Wires core + branches and runs a turn-based exchange.
Prints structured events so the log can later feed analytics or replay.
"""
from core.combatant import Combatant
from core.events import EventBus
from core.resolver import resolve
from branches.weapons.single_stick import SingleStick
from branches.weapons.knife import Knife
from branches.ai.aggressor import Aggressor
from branches.ai.counter_fighter import CounterFighter


def run_match(max_ticks: int = 20, seed: int = 42) -> None:
    import random
    random.seed(seed)

    bus = EventBus()
    bus.subscribe("exchange", lambda e: print(f"  → {e}"))

    a_weapon = SingleStick()
    b_weapon = Knife()

    fighter_a = Combatant(name="Alon",   weapon=a_weapon)
    fighter_b = Combatant(name="Brando", weapon=b_weapon)

    brain_a = Aggressor(a_weapon)
    brain_b = CounterFighter(b_weapon)

    last_a = last_b = None

    for tick in range(1, max_ticks + 1):
        print(f"\n[Tick {tick}]  Alon HP={fighter_a.health:.1f}  "
              f"Brando HP={fighter_b.health:.1f}")

        action_a = brain_a.decide(fighter_a, last_b)
        action_b = brain_b.decide(fighter_b, last_a)

        # Alon attacks first; Brando defends
        result = resolve(fighter_a, fighter_b, action_a, action_b)
        bus.publish("exchange", result)

        if not fighter_b.alive:
            print(f"\n>>> {fighter_a.name} wins on tick {tick}")
            return

        # Recovery phase
        fighter_a.stamina.recover()
        fighter_b.stamina.recover()

        last_a, last_b = action_a, action_b

    print("\n>>> Match ends without KO.")
    print(f"    Final: Alon {fighter_a.health:.1f} / Brando {fighter_b.health:.1f}")


if __name__ == "__main__":
    run_match()
