import pytest
from bowling import Bowling

def test_first_frame():
    player1 = Bowling()

    player1.add_points(10)
    player1.calculate_points()

    assert player1.score_table[0] == None