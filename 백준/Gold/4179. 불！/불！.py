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
                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == ".": 
                    maps[nx][ny] = "F"
                    fire.append((nx, ny))
        for j in range(len(start)):
            x, y = start.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c:
                    if maps[nx][ny] == ".":
                        maps[nx][ny] = "J"
                        start.append((nx, ny))
                else:
                    return time
    return "IMPOSSIBLE"
r, c = map(int, input().split())
maps = []

fire = deque()
start = deque()
time = 0
for i in range(r):
    row = list(map(str, input().rstrip()))
    for j in range(c):
        if row[j] == "J":
            start.append((i, j))
        elif row[j] == "F":
            fire.append((i, j))
    maps.append(row)

print(bfs())