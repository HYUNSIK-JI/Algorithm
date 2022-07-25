import sys
from collections import deque

# 입력 시간을 줄이기 위함
input = sys.stdin.readline

#4방향 탐색을 위한 도구
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y ,start_cnt):
    queue = deque()
    queue.append((start_x, start_y, start_cnt))

    # 마네킹 에서 거리가 k이하인 곳들 미리 방문배열 처리
    while mannequin_position:
        mx, my , dis = mannequin_position.popleft()
        visit[mx][my] = True

        for i in range(4):
            mn_x = mx + dx[i]
            mn_y = my + dy[i]

            if 0 <= mn_x < n and 0 <= mn_y < m and not visit[mn_x][mn_y]:
                # 거리가 k이하 인 곳은 다 방문처리
                if dis <= k:
                    visit[mn_x][mn_y] = True
                    mannequin_position.append((mn_x, mn_y , dis + 1))
    while queue:
        x , y , cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 넘어 서지 않고 방문하지 않은곳을 찾기 위한 조건문
            if 0<= nx < n and 0<= ny < m and not visit[nx][ny]:
                # 그곳이 지나갈수 있는 길 인지 판별
                if maps[nx][ny] == 0:
                    # 지나갈수 있는 곳이면 방문처리
                    visit[nx][ny] = True
                    # 큐에 그 위치를 와 체력 소모 + 1 를 넣어 준다.
                    queue.append((nx, ny, cnt + 1))
                # 만약 그곳이 의자 라면
                elif maps[nx][ny] == 2:
                    # 그전 까지 소비 했던 체력 소비에 + 1 값을 리턴
                    return cnt + 1
    return -1

# 세로 길이 ,가로 길이, 마네킹과 떨어져야 하는 거리
n, m ,k = map(int, input().split())

# 맵을 그리기 위한 변수
maps = []

# 시루의 스타트 지점을 알기 위한 변수들
s_x, s_y = 0, 0

# 방문배열
visit = [[False] * m for _ in range(n)]

# 마네킹들의 위치를 알기 위한 리스트
mannequin_position = deque()

# maps을 받는과정
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        # 만약 그곳이 시루가 있는 곳이라면
        if a[j] == 4:
            # 스타트 지점
            s_x, s_y = i, j
        # 그곳이 마네킹 이라면
        elif a[j] == 3:
            # 마네킹리스트에 넣어
            mannequin_position.append((i, j, 1))
    maps.append(a)
print(bfs(s_x, s_y, 0))