import sys

input = sys.stdin.readline
INF = int(1e9)

for test_case in range(int(input())):
	n, m, w = map(int, input().split())

	distance = [INF] * (n + 1)
	edges = []

	# 도로 정보
	for _ in range(m):
		a, b, c = map(int, input().split())
		edges.append((a, b, c))
		edges.append((b, a, c))

	# 웜홀 정보
	for _ in range(w):
		a, b, c = map(int, input().split())
		edges.append((a, b, -c))

	distance[1] = 0

	check = False
	for i in range(n):
		for start, end, cost in edges:
			if distance[end] > distance[start] + cost:
				distance[end] = distance[start] + cost

				if i == n - 1:
					check = True
					break
	if not check:
		print("NO")
	else:
		print("YES")