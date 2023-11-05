class StatItem:
    def __init__(self):
        self.correct_answers = 0
        self.wrong_answers = 0
        self.is_well_known = False


class Statistics:

    def __init__(self, minimum_required_correct_answers=5):
        self.storage = {}
        self.minimum_required_correct_answers = minimum_required_correct_answers
        self.all_answers = 0

    def add(self, identifier):
        self.storage[identifier] = StatItem()

    def update_stats(self, identifier, is_correct=False):
        if identifier not in self.storage:
            self.storage[identifier] = StatItem()

        if is_correct:
            self.storage[identifier].correct_answers += 1
            if self.storage[identifier].correct_answers > self.minimum_required_correct_answers and \
                    self.storage[identifier].correct_answers > self.storage[identifier].wrong_answers + 5:
                self.storage[identifier].is_well_known = True
        else:
            self.storage[identifier].wrong_answers += 1
        self.all_answers += 1

    def is_all_known(self):
        for v in self.storage.values():
            if v.is_well_known is False:
                return False
        return True

    def well_known(self):
        return {key: value for (key, value) in self.storage.items() if value.is_well_known is True}

    def needs_practice(self):
        return {key: value for (key, value) in self.storage.items() if value.is_well_known is False}

    def print_stats(self):
        well_known = self.well_known()
        needs_practice = self.needs_practice()
        print(f"Osszes valasz: {self.all_answers}")
        print("Ami jol megy:")
        for k, v in well_known.items():
            print(f"{k} : jo:{v.correct_answers}, hibas:{v.wrong_answers}")
        print("Amit meg gyakorolni kell:")
        for k, v in needs_practice.items():
            print(f"{k} : jo:{v.correct_answers}, hibas:{v.wrong_answers}")


if __name__ == '__main__':
    # s = Statistics()
    # for i in range(20):
    #     s.update_stats(random.randint(100, 200), random.choice([True, False]))
    #
    # for i in range(20):
    #     for k in s.storage:
    #         s.update_stats(k, random.choice([True, False]))
    #
    # s.print_stats()
    pass