from collections.abc import Sequence, Generator, Iterable


def sum_of_numbers(numbers: Iterable[int]):
    sum = 0
    for n in numbers:
        sum += n
    return sum


class CustomSequence(Sequence):
    def __init__(self, numbers):
        self.numbers = numbers

    def __len__(self):
        return len(self.numbers)

    def __getitem__(self, index):
        return self.numbers[index]


sum_of_numbers([1, 2, 3, 4, 5])
sum_of_numbers((1, 2, 3, 4, 5))
sum_of_numbers(set((1, 2, 3, 4, 5)))
sum_of_numbers(n for n in range(1, 6))
custom_sequence = CustomSequence([1, 2, 3, 4, 5])
sum_of_numbers(custom_sequence)
