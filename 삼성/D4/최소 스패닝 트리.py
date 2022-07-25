#특정 원소가 속한 집합 찾기
def find_parent(parant, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을때 까지 재귀적으로 호출
    if parant[x] != x:
        parant[x] = find_parent(parant, parant[x])
    return parant[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parant, a, b):
    a = find_parent(parant, a)
    b = find_parent(parant ,b)

    if a < b:
        parant[b] = a
    else:
        parant[a] = b

for test_case in range(1, int(input()) + 1):

    # 노드의 개수와 간선의 개수 입력받기
    v, e = map(int ,input().split())
    parant = [0] * (v + 1)

    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    edges = []
    result = 0

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parant[i] = i

    # 모든 간선에 대한 정보를 입력받기
    for _ in range(e):
        a, b , cost = map(int, input().split())
        # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
        edges.append((cost, a, b))
    # 간선을 비용순으로 정렬
    edges.sort()

    # 간선을 하나씩 확인
    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parant,a) != find_parent(parant, b):
            union_parent(parant, a, b)
            result += cost
    print(f"#{test_case} {result}")