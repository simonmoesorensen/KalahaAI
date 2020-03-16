def evaluation_function(game):
    state = game.get_state()
    player_turn = game.get_player_turn()
    opposite_player_turn = 1 if player_turn == 0 else 0

    utility = 0

    # Check player's utility
    utility += check_player_utility(player_turn, state)
    # Check AI utility
    utility += check_player_utility(opposite_player_turn, state)

    # Mancala score utility

    # Compute player 1 score
    player_1_score = state[0][-1]

    # Compute player 2 score
    player_2_score = state[1][-1]

    utility += player_2_score - player_1_score
    return utility


def check_player_utility(player_turn, state):
    utility = 0
    opposite_player_turn = 1 if player_turn == 0 else 0
    # Check steal and extra turn
    for slot, slot_count in enumerate(state[player_turn][0:6]):
        # Extra turn
        if (6 - slot) == slot_count:
            utility += (-1 if player_turn == 0 else 1) * 5  # Extra turns are weighted highly

        # Steal
        # Check for empty slot and can steal more than 0 pieces
        pieces_to_steal = state[opposite_player_turn][abs(5 - slot)]
        if slot_count == 0 and pieces_to_steal > 0:
            # Check if we can land in empty slot
            for slot2, slot_count2 in enumerate(state[player_turn][0:slot]):
                if (slot - slot2) == slot_count2:
                    # Utility based on how many pieces we can steal (plus the piece which lands in slot with 0)
                    utility += -pieces_to_steal - 1 if player_turn == 0 else pieces_to_steal + 1

    return utility