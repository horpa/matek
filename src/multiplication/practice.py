import random

from . import multiplication_table
from src.util import stats


class Practice:
    def __init__(
        self,
        range_min=1,
        range_max=10,
        minimum_required_correct_answers=5,
        base_numbers=None,
    ):
        self.range_min = range_min
        self.range_max = range_max
        if base_numbers is not None:
            self.base_numbers = base_numbers
        else:
            self.base_numbers = [2]
        self.__init_stats(minimum_required_correct_answers)

    def __init_stats(self, minimum_required_correct_answers):
        self.stats = stats.Statistics(minimum_required_correct_answers)

        for i in self.base_numbers:
            for j in range(self.range_min, self.range_max + 1):
                self.stats.add(multiplication_table.Identifier(i, j))

    def new_exercise(self):
        potentials = [k for k in self.stats.needs_practice()]
        r = random.choice(potentials)
        fx = random.choice(multiplication_table.functions())
        return fx(r.x, r.y)


def practice_multiplication(
    range_min=1, range_max=10, minimum_required_correct_answers=5, base_numbers=None
):
    if range_min < 1:
        range_min = 1
    if range_max < 1:
        range_max = 1
    if range_min > range_max:
        range_max = range_min

    p = Practice(range_min, range_max, minimum_required_correct_answers, base_numbers)

    p.stats.start()
    while p.stats.is_all_known() is False:
        ex = p.new_exercise()

        i = input(ex.question)
        if not i.isdigit():
            break

        if int(i) == ex.answer:
            p.stats.print_correct_answer()
            p.stats.update_stats(ex.identifier, True)
        else:
            p.stats.print_wrong_answer(ex.answer)
            p.stats.update_stats(ex.identifier, False)

    p.stats.stop()
    p.stats.print_stats()


if __name__ == "__main__":
    pass
