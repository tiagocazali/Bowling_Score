import pytest
from bowling import Bowling

frame_test = [[10,0],[10,0],[10,0],[7,3],[8,1],[9,0],[9,1],[10,0],[7,0],[8,2,9]]
score_test = [  30,    27,   20,     18,   9,    9,    20,   17,    7,    19]

frame_test2 = [[9,1],[10],[9,1],[10],[9,0],[4,4],[10],[2,6],[10,0],[6,4,8]]
score_test2 = [  20,  20,  20,   19,   9,    8,   18,   8,    20,     18]

def test_first_frame_spere():
    player1 = Bowling()

    player1.add_points(6,4)
    player1.calculate_points(True)

    assert player1.score_table[0] == None

def test_first_frame_spere2():
    player1 = Bowling()

    player1.add_points(6,4)
    player1.add_points(5,4)
    player1.calculate_points(True)

    assert player1.score_table[0] == 15
    assert player1.score_table[1] == 9

def test_first_frame_strike():
    player1 = Bowling()

    player1.add_points(10)
    player1.calculate_points(True)

    assert player1.score_table[0] == None

def test_first_frame_strike2():
    player1 = Bowling()

    player1.add_points(10)
    player1.add_points(5,4)
    player1.calculate_points(True)

    assert player1.score_table[0] == 19
    assert player1.score_table[1] == 9

def test_first_frame_Duble_strike():
    player1 = Bowling()

    player1.add_points(10)
    player1.add_points(10)
    player1.calculate_points(True)

    assert player1.score_table[0] == None
    assert player1.score_table[1] == None

def test_first_frame_Duble_strike2():
    player1 = Bowling()

    player1.add_points(10)
    player1.add_points(10)
    player1.add_points(5,4)
    player1.calculate_points(True)

    assert player1.score_table[0] == 25
    assert player1.score_table[1] == 19
    assert player1.score_table[2] == 9

def test_first_frame_Duble_strike_and_Spere():
    player1 = Bowling()

    player1.add_points(10)
    player1.add_points(10)
    player1.add_points(5,5)
    player1.calculate_points(True)

    assert player1.score_table[0] == 25
    assert player1.score_table[1] == 20
    assert player1.score_table[2] == None

def test_triple_Strike():
    player1 = Bowling()

    player1.add_points(6,3)
    player1.add_points(10)
    player1.add_points(10)
    player1.add_points(10)
    player1.add_points(3,4)
    player1.calculate_points(True)

    assert player1.score_table[1] == 30

def test_duble_Strike():
    player1 = Bowling()

    player1.add_points(6,3)
    player1.add_points(4,3)
    player1.add_points(6,4)
    player1.add_points(10)
    player1.add_points(10)
    player1.add_points(3,3)
    player1.add_points(3,4)
    player1.calculate_points(True)

    assert player1.score_table[3] == 23

def test_LAST_Frame_Normal():
    player1 = Bowling()

    player1.frame_table = [[10,0],[10,0],[10,0],[7,3],[8,1],[9,0],[9,1],[10,0],[7,0],[8,1,0]]
    player1.calculate_points(True)

    assert player1.score_table[9] == 9

def test_LAST_Frame_Strike():
    player1 = Bowling()

    player1.frame_table = [[10,0],[10,0],[10,0],[7,3],[8,1],[9,0],[9,1],[10,0],[7,0],[8,2,5]]
    player1.calculate_points(True)

    assert player1.score_table[9] == 15

def test_LAST_Frame_Strike_and_Before_Strike():
    player1 = Bowling()

    player1.frame_table = [[10,0],[10,0],[10,0],[7,3],[8,1],[9,0],[9,1],[10,0],[10,0],[8,2,5]]
    player1.calculate_points(True)

    assert player1.score_table[8] == 20
    assert player1.score_table[9] == 15

def test_LAST_Frame_Strike_and_Before_Spare():
    player1 = Bowling()

    player1.frame_table = [[10,0],[10,0],[10,0],[7,3],[8,1],[9,0],[9,1],[10,0],[5,5],[8,2,5]]
    player1.calculate_points(True)

    assert player1.score_table[8] == 18
    assert player1.score_table[9] == 15

def test_LAST_Frame_Triple_Strike():
    player1 = Bowling()

    player1.frame_table = [[10,0],[10,0],[10,0],[7,3],[8,1],[9,0],[9,1],[10,0],[5,5],[10,10,10]]
    player1.calculate_points(True)

    assert player1.score_table[8] == 20
    assert player1.score_table[9] == 30

def test_ALL_Strike_The_Best_Game():
    player1 = Bowling()

    player1.frame_table = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,10,10]]
    player1.calculate_points(True)

    assert sum(player1.score_table) == 300

def test_full_play():
    
    player1 = Bowling()

    player1.frame_table = frame_test2
    player1.calculate_points(True)

    for index, point in enumerate(player1.score_table):
        assert point == score_test2[index]
   

   