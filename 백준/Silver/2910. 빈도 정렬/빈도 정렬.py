import sys

input = sys.stdin.readline

n, c = map(int, input().split())
nums = list(map(int, input().split()))

dic = {}

for i in nums:
    dic[i] = dic.get(i, 0) + 1

dic = sorted(dic.items(), key=lambda x: -x[1])
for k, v in dic:
    for _ in range(v):
        print(k, end=" ")