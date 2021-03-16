class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])


    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        sum_txt = 0
        for u, v, weight in result:
            sum_txt += weight
            print("%d  %d  %d" % (u, v, weight))
        print(f"Weight รวมรวามของ Minimun spanning tree คือ  {sum_txt}")

vNumber = int(input('โปรดระบุจำนวน Vertex ในกราฟ : '))
g = Graph(vNumber)


i = int(input('โปรดระบุจำนวนเส้นเชื่อม (Edge) ในกราฟ: '))
print('โปรดระบุเส้นเชื่อม (Edge) ในกราฟ: ')


while i > 0:
    print('='*60)

    source = int(input('Source : '))
    destination = int(input('Destination : '))
    weight = int(input('weight : '))
    g.add_edge(source,destination,weight)
    i -= 1

print('='*60)

g.kruskal_algo()

