import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

# 4방향 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    # 거리 값을 표기 하기 위한 이중 리스트
    v = [[0] * w for _ in range(h)]

    # 처음 도착한 곳은 거리는 0이지만 코드상의 이유로 1로 표기
    v[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어 나지 않고 한번도 방문 하지 않았던 곳이라면
            if 0 <= nx < h and 0 <= ny < w and not v[nx][ny]:
                # 그리고 가구가 아니라면
                if maps[nx][ny] != "x":
                    # 전 칸 기준으로 이동거리 값 표기
                    v[nx][ny] = v[x][y] + 1
                    queue.append((nx, ny))
    return v
while True:
    w, h = map(int, input().split())
    # w, h 둘다 0 이라면 무한 루프 종료
    if not w and not h:
        break
    maps = []
    r_x, r_y = 0, 0 # 로봇의 위치를 받을 x, y
    trash = [] # 더러운 칸을 받을 리스트

    for i in range(h):
        row = list(map(str, input().rstrip()))
        for j in range(w):
            if row[j] == "*":
                trash.append((i, j))
            elif row[j] == "o":
                r_x, r_y = i, j
        maps.append(row)
    r_ftd = [0] * len(trash) # 로봇을 기준으로 첫 번째로 청소 할 더러운 칸 까지의 거리를 담을 리스트
    check = False # 가구에 막혀 갈 수있는지 없는지 판단 할 플래그

    v = bfs(r_x, r_y) # 로봇을 기준으로 bfs을 하여 최솟 값으로 갈수 있는 곳을 표시!!!

    for i, xy in enumerate(trash): # 더러운 칸의 순서 와 위치를 뽑기 위해 enumerate 실행
        k = v[xy[0]][xy[1]] - 1 # 로봇 기준으로 첫번째 더러운 칸들의 거리 값
        if not v[xy[0]][xy[1]]: # 만약 도달 하지 못한다면
            print(-1) # 출력
            check = True # 플래그 수정
            break
        r_ftd[i] += k # 거리 값 더해주기
    # 만약 도달 할수 있는 곳이라면
    if not check:
        # 각 더러운 칸 들 끼리 거리 값을 나타 내기 위한 이중 리스트
        dists = [[0] * len(trash) for _ in range(len(trash))]

        # 각 더러운 칸들 끼리 거리 값을 나타 내기 위한 이중문
        for i in range(len(trash) - 1):
            # 거리 값을 표시 하기 위한 bfs 실시
            v = bfs(trash[i][0], trash[i][1])

            # ex) 첫 번째 더러운 칸을 기준으로 두번째, 세번째 ... n번째 칸 마다 거리 값을 표기
            for j in range(i + 1, len(trash)):
                dists[i][j] = v[trash[j][0]][trash[j][1]] - 1
                dists[j][i] = dists[i][j]
        # 최솟값 비교를 위함
        ans = int(1e9)

        # 순열로 모든 경우의 수 뽑아 내기
        for k in permutations(range(len(dists))):
            # 로봇 기준으로 첫번째 더러운 칸은 아까 저장했던 (각각의 첫번째 더러운 칸 거리)값으로 시작
            t = r_ftd[k[0]]

            # 시작도 여기!!
            start = k[0]

            for i in range(1, len(k)):
                # 도착지점두 다음 지점이다.
                end = k[i]
                # 거리 값을 더해주고
                t += dists[start][end]
                # 시작 지점을 도착지점으로 변경
                start = end
            # 최솟값 비교
            ans = min(ans, t)
        # 출력력
        print(ans)