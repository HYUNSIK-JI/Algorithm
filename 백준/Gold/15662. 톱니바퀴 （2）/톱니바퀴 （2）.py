import sys; input = sys.stdin.readline
from collections import deque

# 한 톱니바퀴 회전 함수
def rotate(cogwheel, direction):
    if direction == 1:
        # 시계 방향 (오른쪽으로 회전)
        cogwheel.appendleft(cogwheel.pop())
    else:
        # 반시계 방향 (왼쪽으로 회전)
        cogwheel.append(cogwheel.popleft())

# 연쇄적으로 톱니바퀴 회전
def rotate_all(start, direction, t):
    directions = [0] * t  # 각 톱니바퀴의 회전 방향 (0: 회전 안함)
    directions[start] = direction

    # 왼쪽 톱니바퀴 회전 여부 결정
    for i in range(start - 1, -1, -1):
        if cogwheels[i][2] != cogwheels[i + 1][6]:
            directions[i] = -directions[i + 1]
        else:
            break

    # 오른쪽 톱니바퀴 회전 여부 결정
    for i in range(start + 1, t):
        if cogwheels[i][6] != cogwheels[i - 1][2]:
            directions[i] = -directions[i - 1]
        else:
            break

    # 모든 톱니바퀴 회전 적용
    for i in range(t):
        if directions[i]:
            rotate(cogwheels[i], directions[i])

# 입력 처리
t = int(input())
cogwheels = [deque(list(input().strip())) for _ in range(t)]
k = int(input())
rotation_infos = [list(map(int, input().split())) for _ in range(k)]

# 각 회전 정보에 따라 톱니바퀴 회전 수행
for a, b in rotation_infos:
    rotate_all(a - 1, b, t)

result = 0
# 결과 출력 (예시: 각 톱니바퀴의 12시 방향 값 출력)
for k, v in enumerate(cogwheels):
    if v[0] == '0':
        continue
    result += 1
print(result)
