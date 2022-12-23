import sys

input = sys.stdin.readline

n, t = map(int, input().split())
score = []
dp = [[0] * (t + 1) for _ in range(n + 1)]

for _ in range(n):
	a, b = map(int, input().split())
	score.append((a, b))

for i in range(1, n + 1):
	for j in range(1, t + 1):
		time = score[i - 1][0]
		num = score[i - 1][1]

		if j < time:
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i][j] = max(num + dp[i - 1][j - time], dp[i - 1][j])
print(dp[n][t])