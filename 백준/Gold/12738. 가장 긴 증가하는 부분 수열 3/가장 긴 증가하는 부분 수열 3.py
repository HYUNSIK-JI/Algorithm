import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
d = [0] * (n + 1)
k = [-1e9 -1]
mx = 0

for i in range(1, n + 1):
	if k[-1] < a[i]:
		k.append(a[i])
		d[i] = len(k) - 1
		mx = d[i]
	else:
		d[i] = bisect_left(k, a[i])
		k[d[i]]=a[i]
print(mx)