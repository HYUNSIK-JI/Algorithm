import sys

sys.setrecursionlimit(10 ** 8)

dx = [0, 1]
dy = [1, 0]

def dfs(x, y, dp, m, n, maps):
    if x == n - 1 and y == m - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    ways = 0
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny]:
                ways += dfs(nx, ny, dp, m, n, maps)
    dp[x][y] = ways
    return dp[x][y] % 1000000007
def solution(m, n, puddles):
    maps = [[1] * m for _ in range(n)]
    
    for x, y in puddles:
        maps[y - 1][x - 1] = 0
    dp = [[-1] * m for _ in range(n)]
    return(dfs(0, 0, dp, m, n, maps))
    