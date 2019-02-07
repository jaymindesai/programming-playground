from operator import add, sub, mul, truediv

from ads.tree.binary_tree import BinaryTree
from ads.linear.stack import Stack
from ads.tree.traversals import postorder


def parse_tree(expr):
    tokens = list(expr)
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current = tree

    for t in tokens:
        if t == '(':
            current.insert_left('')
            stack.push(current)
            current = current.get_left()

        elif t in ['*', '/', '+', '-']:
            current.set_root_value(t)
            current.insert_right('')
            stack.push(current)
            current = current.get_right()

        elif t == ')':
            current = stack.pop()

        else:
            current.set_root_value(int(t))
            parent = stack.pop()
            current = parent

    return tree


def evaluate(tree: BinaryTree):
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    left = tree.get_left()
    right = tree.get_right()

    if left and right:
        f = ops[tree.get_root_value()]
        return f(evaluate(left), evaluate(right))

    else:
        return tree.get_root_value()


def postorder_eval(tree: BinaryTree):
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    if tree:
        res1 = postorder_eval(tree.get_left())
        res2 = postorder_eval(tree.get_right())
        if res1 and res2:
            return ops[tree.get_root_value()](res1, res2)
        else:
            return tree.get_root_value()


def getexpr(tree: BinaryTree):
    expr = ''
    if tree:
        expr = '(' + getexpr(tree.get_left())
        expr += str(tree.get_root_value())
        expr += getexpr(tree.get_right()) + ')'
    return expr


expr = '((4+5)*5)'
tree = parse_tree(expr)
print(getexpr(tree))
# print(evaluate(tree))
# print(post_order_eval(tree))
# postorder(tree)
