import sys;

input = sys.stdin.readline;
import heapq

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

distance = [[] for _ in range(n + 1)]
distance[1].append(0)
pq = [[0, 1]]

while pq:
    cost, node = heapq.heappop(pq)

    for nex, weight in graph[node]:
        total = cost + weight
        if len(distance[nex]) < k:
            heapq.heappush(distance[nex], -total)
            heapq.heappush(pq, [total, nex])
        elif total < -distance[nex][0]:
            heapq.heappop(distance[nex])
            heapq.heappush(distance[nex], -total)
            heapq.heappush(pq, [total, nex])

for i in range(1, n + 1):
    if len(distance[i]) < k:
        print(-1)
    else:
        print(-distance[i][0])