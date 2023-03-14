import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()

    s, e = 0, len(nums) - 1
    ans = 0
    mn = 1e9

    while s < e:
        hap = nums[s] + nums[e]

        if mn > abs(k - hap):
            mn = abs(k - hap)
            ans = 0

        if hap < k:
            if abs(k - hap) == mn:
                ans += 1
            s += 1
        elif hap > k:
            if abs(k - hap) == mn:
                ans += 1
            e -= 1
        else:
            ans += 1
            s += 1
    print(ans)