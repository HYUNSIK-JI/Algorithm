import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def input():
    return sys.stdin.readline().rstrip()

def within_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def color(data, _type, queue):
    for x, y in data:
        arr[x][y] = _type
        queue.append((x, y))
        ans[_type - 1] += 1

def process_queue(queue):
    result = set()
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not within_bounds(nx, ny, n, m) or arr[nx][ny]:
                continue
            result.add((nx, ny))
    return result

def bfs(queue1, queue2):
    while queue1 or queue2:
        v1 = process_queue(queue1)
        v2 = process_queue(queue2)
        v3 = v1 & v2
        color(v3, 3, [])
        color(v1 - v3, 1, queue1)
        color(v2 - v3, 2, queue2)
    return ans

n, m = map(int, input().split())
queue1 = deque()
queue2 = deque()
arr = []
ans = [1, 1, 0]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            queue1.append((i, j))
        elif temp[j] == 2:
            queue2.append((i, j))
    arr.append(temp)

print(*bfs(queue1, queue2))
