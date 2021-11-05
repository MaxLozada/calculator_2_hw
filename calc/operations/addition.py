"""Addition Class"""
from calc.operations.calculations import Calculation

class Addition(Calculation): # pylint: disable=too-few-public-methods
    """ addition class"""

    def get_result(self):
        """results"""
        sum_of_values = 0.0
        list_of_values = self.values[0]
        for value in list_of_values:
            sum_of_values = float(value) + sum_of_values
        return sum_of_values
