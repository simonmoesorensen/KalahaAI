import copy

from kalaha.Game import Game
from AI.TreeBuilder import TreeBuilder, Node, Leaf

class Minimax:
    def __init__(self, util_func, result_func, actions=range(0,6)):
        self.util_func = util_func
        self.actions = actions
        self.result_func = result_func

    def alpha_beta_search(self, tree):
        """
        Runs alpha-beta search on a game tree. Returns the utility with best move
        :param tree: TreeBuilder obj
        :return: (int, int)-tuple with utility and best move index respectively
        """
        v, i = self.max_value(tree.root, float('-inf'), float('inf'))
        return v, i
    
    def max_value(self, node, a, b):
        # Check for terminal state (Leaf nodes are only generated in terminal state)
        if isinstance(node, Leaf):
            return node.calculate_utility(self.util_func), 0

        data = node.get_data()
        v = float('-inf')
        best_i = -1

        # Iterate over number of actions
        for i in self.actions:
            data_copy = copy.deepcopy(data)  # Save game state
            v = max(v, self.min_value(self.result_func(node, i), a, b)[0])
            node.set_data(data_copy)  # Reset to former game state

            # Alpha-beta pruning
            if v >= b:
                return v, best_i

            if v > a:
                best_i = i

            a = max(a, v)

        return v, best_i
    
    def min_value(self, node, a, b):
        # Check for terminal state (Leaf nodes are only generated in terminal state)
        if isinstance(node, Leaf):
            return node.calculate_utility(self.util_func), 0

        data = node.get_data()
        v = float('inf')
        best_i = -1

        # Iterate over number of actions
        for i in self.actions:
            data_copy = copy.deepcopy(data)  # Save game state
            v = min(v, self.max_value(self.result_func(node, i), a, b)[0])
            node.set_data(data_copy)  # Reset to former game state
    
            # Alpha-beta pruning
            if v <= a:
                return v, best_i

            if v < b:
                best_i = i

            b = min(b, v)

        return v, best_i
