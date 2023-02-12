import sys

input = sys.stdin.readline

def divide(x, y, n):
    global w, b
    color = maps[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if not color == maps[i][j]:
                divide(x, y, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                return
    if not color:
        w += 1
    else:
        b += 1
    return

n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]

w = 0
b = 0

divide(0, 0, n)

print(w)
print(b)