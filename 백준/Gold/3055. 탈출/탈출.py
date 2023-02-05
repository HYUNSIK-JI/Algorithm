import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    global time

    while start:
        time += 1
        for j in range(len(water)):
            x, y = water.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c:
                    if maps[nx][ny] == "." or maps[nx][ny] == "S":
                        maps[nx][ny] = "*"
                        water.append((nx, ny))
        for j in range(len(start)):
            x, y = start.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx == e_x and ny == e_y:
                    return time + 1
                if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == ".":
                    maps[nx][ny] = "S"
                    start.append((nx, ny))
    return "KAKTUS"
r, c = map(int, input().split())

water = deque()
start = deque()
e_x, e_y = 0, 0
maps = []
time = -1
for i in range(r):
    row = list(map(str, input().rstrip()))
    for j in range(c):
        if row[j] == "S":
            start.append((i, j))
        elif row[j] == "*":
            water.append((i, j))
        elif row[j] == "D":
            e_x, e_y = i, j
    maps.append(row)

print(bfs())