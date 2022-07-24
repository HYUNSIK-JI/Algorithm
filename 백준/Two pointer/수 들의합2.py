import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sequence = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while left <= right and right <= n:
    hap = sequence[left:right]
    answer = sum(hap)

    if answer == m:
        cnt += 1
        right += 1
    elif answer < m:
        right += 1
    else:
        left += 1
print(cnt)
