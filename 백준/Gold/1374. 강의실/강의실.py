import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[2]))

room = []
cnt = 0

for i in times:
    while room and room[0] <= i[1]:
        heappop(room)
    heappush(room, (i[2]))
    cnt = max(cnt, len(room))
print(cnt)