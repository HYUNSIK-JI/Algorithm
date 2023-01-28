import sys

input = sys.stdin.readline

n = input().rstrip()

k = len(n) - 1

ans = 0
p = 0

while p < k:
    ans += 9 * (10 ** p) * (p + 1)
    p += 1
ans += (int(n) - (10 ** p) + 1) * (k + 1)
print(ans)