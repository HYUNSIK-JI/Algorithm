import sys
from collections import deque

# bfs 간단
# 단, 그룹화를 통해서 시간 단축를 해야하는 문제


input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    result = 1
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        ans[x][y] = group
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visit[nx][ny]:
                continue
            if arr[nx][ny] == 1:
                continue
            visit[nx][ny] = True
            queue.append((nx, ny))
            result += 1
    return result
n, m = map(int, input().split())

arr = []
visit = []
ans = []
group = 1
info = {0: 0}

for x in range(n):
    temp1 = list(map(int, input().rstrip()))
    temp2 = [False] * m
    temp3 = [0]  * m

    arr.append(temp1)
    visit.append(temp2)
    ans.append(temp3)

for x in range(n):
    for y in range(m):
        if not arr[x][y] and not visit[x][y]:
            visit[x][y] = True
            k = bfs(x, y)
            info[group] = k
            group += 1

for x in range(n):
    for y in range(m):
        kk = set()

        if arr[x][y]:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                kk.add(ans[nx][ny])
                        
            for _k in kk:
                arr[x][y] += info[_k]
                arr[x][y] %= 10
        
for temp in arr:
    print("".join(map(str, temp)))