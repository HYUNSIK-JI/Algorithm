import heapq
from collections import deque

def solution(n, roads, sources, destination):
    result = []
    INF = int(1e9)
    visit = [-1] * (n + 1)
    gragh = [[] for _ in range(n + 1)]
    for a, b in roads:
        gragh[a].append(b)
        gragh[b].append(a)

    q = deque()
    q.append(destination)
    visit[destination] = 0

    while q:
        now = q.popleft()

        for node in gragh[now]:
            if visit[node] == -1:
                visit[node] = visit[now] + 1
                q.append(node)

    for i in sources:
        result.append(visit[i])
    return result