import sys

input = sys.stdin.readline

def dfs(start):
    visit[start] = True

    for i in maps[start]:
        if not visit[i]:
            visit[i] = True
            dfs(i)

for _ in range(int(input())):
    n, m = map(int, input().split())

    maps = [[] for _ in range(n + 1)]


    for _ in range(m):
        a, b = map(int, input().split())
        maps[a].append(b)
        maps[b].append(a)
    ans = 0
    for i in range(1, n + 1):
        visit = [False] * (n + 1)
        dfs(i)
        ans += 1
    print(ans - 1)