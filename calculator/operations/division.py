""" division class"""


class Division: # pylint: disable=too-few-public-methods
    """ disabling too few public methods """

    @staticmethod
    def div(value_a: float, value_b: float):
        """ dividing both value_a and value_b """
        try:
            return value_a / value_b
        except ZeroDivisionError as e:
            print(e)
            return 0
