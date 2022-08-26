from collections import defaultdict
from operator import ne


class Graph:

    def __init__(self) -> None:
        
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    
    def BFS(self, s):

        visited = []
        queue = []

        visited.append(s)
        queue.append(s)

        while queue:

            s = queue.pop(0)
            print(s, end = " ")

            for neighbor in self.graph[s]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)
