import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

left = 0
right = 0
ans = 0

for i in nums:
    if i == 1:
        left += 1
        right -= 1
    else:
        right += 1
        left -= 1
    left = max(left, 0)
    right = max(right, 0)
    ans = max(ans, abs(left - right))
print(ans)