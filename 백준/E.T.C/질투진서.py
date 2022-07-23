import sys
from collections import deque

input = sys.stdin.readline

# 행,열 다 탐색 하기 위한 도구
dx = [0, 0, 1, -1]
dy = [1, -1 ,0 ,0]

def check(x, y):
    queue = deque()
    queue.append((x,y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 맵의 범위를 벗어나지 않는 행,열 다 탐색하기 위한 while문
        while 0<= nx < n and 0<= ny< n:
            # 만약 진서 본인보다 높은 매력지수를 발견하면 함수 종료
            if maps[nx][ny] > me:
                return "ANGRY"
            #진서 본인 보다 낮은 매력지수 면 더 깊게 탐색
            nx += dx[i]
            ny += dy[i]
    # 진서 본인보다 매력지수가 다 낮으면 리턴 happy
    return "HAPPY"

# 맵의 크기 와 진서의 위치
n, a, b = map(int, input().split())

# 지도 만들기
maps = [list(map(int ,input().split())) for _ in range(n)]

# 진서 본인의 매력 지수
me = maps[a-1][b-1]

#본인이 있던 행,열 다 확인 하기 위한 함수
print(check(a-1,b-1))