class Graph(object):
    class AdjNode(object):
        def __init__(self, src, des, cost=1):
            self.source = src
            self.destination = des
            self.cost = cost

            self.next = None

    class AdjList(object):
        def __init__(self):
            self.head = None

    def __init__(self, cnt):
        self.count = cnt
        self.list = [None] * cnt

        i = 0

        while i < cnt:
            self.list[i] = self.AdjList()
            self.list[i].head = None

            i += 1

    def AddEdge(self, source, destination, cost):
        node = self.AdjNode(source, destination, cost)
        node.next = self.list[source].head
        self.list[source].head = node

    def AddBiEdge(self, source, destination, cost):
        self.AddEdge(source, destination, cost)
        self.AddEdge(destination, source, cost)

    def Print(self):
        ad = None
        i = 0
        while i < self.count:
            ad = self.list[i].head

            if ad != None:
                print "Vertex ", i, " is connected to: ",
                while ad != None:
                    print ad.destination,
                    ad = ad.next
                print("")

            i += 1

    def DFSStack(self, graph):
        count = self.count
        visited = [0] * count
        stk = []

        visited[0] = 1
        stk.append(graph.list[0])
        while len(stk) != 0:
            curr = stk.pop()
            print curr
            head = graph.list[curr].head
            while head != None:
                if visited[head.destination] == 0:
                    visited[head.destination] = 1
                    stk.append(head.destination)
                head = head.next
        return stk

    @classmethod
    def PathExist(cls, graph, source, dest):
        count = graph.count
        visited = [0] * count
        visited[source] = 1
        cls.DFSRec(graph)
        return visited[dest]


if __name__ == "__main__":
    gph = Graph(9)
    gph.AddBiEdge(0, 2, 1)
    gph.AddBiEdge(1, 2, 5)
    gph.AddBiEdge(1, 3, 7)
    gph.AddBiEdge(1, 4, 9)
    gph.AddBiEdge(3, 2, 2)
    gph.AddBiEdge(3, 5, 4)
    gph.AddBiEdge(4, 5, 6)
    gph.AddBiEdge(4, 6, 3)
    gph.AddBiEdge(5, 7, 1)
    gph.AddBiEdge(6, 7, 7)
    gph.AddBiEdge(7, 8, 17)
    gph.Print()
