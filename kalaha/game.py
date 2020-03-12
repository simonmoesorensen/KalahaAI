class Game(object):
    def __init__(self):
        self.state = {0: [4] * 6 + [0],
                      1: [4] * 6 + [0]}
        self.players = [0, 1]
        self.player_turn = 0
        return

    def get_state(self):
        return self.state

    def get_player_turn(self):
        return self.player_turn

    def move_piece(self, pocket):
        if pocket > 5:
            return
        if pocket < 0:
            return
        if self.state[self.player_turn][pocket] == 0:
            return

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

        # Check for steal
        if concat_states[pocket] == 1:
            self.capture(pocket)

        # New turn if pocket isnt in store
        self.player_turn = opposite_player_turn if pocket != 6 else self.player_turn

    def capture(self, pocket):
        # Add pieces from both sides to player turns store
        self.state[self.player_turn][-1] += self.state[self.player_turn][pocket]
        self.state[self.player_turn][pocket] = 0

        opposite_player_turn = 0 if self.player_turn == 1 else 1
        self.state[self.player_turn][-1] += self.state[opposite_player_turn][pocket]
        self.state[opposite_player_turn][pocket] = 0

    def is_terminal_state(self):
        # Is terminal state if one of the sides have no pieces
        if sum(self.state[self.player_turn][0:-1]) == 0:
            return True
        if sum(self.state[self.player_turn if self.player_turn == 1 else 1][0:-1]) == 0:
            return True

    def end_game(self):
        # Player 1 not empty
        player1_sum = sum(self.state[0][0:-1])
        if player1_sum != 0:
            self.state[0][-1] += player1_sum

            for i in range(len(self.state[0])):
                self.state[0][i] = 0

        # Player 2 not empty
        player2_sum = sum(self.state[1][0:-1])
        if player2_sum != 0:
            self.state[1][-1] += player2_sum

            for i in range(len(self.state[1])):
                self.state[1][i] = 0
