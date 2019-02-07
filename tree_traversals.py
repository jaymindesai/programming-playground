from ads.tree.binary_tree import BinaryTree


def preorder(tree: BinaryTree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left())
        preorder(tree.get_right())


def postorder(tree: BinaryTree):
    if tree:
        postorder(tree.get_left())
        postorder(tree.get_right())
        print(tree.get_root_value())


def inorder(tree: BinaryTree):
    if tree:
        inorder(tree.get_left())
        print(tree.get_root_value())
        inorder(tree.get_right())


def inorder_iterative(tree: BinaryTree):
    stack = []
    node = tree
    done = False
    while not done:
        if node:
            stack.append(node)
            node = node.get_left()
        elif stack:
            node = stack.pop()
            print(node.get_root_value())
            node = node.get_right()
        else:
            done = True


ritree = BinaryTree(1)
ritree.insert_right(2)
ritree.get_right().insert_right(3)

leftree = BinaryTree(1)
leftree.insert_left(2)
leftree.get_left().insert_left(3)

inorder(ritree)
preorder(ritree)
postorder(ritree)

print('')

inorder(leftree)
preorder(leftree)
postorder(leftree)
