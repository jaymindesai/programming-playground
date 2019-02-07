
def preorder(tree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left())
        preorder(tree.get_right())

def postorder(tree):
    if tree:
        postorder(tree.get_left())
        postorder(tree.get_right())
        print(tree.get_root_value())

def inorder(tree):
    if tree:
        inorder(tree.get_left())
        print(tree.get_root_value())
        inorder(tree.get_right())
