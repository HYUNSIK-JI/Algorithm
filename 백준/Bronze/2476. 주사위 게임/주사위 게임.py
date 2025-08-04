import sys

input = sys.stdin.readline

def check_number(a, b, c):
    if a == b == c:
        return 1, a
    if a == b or a == c:
        return 2, a
    if b == c:
        return 2, b
    return 3, max(a, b, c)


def pay(a, b, c):
    chk, num = check_number(a, b, c)

    if chk == 1:
        return 10000 + (num * 1000)
    elif chk == 2:
        return 1000 + (num * 100)
    else:
        return num * 100

ans = 0


for _ in range(int(input())):
    ans = max(ans, pay(*map(int, input().split())))

print(ans)