import inspect

from . import exercise


class Exercises:
    @staticmethod
    def simple_multiplication(x, y):
        identifier = (x, y)
        question = f"{x} * {y} = ? "
        answer = x * y
        return exercise.MathExercise(identifier, question, answer)

    @staticmethod
    def simple_division(x, y):
        identifier = (x, y)
        question = f"{x * y} : {x} = ? "
        answer = y
        return exercise.MathExercise(identifier, question, answer)

    @staticmethod
    def what_makes_div(x, y):
        identifier = (x, y)
        question = f"? : {x} = {y} "
        answer = x * y
        return exercise.MathExercise(identifier, question, answer)

    @staticmethod
    def what_makes_multi(x, y):
        identifier = (x, y)
        question = f"{x} * ? = {x * y} "
        answer = y
        return exercise.MathExercise(identifier, question, answer)


def functions():
    return [f[1] for f in inspect.getmembers(Exercises, predicate=inspect.isfunction)]


if __name__ == '__main__':
    pass
