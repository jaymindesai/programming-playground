def alienOrder(words):
    def _findEdge(before, after):
        if not before or not after:
            return None, None
        elif before[0] != after[0]:
            return before[0], after[0]
        else:
            return _findEdge(before[1:], after[1:])

    def _populateGraph(graph, words):
        for i in range(1, len(words)):
            frm, to = _findEdge(words[i - 1], words[i])
            if frm and to:
                graph[frm].add(to)

    def _dfsTopSort(graph, vertex, color, order):
        color[vertex] = 1
        for nbr in graph[vertex]:
            if color[nbr] == 1:
                raise Exception
            if not color[nbr]:
                _dfsTopSort(graph, nbr, color, order)
        color[vertex] = 2
        order.append(vertex)

    graph, color = {}, {}
    for word in words:
        for v in word:
            graph[v], color[v] = set(), None

    _populateGraph(graph, words)
    order = []

    for v in color:
        if not color[v]:
            try:
                _dfsTopSort(graph, v, color, order)
            except:
                return ''

    return ' '.join(list(reversed(order)))


print(alienOrder(["wrt","wrf","er","ett","rftt"]))
