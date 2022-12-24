import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
bag = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

for a in range(1, n + 1):
    burger, potato = bag[a]
    for b in range(1, m + 1):
        for c in range(1, k + 1):
            if burger <= b and potato <= c:
                dp[a][b][c] = max(dp[a - 1][b][c], dp[a - 1][b - burger][c - potato] + 1)
            else:
                dp[a][b][c] = dp[a - 1][b][c]
print(dp[n][m][k])

# 전형적인 냅색문제이다.
# 하지만 냅색문제의 본질을 알고 있다면 3차원으로 쉽게 풀어 낼수 있는 문제이다.
