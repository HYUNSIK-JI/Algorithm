import sys
from collections import deque

input =  sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((1, 0))
    dis[1][0] = 0
    while queue:
        x, t = queue.popleft()

        if dis[x][x] == -1:
            dis[x][x] = dis[x][t] + 1
            queue.append((x, x))
        if 0 <= x + t <= n and dis[x + t][t] == -1:
            dis[x + t][t] = dis[x][t] + 1
            queue.append((x + t, t))
        if 0 <= x - 1 <= n and dis[x - t][t] == -1:
            dis[x - 1][t] = dis[x][t] + 1
            queue.append((x - 1, t))

n = int(input())
dis = [[-1] * (n + 1) for _ in range(n + 1)]
bfs()
ans = 1e9
for i in dis[n]:
    if not i == -1:
        ans = min(ans, i)
print(ans)