import sys

input = sys.stdin.readline
INF = int(1e9)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())

distance = [INF] * (m + 1)
parent = [i for i in range(n + 1)]
graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()
ans = 0
for edge in graph:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(parent, a, b)
        ans += cost
print(ans + ((n - 2) * (n - 1) // 2) * k)