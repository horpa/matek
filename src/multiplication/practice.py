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
                self.stats.add(multiplication_table.Identifier(i, j))

    def print_stats(self):
        self.stats.print_stats()

    def new_exercise(self):
        potentials = [k for k in self.stats.needs_practice()]
        r = random.choice(potentials)
        fx = random.choice(multiplication_table.functions())
        return fx(r.x, r.y)


def practice_multiplication(range_min=1, range_max=10, base_numbers=None):
    p = Practice(range_min, range_max, base_numbers)

    p.stats.start()
    while p.stats.is_all_known() is False:
        ex = p.new_exercise()

        i = input(ex.question)
        if not i.isdigit():
            break

        if int(i) == ex.answer:
            print("✅")
            p.stats.update_stats(ex.identifier, True)
        else:
            print("❌")
            p.stats.update_stats(ex.identifier, False)
    if p.stats.is_all_known():
        print("✨ Ugyes voltal! ✨")

    p.stats.stop()
    p.print_stats()


if __name__ == '__main__':
    pass
