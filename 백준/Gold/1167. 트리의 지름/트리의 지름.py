import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(start, cost):
    for i in maps[start]:
        if dis[i[0]] == -1:
            c = i[1] + cost
            dis[i[0]] = c
            dfs(i[0], c)

n = int(input())

maps = [[] for _ in range(n + 1)]

for _ in range(n):
    nums = list(map(int, input().split()))
    start = nums[0]
    for i in range(1, len(nums), 2):
        if len(nums[i: i + 2]) == 2:
            maps[start].append((nums[i], nums[i + 1]))
            maps[nums[i]].append((start, nums[i + 1]))
dis = [-1] * (n + 1)
dis[1] = 0
dfs(1, 0)


node = dis.index(max(dis))
dis = [-1] * (n + 1)
dis[node] = 0
dfs(node, 0)

print(max(dis))