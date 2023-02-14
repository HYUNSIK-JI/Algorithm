import sys

input = sys.stdin.readline
from collections import deque

def BFS(a):
    dis = [0] * (n + 1)
    queue = deque()
    queue.append(a)

    while queue:
        x = queue.popleft()

        for i in maps[x]:
            if not visit[i]:
                visit[i] = True
                dis[i] = dis[x] + 1
                queue.append(i)
    return sum(dis)
n, m = map(int, input().split())

maps = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)
ans = []
for i in range(1, n + 1):
    visit = [False] * (n + 1)
    ans.append(BFS(i))
print(ans.index(min(ans)) + 1)