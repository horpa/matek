import inspect

from . import exercise


class Identifier:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}*{self.y}"

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Identifier):
            return self.x == other.x and self.y == self.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))


class Exercises:
    @staticmethod
    def simple_multiplication(x, y):
        identifier = Identifier(x, y)
        question = f"{x} * {y} = ? "
        answer = x * y
        return exercise.MathExercise(identifier, question, answer)

    @staticmethod
    def simple_division(x, y):
        identifier = Identifier(x, y)
        question = f"{x * y} : {x} = ? "
        answer = y
        return exercise.MathExercise(identifier, question, answer)

    @staticmethod
    def what_makes_div(x, y):
        identifier = Identifier(x, y)
        question = f"? : {x} = {y} "
        answer = x * y
        return exercise.MathExercise(identifier, question, answer)

    @staticmethod
    def what_makes_multi(x, y):
        identifier = Identifier(x, y)
        question = f"{x} * ? = {x * y} "
        answer = y
        return exercise.MathExercise(identifier, question, answer)


def functions():
    return [f[1] for f in inspect.getmembers(Exercises, predicate=inspect.isfunction)]


if __name__ == '__main__':
    pass
