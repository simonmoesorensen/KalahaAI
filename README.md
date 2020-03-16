# KalahaAI
Mancala (EN) / Kalaha (DK) game written in python with functioning AI based on the minimax algorithm


## Prerequisites
- Python 3.x
- cx_freeze 6.1 (optional)

## Running the script

If on windows double-click `run_me.bat` or 

run `python main.py` in a console when in main.py directory.

## The game

The game is implemented with the following rules:

1. The game begins with one player picking up all of the pieces in any one of the pockets on his/her side.
2. Moving counter-clockwise, the player deposits one of the stones in each pocket until the stones run out.
3. If you run into your own Mancala (store), deposit one piece in it. If you run into your opponent's Mancala, skip it and
 continue moving to the next pocket.
4. If the last piece you drop is in your own Mancala, you take another turn.
5. If the last piece you drop is in an empty pocket on your side, you capture that piece and any pieces in the pocket directly
opposite.
6. Always place all captured pieces in your Mancala (store).
7. The game ends when all six pockets on one side of the Mancala board are empty.
8. The player who still has pieces on his/her side of the board when the game ends captures all of those pieces.
9. Count all the pieces in each Mancala. The winner is the player with the most pieces.

### Playing the game

When running the script you are presented the initial game state:

```
Running game (anti-clockwise)
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 4 | 4 | 4 | 4 | 4 | 4 | Score: 0
---------------------------------------
Player 1 | 4 | 4 | 4 | 4 | 4 | 4 | Score: 0
=======================================

It is player 1's turn
Choose which slot to pick up (index at 0): 
```

You are player 1.

Choose a value in the `Slots: ` row to pick up the corresponding pieces on your side 
and place them anti-clockwise in other slots

When it is the AI's turn it will compute it's next move:

```
It is player 1's turn
Choose which slot to pick up (index at 0): 4
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 4 | 4 | 4 | 5 | 5 | 5 | Score: 0  <-- Notice the 3'rd slot
---------------------------------------
Player 1 | 4 | 4 | 0 | 5 | 0 | 6 | Score: 2
=======================================

It is player 2's turn
AI computing tree
AI computing best move
AI found utility: -4, move: 3  <-- AI found the best move in slot 3
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 5 | 5 | 5 | 0 | 5 | 5 | Score: 1  <-- Slot 3 has been picked up
---------------------------------------
Player 1 | 5 | 4 | 0 | 5 | 0 | 6 | Score: 2
=======================================

It is player 1's turn
Choose which slot to pick up (index at 0): 
```

The above printout is explained by the `<--` arrows.

When one of the player's side is empty, the game will sum all the pieces together on each side
and compute the winner. Moreover, it will also record and print the game sequence in a 2-tuple
of (player_turn, move)

```
It is player 1's turn
Choose which slot to pick up (index at 0): 5
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 9 | 2 | 10 | 1 | 9 | 1 | Score: 10
---------------------------------------
Player 1 | 0 | 0 | 0 | 0 | 0 | 0 | Score: 6  <-- Empty side
=======================================

It is player 2's turn
AI computing tree
AI computing best move
AI found utility: 36, move: 5
Slots:   | 0 | 1 | 2 | 3 | 4 | 5 |
=======================================
Player 2 | 0 | 0 | 0 | 0 | 0 | 0 | Score: 42  <-- All pieces summed together and added to score
---------------------------------------
Player 1 | 0 | 0 | 0 | 0 | 0 | 0 | Score: 6
=======================================
Game over, winner is Player 2
Game sequence: [(0, 0), (1, 4), (0, 2), (1, 2), (1, 0), (0, 3), (1, 4), (1, 2), (0, 4), (1, 0), (0, 0), (1, 2), (0, 5), (1, 0)]
Press Enter to end...
```

### AI
The AI is built upon the Minimax algorithm. To make the tree search more efficient, 
alpha-beta pruning is used. Moreover, a cut-off test has been implemented to limit 
the recursion depth of the algorithm.

The game tree is regenerated every time it is the AI's turn.

The evaluation function is passed a game state and computes a utility value, which represents 
the 'goodness' of a given state. The utility value is computed by comparing the current and 
opposite player's states. The following parameters are compared between the two players: 
- No. Extra turns * 5
- No. Steals + steal amount 
- No. Pieces on a player's side (including mancala store)

## Building an executable file
If cx_freeze is not installed, then run `pip install cx_freeze` in the console.

Open a console and navigate to `setup.py` and run `python setup.by build`. You'll see a
folder 'build' in the current directory. Inside you will find another folder with the freezed
script. Run main.exe

