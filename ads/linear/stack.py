
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peep(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0