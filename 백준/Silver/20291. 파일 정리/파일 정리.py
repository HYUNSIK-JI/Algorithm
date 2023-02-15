import sys

input = sys.stdin.readline

dic = {}
for _ in range(int(input())):
    k = input().split(".")
    k[1] = k[1].rstrip()
    dic[k[1]] = dic.get(k[1], 0) + 1

for key, value in sorted(dic.items()):
    print(key, value)