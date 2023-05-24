# 1. start, end 노드 기준으로 다익스트라 실행
# 2. 1번에서 나온 최단 경로들을 최소 스패닝 트리로 완성
# 3. 2번 트리를 효율적으로 만들고 다루기 위해 세그 먼트 트리 구성
# 4. 3번 역시 모든 세그먼트 트리에 대해 Update을 진행 하게 되면 매우 불리
# 5. 4번을 개선한 느리게 갱신 되는 세그먼트 트리로 접근 해야 한다.
# 6. 파이썬의 속도 한계 or PyPy의 메모리 한계를 고려 해야한다.
# 1 ~ 6 번을 모두 고려하며, 시간복잡도, 공간복잡도를 고려 해야 한다.

# 현재 문제를 해결 하기 위한 좋은 방식
# 1) 테스트케이스를 구해서 돌려보며 어디가 문제점 인지 찾아 낸다.
# 2) 현재 문제로서 size의 크기를 적절하게 해야 한다.
# 3) 2번과 다른 방식 으로서 리스트의 overallocation 줄이기 위해 튜플 로 변환한다.
# 4) 1번, 2번 과 다른 방식 으로서 인접 행렬이 아닌 인접 리스트로 접근 한다.
import sys
from heapq import heappush, heappop

INF = sys.maxsize
sys.setrecursionlimit(10 ** 6)

size = 1 << 11

class SegTree:
    def __init__(self):
        self.tree = [INF] * (size << 1)
        self.lazy = [INF] * (size << 1)

    def push(self, node):
        if node < size:
            for next in [node << 1, node << 1 | 1]:
                self.lazy[next] = min(self.lazy[next], self.lazy[node])
        self.tree[node] = min(self.tree[node], self.lazy[node])
        self.lazy[node] = INF

    def update(self, l, r, val, node = 1, L = 1, R = size):
        self.push(node)
        if r < L or R < l:
            return
        if l <= L and R <= r:
            self.lazy[node] = min(self.lazy[node], val)
            self.push(node)
            return
        mid = (L + R) // 2
        self.update(l, r, val, node << 1, L, mid)
        self.update(l, r, val, node << 1 | 1, mid + 1, R)
        self.tree[node] = min(self.tree[node << 1], self.tree[node << 1 | 1])

    def query(self, l, r, node = 1, L = 1, R = size):
        self.push(node)
        if r < L or R < l:
            return INF
        if l <= L and R <= r:
            return self.tree[node]
        mid = (L + R) // 2
        return min(self.query(l, r, node << 1, L, mid), self.query(l, r, node << 1 | 1, mid + 1, R))

def dijkstra(st, graph, dis):
    dis[st] = 0
    queue = [(0, st)]

    while queue:
        dist, now = heappop(queue)
        if dis[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < dis[i[0]]:
                dis[i[0]] = dis[now] + i[1]
                heappush(queue, (dis[i[0]], i[0]))

def dfs(par, dist, now, pre, t):
    if par[now]:
        return
    if ins[now]:
        t = now
    par[now] = t
    for i in graph[now]:
        if i[0] == pre or dist[now] + i[1] != dist[i[0]]:
            continue
        if not t and ins[i[0]]:
            continue
        dfs(par, dist, i[0], now, t)

def solution(n, start, end, graph, path):
    par_start = [0] * 2001
    par_end = [0] * 2001

    dijkstra(start, graph, dist_start)
    dijkstra(end, graph, dist_end)


    dfs(par_start, dist_start, path[1], -1, path[1])
    dfs(par_end, dist_end, path[-1], -1, path[-1])

    ST = SegTree()

    for i in range(1, n + 1):
        for j, cost in graph[i]:
            if ins[i] and ins[j] and abs(ins[i] - ins[j]) <= 1:
                continue
            t1 = ins[par_start[i]]
            t2 = ins[par_end[j]]
            ST.update(t1, t2 - 1, dist_start[i] + cost + dist_end[j])
    ans = []
    for i in range(1, k):
        result = ST.query(i, i)
        ans.append(result if result != INF else -1)
    return ans


n, m, start, end = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

k, *path = list(map(int, input().split()))

ins = [0] * 2001
for index in range(k):
    ins[path[index]] = index + 1

dist_start = [INF] * (n + 1)
dist_end = [INF] * (n + 1)

answer = solution(n, start, end, graph, path)

print(*answer, sep="\n")
