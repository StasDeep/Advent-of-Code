from abc import ABC, abstractmethod

from utils import read, p1, p2


def main():
    pl1, pl2 = "\n".join(read()).split("\n\n")
    pl1 = [int(x) for x in pl1.split("\n")[1:]]
    pl2 = [int(x) for x in pl2.split("\n")[1:]]

    p1(ClassicalCombat(pl1, pl2).play().winner_score)
    p2(RecursiveCombat(pl1, pl2).play().winner_score)


class BaseCombatGame(ABC):

    def __init__(self, deck1, deck2):
        self.deck1 = deck1.copy()
        self.deck2 = deck2.copy()

    def draw_cards(self):
        return self.deck1.pop(0), self.deck2.pop(0)

    def cards_to_round_winner(self, c1, c2, round_winner):
        if int(round_winner) == 0:
            self.deck1.extend([c1, c2])
        else:
            self.deck2.extend([c2, c1])

    @property
    def winner(self):
        return 0 if self.deck1 else 1

    @property
    def winner_score(self):
        winner_deck = [self.deck1, self.deck2][self.winner]
        return sum((len(winner_deck) - i) * x for i, x in enumerate(winner_deck))

    @abstractmethod
    def play(self):
        pass


class ClassicalCombat(BaseCombatGame):

    def play(self):
        while self.deck1 and self.deck2:
            c1, c2 = self.draw_cards()
            self.cards_to_round_winner(c1, c2, c1 < c2)
        return self


class RecursiveCombat(BaseCombatGame):

    def play(self):
        seen = set()
        while self.deck1 and self.deck2:
            if (tuple(self.deck1), tuple(self.deck2)) in seen:
                break

            seen.add((tuple(self.deck1), tuple(self.deck2)))

            c1, c2 = self.draw_cards()

            if c1 <= len(self.deck1) and c2 <= len(self.deck2):
                winner = RecursiveCombat(self.deck1[:c1], self.deck2[:c2]).play().winner
            else:
                winner = int(c1 < c2)

            self.cards_to_round_winner(c1, c2, winner)

        return self
