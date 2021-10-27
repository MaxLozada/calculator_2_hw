""" testing addition """

from calculator.Operations.addition import Addition

def test_addition():
    """ testing result"""
    assert Addition.add(1, 1) == 2