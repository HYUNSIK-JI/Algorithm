dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
f_n = int(input())

arr = [[0] * n for _ in range(n)]

d = -1
k = n * n
x, y = -1, 0
ans = []
for _ in range(n * 2 - 1):
    d = (d + 1) % 4
    for _ in range(n):
        x += dx[d]
        y += dy[d]
        arr[x][y] = k
        if k == f_n:
            ans.append((x + 1, y + 1))
        k -= 1
    if not d or not d % 2:
        n -= 1
for i in range(len(arr)): print(*arr[i])
print(*ans[0])