class BinaryTree:

    def __init__(self, root_value):
        self.key = root_value
        self.left: BinaryTree = None
        self.right: BinaryTree = None

    def insert_left(self, root_value):
        new = BinaryTree(root_value)
        if self.left is None:
            self.left = new
        else:
            new.left = self.left
            self.left = new

    def insert_right(self, root_value):
        new = BinaryTree(root_value)
        if self.right is None:
            self.right = new
        else:
            new.right = self.right
            self.right = new

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_root_value(self, value):
        self.key = value

    def get_root_value(self):
        return self.key


# root_node = BinaryTree('a')
# root_node.insert_left('b')
# root_node.insert_right('c')
# l = root_node.get_left()
# l.insert_right('d')
# r = root_node.get_right()
# r.insert_left('e')
# r.insert_right('f')
#
# print(root_node.get_left().get_right().get_root_value())

