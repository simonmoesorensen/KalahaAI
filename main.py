from kalaha.game import Game

if __name__ == "__main__":
    # Run game
    game = Game()
    should_end = game.is_terminal_state()

    print("Running game")

    while not should_end:
        print(game.get_state())

        print("It is player {0}'s turn".format(1 + game.get_player_turn()))
        slot = int(input("Choose which slot to pick up (index at 0): "))
        game.move_piece(slot)

        if game.is_terminal_state():
            game.end_game()
            should_end = True


