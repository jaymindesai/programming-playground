from collections import deque


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def prep_tree1():
    """
    in_order: 4 2 5 1 6 3 7
    pre_order: 1 2 4 5 3 6 7
    post_order: 4 5 2 6 7 3 1
    level_order: 1 2 3 4 5 6 7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


def in_order(root, func):
    if root:
        in_order(root.left, func)
        func(root.val)
        in_order(root.right, func)


def pre_order(root, func):
    if root:
        func(root.val)
        pre_order(root.left, func)
        pre_order(root.right, func)


def post_order(root, func):
    if root:
        post_order(root.left, func)
        post_order(root.right, func)
        func(root.val)


def in_order_iterative(root, func):
    stack = []
    curr = root
    done = False
    while not done:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            func(curr.val)
            curr = curr.right
        else:
            done = True


def pre_order_iterative(root, func):
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr:
            func(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)


def post_order_iterative(root, func):
    stack = []
    curr = root
    done = False
    while not done:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            func(curr.val)
            if stack:
                top = stack[-1]
                if top.left is curr:
                    curr = top.right
                else:
                    curr = None
            else:
                done = True
        else:
            done = True


def level_order(root, func):
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        func(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


if __name__ == '__main__':

    tree = prep_tree1()

    print('Recursive Inorder Traversal')
    in_order(tree, print)
    print('\n')
    print('Iterative Inorder Traversal')
    in_order_iterative(tree, print)

    print('\n')

    print('Recursive Preorder Traversal')
    pre_order(tree, print)
    print('\n')
    print('Iterative Preorder Traversal')
    pre_order_iterative(tree, print)

    print('\n')

    print('Recursive Postorder Traversal')
    post_order(tree, print)
    print('\n')
    print('Iterative Postorder Traversal')
    post_order_iterative(tree, print)

    print('\n')

    print('Levelorder Traversal')
    level_order(tree, print)