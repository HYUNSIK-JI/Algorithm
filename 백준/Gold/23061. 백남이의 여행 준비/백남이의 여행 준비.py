import sys

input = sys.stdin.readline

n, m = map(int, input().split())

thing = []
bag = []
num = 0
answer = 0
for _ in range(n):
    thing.append((list(map(int, input().split()))))
for _ in range(m):
    bag.append(int(input()))

dp = [[0] * (max(bag) + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, max(bag) + 1):
        w = thing[i - 1][0]
        v = thing[i - 1][1]

        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
for i in bag:
    p = dp[n][i] / i
    if answer < p:
        answer = p
        num = bag.index(i)
print(num + 1)