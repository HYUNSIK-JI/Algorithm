import sys

input = sys.stdin.readline

n = int(input())
k = len(bin(n)[2:])
ans = 0
for i in bin(n)[2:]:
    i = int(i)
    if i:
        ans += 3 ** (k - 1)
    k -= 1
print(ans)