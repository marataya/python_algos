from dfs import DepthFirstTraversal

class Graph:
    def __init__(self):
        self.edges = {}

    def addVertex(self, v):
        if v not in self.edges:
            self.edges[v] = []

    def addEdge(self, from_v, to_v):
        if from_v not in self.edges:
            self.edges[from_v] = []
        if to_v not in self.edges:
            self.edges[to_v] = []

        if to_v not in self.edges[from_v]:
            self.edges[from_v].append(to_v)
        if from_v not in self.edges[to_v]:
            self.edges[to_v].append(from_v)

    def isEdge(self, from_v, to_v):
        """Determines whether edge exists"""
        if to_v not in self.edges:
            return False
        if from_v not in self.edges:
            return False

        return to_v in self.edges[from_v]


def loadGraph(edges):
    """Create a graph instance"""
    g = Graph()
    for v in edges:
        g.addVertex(v)
        for neighbor in edges[v]:
            g.addEdge(v, neighbor)
    return g

if __name__ == '__main__':
    simpleGraph = {
        1: [2, 3, 5],
        2: [1, 4],
        3: [1],
        4: [2, 5],
        5: [1, 4]
    }
    g = Graph()
    g.addVertex(2)
    g.addVertex(3)
    print(g.isEdge(2, 3))
    g.addEdge(2, 3)
    print(g.isEdge(2, 3))
    print(g.isEdge(3, 2))
    g.addEdge(2, 5)
    print(g.isEdge(5, 2))

    g1 = loadGraph(simpleGraph)
    print(g1.isEdge(2,1))
    dfs = DepthFirstTraversal(g1, 3)
    print(dfs.solution(1))
    print(dfs.solution(5))

    g2 = Graph()
    g2.addEdge(1, 2)
    g2.addEdge(4, 5)
    dfs = DepthFirstTraversal(g2, 1)
    print(dfs.solution(2))
    print(dfs.solution(4)) # not possible disconnected
