import sys

input = sys.stdin.readline

def search(k):
    global ans

    low, high = arr[0], arr[0]
    d = 1

    for i in arr:
        if high < i:
            high = i
        if low > i:
            low = i

        if high - low > k:
            d += 1
            low = i
            high = i
    return m >= d
n, m = map(int, input().split())
arr = list(map(int, input().split()))

mn, mx = 0, max(arr)
ans = mx

while mn <= mx:
    mid = (mn + mx) // 2

    if search(mid):
        mx = mid - 1
        ans = min(ans, mid)
    else:
        mn = mid + 1
print(ans)