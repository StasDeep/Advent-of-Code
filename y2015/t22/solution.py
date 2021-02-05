from copy import deepcopy

from utils import p1, p2


def main():
    init_state = {
        "player_hp": 50,
        "player_mana": 500,
        "boss_hp": 71,
        "boss_dmg": 10,
        "spells": {
            "Magic Missile": {"cost": 53, "effect": {"damage": 4}, "timer": 0},
            "Drain": {"cost": 73, "effect": {"damage": 2, "heal": 2}, "timer": 0},
            "Shield": {"cost": 113, "effect": {"armor": 7}, "timer": 6},
            "Poison": {"cost": 173, "effect": {"damage": 3}, "timer": 6},
            "Recharge": {"cost": 229, "effect": {"mana": 101}, "timer": 5},
        },
        "active_spells": {},
    }

    moves, cost = Fight.perfect_moves(init_state, start=True)
    # ['Poison', 'Recharge', 'Shield', 'Poison', 'Recharge', 'Shield', 'Poison', 'Recharge', 'Shield', 'Magic Missile', 'Poison', 'Magic Missile']
    p1(cost)

    moves, cost = HardFight.perfect_moves(init_state, start=True)
    p2(cost)


class Fight:

    fields = ["player_hp", "player_mana", "boss_hp", "boss_dmg", "spells", "active_spells"]

    def __init__(self, state: dict, spell_to_use):
        self.state = state
        self.spell = spell_to_use

    def get_best_moves(self):
        result = self.simulate()

        if isinstance(result, list):
            return result

        if result is None:
            return None

        perfect_next_moves = self.perfect_moves(self.state)[0]

        if perfect_next_moves is None:
            return None

        return [self.spell] + perfect_next_moves

    def simulate(self):
        # Player's turn
        self.apply_effects()

        if self.is_player_dead():
            return None

        if self.is_boss_dead():
            # If boss dies before the spell is applied, best move is doing nothing
            return []

        success = self.player_moves()

        if not success:
            # If player could not move, he loses
            return None

        if self.is_boss_dead():
            return [self.spell]

        # Boss' turn
        self.apply_effects()

        if self.is_boss_dead():
            return [self.spell]

        self.boss_moves()

        if self.is_player_dead():
            return None

        return "continue playing"

    def apply_effects(self):
        for spell in list(self.state["active_spells"]):
            spell_effect = self.state["spells"][spell]["effect"]

            self.apply_effect(spell_effect)

            # Decrease spell effect timer
            self.state["active_spells"][spell] -= 1

            # Delete depleted spell
            if self.state["active_spells"][spell] == 0:
                del self.state["active_spells"][spell]

    def apply_effect(self, spell_effect):
        self.state["boss_hp"] -= spell_effect.get("damage", 0)
        self.state["player_hp"] += spell_effect.get("heal", 0)
        self.state["player_mana"] += spell_effect.get("mana", 0)

    def player_moves(self) -> bool:
        spell_info = self.state["spells"][self.spell]
        spell_cost = spell_info["cost"]

        # Can't cast a spell when not enough mana
        if self.state["player_mana"] < spell_cost:
            return False

        # Can't cast a spell that is currently active
        if self.spell in self.state["active_spells"]:
            return False

        self.state["player_mana"] -= spell_cost

        if spell_info["timer"] == 0:
            # If the effect is instant, apply it right away
            self.apply_effect(spell_info["effect"])
        else:
            # Activate spell by setting a timer for it
            self.state["active_spells"][self.spell] = spell_info["timer"]

        return True

    def boss_moves(self):
        dmg = self.state["boss_dmg"]

        # Reduce damage by armor spells
        for spell in self.state["active_spells"]:
            dmg -= self.state["spells"][spell]["effect"].get("armor", 0)

        # Boss always deals at least 1 damage
        dmg = max(dmg, 1)

        self.state["player_hp"] -= dmg

    def is_boss_dead(self):
        return self.state["boss_hp"] <= 0

    def is_player_dead(self):
        return self.state["player_hp"] <= 0

    @classmethod
    def perfect_moves(cls, state, start=False):
        best_sequence = None
        best_sequence_cost = None
        for spell in state["spells"]:
            moves = cls(deepcopy(state), spell_to_use=spell).get_best_moves()

            if moves is None:
                continue

            total_cost = sum(state["spells"][move]["cost"] for move in moves)
            if best_sequence is None or total_cost < best_sequence_cost:
                best_sequence = moves
                best_sequence_cost = total_cost
                if start:
                    print(best_sequence)
                    print(best_sequence_cost)

        return best_sequence, best_sequence_cost


class HardFight(Fight):

    def apply_effects(self):
        self.state["player_hp"] -= 1
        super().apply_effects()


class Simulation(Fight):

    def __init__(self, state, moves):
        self.state = state
        self.moves = moves

    def simulate_all(self):
        for move in self.moves:
            self.spell = move
            self.simulate()

    def player_moves(self) -> bool:
        print(f"Player plays {self.spell}")
        res = super().player_moves()
        print({**self.state, "spells": ""})
        print()
        return res

    def boss_moves(self):
        print("Boss moves")
        super().boss_moves()
        print({**self.state, "spells": ""})
        print()
