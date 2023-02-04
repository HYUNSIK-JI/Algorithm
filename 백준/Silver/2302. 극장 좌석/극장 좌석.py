import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1

if m:
    previous = 0
    for i in range(m):
        ans *= dp[vip[i] - 1 - previous]
        previous = vip[i]
    ans *= dp[n - previous]
    print(ans)
else:
    print(dp[n])