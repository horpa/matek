from . import practice


def practice_multiplication(range_min=1, range_max=10, base_numbers=None):
    p = practice.Practice(range_min, range_max, base_numbers)

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
        print("✨ Ugyes voltal! ✨l j")

    p.print_stats()


if __name__ == '__main__':
    # practice_multiplication(1, 10, [2])
    pass
