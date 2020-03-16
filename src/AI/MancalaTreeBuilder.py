import copy
import json

from src.kalaha import Game


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Node):
            return obj.__dict__
        elif isinstance(obj, Game):
            return obj.__dict__

        return super(JsonEncoder, self).default(obj)


class MancalaTreeBuilder:
    def __init__(self, rec_limit=3):
        self.rec_limit = rec_limit  # Recursion limit
        self.root = None

    def set_root(self, root):
        self.root = root

    def build(self):
        self.build_from(self.root)

    def build_from(self, node, rec_depth=0):
        # Exit if reached recursion limit
        if rec_depth >= self.rec_limit:
            return

        # Add child for all possible actions (moves)
        for i in range(0, 6):
            game = copy.deepcopy(node.get_data())  # Separate game states across sibling nodes

            # Add child if it was a valid move
            if game.take_slot(i):
                if game.is_terminal_state():
                    game.end_game()
                    node.add_child(move=i, child=Leaf(game))
                else:
                    node.add_child(move=i, child=Node(game))

        # For every Node child, keep adding children
        for child in node.get_children().values():
            if isinstance(child, Node):
                self.build_from(child, rec_depth + 1)

    def save_tree(self, name="tree.json"):
        json_str = json.dumps(self.root, cls=JsonEncoder)
        with open(name, 'w') as f:
            f.write(json_str)
            f.close()

    def load_tree(self, name):
        dict = json.load(open(name))
        self.set_root(Node(Game()))

        # Iterate children function
        def iter_children(children, parent):
            for move, child in children.items():
                move = int(move)

                # Construct game
                game = Game()
                game.state[0] = child['data']['state']['0']
                game.state[1] = child['data']['state']['1']
                game.player_turn = child['data']['player_turn']

                # Add a Leaf or Node to parent
                if 'children' in child:
                    # Node
                    child_node = Node(game)
                    parent.add_child(move, child_node)
                    iter_children(child['children'], child_node)
                else:
                    # Leaf
                    child_node = Leaf(game)
                    parent.add_child(move, child_node)

        iter_children(dict['children'], self.root)


class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}

    def add_child(self, move, child):
        self.children[move] = child

    def get_children(self):
        return self.children

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    # Evaluation function
    def calculate_utility(self, fn):
        return fn(self.data)


class Leaf:
    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def calculate_utility(self, fn):
        return fn(self.data)
