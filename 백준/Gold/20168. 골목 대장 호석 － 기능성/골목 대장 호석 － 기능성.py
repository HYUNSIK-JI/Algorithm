import sys

input = sys.stdin.readline

def dfs(start, end, money, mx):
    visit[start] = True
    global ans
    if start == end:
        ans = min(ans, mx)
        return

    for i in maps[start]:
        if visit[i[0]] == True:
            continue
        if i[1] > money:
            continue
        visit[i[0]] = True
        dfs(i[0], end, money - i[1], max(mx, i[1]))
        visit[i[0]] = False

n, m, a, b, c = map(int, input().split())

maps = [[] for _ in range(n + 1)]
visit = [[False] for _ in range(n + 1)]
ans = sys.maxsize

for _ in range(m):
    s, e, cost = map(int, input().split())
    maps[s].append((e, cost))
    maps[e].append((s, cost))

dfs(a, b, c, 0)

if ans == sys.maxsize:
    ans = -1
print(ans)