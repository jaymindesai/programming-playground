from collections import deque

GRAPH = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}

DAG = {'A': {'B', 'C'},
       'B': {'D', 'E'},
       'C': {'E', 'F'},
       'D': set(),
       'E': set(),
       'F': set()}

DISGRAPH = {'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'},
            'G': {'H'},
            'H': {'G'}}


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


print(list(dfs_iterative(GRAPH, 'A')))


def dfs_recursive(graph, start, visited):
    visited.add(start)
    for vertex in graph[start] - visited:
        dfs_recursive(graph, vertex, visited)
    return visited


print(list(dfs_recursive(GRAPH, 'A', visited=set())))


def topSort(graph):
    def _topSort(graph, vertex, marker, topStack):
        marker[vertex] = 1
        for nbr in graph[vertex]:
            if marker[nbr] == 1:
                raise Exception('Graph is cyclic, topological sort not possible!')
            if marker[nbr] == 0:
                _topSort(graph, nbr, marker, topStack)
        marker[vertex] = 2
        topStack.append(vertex)

    marker = dict.fromkeys(graph, 0)
    topStack = []
    for v in graph.keys():
        if marker[v] == 0:
            try:
                _topSort(graph, v, marker, topStack)
            except Exception as e:
                return e
    return list(reversed(topStack))


print(topSort(GRAPH))
print(topSort(DAG))


def connComps(graph):
    def _dfs(graph, vertex, visited):
        visited[vertex] = True
        for nbr in graph[vertex]:
            if not visited[nbr]:
                _dfs(graph, nbr, visited)

    visited = dict.fromkeys(graph, False)
    comps = 0
    for v in graph.keys():
        if not visited[v]:
            comps += 1
            _dfs(graph, v, visited)
    return comps


print(connComps(DISGRAPH))


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


print(list(bfs(GRAPH, 'A')))


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        for nbr in graph[vertex] - set(path):
            if nbr == goal:
                return path + [nbr]
            else:
                stack.append((nbr, path + [nbr]))


print(dfs_paths(GRAPH, 'A', 'F'))


def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        vertex, path = queue.popleft()
        for nbr in graph[vertex] - set(path):
            if nbr == goal:
                return path + [nbr]
            else:
                queue.append((nbr, path + [nbr]))


print(bfs_paths(GRAPH, 'A', 'F'))


def bfs_paths_cyclic(graph, start, goal):
    """Extremely fast compared to upper variant in case of big dense cyclic graphs"""
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        vertex, path = queue.popleft()
        for nbr in graph[vertex] - visited:
            visited.add(nbr)
            if nbr == goal:
                return path + [nbr]
            else:
                queue.append((nbr, path + [nbr]))


print(bfs_paths_cyclic(GRAPH, 'A', 'F'))
