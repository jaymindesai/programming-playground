import unittest

class PriorityQueue:
    def __init__(self):
        self.heap = [(0, 0)]
        self.size = 0

    def buildheap(self, items):
        self.size = len(items)
        self.heap = [(0, 0)]
        for i in items:
            self.heap.append(i)
        i = len(items) // 2
        while i > 0:
            self._bubbledown(i)
            i = i - 1

    def _bubbledown(self, i):
        while (i * 2) <= self.size:
            mc = self._minchild(i)
            if self.heap[i][0] > self.heap[mc][0]:
                self._swap(i, mc)
            i = mc

    def _minchild(self, i):
        if i * 2 > self.size:
            return -1
        else:
            if i * 2 + 1 > self.size:
                return i * 2
            else:
                if self.heap[i * 2][0] < self.heap[i * 2 + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    def _bubbleup(self, i):
        while i // 2 > 0:
            if self.heap[i][0] < self.heap[i // 2][0]:
                self._swap(i, i // 2)
            i = i // 2

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, item):
        self.heap.append(item)
        self.size = self.size + 1
        self._bubbleup(self.size)

    def extract_min(self):
        val = self.heap[1][1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self._bubbledown(1)
        return val

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def decrease_key(self, val, amt):
        done = False
        i = 1
        key = 0
        while not done and i <= self.size:
            if self.heap[i][1] == val:
                done = True
                key = i
            else:
                i = i + 1
        if key > 0:
            self.heap[key] = (amt, self.heap[key][1])
            self._bubbleup(key)

    def __contains__(self, v):
        for pair in self.heap:
            if pair[1] == v:
                return True
        return False


class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.pqueue = PriorityQueue()
        self.pqueue.insert((2, 'x'))
        self.pqueue.insert((3, 'y'))
        self.pqueue.insert((5, 'z'))
        self.pqueue.insert((6, 'a'))
        self.pqueue.insert((4, 'd'))

    def test_insert(self):
        assert self.pqueue.size == 5

    def test_extract_min(self):
        assert self.pqueue.extract_min() == 'x'
        assert self.pqueue.extract_min() == 'y'

    def test_decrease_key(self):
        self.pqueue.decrease_key('d', 1)
        assert self.pqueue.extract_min() == 'd'

if __name__ == '__main__':
    unittest.main()
