def dfs(start, visit, maps):
    visit[start] = True
    
    for i in maps[start]:
        if not visit[i]:
            dfs(i, visit, maps)
def solution(n, computers):
    ans = 0
    visit = [False] * (n + 1)
    maps = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                maps[i + 1].append(j + 1)
    for i in range(1, n + 1):
        for j in maps[i]:
            if not visit[j]:
                dfs(j, visit, maps)
                ans += 1
    return ans