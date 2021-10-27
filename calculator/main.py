""" This is the increment function"""
from calculator.operations.addition import Addition
from calculator.operations.division import Division
from calculator.operations.multiplication import Multiplication
from calculator.operations.subtraction import Subtraction

class Calculator:
    """ This is the Calculator class"""

    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a, value_b):
        """ adds number to result"""
        self.result = Addition.add(value_a, value_b)
        return self.result

    def subtract_number(self, value_a, value_b):
        """ subtract number from result"""
        self.result = Subtraction.sub(value_a, value_b)
        return self.result

    def multiply_numbers(self, value_a, value_b):
        """ multiply two numbers and store the result"""
        self.result = Multiplication.mul(value_a, value_b)
        return self.result

    def divide_numbers(self, value_a, value_b):
        """ divide two numbers abd store the result"""
        self.result = Division.div(value_a, value_b)
        return self.result
