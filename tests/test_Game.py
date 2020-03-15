from kalaha.Game import Game


def test_terminal_state():
    game = Game()

    # Sequence to end the game
    game.take_slot(2)
    game.take_slot(5)
    game.take_slot(1)
    game.take_slot(5)
    game.take_slot(0)
    game.take_slot(3)
    game.take_slot(2)
    game.take_slot(2)
    game.take_slot(0)
    game.take_slot(4)
    game.take_slot(2)
    game.take_slot(5)

    assert game.is_terminal_state()


def test_capture_pieces_on_end():
    game = Game()

    # Sequence to end the game
    game.take_slot(2)
    game.take_slot(5)
    game.take_slot(1)
    game.take_slot(5)
    game.take_slot(0)
    game.take_slot(3)
    game.take_slot(2)
    game.take_slot(2)
    game.take_slot(0)
    game.take_slot(4)
    game.take_slot(2)
    game.take_slot(5)

    game.end_game()
    state = game.get_state()
    assert state[0][6] == 42 and state[1][6] == 6 and sum(state[0][0:6] + state[1][0:6]) == 0


def test_extra_turn_player1():
    game = Game()

    game.take_slot(2)

    assert game.get_player_turn() == 0


def test_extra_turn_player2():
    game = Game()

    game.take_slot(0)
    game.take_slot(2)

    assert game.get_player_turn() == 1


def test_player2_steal():
    game = Game()

    game.take_slot(0)
    game.take_slot(4)
    game.take_slot(0)
    game.take_slot(0)  # Player 2 steals 7 from player 1

    state = game.get_state()

    assert state[1][-1] == 9 and state[0][-1] == 0 and state[0][1] == 0 and state[1][4] == 0


def test_player1_steal():
    # Run game
    game = Game()

    game.take_slot(4)
    game.take_slot(0)
    game.take_slot(0)  # Player 1 steals 6 from player 2

    state = game.get_state()

    assert state[0][-1] == 8 and state[1][-1] == 0 and state[0][4] == 0 and state[0][5] == 5 and state[1][0] == 0


def test_invalid_pocket():
    game = Game()

    assert not game.take_slot(7) and not game.take_slot(-1)
