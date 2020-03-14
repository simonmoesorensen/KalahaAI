from kalaha.Game import Game

def print_game(game):
    state = game.get_state()
    slots = list(range(0,6))
    player1_state = state[0]
    player2_state = state[1]
    player2_state.reverse()

    print("Slots:   | ", end=""); print(*slots, sep=" | ", end=""); print(" |")
    print("=======================================")
    print("Player 2 | ", end="")
    print(*player2_state[1:], sep=" | ", end=""); print(" | Score: {0}".format(player2_state[0]))
    print("---------------------------------------")
    print("Player 1 | ", end="")
    print(*player1_state[0:-1], sep=" | ", end=""); print(" | Score: {0}".format(player1_state[-1]))
    print("=======================================")

if __name__ == "__main__":
    # Run game
    game = Game()
    should_end = game.is_terminal_state()

    print("Running game (anti-clockwise)")
    game_seq = []
    while not should_end:
        print_game(game)

        print("\nIt is player {0}'s turn".format(1 + game.get_player_turn()))
        slot = int(input("Choose which slot to pick up (index at 0): "))
        game_seq.append(slot)
        # Reverse slot if player 2 is playing
        slot = abs(5 - slot) if game.get_player_turn() == 1 else slot
        game.take_slot(slot)

        winner = 0
        if game.is_terminal_state():
            winner = game.end_game()
            should_end = True
            print_game(game)

    print("Game over, winner is Player {0}".format(winner))
    print("Game sequence:", game_seq)

