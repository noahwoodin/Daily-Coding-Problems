# Coding Challenge #1 (Medium)

# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    n_list = preorder(node)
    n_string = ' '.join([str(n) for n in n_list])
    return n_string


def preorder(node):
    n_list = []
    if node is not None:
        n_list.append(node.val)
        n_list.extend(preorder(node.left))
        n_list.extend(preorder(node.right))

    else:
        n_list.append('Empty')

    return n_list


def deserialize(n_string):
    n_list = n_string.split(' ')
    n_list.reverse()
    new_node = build(n_list)
    return new_node


def build(n_list):
    if len(n_list) > 0:
        cur = n_list.pop(-1)
        if cur != 'Empty':
            new_node = Node(cur)
            new_node.left = build(n_list)
            new_node.right = build(n_list)
            return new_node


# Test
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(serialize(deserialize(serialize(node))))
