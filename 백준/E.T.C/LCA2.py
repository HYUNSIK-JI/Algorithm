import sys
input = sys.stdin.readline

# 재귀 깊이 설정
sys.setrecursionlimit(10 ** 5)

# 2^20 = 1,000,000
LOG = 21

# 루트노드부터 출발하여 깊이를 구하는 함수
def dfs(x, d):
    depth_cal[x] = True
    depth[x] = d

    for y in graph[x]:
        if not depth_cal[y]:
            parent[y][0] = x
            dfs(y, d + 1)

# 전체 부모 관계를 설정하기
def set_parent():
    dfs(1, 0) # 루트노드 1번부터 시작
    for i in range(1, LOG):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# A와 B의 최소 공통 조상 찾기
def lca(a, b):
    # B가 더 깊도록 설정
    if depth[a] > depth[b]:
        a, b = b, a
    # 깊이가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a

    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 부모가 찾고자 하는 조상
    return parent[a][0]

n = int(input())
parent = [[0] * LOG for _ in range(n + 1)] # 부모 노드 정보
depth = [0] * (n + 1) # 각 노드까지의 깊이
depth_cal = [0] * (n + 1) # 각 노드 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()
m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
    
