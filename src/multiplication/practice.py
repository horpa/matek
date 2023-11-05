import random

from . import multiplication_table
from . import stats


class Practice:
    def __init__(self, range_min=1, range_max=10, base_numbers=None):
        self.range_min = range_min
        self.range_max = range_max
        if base_numbers is not None:
            self.base_numbers = base_numbers
        else:
            self.base_numbers = [2]
        self.__init_stats()

    def __init_stats(self):
        self.stats = stats.Statistics()

        for i in self.base_numbers:
            for j in range(self.range_min, self.range_max + 1):
                self.stats.add((i, j))

    def print_stats(self):
        self.stats.print_stats()

    def new_exercise(self):
        potentials = [k for k in self.stats.needs_practice()]
        x, y = random.choice(potentials)
        fx = random.choice(multiplication_table.functions())
        return fx(x, y)
