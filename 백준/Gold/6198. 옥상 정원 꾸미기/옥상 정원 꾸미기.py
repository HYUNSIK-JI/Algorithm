import sys

input = sys.stdin.readline

n = int(input())
b = [int(input()) for _ in range(n)]

stack = []
ans = 0
for v in b:
    while stack and stack[-1] <= v:
        stack.pop()
    stack.append(v)
    ans += len(stack) - 1
print(ans)