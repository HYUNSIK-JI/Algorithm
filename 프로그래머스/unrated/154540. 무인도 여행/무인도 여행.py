from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(n, m, a, b, maps, visit, hap):
    queue = deque()
    queue.append((a, b))
    visit[a][b] = 1
    hap += int(maps[a][b])
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if not maps[nx][ny] == "X":
                    hap += int(maps[nx][ny])
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
    return hap
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visit = [[0] * m for _ in range(n)]
    
    ans = []
    for i in range(n):
        for j in range(m):
            if not visit[i][j] and maps[i][j].isdigit():
                ans.append(bfs(n, m, i, j, maps, visit, hap = 0))
    if not ans:
        return [-1]
    else:
        ans.sort()
        return ans