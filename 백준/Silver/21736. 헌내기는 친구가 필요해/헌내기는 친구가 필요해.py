import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(s, e):
    global result  # 함수 내부에서 result 변수 사용을 허용
    queue = deque()
    queue.append((s, e))
    is_moving[s][e] = 1
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인덱스 범위 검사 수정
            if nx >= N or nx < 0 or ny < 0 or ny >= M:
                continue

            if is_moving[nx][ny]:
                continue
            
            # 이동할 수 없는 곳인 경우
            if arrs[nx][ny] == 'X':
                continue
            
            # 이동 가능한 곳
            is_moving[nx][ny] = 1
            
            # 사람이 있는 경우 result 증가
            if arrs[nx][ny] == 'P':
                result += 1
            
            queue.append((nx, ny))

N, M = map(int, input().split())
is_moving = [[False] * M for _ in range(N)]  # 방문 여부 체크

arrs = []  # 맵 입력

s, e = 0, 0
found_start = False

# 맵 정보 입력
for i in range(N):
    arr = list(input().strip())
    arrs.append(arr)
    if not found_start:
        for k, v in enumerate(arr):
            if v == "I":  # 시작점 'I' 찾기
                s, e = i, k
                found_start = True
                break

result = 0

# bfs 탐색 시작
bfs(s, e)

# 결과 출력
if result == 0:
    print("TT")
else:
    print(result)
