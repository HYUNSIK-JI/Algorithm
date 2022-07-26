from collections import deque

def ladder(a, b, c):
    queue = deque()
    queue.append((a, b, c))

    visit = [[False] * 100 for _ in range(100)]
    visit[a][b] = True

    while queue:
        x, y , cnt = queue.popleft()
        # 오른쪽에 1이 있는지 확인
        if 0 <= x < 100 and 0 <= y + 1 < 100 and maps[x][y + 1] == 1 and not visit[x][y + 1]:
            visit[x][y + 1] = True
            queue.append((x, y + 1, cnt + 1))
        # 왼쪽에 1이 있는지 확인
        elif 0 <= x < 100 and 0 <= y - 1 < 100 and maps[x][y - 1] == 1 and not visit[x][y - 1]:
            visit[x][y - 1] = True
            queue.append((x, y - 1, cnt + 1))
        # 오른쪽,왼쪽에 둘다 없다면 위에 1이 있는지 확인
        elif 0 <= x + 1 < 100 and 0 <= y < 100 and maps[x + 1][y] == 1 and not visit[x + 1][y]:
            visit[x + 1][y] = True
            queue.append((x + 1, y, cnt + 1))
    if x == 99:
        return cnt,b

for test_case in range(1, 11):
    T = int(input())

    maps = []
    start_position = []
    result = []
    for i in range(100):
        a = list(map(int, input().split()))
        for j in range(100):
            if i == 0 and a[j] == 1:
                start_position.append((i, j, 1))
        maps.append(a)

    while start_position:
        x, y, cnt = start_position.pop(0)
        result.append(ladder(x, y, cnt))
    print(f"#{test_case} {min(result)[1]}")