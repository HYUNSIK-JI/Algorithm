import sys
from collections import deque

input = sys.stdin.readline

# 4방향 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어 나지 않고 전염이 이루어지지 않은 곳이라면
            if 0 <= nx < n and 0 <= ny < n and not maps[nx][ny]:
                # 해당 바이러스 값으로 전염
                maps[nx][ny] = maps[a][b]

                # 지속적으로 전염된 위치 값 추가
                posit.append([maps[a][b], nx, ny])


# 바이러스 위치 를 위한 리스트
posit = []

# 그래프 리스트
maps = []

n, k = map(int, input().split())
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        # 바이러스 라면
        if a[j]:
            # 위치 값 넣어주기
            posit.append([a[j], i, j])
    maps.append(a)
s, x, y = map(int, input().split())

# 바이러스 값 기준으로 낮은 값부터 전염 이기때문에 sort 진행
posit.sort()

# 초 만큼 반복문
for _ in range(s):
    # 추가 되는 바이러스 길이에 맞춰 반복문 진행
    for i in range(len(posit)):

        # 해당 바이러스가 전염이 이루어 진것이 아니라면
        if posit[i][0]:
            # 바이러스 전염 진행
            bfs(posit[i][1], posit[i][2])

            # 전염 이후에는 전염성 제로로 만들기
            posit[i][0] = 0

# 출력문
if maps[x - 1][y - 1]:
    print(maps[x - 1][y - 1])
else:
    print(0)