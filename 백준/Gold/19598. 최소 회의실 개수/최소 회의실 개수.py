import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x: (x[0], x[1]))
room = []
ans = 0

for s, e in times:
    while room and room[0] <= s:
        heappop(room)
    heappush(room, e)
    ans = max(ans, len(room))
print(ans)