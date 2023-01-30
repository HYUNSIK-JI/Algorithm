import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if not i or not j:
            dp[i][j] = maps[i][j]
        elif not maps[i][j]:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(answer, dp[i][j])
print(answer ** 2)