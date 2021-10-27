""" testing multiplication """

from calculator.Operations.multiplication import Multiplication

def test_multiplication():
    """ testing result"""
    assert Multiplication.mul(1, 2) == 2