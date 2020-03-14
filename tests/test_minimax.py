from AI.TreeBuilder import Node, Leaf, TreeBuilder
from AI.Minimax import Minimax


def test_minimax_simple_case():
    # Build tree from slides
    tree = Node(0)
    tree.children = [Node(0), Node(0), Node(0)]
    tree.children[0].children = [Leaf(3), Leaf(12), Leaf(8)]
    tree.children[1].children = [Leaf(2), Leaf(4), Leaf(6)]
    tree.children[2].children = [Leaf(14), Leaf(2), Leaf(5)]

    obj = TreeBuilder()
    obj.root = tree

    # Define the 'game'

    def utility_function(data):
        return data

    def result_function(data, i):
        return data.children[i]

    actions = range(0, 3)

    minimax = Minimax(utility_function, result_function, actions)

    assert 3 == minimax.alpha_beta_search(obj)[0] and 0 == minimax.alpha_beta_search(obj)[1]




