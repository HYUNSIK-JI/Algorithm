from collections import deque
def rotate(x1, y1, x2, y2, maps, rows, columns):
    mn = 100001
    queue = deque()
    if 0 <= x1 < rows and 0 <= y1 < columns:
        queue.append(maps[x1][y1])
        mn = min(mn, maps[x1][y1])
    k = 0
    
    while queue:
        if k == 4:
            if 0 <= x1 < rows and 0 <= y1 < columns:
                if maps[x1][y1] and mn > maps[x1][y1]:
                    mn = maps[x1][y1]
                maps[x1][y1] = queue.popleft()
        if k == 0:
            for i in range(y1, y2):
                if 0 <= x1 < rows and 0 <= i < columns:
                    queue.append(maps[x1][i])
                    if maps[x1][i] and mn > maps[x1][i]:
                        mn = maps[x1][i]
                    maps[x1][i] = queue.popleft()
            k += 1
        elif k == 1:
            for i in range(x1, x2):
                if 0 <= i < rows and 0 <= y2 < columns:
                    queue.append(maps[i][y2])
                    if mn > maps[i][y2] and maps[i][y2]:
                        mn = maps[i][y2]
                    maps[i][y2] = queue.popleft()
            k += 1
        elif k == 2:
            for i in range(y2, y1, -1):
                if 0 <= x2 < rows and 0 <= i < columns:
                    queue.append((maps[x2][i]))
                    if mn > maps[x2][i] and maps[x2][i]:
                        mn = maps[x2][i]
                    maps[x2][i] = queue.popleft()
            k += 1
        elif k == 3:
            for i in range(x2, x1, -1):
                if 0 <= i < rows and 0 <= y1 < columns:
                    queue.append((maps[i][y1]))
                    if mn > maps[i][y1] and maps[i][y1]:
                        mn = maps[i][y1]
                    maps[i][y1] = queue.popleft()
            k += 1
    return mn

def solution(rows, columns, queries):
    answer = []
    maps = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            maps[i][j] = cnt
            cnt += 1
    for a, b, c, d in queries:
        answer.append(rotate(a - 1, b - 1, c - 1, d - 1, maps, rows, columns))
    return answer