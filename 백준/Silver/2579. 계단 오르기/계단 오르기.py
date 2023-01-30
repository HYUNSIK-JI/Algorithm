import sys

input = sys.stdin.readline

stair = [0] * 301
dp = [0] * 301

n = int(input())
for i in range(n):
    stair[i] = int(input())


dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n + 1):
    # 0 1 3, 0 2 3
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])
print(dp[n - 1])