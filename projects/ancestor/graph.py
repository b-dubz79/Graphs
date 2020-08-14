"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create empty queue
        q = Queue()
        q.enqueue(starting_vertex)
        # create set to store visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            v = q.dequeue()
            # if vertex isn't in visited set
            if v not in visited:
                # add vertex to vistied set
                visited.add(v)
                print(v)
                # add all neighbors to the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)

                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue PATH to starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first PATH
            p = q.dequeue()
            # grab last vertex from the path
            v = p[-1]
            # check if the vertex has not been visited
            if v not in visited:
                # is this vertex the target?
                if v == destination_vertex:
                    # if is, return the path
                    return p
                # if it isn't, mark it as visited
                visited.add(v)
                # then add a path to its neighbors to the back of the queue
                for neighbors in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = list(p)
                    # append the neighbor to the back of the path
                    path_copy.append(neighbors)
                    # enqueue out the new path
                    q.enqueue(path_copy)
        return None
                        
                    
                
        

                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push PATH to starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue is not empty
        while s.size() > 0:
            # dequeue the first PATH
            p = s.pop()
            # grab last vertex from the path
            v = p[-1]
            # check if the vertex has not been visited
            if v not in visited:
                # is this vertex the target?
                if v == destination_vertex:
                    # if is, return the path
                    return p
                # if it isn't, mark it as visited
                visited.add(v)
                # then add a path to its neighbors to the back of the queue
                for neighbors in self.get_neighbors(v):
                    path_copy = list(p)
                    # make a copy of the path
                    # append the neighbor to the back of the path
                    path_copy.append(neighbors)
                    # enqueue out the new path
                    s.push(path_copy)
        return None
                
                
                        
        


    def dfs_recursive(self, vertex, destination, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = []
        # visited.add(starting_vertex)
        # path = path + [starting_vertex]
        # if starting_vertex == destination_vertex:
        #     return path
        # for neighbor in self.get_neighbors(starting_vertex):
        #     if neighbor not in path:
        #         new_path = self.dfs_recursive(neighbor, destination_vertex, path)
        #         if new_path:
        #             return new_path
        path = path + [vertex]                                        # path will whatever path currently is + [vertex] (note that first pass will be just that first vertex)
        if vertex == destination:                                     # base case - if our vertex is our destination, return path at that point
            return path                                               
        neighbors = self.get_neighbors(vertex)                        # if our vertex is not what we are looking for, get the neighbors of that vertex...
        for neighbor in neighbors:                                    # for every neighbor in neighbors...
            if neighbor not in path:                                  # if that neighbor is not in our path
                path_copy = self.dfs_recursive(neighbor,destination, path) # create a copy and it'll equal the next recursion of the function, only this time we pass the neighbor, destination, and current state of our path
                if path_copy:                                              # return path_copy if we have one
                    return path_copy
        
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
