import sys
from collections import deque

input = sys.stdin.readline

def topological_sort():
    queue = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = costs[i]
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + costs[i])
            if indegree[i] == 0:
                queue.append(i)
    print(dp[victory])
for test_case in range(int(input())):
    v, e = map(int, input().split())

    costs = [0] + list(map(int, input().split()))
    indegree = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    dp = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    victory = int(input())
    topological_sort()