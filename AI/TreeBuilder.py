import copy
import json
from kalaha.Game import Game


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Node):
            return obj.__dict__
        elif isinstance(obj, Game):
            return obj.__dict__

        return super(JsonEncoder, self).default(obj)


class TreeBuilder:
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
                node.add_child(
                    Node(game) if not game.is_terminal_state() else Leaf(game)
                )

        # For every Node child, keep adding children
        for child in node.get_children():
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
            for child in children:
                # Construct game
                game = Game()
                game.state[0] = child['game']['state']['0']
                game.state[1] = child['game']['state']['1']
                game.player_turn = child['game']['player_turn']

                # Add a Leaf or Node to parent
                if 'children' in child:
                    # Node
                    child_node = Node(game)
                    parent.add_child(child_node)
                    iter_children(child['children'], child_node)
                else:
                    # Leaf
                    child_node = Leaf(game)
                    parent.add_child(child_node)

        iter_children(dict['children'], self.root)


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class Leaf:
    def __init__(self, data):
        self.data = data
        return

    def calculate_utility(self, fn):
        return fn(self.data)

