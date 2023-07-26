from collections.abc import Sequence


class FrenchDeck:
    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]


Sequence.register(FrenchDeck)

print(isinstance(FrenchDeck([1, 2, 3, 4, 5]), Sequence))
