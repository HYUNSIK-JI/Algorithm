from heapq import heappush, heappop

INF = 10 ** 9 + 7
size = 1 << 11

class SegTree:
    def __init__(self):
        self.tree = [INF] * (size << 1)
        self.lazy = [INF] * (size << 1)

    def push(self, node):
        if node < size:
            for _next in [node << 1, node << 1 | 1]:
                self.lazy[_next] = min(self.lazy[_next], self.lazy[node])
        self.tree[node] = min(self.tree[node], self.lazy[node])
        self.lazy[node] = INF

    def update(self, l, r, val, node = 1, LEFT = 1, RIGHT = size):
        self.push(node)
        if r < LEFT or RIGHT < l:
            return
        if l <= LEFT and RIGHT <= r:
            self.lazy[node] = min(self.lazy[node], val)
            self.push(node)
            return
        mid = (LEFT + RIGHT) // 2
        self.update(l, r, val, node << 1, LEFT, mid)
        self.update(l, r, val, node << 1 | 1, mid + 1, RIGHT)
        self.tree[node] = min(self.tree[node << 1], self.tree[node << 1 | 1])

    def query(self, l, r, node = 1, LEFT = 1, RIGHT = size):
        self.push(node)
        if r < LEFT or RIGHT < l:
            return INF
        if l <= LEFT and RIGHT <= r:
            return self.tree[node]
        mid = (LEFT + RIGHT) // 2
        return min(self.query(l, r, node << 1, LEFT, mid), self.query(l, r, node << 1 | 1, mid + 1, RIGHT))


def dijkstra(start, graph, dis):
    dis[start] = 0
    queue = [(0, start)]

    while queue:
        dist, now = heappop(queue)
        if dis[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < dis[i[0]]:
                dis[i[0]] = dis[now] + i[1]
                heappush(queue, (dis[i[0]], i[0]))


def DAG(parent, dist, now, pre, t):
    stack = [(now, pre, t)]

    while stack:
        now, pre, t = stack.pop()

        if parent[now]:
            continue

        if ins[now]:
            t = now

        parent[now] = t

        for i in graph[now]:
            if i[0] == pre or dist[now] + i[1] != dist[i[0]]:
                continue

            if not t and ins[i[0]]:
                continue

            stack.append((i[0], now, t))


def solution(n, start, end, graph, path):
    parent_start = [0] * 2001
    parent_end = [0] * 2001

    dist_start = [INF] * (n + 1)
    dist_end = [INF] * (n + 1)

    dijkstra(start, graph, dist_start)
    dijkstra(end, graph, dist_end)

    DAG(parent_start, dist_start, path[0], -1, path[0])
    DAG(parent_end, dist_end, path[-1], -1, path[-1])

    ST = SegTree()

    for i in range(1, n + 1):
        for j, cost in graph[i]:
            if ins[i] and ins[j] and abs(ins[i] - ins[j]) <= 1:
                continue
            t1 = ins[parent_start[i]]
            t2 = ins[parent_end[j]]
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

answer = solution(n, start, end, graph, path)

print(*answer, sep="\n")