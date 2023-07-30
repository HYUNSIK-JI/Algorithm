import heapq
import sys
from collections import defaultdict

class ShortestPath:
    def __init__(self):
        self.input = sys.stdin.readline
        self.graph = []
        self.dist = []
        self.x = []
        self.nodes = []
        self.queries = []
        self.answers = []
        self.chk = []
        self.parent = []
        self.pq = []
        self.qq = defaultdict(list)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.chk[a] + self.chk[b] != 2:
            return
        self.parent[a] = b

    def dijkstra(self):
        while self.pq:
            d, now = heapq.heappop(self.pq)
            if self.dist[now] < d:
                continue
            for i in self.graph[now]:
                if self.dist[now] + i[1] < self.dist[i[0]]:
                    self.dist[i[0]] = self.dist[now] + i[1]
                    heapq.heappush(self.pq, (self.dist[i[0]], i[0]))

    def read_input(self):
        n, m, k, q = map(int, self.input().split())
        self.graph = [[] for _ in range(n + 1)]
        self.dist = [1e9] * (n + 1)
        self.x = [-1]
        self.nodes = [[] for _ in range(n + 1)]
        self.queries = [0] * (q + 1)
        self.answers = [0] * (q + 1)
        self.chk = [0] * (n + 1)
        self.parent = list(range(n + 1))

        for _ in range(m):
            a, b, c = map(int, self.input().split())
            self.graph[a].append((b, c))
            self.graph[b].append((a, c))

        for _ in range(k):
            a = int(self.input())
            self.dist[a] = 0
            heapq.heappush(self.pq, (0, a))

        self.dijkstra()

        for i in range(1, n + 1):
            self.x.append(self.dist[i])
        self.x = sorted(list(set(self.x)))
        size = len(self.x)

        for i in range(1, n + 1):
            idx = self.x.index(self.dist[i])
            self.nodes[idx].append(i)

        for i in range(1, q + 1):
            self.queries[i] = list(map(int, self.input().split())) + [0, size]
            mid = (self.queries[i][2] + self.queries[i][3]) // 2
            self.qq[mid].append(i)

        for _ in range(20):
            for i in range(1, n + 1):
                self.parent[i] = i
                self.chk[i] = 0

            for i in range(size - 1, 0, -1):
                for node in self.nodes[i]:
                    self.chk[node] = 1
                    for linked_node, _ in self.graph[node]:
                        self.union(node, linked_node)

                for idx in self.qq[i]:
                    if self.find(self.queries[idx][0]) == self.find(self.queries[idx][1]):
                        self.answers[idx] = max(self.answers[idx], i)
                        self.queries[idx][2] = i + 1
                    else:
                        self.queries[idx][3] = i - 1
                self.qq[i].clear()

            for idx in range(1, q + 1):
                if self.queries[idx][2] <= self.queries[idx][3]:
                    mid = (self.queries[idx][2] + self.queries[idx][3]) // 2
                    self.qq[mid].append(idx)

        for i in range(1, q + 1):
            print(max(self.x[self.answers[i]], 0))

shortestPath = ShortestPath()
shortestPath.read_input()
