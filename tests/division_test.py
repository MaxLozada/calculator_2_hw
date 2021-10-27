""" testing division """

from calculator.operations.division import Division

def test_division():
    """ testing result"""
    assert Division.div(4, 2) == 2
