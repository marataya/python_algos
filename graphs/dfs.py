White = 0
Gray = 1
Black = 2

class DepthFirstTraversal:
    def __init__(self, graph, s):
        """Initiate a DFS traversal of graph"""
        self.graph = graph
        self.start = s
        self.color = {}
        self.pred = {}

        for v in graph.edges:
            self.color[v] = White
            self.pred[v] = None

        self.dfs_visit(s)


    def dfs_visit(self, u):
        """Recursive traversal of graph using DFS"""
        self.color[u] = Gray

        for v in self.graph.edges[u]:
            if self.color[v] is White:
                self.pred[v] = u
                self.dfs_visit(v)

        self.color[u] = Black

    def solution(self, v):
        """Recover path from start to this vertex v"""
        if v not in self.graph.edges:
            return None

        if self.pred[v] is None:
            return None

        path = [v]

        while v != self.start:
            v = self.pred[v]
            path.insert(0, v)

        return path
