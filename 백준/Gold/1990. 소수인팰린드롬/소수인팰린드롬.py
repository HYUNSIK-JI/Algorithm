import sys

input = sys.stdin.readline

a, b = map(int, input().split())

if b > 10 ** 7:
    b = 10 ** 7

prime = [False, False] + [True] * (b + 1)

for i in range(2, b + 1):
    if prime[i]:
        k = str(i)
        if k == k[::-1] and i >= a:
            print(i)
        for j in range(2 * i, b + 1, i):
            prime[j] = False
print(-1)