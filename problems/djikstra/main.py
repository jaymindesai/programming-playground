"""Djikstra's algorithm to find all the shortest paths"""

from math import inf


class PriorityQueue:
    def __init__(self):
        self.heap = [(0, 0)]
        self.size = 0

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

    def is_empty(self):
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


class Graph:
    def __init__(self):
        self.vertices = {}
        self.no_vertices = 0

    def add_vertex(self, key):
        self.no_vertices += 1
        new = Vertex(key)
        self.vertices[key] = new
        return new

    def add_edge(self, frm, to, weight=0):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)
        self.vertices[frm].add_neighbour(self.vertices[to], weight)

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def __iter__(self):
        return iter(self.vertices.keys())


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbour(self, vertex, weight=0):
        self.connected_to[vertex] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, vertex):
        return self.connected_to[vertex]


def djikstra(src, dest, graph):
    """Djikstra implementation"""

    d, pred, pqueue = _initialize(src, graph)

    S = set()
    while not pqueue.is_empty():
        u = pqueue.extract_min()
        S.add(u)
        for v in graph.get_vertex(u).get_connections():
            if v.get_id() not in S:
                _relax(u, v, d, pred, graph)
                pqueue.decrease_key(v.get_id(), d[v.get_id()])

    paths = _find_paths(src, dest, pred, [])

    smaller_paths = _find_paths_with_fewest_edges(paths)

    lexico_smallest_path = min(smaller_paths)

    print(d[dest])
    print(' '.join(map(str, lexico_smallest_path)))


def _initialize(src, graph):
    d = {}
    pred = {}
    pqueue = PriorityQueue()
    for v in graph:
        pred[v] = []
        if v == src:
            d[v] = 0
            pqueue.insert((0, v))
        else:
            d[v] = inf
            pqueue.insert((inf, v))
    return d, pred, pqueue


def _relax(u, v, d, pred, graph):
    dist = d[u] + v.get_weight(graph.get_vertex(u))
    if dist < d[v.get_id()]:
        d[v.get_id()] = dist
        pred[v.get_id()] = [u]
    elif dist == d[v.get_id()]:
        pred[v.get_id()].append(u)


def _find_paths(src, dest, pred, paths):
    if dest == src:
        paths.append(dest)
        new = []
        temp = []
        brk = None
        prev = None
        for p in paths:
            if type(p) is not list:
                brk = p
                prev = paths.index(brk) - 1
                break
        for p in paths:
            if type(p) is list:
                if paths.index(p) == prev:
                    for j in p:
                        if j == brk:
                            break
                        temp.append(j)
                new.append(p)
            else:
                temp.append(p)
        new.append(temp)
        return new
    current = dest
    for p in pred[current]:
        paths.append(current)
        paths = _find_paths(src, p, pred, paths)
    return paths


def _find_paths_with_fewest_edges(paths):
    smaller_paths = []
    mx = inf
    for p in paths:
        p.reverse()
        if len(p) < mx:
            smaller_paths.clear()
            smaller_paths.append(p)
            mx = len(p)
        elif len(p) == mx:
            smaller_paths.append(p)
    return smaller_paths


V, E = [int(x) for x in input().split()]

GRAPH = Graph()

for i in range(V):
    GRAPH.add_vertex(i)

for i in range(E):
    edge = [int(x) for x in input().split()]
    GRAPH.add_edge(edge[0], edge[1], edge[2])
    GRAPH.add_edge(edge[1], edge[0], edge[2])

SOURCE, DESTINATION = [int(x) for x in input().split()]

djikstra(SOURCE, DESTINATION, GRAPH)
