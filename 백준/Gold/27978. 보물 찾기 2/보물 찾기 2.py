import sys
from collections import deque

INF = int(1e9)
input = sys.stdin.readline

dy = [-1, 0, 1, 1, 1, 0, -1, -1]
dx = [1, 1, 1, 0, -1, -1, -1, 0]

def bfs():
    while queue:
        nowpos, nowcost = queue.popleft()
        y, x = nowpos

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] != -1:
                if i in (0, 1, 2):
                    nextcost = nowcost
                else:
                    nextcost = nowcost + 1

                if visit[ny][nx] > nextcost:
                    visit[ny][nx] = nextcost
                    if nextcost == nowcost:
                        queue.appendleft(((ny, nx), nextcost))
                    else:
                        queue.append(((ny, nx), nextcost))
h, w = map(int, input().split())
maps = [[0] * w for _ in range(h)]
start = (0, 0)
end = (0, 0)

for i in range(h):
    row = input().strip()
    for j in range(w):
        if row[j] == '#':
            maps[i][j] = -1
        elif row[j] == '*':
            end = (i, j)
        elif row[j] == 'K':
            start = (i, j)

visit = [[INF] * w for _ in range(h)]

queue = deque()
queue.append((start, 0))
visit[start[0]][start[1]] = 0


bfs()
if visit[end[0]][end[1]] == INF:
    print("-1")
else:
    print(visit[end[0]][end[1]])
