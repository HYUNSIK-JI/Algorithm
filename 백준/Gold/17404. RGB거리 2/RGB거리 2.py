import sys

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
ans = INF
for i in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][i] = maps[0][i]

    for j in range(1, n):
        dp[j][0] = maps[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = maps[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = maps[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)