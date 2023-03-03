import sys
from collections import deque

input = sys.stdin.readline

def BFS(k):
    queue = deque()
    queue.append(start)
    check = [False] * (n + 1)
    check[start] = True

    while queue:
        x = queue.popleft()
        for i, j in graph[x]:
            if not check[i] and j >= k:
                check[i] = True
                queue.append(i)
    return True if check[end] else False


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, input().split())
mx, mn = 1000000000, 1
answer = 0

while mn <= mx:
    mid = (mn + mx) // 2

    if BFS(mid):
        answer = mid
        mn = mid + 1
    else:
        mx = mid - 1

print(answer)