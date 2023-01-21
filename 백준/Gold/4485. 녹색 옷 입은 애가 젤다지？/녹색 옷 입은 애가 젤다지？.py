import sys
from heapq import heappush, heappop

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijstra(cnt):
    queue = []
    heappush(queue, (maps[0][0], 0, 0))
    dis[0][0] = 0

    while queue:
        c, x, y = heappop(queue)

        if x == n - 1 and y == n - 1:
            print(f"Problem {cnt}: {c}")
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                nc = maps[nx][ny] + c

                if nc < dis[nx][ny]:
                    dis[nx][ny] = nc
                    heappush(queue, (nc, nx, ny))
cnt = 1
while True:
    n = int(input())

    if not n:
        break
    maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
    dis = [[int(1e9)] * n for _ in range(n)]
    dijstra(cnt)
    cnt += 1