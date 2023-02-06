import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 1]
dy = [1, -1]
def b_search(visit):
    global b_cnt
    visit2 = list(map(list, zip(*visit)))
    for i in range(5):
        b_cnt += "".join(visit[i]).split("F").count("T" * 5)
        b_cnt += "".join(visit2[i]).split("F").count("T" * 5)
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(1):
            nx = x + dx[i]
            ny = y + dy[i]
            if visit[x][y] == "T":
                count = 1
                while 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == "T":
                    count += 1

                    if count == 5:
                        b_cnt += 1
                        break
                    nx += dx[i]
                    ny += dy[i]
            else:
                break
    queue.append((0, 4))
    while queue:
        x, y = queue.popleft()
        for i in range(1, 2):
            nx = x + dx[i]
            ny = y + dy[i]
            if visit[x][y] == "T":
                count = 1
                while 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == "T":
                    count += 1
                    if count == 5:
                        b_cnt += 1
                        break
                    nx += dx[i]
                    ny += dy[i]
            else:
                break


def search(target, maps):
    for i in range(5):
        if maps[i] == target:
            return i
    return -1


visit = [["F"] * 5 for _ in range(5)]

maps = [list(map(int, input().split())) for _ in range(5)]
answer = [list(map(int, input().split())) for _ in range(5)]


cnt = 0
b_cnt = 0
check = False
for i in range(5):
    for j in range(5):
        cnt += 1
        target = answer[i][j]
        for p in range(5):
            k = search(target, maps[p])
            if k >= 0:
                visit[p][k] = "T"
        b_search(visit)

        if b_cnt >= 3:
            check = True
            break
        else:
            b_cnt = 0
    if check:
        break
print(cnt)