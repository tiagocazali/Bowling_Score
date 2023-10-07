import pytest
from bowling import Bowling

frame_test = [[9,1],[10],[9,1],[10],[9,0],[4,4],[10],[2,6],[10,0],[6,4,8]]
score_test = [20, 20, 20, 19, 9, 8, 18, 8, 20, 18]

def test_first_frame_spere():
    player1 = Bowling()

    player1.add_points(6,4)
    player1.calculate_points(True)

    assert player1.score_table[0] == None

def test_first_frame_strike():
    player1 = Bowling()

    player1.add_points(10)
    player1.calculate_points(True)

    assert player1.score_table[0] == None

def test_triple_Strike():
    player1 = Bowling()

    player1.add_points(6,3)
    player1.add_points(10)
    player1.add_points(10)
    player1.add_points(10)
    player1.add_points(3,4)
    player1.calculate_points(True)

    assert player1.score_table[1] == 30

def test_full_play():
    
    player1 = Bowling()

    player1.frame_table = frame_test
    player1.calculate_points(True)

    for index, point in enumerate(player1.score_table):
        assert point == score_test[index]
   

   