import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, k = map(int, input().split())

b = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

# 정렬를 통해서 가방 무게 에 맞게 가격을 최대화 시키기 위함
b.sort()
bag.sort()

ans = []
result = 0
# 가방 무게
for w in bag:
    # 만약 보석들이 존재 하면서 가방의 무게가 보석의 무게보다 더 크면
    while b and w >= b[0][0]:
        # 최대힙으로 보석의 가치를 넣어줌
        heappush(ans, -b[0][1])
        # 가방에 넣어준 보석을 뺌
        heappop(b)
    # while에 있는 조건문 true 였다면 진행
    if ans:
        result += heappop(ans)
    # 보석들이 남아 있으면 게속 진행
    elif b:
        continue
print(-result)