import inspect

from src.util import exercise


class RomanNumerals:
    roman_symbols = [
        (1, "I"),
        (4, "IV"),
        (5, "V"),
        (9, "IX"),
        (10, "X"),
        (40, "XL"),
        (50, "L"),
        (90, "XC"),
        (100, "C"),
        (400, "CD"),
        (500, "D"),
        (900, "CM"),
        (1000, "M"),
    ]

    @classmethod
    def dec2rom(cls, n):
        ret = ""

        for a, r in cls.roman_symbols[::-1]:
            div = n // a
            n %= a
            for _ in range(div):
                ret += r
        return ret


class RomanNumeralsExercises:
    @staticmethod
    def decimal_to_roman(d):
        question = f"{d} = ? "
        answer = RomanNumerals.dec2rom(d)
        return exercise.MathExercise(d, question, answer)

    @staticmethod
    def roman_to_decimal(d):
        r = RomanNumerals.dec2rom(d)
        question = f"{r} = ? "
        answer = str(d)
        return exercise.MathExercise(d, question, answer)


def functions():
    return [
        f[1]
        for f in inspect.getmembers(
            RomanNumeralsExercises, predicate=inspect.isfunction
        )
    ]


if __name__ == "__main__":
    pass
