import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
reverse_nums = nums[::-1]

dp1 = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if reverse_nums[i] > reverse_nums[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

ans = [0] * n
for i in range(n):
    ans[i] = dp1[i] + dp2[n - i - 1]
print(max(ans) - 1)
