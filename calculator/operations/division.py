""" division class"""


class Division:

    @staticmethod
    def div(value_a: int, value_b: int):
        try:
            return value_a / value_b
        except ZeroDivisionError as e:
            print(e)
            return 0

    @staticmethod
    def div(value_a: float, value_b: float):
        try:
            return value_a / value_b
        except ZeroDivisionError as e:
            print(e)
            return 0
