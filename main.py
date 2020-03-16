from src.AI import MancalaTreeBuilder, Node, Minimax, evaluation_function
from src.kalaha import Game

"""
This is the main script which runs the game with one player and one AI.

The human player starts.
"""

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
    # Tree recursion limit
    rec_limit = 6

    # Minimax algorithm
    def result_function(node, a):
        children = node.get_children()
        return children[a]

    # Construct minimax object
    minimax = Minimax(evaluation_function, result_function, max_depth=rec_limit)

    # Run game
    game = Game()
    should_end = game.is_terminal_state()

    print("Running game (anti-clockwise)")
    game_seq = []
    while not should_end:
        print_game(game)

        player_turn = game.get_player_turn()
        print("\nIt is player {0}'s turn".format(1 + player_turn))

        slot = None
        if player_turn == 0:
            slot = int(input("Choose which slot to pick up (index at 0): "))
            # Player
        else:
            print("AI computing tree")
            # AI
            tree = MancalaTreeBuilder(rec_limit)
            tree.set_root(Node(game))
            tree.build()

            print("AI computing best move")
            v, slot = minimax.alpha_beta_search(tree)
            print("AI found utility: {0}, move: {1}".format(v, 5 - slot))

        game_seq.append((player_turn, slot))
        # Reverse slot if player 2 is playing
        game.take_slot(slot)

        winner = 0
        if game.is_terminal_state():
            winner = game.end_game()
            should_end = True
            print_game(game)

    print("Game over, winner is Player {0}".format(winner))
    print("Game sequence:", game_seq)
    input("Press Enter to end...")
