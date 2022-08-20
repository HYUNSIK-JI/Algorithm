import sys

# 최댓값 설정
INF = int(1e9)

input = sys.stdin.readline

# 지역의 개수, 수색 범위, 길의 개수
n, m, r = map(int, input().split())

# 각 지역별 얻을수 있는 아이템 수
items = list(map(int, input().split()))

# 비용이 무한대인 n * n 그래프 설정
graph = [[INF] * n for _ in range(n)]

# 자기 자신은 비용은 0이므로 0으로 설정
for i in range(n):
	for j in range(n):
		if i == j:
			graph[i][j] = 0

# 양방향 길마다 설정된 비용설정
for _ in range(r):
	a, b, c = map(int, input().split())
	graph[a - 1][b - 1] = c
	graph[b - 1][a - 1] = c

# 플로이드 워셜 알고리즘 핵심 각각의 위치에서 다른 위치로 이동할때 드는 비용들을 최소비용으로 정리
for k in range(n):
	for a in range(n):
		for b in range(n):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 얻을수 있는 최대 아이템 수 비교를 위한 변수
answer = 0
for i in range(n):
	# 수색범위 안에서 얻을수 있는 아이템 수를 측정하기 위한 변수
	check = 0
	for j in range(n):
		# 수색범위 안에있는지 확인
		if graph[i][j] <= m:
			# 수색범위 안에 있는 거라면 아이템수 플러스
			check += items[j]
	# 최댓값 비교
	answer = max(answer, check)
# 최대 아이템수
print(answer)