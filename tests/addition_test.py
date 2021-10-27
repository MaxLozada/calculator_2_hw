""" testing addition """

from calculator.operations.addition import Addition

def test_addition():
    """ testing result"""
    assert Addition.add(1, 1) == 2