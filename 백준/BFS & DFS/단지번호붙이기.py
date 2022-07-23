import sys
from collections import deque
#입력 시간을 줄이기 위함
input = sys.stdin.readline

# 4방향 탐색
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a, b):
	queue = deque()
	queue.append((a,b))

	visit[a][b] = True
	# 단지 내 집의 수를 세기 위한 변수 1로 초기화 하는 이유는 bfs함수 내로 들어온 곳도 집의 일부 이기때문이다.
	cnt = 1

	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 지도의 크기을 벗어나지 않고 집의 수를 세기 위한 조건문
			if 0 <= nx < n and 0<= ny <n:
				# 그곳이 방문 하지 않았고 집이라면
				if not visit[nx][ny] and maps[nx][ny] == "1":
					#방문 처리
					visit[nx][ny] = True
					#집의 수 증가
					cnt += 1
					queue.append((nx, ny))
	#단지 내 집의 수로 리턴
	return cnt
#지도의 크기
n = int(input())

#지도
maps = [list(input().rstrip()) for _ in range(n)]

#방문여부를 체크하는 리스트
visit = [[False] * n for _ in range(n)]

#단지 내 집의 수를 넣기 위한 리스트
village_count = []

for i in range(n):
	for j in range(n):
		if maps[i][j] == "1" and not visit[i][j]:
			#한 단지에 내 집의 개수를 village_count 리스트에 넣어주기
			village_count.append(bfs(i,j))

#단지 내 집의 수를 나타내주는 리스트의 길이가 단지의 개수.
print(len(village_count))
#오름차순으로 보여주기 위해 정렬
village_count.sort()

for ans in village_count:
	print(ans)