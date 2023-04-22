import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
cnt = 1

def dfs(k):
    global cnt
    if not visit[k]:
        answer[k] = cnt
        visit[k] = True

    for i in graph[k]:
        if not visit[i]:
            cnt += 1
            dfs(i)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0] * (n + 1)

for i in range(1, n + 1):
    graph[i].sort()
dfs(r)

for i in range(1, n + 1):
    print(answer[i])