import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
maps = []

virus_1 = deque()
virus_2 = deque()

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        if a[j] == 1:
            virus_1.append((i, j))
        elif a[j] == 2:
            virus_2.append((i, j))
    maps.append(a)
cnt1, cnt2, cnt3 = 1, 1, 0

while virus_1 or virus_2:
    set1, set2, set3 = set(), set(), set()
    while virus_1:
        x, y = virus_1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny]:
                set1.add((nx, ny))
    while virus_2:
        x, y = virus_2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny]:
                set2.add((nx, ny))
    set3 = set1 & set2
    for x, y in set3:
        maps[x][y] = 3
        cnt3 += 1
    for x, y in set1 - set3:
        maps[x][y] = 1
        cnt1 += 1
        virus_1.append((x, y))
    for x, y in set2 - set3:
        maps[x][y] = 2
        cnt2 += 1
        virus_2.append((x, y))
print(cnt1, cnt2, cnt3)