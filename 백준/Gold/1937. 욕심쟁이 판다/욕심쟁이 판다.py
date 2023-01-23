import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] > maps[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny))
    return dp[x][y] + 1
n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)