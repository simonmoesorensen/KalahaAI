from kalaha.game import Game


def test_terminal_state():
    return False

def test_capture_pieces_on_end():
    return False

def test_extra_turn_player1():
    game = Game()

    game.move_piece(2)

    assert game.get_player_turn() == 0

def test_extra_turn_player2():
    game = Game()

    game.move_piece(0)
    game.move_piece(2)

    assert game.get_player_turn() == 1

def test_player2_steal():
    game = Game()

    game.move_piece(0)
    game.move_piece(4)
    game.move_piece(0)
    game.move_piece(0)  # Player 2 steals 7 from player 1

    state = game.get_state()

    assert state[1][-1] == 9 and state[0][-1] == 0

def test_player1_steal():
    # Run game
    game = Game()

    game.move_piece(4)
    game.move_piece(0)
    game.move_piece(0)  # Player 1 steals 6 from player 2

    state = game.get_state()

    assert state[0][-1] == 8 and state[1][-1] == 0 and state[0][4] == 0 and state[0][5] == 5 and state[1][0] == 0
