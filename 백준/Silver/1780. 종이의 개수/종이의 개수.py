import sys

input = sys.stdin.readline

def divide(x, y, n):
    global a, b, c
    color = maps[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if not color == maps[i][j]:
                for k1 in range(3):
                    for k2 in range(3):
                        divide(x + k1 * n // 3, y + k2 * n // 3, n // 3)
                return
    if color == - 1:
        a += 1
    elif color == 0:
        b += 1
    else:
        c += 1
    return

n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]

a = 0
b = 0
c = 0

divide(0, 0, n)

print(a)
print(b)
print(c)