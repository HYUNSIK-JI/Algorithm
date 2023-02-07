import sys

input = sys.stdin.readline

sen = input().rstrip()

ans = 0
mul = 1
stack = []
for i, v in enumerate(sen):
    if v == "(":
        stack.append(v)
        mul *= 2
    elif v == "[":
        stack.append(v)
        mul *= 3
    elif v == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if sen[i - 1] == "(":
            ans += mul
        stack.pop()
        mul //= 2
    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if sen[i - 1] == "[":
            ans += mul
        stack.pop()
        mul //= 3
if stack:
    print(0)
else:
    print(ans)