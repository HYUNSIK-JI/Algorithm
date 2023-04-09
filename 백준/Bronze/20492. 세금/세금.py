import sys

input = sys.stdin.readline

n = int(input())
a = int(n * 0.78)
b = int(n - (n * 0.2) * 0.22)

print(a, b)