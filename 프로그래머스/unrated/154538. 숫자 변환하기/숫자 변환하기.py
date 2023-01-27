from collections import deque

def solution(start, y, n):
    visit = [-1] * (10 ** 6 + 1)
    visit[start] = 0
    queue = deque()
    queue.append(start)
    
    while queue:
        x = queue.popleft()
        if x == y:
            return visit[x]
        for i in (x + n, x * 2, x * 3):
            if 1 <= i <= 10 ** 6 and visit[i] == -1:
                visit[i] = visit[x] + 1
                queue.append(i)
    return -1