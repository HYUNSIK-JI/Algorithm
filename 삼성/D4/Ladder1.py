from collections import deque

def ladder(a, b):
    queue = deque()
    queue.append((a, b))

    visit = [[False] * 100 for _ in range(100)]
    visit[a][b] = True

    while queue:
        x, y = queue.popleft()
        if 0 <= x < 100 and 0 <= y + 1 < 100 and maps[x][y + 1] == 1 and not visit[x][y + 1]:
            visit[x][y + 1] = True
            queue.append((x, y + 1))
        elif 0 <= x < 100 and 0 <= y - 1 < 100 and maps[x][y - 1] == 1 and not visit[x][y - 1]:
            visit[x][y - 1] = True
            queue.append((x, y - 1))
        elif 0 <= x - 1 < 100 and 0 <= y < 100 and maps[x - 1][y] == 1 and not visit[x - 1][y]:
            visit[x - 1][y] = True
            queue.append((x - 1 ,y))
    if x == 0:
        return y
for test_case in range(1, 11):
    t = int(input())
    maps = []
    start = deque()
    e_x, e_y = 0, 0
    for i in range(100):
        a = list(map(int, input().split()))
        for j in range(100):
            if a[j] == 1 and i == 99:
                start.append((i,j))
            elif a[j] == 2:
                e_x, e_y = i, j
        maps.append(a)
    print(f"#{test_case} {ladder(e_x, e_y)}")