import sys

input = sys.stdin.readline

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

n = int(input())
print(dp[n])