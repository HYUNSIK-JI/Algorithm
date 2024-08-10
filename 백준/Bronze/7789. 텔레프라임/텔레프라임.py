import sys
import math
input = sys.stdin.readline

k = 10 ** 7

prime = [False, False] + [True] * (k + 1)

for i in range(2, k + 1):
    if prime[i]:
        for j in range(2 * i, k + 1, i):
            prime[j] = False

num_list = list(input().split())

new_number = int(num_list[1] + num_list[0])

if prime[new_number] and prime[int(num_list[0])]:
    print("Yes")
else:
    print("No")