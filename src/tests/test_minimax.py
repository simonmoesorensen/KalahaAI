from src.AI import Node, Leaf, MancalaTreeBuilder
from src.AI import Minimax


def test_minimax_simple_case():
    # Build tree from slides
    tree = Node(0)
    tree.children = {0: Node(0), 1:Node(0), 2:Node(0)}
    tree.children[0].children = {0: Leaf(3), 1: Leaf(12), 2: Leaf(8)}
    tree.children[1].children = {0: Leaf(2), 1: Leaf(4), 2: Leaf(6)}
    tree.children[2].children = {0: Leaf(14), 1: Leaf(2), 2: Leaf(5)}

    obj = MancalaTreeBuilder()
    obj.root = tree

    # Define the 'game'
    def utility_function(data):
        return data

    def result_function(data, a):
        return data.children[a]

    minimax = Minimax(utility_function, result_function, 5)

    assert 3 == minimax.alpha_beta_search(obj)[0] and 0 == minimax.alpha_beta_search(obj)[1]




