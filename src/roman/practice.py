import random

from src.util import stats
from . import roman_mumbers


class Practice:
    def __init__(self, range_min=1, range_max=20, minimum_required_correct_answers=5):
        self.range_min = range_min
        self.range_max = range_max
        self.__init_stats(minimum_required_correct_answers)

    def __init_stats(self, minimum_required_correct_answers):
        self.stats = stats.Statistics(minimum_required_correct_answers)

        for i in range(self.range_min, self.range_max + 1):
            self.stats.add(i)

    def new_exercise(self):
        potentials = [k for k in self.stats.needs_practice()]
        r = random.choice(potentials)
        fx = random.choice(roman_mumbers.functions())
        return fx(r)


def practice_roman_numerals(
    range_min=1, range_max=20, minimum_required_correct_answers=5
):
    if range_min < 1:
        range_min = 1
    if range_max < 1:
        range_max = 1
    if range_max > 3999:
        range_max = 3999
    if range_min > range_max:
        range_max = range_min

    p = Practice(range_min, range_max, minimum_required_correct_answers)

    p.stats.start()
    while p.stats.is_all_known() is False:
        ex = p.new_exercise()

        i = input(ex.question)
        if i == "":
            break

        if not i.isdigit():
            i = i.upper()

        if i == ex.answer:
            p.stats.print_correct_answer()
            p.stats.update_stats(ex.identifier, True)
        else:
            p.stats.print_wrong_answer(ex.answer)
            p.stats.update_stats(ex.identifier, False)

    p.stats.stop()
    p.stats.print_stats()


if __name__ == "__main__":
    pass
