import sys

input = sys.stdin.readline

# 북, 동, 남, 서 => 4방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 맵의 크기
n, m = map(int, input().split())

# 로봇의 x, y 위치 와 바라 보고 있는 방향
r_x, r_y, d = map(int, input().split())

# 맵!!
maps = [list(map(int, input().split())) for _ in range(n)]

# 문제에서 지문이 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다. 주어졌다.
# 즉 다시 말하면 로봇의 위치 와 방향이 주어지는데 로봇이 주어지는 곳까지 벽 일순 없단 말로도 해석이 가능하다.
# 즉 무조건 답은 1이상 이라는 것!! 그러므로 cnt = 1 로 시작한다.
cnt = 1
# 0인 곳을 청소했다면 즉! 방문했다면 2로 방문처리해준다.
maps[r_x][r_y] = 2

while True:
    # 처음 방문한 칸이 있는지 없는지 판별 하기 위한 플래그
    check = False

    # 4방향! 이므로
    for _ in range(4):
        # 방향을 좌측으로 돌리는 방식이다. 한 가지 더있다면 d = (d + 3) % 4 로도 가능하다.
        d = (d - 1) % 4

        # 로봇이 바라보는 방향 기준으로 다음 칸의 좌표 값 구하기
        nx = r_x + dx[d]
        ny = r_y + dy[d]

        # 범위를 벗어 나지 않고 방문하지 않았던 곳이라면
        if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny]:
            # 청소를 한칸 +1
            cnt += 1
            # 방문 처리
            maps[nx][ny] = 2

            # 다음 칸 기준으로 로봇의 x, y 값 바꿔주기
            r_x, r_y = nx, ny

            # 방문 했던 칸이 존재 하므로 플래그 수정
            check = True

            # r_x, r_y의 값을 바꿧기 때문에 그 로봇의 위치 값 기준으로 다시 시뮬레이션 실시
            break

    # 방문하지 않았던 칸이 있다면!
    if not check:

        # 후진!!
        nx = r_x - dx[d]
        ny = r_y - dy[d]

        # 만약 후진 한곳이 청소를 했던 곳이라면
        if not maps[nx][ny] % 2:
            # 후진한 로봇의 x, y 값 기준으로 시뮬레이션 다시 시작
            r_x, r_y = nx, ny
        # 후진 한곳이 벽이라면
        elif not maps[nx][ny] - 1:
            # 지금 까지 청소 했던 곳 출력
            print(cnt)
            # 종료
            break