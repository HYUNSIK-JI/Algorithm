import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def dfs(x):
	global result
	visit[x] = True
	cycle.append(x)
	k = numbers[x]

	if visit[k]:
		if k in cycle:
			result += 1
		return
	else:
		dfs(k)

for _ in range(int(input())):
	n = int(input())
	numbers = [0] + list(map(int, input().split()))
	visit = [True] + [False] * n
	result = 0

	for i in range(1, n + 1):
		if not visit[i]:
			cycle = []
			dfs(i)
	print(result)