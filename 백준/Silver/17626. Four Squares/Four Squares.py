import sys

input = sys.stdin.readline

n = int(input())

square = [i * i for i in range(1, 225)]
dp = [0] * 50001

for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])