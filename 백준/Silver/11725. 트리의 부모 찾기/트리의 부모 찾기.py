import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(start):
    visit[start] = True

    for i in maps[start]:
        if not visit[i]:
            ans[i] = start
            dfs(i)

n = int(input())

maps = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
ans = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

dfs(1)
for i in range(2, n + 1):
    print(ans[i])