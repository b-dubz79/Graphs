class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
def earliest_ancestor(ancestors, starting_node):
    # create graph
    g = Graph()
    # loop through ancestors and add vertices/edges
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        g.add_edge(pair[1], pair[0])
    q = Queue()
    q.enqueue([starting_node])
    max_path_length = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        print('path', path)
        v = path[-1]
        if (len(path) >= max_path_length and v < earliest_ancestor):  
            earliest_ancestor = v 
        if (len(path) > max_path_length):
            max_path_length = len(path)
            earliest_ancestor = v 
        for neighbor in g.get_neighbors(v):
            print('g vert', g.get_neighbors(v))
            path_copy = list(path)
            print(('path copy', path_copy))
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    print('early anc', earliest_ancestor)
    print('g get neig', g.get_neighbors(8))
    return earliest_ancestor





# earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 9)
    # if parents exist, use bft to get to leaf
    # if multiple leaves, return lowest value
    