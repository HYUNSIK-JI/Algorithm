import sys; input = sys.stdin.readline
from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(sx, sy, score, arr):
    global result
    score += arr[sx][sy][0]
    result = max(result, score)
    arr[sx][sy][0] = 0

    fish_moving(sx, sy, arr)
    shark_moving(sx, sy, score, arr)


def fish_moving(sx, sy, arr):
    for fish_value in range(1, 17):
        fx, fy = -1, -1

        for x in range(4):
            for y in range(4):
                if fish_value == arr[x][y][0]:
                    fx, fy = x, y
                    break
        if fx == -1 and fy == -1:
            continue
        # 물고기 방향
        f_d = arr[fx][fy][1]

        for i in range(8):
            nd = (f_d + i) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            arr[fx][fy][1] = nd
            arr[fx][fy], arr[nx][ny] = arr[nx][ny], arr[fx][fy]
            break

def shark_moving(sx, sy, score, arr):
    s_d = arr[sx][sy][1]

    for i in range(1, 4):
        nx = sx + dx[s_d] * i
        ny = sy + dy[s_d] * i

        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny][0] != 0:
            dfs(nx, ny, score, deepcopy(arr))

arr = []
result = 0

# 입력
for i in range(4):
    fish_info = list(map(int, input().split()))
    fish = []
    # 물고기 번호, 방향
    for j in range(4):
        fish.append([fish_info[j * 2], fish_info[j * 2 + 1] - 1])
    arr.append(fish)

dfs(0, 0, 0, arr)
print(result)