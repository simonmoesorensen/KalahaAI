from AI.evaluation_function import check_player_utility

def test_player_steal_and_AI_steal_and_player_extra_turn():
    # Player: 0 can steal and get 1 extra turn.
    state = {0: [1, 0, 4, 4, 4, 4, 0],
             1: [4, 4, 1, 0, 4, 4, 0]}

    # AI score
    assert check_player_utility(1, state, 0) == -5
    # Player score
    assert check_player_utility(0, state, 0) == 6


def test_check_AI_steal():
    # AI steals from player: minimizing score
    state = {0: [4, 4, 4, 4, 4, 4, 0],
             1: [4, 4, 0, 4, 4, 0, 0]}

    # Check if AI (1) can steal
    assert check_player_utility(1, state, 0) == -5


def test_check_AI_extra_turn():
    # AI gets an extra turn: minimizing score
    state = {0: [4, 4, 4, 4, 4, 4, 0],
             1: [4, 0, 4, 4, 4, 0, 0]}

    # Check if AI (1) can make an extra move
    assert check_player_utility(1, state, 0) == -1


def test_check_player_steal():
    # Player steals from AI: maximizing score
    state = {0: [4, 4, 0, 4, 4, 0, 0],
             1: [4, 4, 4, 4, 4, 4, 0]}

    # Check if player (0) can steal
    assert check_player_utility(0, state, 0) == 5


def test_check_player_extra_turn():
    # Player gets an extra turn: maximizing score

    state = {0: [4, 0, 4, 4, 4, 0, 0],
             1: [4, 4, 4, 4, 4, 4, 0]}

    # Check if player (0) can make an extra move
    assert check_player_utility(0, state, 0) == 1
