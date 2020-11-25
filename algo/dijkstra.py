
import math


class Graph(object):

    class Edge(object):

        def __init__(self, to, cost):
            self.to = to
            self.cost = cost

    def __init__(self, n):
        self.n = n
        self.createEmptyGraph()
        self.edgeCount = 0
        self.dist = []
        self.prev = []

    def createEmptyGraph(self):
        self.graph = [[] for i in range(self.n)]

    def addEdge(self, _from, to, cost):
        self.edgeCount += 1
        self.graph[_from].append(self.Edge(to, cost))

    def dijkstra(self, start, end):
