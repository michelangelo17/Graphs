"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('Vertex not found')

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('Vertex_id not found')

    def bft(self, starting_vertex):
        todo = Queue()
        todo.enqueue(starting_vertex)
        completed = set()

        while todo.size() > 0:
            cur_vertex = todo.dequeue()

            if cur_vertex not in completed:
                print(cur_vertex)
            completed.add(cur_vertex)

            for v in self.vertices[cur_vertex]:
                if v not in completed:
                    todo.enqueue(v)

    def dft(self, starting_vertex):
        todo = Stack()
        todo.push(starting_vertex)
        completed = set()

        while todo.size() > 0:
            cur_vertex = todo.pop()

            if cur_vertex not in completed:
                print(cur_vertex)
                completed.add(cur_vertex)

            for v in self.vertices[cur_vertex]:
                if v not in completed:
                    todo.push(v)

    def dft_recursive(self, starting_vertex, completed=set()):
        if starting_vertex in completed:
            return

        completed.add(starting_vertex)
        print(starting_vertex)

        for v in self.vertices[starting_vertex]:
            self.dft_recursive(v)

    def bfs(self, starting_vertex, destination_vertex):
        todo = Queue()
        todo.enqueue([starting_vertex])
        completed = set()

        while todo.size() > 0:
            path = todo.dequeue()
            cur_vertex = path[-1]

            if cur_vertex not in completed:
                if path[0] == starting_vertex and cur_vertex == destination_vertex:
                    return path
                completed.add(cur_vertex)

                for v in self.vertices[cur_vertex]:
                    new_path = list(path)
                    new_path.append(v)
                    todo.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        todo = Stack()
        todo.push([starting_vertex])
        completed = set()

        while todo.size() > 0:
            path = todo.pop()
            cur_vertex = path[-1]

            if cur_vertex not in completed:
                if path[0] == starting_vertex and cur_vertex == destination_vertex:
                    return path
                completed.add(cur_vertex)

                for v in self.vertices[cur_vertex]:
                    new_path = list(path)
                    new_path.append(v)
                    todo.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[]):
        result = None

        if len(path) == 0:
            path.append(starting_vertex)

        if path[0] == starting_vertex and path[-1] == destination_vertex:
            return path

        next_vertex = path[-1]

        for v in self.vertices[next_vertex]:
            if v not in path:
                new_path = list(path)
                new_path.append(v)

                found = self.dfs_recursive(
                    starting_vertex, destination_vertex, new_path)

                if not result:
                    result = found
                elif len(result) > len(found):
                    result = found

        return result


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
    # print(graph.vertices)
    # print(graph.get_neighbors(3))

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
