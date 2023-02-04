import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

check = [False] * (n + 1)

dp = [0] * 41
for i in range(m):
    check[int(input())] = True

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

cnt = 0
ans = 1
for i in range(1, n + 1):
    if not check[i]:
        cnt += 1
    else:
        if cnt:
            ans *= dp[cnt]
        cnt = 0
if cnt:
    ans *= dp[cnt]
print(ans)
