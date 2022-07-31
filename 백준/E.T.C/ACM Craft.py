import sys
from collections import deque

def topology_sort():
	result = []
	queue = deque()

	for i in range(1, v + 1):
		if indegree[i]  == 0:
			# 진입 차수가 0 인 곳에 대한 들어간 비용 처리
			dp[i] = costs [i]
			queue.append(i)
	while queue:
		now = queue.popleft()

		# 각 진입차수 마다 연결 된 건물들
		for i in graph[now]:
			# 진입 차수 -1
			indegree[i] -= 1
			# 각 진입 차수 마다 들어갈 최소 비용
			dp[i] = max(dp[i], dp[now] + costs[i])
			if indegree[i]  == 0:
				queue.append(i)
	# 승리 하기 위한 건물에 들어간 비용 출력
	print(dp[victory])
for test_case in range(int(input())):
	# 건물의 개수 와 건물간 건설 순서 규칙 개수
	v, e = map(int, input().split())
	# 진입차수
	indegree = [0] * (v + 1)
	# 간선
	graph = [[] for _ in range(v + 1)]
	# 각 건물 건설 비용
	costs = [0] + list(map(int, input().split()))

	# 각 진입차수 마다 들어갈 건설비용을 메모제이션을 위한 리스트
	dp = [0] * (v + 1) 
	for _ in range(e):
		a, b = map(int, input().split())
		# a -> b로 간선을 연결의 의미
		graph[a].append(b)

		# 진입차수 +1
		indegree[b] += 1
	# 이 건물이 지어 지면 이김
	victory = int(input())
	# 위상정렬
	topology_sort()