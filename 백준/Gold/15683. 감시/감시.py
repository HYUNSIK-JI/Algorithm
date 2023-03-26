import copy, sys

input = sys.stdin.readline

def start(maps2, dir, x, y):
    for i in dir:
        nx = x
        ny = y

        while True:
            nx += dx[i]
            ny += dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                break
            if maps2[nx][ny] == 6:
                break
            elif not maps2[nx][ny]:
                maps2[nx][ny] = -1

def dfs(v, maps):
    global ans
    if v == len(cctv):
        count = 0
        for i in range(n):
            count += maps[i].count(0)
        ans = min(ans, count)
        return
    maps2 = copy.deepcopy(maps)
    cctv_n, x, y = cctv[v]

    for i in dir[cctv_n]:
        start(maps2, i, x, y)
        dfs(v + 1, maps2)
        maps2 = copy.deepcopy(maps)

dir = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [0, 3]], [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], [[0, 1, 2, 3]]]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
cctv = []
maps = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] in [1, 2, 3, 4, 5]:
            cctv.append((row[j], i, j))
    maps.append(row)
ans = 1e9
dfs(0, maps)
print(ans)