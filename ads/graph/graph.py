
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

    def get_vertices(self):
        return self.vertices.keys()

    def __contains__(self, vertex):
        return vertex in self.vertices

    # def __iter__(self):
    #     return iter(self.vertices.values())

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
