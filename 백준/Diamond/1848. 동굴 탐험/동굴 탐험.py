import sys
from heapq import heappush, heappop
from collections import defaultdict

INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start, graph, dist):
    queue = []
    dist[start] = 0

    for i in range(len(graph[start])):
        cost, des = graph[start][i]  # 출발 노드에서 연결된 노드들의 비용과 목적지 정보를 가져옴
        queue.append((cost, des, des))  # 큐에 비용, 목적지, 목적지 노드 추가
        dist[des] = cost  # 출발 노드에서 목적지 노드까지의 거리를 해당 노드의 값으로 초기화

    # 다익스트라
    while queue:
        cost, vertex, prev = heappop(queue)  # 우선순위 큐에서 가장 작은 비용을 가진 노드를 꺼냄
        if cost != dist[vertex]:  # 이미 더 작은 거리로 갱신된 경우 무시
            continue
        p[vertex] = prev  # 이전 노드 정보를 저장
        for i in graph[vertex]:
            new_cost = cost + i[0]  # 출발 노드에서 목적지 노드까지의 비용 계산
            if dist[i[1]] > new_cost:  # 저장된 거리보다 더 작은 경우 갱신
                dist[i[1]] = new_cost  # 거리 갱신
                heappush(queue, (dist[i[1]], i[1], prev))  # 큐에 새로운 거리 정보 추가 (비용, 목적지, 이전 노드)
# 입력
n, m = map(int, input().split())

# 정 방향 간선 리스트
graph = defaultdict(list)

# 역 방향 간선 리스트
reverse_graph = defaultdict(list)

# 정 방향 거리, 역 방향 거리 초기화
dist = [INF] * n
dist2 = [INF] * n

queue = []

# 이전 노드들 정점들 저장
p = [-1] * n

for _ in range(m):
    a, b, c, d = map(int, input().split())
    a, b = a - 1, b - 1

    # 정 방향 간선과 역 방향 간선 저장.
    graph[a].append((c, b))
    graph[b].append((d, a))

    # 이 때, 가중치를 반대로 저장하여 역 방향 간선 저장.
    reverse_graph[a].append((d, b))
    reverse_graph[b].append((c, a))

# 시작점 에서 출발 하여 다익스트라 시작
dijkstra(0, graph, dist)

ans = INF
# 역방향 그래프에서 0번 노드로 들어오는 모든 간선에 대해 반복
for i in range(len(reverse_graph[0])):
    # 역방향 그래프에서 0번 노드로 들어오는 i번째 간선의 출발 노드
    col = reverse_graph[0][i][1]

    # col로부터 0번 노드까지의 거리(dist2)를 업데이트 이후 col에서 시작하는 최단경로의 시작점 삽입
    heappush(queue, (reverse_graph[0][i][0], col, 0))
    dist2[col] = reverse_graph[0][i][0]
    dist2[0] = 0


    while queue:
        # 현재 큐에서 가장 최단거리인 정점을 꺼냄
        cost, vertex, prev = heappop(queue)

        # 현재 정점이 이미 처리된 적 있으면(=최단거리가 업데이트된 적 있으면) 넘어감
        if cost != dist2[vertex]:
            continue
        # col로부터 시작한 최단경로와 0번 노드에서 시작한 최단경로가 만나는 지점을 찾았으면 해당 최단경로의 길이를 구하고 종료
        if p[vertex] != col:
            ans = min(ans, cost + dist[vertex])
            continue
        # 현재 정점에서 이웃한 정점들을 모두 검사
        for k in reverse_graph[vertex]:
            # 이웃한 정점으로 가는 거리를 업데이트하고, 큐에 삽입
            new_cost = cost + k[0]
            if dist2[k[1]] > new_cost:
                dist2[k[1]] = new_cost
                heappush(queue, (dist2[k[1]], k[1], 0))
        # 현재 정점이 col이면, 0번 노드로부터의 최단거리(dist2[0])는 업데이트되면 안 됨
        if vertex == col:
            dist2[0] = INF

# col로부터 시작한 최단경로와 0번 노드에서 시작한 최단경로가 만나는 지점이 없을 경우, INF 출력
# 하지만 문제에서 '언제나 조건을 만족하는 경로가 하나는 있다고 가정해도 좋다.' 라고 하였다.
print(ans)
