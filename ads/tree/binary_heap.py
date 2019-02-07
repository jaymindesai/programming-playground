class BinHeap:
    """Priority Queue / Min Heap"""

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self._bubbleup(self.size)

    def extract_min(self):
        val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._bubbledown(1)
        return val

    def _bubbleup(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] > self.heap[i]:
                self._swap(i, i // 2)
            i //= 2

    def _bubbledown(self, i):
        while i * 2 <= self.size:
            mc = self._minchild(i)
            if self.heap[i] > self.heap[mc]:
                self._swap(i, mc)
            i = mc

    def _minchild(self, i):
        left = i * 2
        right = (i * 2) + 1
        if right > self.size:
            return left
        else:
            if self.heap[left] < self.heap[right]:
                return left
            else:
                return right

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def buildheap(self, items):
        self.size = len(items)
        i = self.size // 2
        self.heap = [0] + items[:]
        while i > 0:
            self._bubbledown(i)
            i -= 1


pqueue = BinHeap()
# pqueue.buildheap([5, 7, 3, 11])

pqueue.insert(5)
pqueue.insert(7)
pqueue.insert(3)
pqueue.insert(11)

print(pqueue.extract_min())
print(pqueue.extract_min())
print(pqueue.extract_min())
print(pqueue.extract_min())
