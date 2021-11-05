"""Subtraction Class"""
from calc.operations.calculations import Calculation

class Subtraction(Calculation): # pylint: disable=too-few-public-methods
    """subtraction class"""

    def get_result(self):
        """results"""

        list_of_values = self.values[0]
        difference_of_values = list_of_values[0]
        for value in list_of_values[1:]:
            difference_of_values =   difference_of_values - float(value)
        return difference_of_values
