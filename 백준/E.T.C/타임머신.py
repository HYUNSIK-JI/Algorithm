import sys

input = sys.stdin.readline
# 무한대
INF = int(1e9)

n, m = map(int, input().split())

# 거리를 나타내는 리스트
distance = [INF] * (n + 1)
# 엣지
edges = []

for _ in range(m):
    # 도시 시작점, 도시 도착점, 비용
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

#벨만포드 알고리즘 시작
distance[1] = 0
cycle = False

for _ in range(n):
    for start, end, cost in edges:
        # 시작점이 무한대가 아니고 도착지점 값이 시작지점 + 비용 보다 크면
        if distance[start] != INF and distance[end] > distance[start] + cost:
            # 도착지점 값 갱신
            distance[end] = distance[start] + cost

for _ in range(n):
    for start, end, cost in edges:
        # 음수 사이클이 존재하는지 판별
        if distance[start] != INF and distance[end] > distance[start] + cost:
            cycle = True
            break
# 존재하지 않는다면
if not cycle:
    # 그값이 무한대가 아니면
    for i in range(2, n + 1):
        if distance[i] != INF:
            # 비용 출력
            print(distance[i])
        # 무한대라면
        else:
            # -1
            print(-1)
# 음수 사이클 존재
else:
    print(-1)