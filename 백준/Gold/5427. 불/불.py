import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    global time

    while start:
        time += 1
        for j in range(len(fire)):
            x, y = fire.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == ".":
                    maps[nx][ny] = "*"
                    fire.append((nx, ny))
        for j in range(len(start)):
            x, y = start.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < h and 0 <= ny < w:
                    if maps[nx][ny] == ".":
                        maps[nx][ny] = "@"
                        start.append((nx, ny))
                else:
                    return time + 1
    return "IMPOSSIBLE"
for _ in range(int(input())):
    w, h = map(int, input().split())
    time = -1
    maps = []
    fire = deque()
    start = deque()

    for i in range(h):
        row = list(map(str, input().rstrip()))
        for j in range(w):
            if row[j] == "@":
                start.append((i, j))
            elif row[j] == "*":
                fire.append((i, j))
        maps.append(row)
    print(bfs())