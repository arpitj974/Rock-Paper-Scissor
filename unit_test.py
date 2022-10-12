from Player import Player
from Game import Game

p1 = Player()
game = Game()
game.initialize()


def test_0_main_validate_action_whitespace():
    x = "    "
    y = False
    assert p1.validate_action(x) == y, "test failed "


def test_1_main_validate_action_digit_plus_character():
    x = "45st"
    y = False
    assert p1.validate_action(x) == y, "test failed"


def test_2_main_validate_action_digit():
    x = "3"
    y = True
    assert p1.validate_action(x) == y, "test failed"


def test_3_main_get_result():
    player_action = 1
    computer_action = 2

    assert game.get_result(player_action, computer_action) == "computer", "test failed"
