import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n = int(input())

p_x, p_y, p_z = [], [], []
parent = [i for i in range(n + 1)]
for i in range(n):
    x, y, z = map(int, input().split())
    p_x.append((x, i + 1))
    p_y.append((y, i + 1))
    p_z.append((z, i + 1))

p_x.sort()
p_y.sort()
p_z.sort()

edge = []
for a in p_x, p_y, p_z:
    for i in range(n - 1):
        edge.append((abs(a[i][0] - a[i + 1][0]), a[i][1], a[i + 1][1]))
edge.sort()

answer = 0
cnt = 0
for cost, a, b in edge:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost
        cnt += 1

        if cnt == n - 1:
            break
print(answer)