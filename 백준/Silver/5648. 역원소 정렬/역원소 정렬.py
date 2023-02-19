import sys

input = sys.stdin.readline

ans = []
nums = list(map(int, input().split()))
n = nums[0]
n -= (len(nums) - 1)
while n:
    if not ans:
        for i in range(1, len(nums)):
            k = str(nums[i])
            ans.append(int(k[::-1]))
    else:
        nums = list(map(int, input().split()))
        n -= len(nums)
        for i in nums:
            k = str(i)
            ans.append(int(k[::-1]))
ans.sort()
print(*ans, sep="\n")