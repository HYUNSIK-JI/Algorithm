import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def openAllDoor():
    for key in keys:
        while doors[key.upper()]:
            x, y = doors[key.upper()].pop()
            maps[x][y] = '.'
            queue.append((x, y))
            visit[x][y] = True

for _ in range(int(input())):
    h, w = map(int, input().split())
    
    maps = [list(input().rstrip()) for _ in range(h)]

    keys = list(input().rstrip())
    
    if keys[0] == '0':
        keys = set()
    else:
        keys = set(keys)

    queue = deque()
    visit = [[False for _ in range(w)] for _ in range(h)]

    doors = {}
    for c in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        doors[c] = []

    answer = 0

    for i in range(h):
        for j in range(w):
            if 0 < i < h - 1 and 0 < j < w - 1:
                continue
            if maps[i][j] == '*':
                continue

            if maps[i][j] == '.':
                queue.append((i, j))
                visit[i][j] = True
            elif maps[i][j] == '$':
                answer += 1
                maps[i][j] = '.'
                queue.append((i, j))
                visit[i][j] = True
            elif 'a' <= maps[i][j] <= 'z':
                keys.add(maps[i][j])
                maps[i][j] = '.'
                queue.append((i, j))
                visit[i][j] = True
            elif 'A' <= maps[i][j] <= 'Z':
                doors[maps[i][j]].append((i, j))

    openAllDoor()

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:

                if maps[nx][ny] == "." and not visit[nx][ny]:
                    queue.append((nx, ny))
                    visit[nx][ny] = True
                elif maps[nx][ny] == "$":
                    answer += 1
                    maps[nx][ny] = '.'
                    queue.append((nx, ny))
                    visit[nx][ny] = True

                elif 'a' <= maps[nx][ny] <= 'z':
                    keys.add(maps[nx][ny])
                    maps[nx][ny] = '.'
                    queue.append((nx, ny))
                    visit[nx][ny] = True

                elif 'A' <= maps[nx][ny] <= 'Z':
                    doors[maps[nx][ny]].append((nx, ny))


        if not queue:
            openAllDoor()

    print(answer)