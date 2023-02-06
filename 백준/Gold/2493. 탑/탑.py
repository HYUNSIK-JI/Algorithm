import sys

input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))

stack = []
answer = [0] * n

for k, v in enumerate(top):
    while stack:
        if stack[-1][1] > v:
            answer[k] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((k, v))
print(*answer)