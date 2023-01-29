import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]
    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] < maps[x][y]:
                ways += dfs(nx, ny)
    dp[x][y] = ways
    return dp[x][y]

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

dfs(0, 0)
print(dp[0][0])