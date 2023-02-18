from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, c, d, maps, n, m):
    visit = [[-1] * m for _ in range(n)]
    visit[a][b] = 0
    queue = deque()
    queue.append((a, b))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1:
                if maps[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
    return visit[c][d]
def solution(maze):
    n, m = len(maze), len(maze[0])
    
    maps = [[0] * m for _ in range(n)]
    
    s_x, s_y = 0, 0
    e_x, e_y = 0, 0
    l_x, l_y = 0, 0
    
    for i in range(n):
        for j in range(m):
            if not maze[i][j] == "X":
                maps[i][j] = 1
                
                if maze[i][j] == "S":
                    s_x, s_y = i, j
                elif maze[i][j] == "L":
                    l_x, l_y = i, j
                elif maze[i][j] == "E":
                    e_x, e_y = i, j
                
    a = bfs(s_x, s_y, l_x, l_y, maps, n, m)
    b = bfs(l_x, l_y, e_x, e_y, maps, n, m)
    
    if a == -1 or b == -1:
        return -1
    else:
        return a + b
    