def BinaryTree(root):
    return [root, [], []]


def insert_left_child(root, new_branch):
    tree = root.pop(1)
    if len(tree) > 1:
        root.insert(1, [new_branch, tree, []])
    else:
        root.insert(1, [new_branch, [], []])


def insert_right_child(root, new_branch):
    tree = root.pop(2)
    if len(tree) > 1:
        root.insert(2, [new_branch, [], tree])
    else:
        root.insert(2, [new_branch, [], []])


def get_root_value(root):
    return root[0]


def set_root_value(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


root_node = BinaryTree('a')
insert_left_child(root_node, 'b')
insert_right_child(root_node, 'c')
l = get_left_child(root_node)
insert_right_child(l, 'd')
r = get_right_child(root_node)
insert_left_child(r, 'e')
insert_right_child(r, 'f')
print(root_node)