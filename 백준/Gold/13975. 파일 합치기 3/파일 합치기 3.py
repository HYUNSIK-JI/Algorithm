import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    files = list(map(int, input().split()))
    heapify(files)

    ans = 0

    for _ in range(k - 1):
        k = 0
        first = heappop(files)
        second = heappop(files)
        
        k = first + second
        ans += k
        heappush(files, k)
    print(ans)
        
