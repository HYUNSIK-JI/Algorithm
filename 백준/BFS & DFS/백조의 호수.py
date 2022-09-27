import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def find_swan(lake, visited, queue):
    next_queue = deque()
    while queue:
        y, x = queue.popleft()
        if y == swan[1][0] and x == swan[1][1]:
            return True, None

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not 0 <= ny < row or not 0 <= nx < column:
                continue
            if visited[ny][nx]:
                continue
            if lake[ny][nx] == 'X':
                next_queue.append((ny, nx))
            else:
                queue.append((ny, nx))
            visited[ny][nx] = True

    return False, next_queue


def melt_ice(water, lake):
    next_water = deque()
    while water:
        y, x = water.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not 0 <= ny < row or not 0 <= nx < column:
                continue
            if lake[ny][nx] == 'X':
                next_water.append((ny, nx))
                lake[ny][nx] = '.'

    return next_water


row, column = map(int, input().split())
lake = []
swan = []
water = deque()

for rr in range(row):
    current_lake_info = list(input().rstrip())
    for cc, vv in enumerate(current_lake_info):
        if vv == '.' or vv == 'L':
            water.append((rr, cc))
        if vv == 'L':
            swan.append((rr, cc))
    lake.append(current_lake_info)

day = -1
visited = [[False for _ in range(column)] for _ in range(row)]
queue = deque()

y, x = swan[0][0], swan[0][1]
queue.append((y, x))
visited[y][x] = True

while True:
    day += 1
    found, next_queue = find_swan(lake, visited, queue)
    if found:
        break
    water = melt_ice(water, lake)
    queue = next_queue

print(day)