import sys

input = sys.stdin.readline

n = int(input())

ans = 0
nums = 9

dic = {}
for _ in range(n):
    sen = input().rstrip()
    k = len(sen)
    for j in sen:
        k -= 1
        dic[j] = dic.get(j, 0) + (10 ** k)

for k, v in sorted(dic.items(), key=lambda x: (-x[1])):
    ans += nums * v
    nums -= 1
print(ans)