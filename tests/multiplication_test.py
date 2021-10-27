""" testing multiplication """

from calculator.operations.multiplication import Multiplication

def test_multiplication():
    """ testing result"""
    assert Multiplication.mul(1, 2) == 2