from itertools import combinations, product, chain

from utils import read, p1, p2


weapons_raw = """\
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

armors_raw = """\
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

rings_raw = """\
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


def main():
    boss_hp, boss_dmg, boss_arm = [int(x.split()[-1]) for x in read()]

    items = {}
    item_types = ["weapon", "armor", "ring"]
    for raw, item_type in zip([weapons_raw, armors_raw, rings_raw], item_types):
        for item_raw in raw.split("\n"):
            item, cost, dmg, arm = item_raw.rsplit(maxsplit=3)
            items[item] = [int(cost), int(dmg), int(arm), item_type]

    # 1 weapon, 0 or 1 armor, 0-2 rings
    num_allowed = [[1], [0, 1], [0, 1, 2]]

    choices = {}
    for item_type, allowed in zip(item_types, num_allowed):
        item_of_type = [item_name for item_name, v in items.items() if v[-1] == item_type]
        choices[item_type] = [comb for i in allowed for comb in combinations(item_of_type, i)]

    win_loadouts = []
    lose_loadouts = []
    for loadout in product(*choices.values()):
        items_chosen = list(chain.from_iterable(loadout))

        my_hp, my_dmg, my_arm = 100, sum(items[x][1] for x in items_chosen), sum(items[x][2] for x in items_chosen)

        if battle_won(my_hp, my_dmg, my_arm, boss_hp, boss_dmg, boss_arm):
            win_loadouts.append(items_chosen)
        else:
            lose_loadouts.append(items_chosen)

    p1(min(sum(items[x][0] for x in loadout) for loadout in win_loadouts))
    p2(max(sum(items[x][0] for x in loadout) for loadout in lose_loadouts))


def battle_won(my_hp, my_dmg, my_arm, boss_hp, boss_dmg, boss_arm):
    pl1 = [my_hp, my_dmg, my_arm]
    pl2 = [boss_hp, boss_dmg, boss_arm]

    is_pl1 = True
    while pl1[0] > 0 and pl2[0] > 0:
        attacker = pl1 if is_pl1 else pl2
        defender = pl2 if is_pl1 else pl1

        damage = max(attacker[1] - defender[2], 1)
        defender[0] -= damage

        is_pl1 = not is_pl1

    return pl1[0] > 0
