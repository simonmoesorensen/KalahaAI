from src.AI import MancalaTreeBuilder, Node
from src.kalaha import Game
import os
import random


def test_save():
    # Setup tree
    game = Game()

    recursion_limit = 4

    tree = MancalaTreeBuilder(recursion_limit)
    tree.set_root(Node(game))
    tree.build()

    # Save tree with random name
    name = random.random()
    path = "{0}.json".format(name)[2:]
    tree.save_tree(path)

    # Check it exists and has build children
    assert tree.root.children.__len__() == 6 and os.path.isfile(path)

    # Remove file
    os.remove(path)


def test_load():
    # Load tree
    game = Game()
    game.take_slot(0)

    tree = MancalaTreeBuilder()

    tree.load_tree("do_not_delete.json")

    # Check children exists and first move is equal
    data = tree.root.children[0].get_data()
    assert tree.root.children.__len__() == 6 and data.state[0][0] == game.state[0][0]
