import copy


class Game:
    def __init__(self):
        self.state = {0: [4] * 6 + [0],
                      1: [4] * 6 + [0]}
        self.player_turn = 0

    def get_state(self):
        return copy.deepcopy(self.state)

    def get_player_turn(self):
        return self.player_turn

    def take_slot(self, pocket):
        if pocket > 5:
            return False
        if pocket < 0:
            return False
        if self.state[self.player_turn][pocket] == 0:
            return False

        # Get players information
        opposite_player_turn = 0 if self.player_turn == 1 else 1

        # Concat all pockets into one long list without the opposing players store, but with current player's store
        concat_states = self.state[self.player_turn] + self.state[opposite_player_turn]
        concat_states = concat_states[0:-1]

        # Take pieces from pocket
        pocket_pieces = concat_states[pocket]
        concat_states[pocket] = 0

        # Place all pieces in next pockets
        for _ in range(pocket_pieces):
            pocket += 1
            if pocket >= len(concat_states):
                pocket = 0
            concat_states[pocket] += 1

        # Split states
        self.state[self.player_turn] = concat_states[0:7]
        self.state[opposite_player_turn] = concat_states[7:len(concat_states)] + [self.state[opposite_player_turn][-1]]

        # Check for steal if slot is empty, on own side, and the opponent has pieces
        if concat_states[pocket] == 1 and pocket < 6 and concat_states[pocket + ((5 - pocket) * 2 + 2)] > 0:
            self.capture(pocket)

        # New turn if pocket isnt in store
        self.player_turn = opposite_player_turn if pocket != 6 else self.player_turn
        return True

    def capture(self, pocket):
        # Add pieces from both sides to player turns store
        self.state[self.player_turn][-1] += self.state[self.player_turn][pocket]
        self.state[self.player_turn][pocket] = 0

        # Pocket index reversed due to anti-clockwise game
        pocket = abs(5 - pocket)
        opposite_player_turn = 0 if self.player_turn == 1 else 1
        self.state[self.player_turn][-1] += self.state[opposite_player_turn][pocket]
        self.state[opposite_player_turn][pocket] = 0

    def is_terminal_state(self):
        # Is terminal state if one of the sides have no pieces
        if sum(self.state[self.player_turn][0:-1]) == 0:
            return True
        if sum(self.state[self.player_turn if self.player_turn == 1 else 1][0:-1]) == 0:
            return True
        return False

    def end_game(self):
        # Calculate final scores
        player1_sum = sum(self.state[0][0:-1])
        player2_sum = sum(self.state[1][0:-1])
        self.state[0][-1] += player1_sum
        self.state[1][-1] += player2_sum

        # Determine winner
        winner = 0
        if self.state[0][-1] > self.state[1][-1]:
            winner = 1  # Player 1
        elif self.state[1][-1] > self.state[0][-1]:
            winner = 2  # Player 2
        else:
            winner = -1  # Draw

        # Empty board
        for _, state in self.state.items():
            for i in range(len(state)):
                # Dont empty the score slot
                if i == 6:
                    continue
                state[i] = 0

        return winner
