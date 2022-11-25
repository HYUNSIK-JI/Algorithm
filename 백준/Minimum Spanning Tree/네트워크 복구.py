import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node, cost in graph[now]:
            c = dist + cost

            if distance[node] > c:
                parent[node] = now
                distance[node] = c
                heapq.heappush(q, (c, node))
n, m = map(int, input().split())

distance = [INF] * (n + 1)
parent = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijstra(1)
print(n - 1)
for i in range(2, n + 1):
    print(i, parent[i])