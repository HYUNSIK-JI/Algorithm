import sys
from copy import deepcopy
from itertools import combinations
from heapq import heappush, heappop

input = sys.stdin.readline

# 적 유무를 파악하기 위한 함수
def enemy_count():
    # 카운트하기 위한 변수
    cnt = 0

    for i in range(n):
        for j in range(m):
            # 만약 적이라면
            if maps2[i][j]:
                # 카운트 증가
                cnt += 1
    # 적의 수 return
    return cnt
def move():
    # 공격 이후에 적은 한칸 씩 내려간다
    maps2[-1] = [0] * m

    for i in range(n - 1, -1, -1):
        maps2[i] = maps2[i - 1]
    maps2[0] = [0] * m
    return maps2

# 공격 시뮬레이션
def attack(index):
    # 제거 된 적을 카운트 하기위한 변수
    cnt = 0

    # 제거 될 적 위치를 넣기 위한 배열
    dead = []

    # 공격 당했는지 아닌지 파악 하기 위한 이중 배열
    attacked = [[False] * m for _ in range(n)]

    # 궁수의 위치
    for posit in bows_posit[index]:

        # 가장 거리가 가깝고 그 적이 여럿일 경우 가장 왼쪽에 있는 적을 제거 하기 위한 heap
        heap = []
        for i in range(n):
            for j in range(m):
                # 만약 적이라면
                if maps2[i][j]:

                    # 궁수의 공격범위 계산
                    dis = abs(n - i) + abs(posit - j)

                    # 만약 궁수의 공격 범위 안에 있는지 파악
                    if dis <= d:
                        # 거리, 가장 왼쪽 기준으로 제거하기 위해 열의 값 부터 heap에 넣음
                        heappush(heap, (dis, j, i))
        # 범위 안에 있는 적이 존재하는지 파악
        if heap:
            # 거리, 열, 행 위치 값 반환
            distance, x, y = heappop(heap)

            # 제거될 적의 위치 넣기
            dead.append((x, y))
    # 위치 기반으로
    for y, x in dead:
        # 공격을 당하지 않았다면
        if not attacked[x][y]:
            # 공격 당했음을 처리
            attacked[x][y] = True

            # 제거된 적의 수 카운트 증가
            cnt += 1

            # 제거 된 적의 위치 0으로 반환
            maps2[x][y] = 0
    return cnt

# 입력
n, m, d = map(int, input().split())

# 맵 입력
maps = [list(map(int, input().split())) for _ in range(n)]

# 정답을 위한 변수
answer = 0

# 궁수의 위치는 가장 아래에 있고 그 위치를 콤비네이션으로 파악
bows_posit = list(combinations([i for i in range(m)], 3))

for i in range(len(bows_posit)):
    # 제거 된 적의 수를 카운트
    cnt = 0

    # 반복 시뮬레이션 하기 위한 maps의 복사
    maps2 = deepcopy(maps)

    # 적이 있는지 없는지 파악으로 디펜스 게임을 종료 할지 말지 결정
    while enemy_count():

        # attack(i) = 콤비네비이션으로 파악한 궁수들의 위치 값을 해당 인덱스 값으로 접근
        cnt += attack(i)
        # 이동
        move()
    # 최대 제거한 적 수 파악
    answer = max(answer, cnt)
print(answer)



# Q. 문제를 보고 든 생각
# 1.궁수의 공격이 끝나면, 적이 이동한다
#     처음에는 엄청 어렵게 생각했었다. 하지만 생각을 해보니 반복문을 마지막 행부터 돌려서 maps[i] = maps[i - 1] 처리이후 처음 행 과 마지막 행의 값을 [0] * m 처리를 하면 단순한 구현이였다.
# 2.궁수의 위치
#     처음에는 문제에서 궁수의 위치가 정확히 어디라는건지 파악을 잘 못했다. 이것 때문에 하루 종일 고민 했었다..
#     문제를 게속적으로 읽다보니 궁수의 위치는 가장 아래에 있다는 것을 파악했고 모든 경우의 수를 따져봐야 하기때문에 combination를 활용했다.
# 3. 적의 수 파악
#     게임 종료를 위해서 적이 있는지 없는지를 파악 하는 단순 이중 반복문 이면 될 것 같았다. 그 생각이 정확했다.
#     공격범위 파악
#     공격 범위를 파악하기 위해서는 궁수의 위치 와 적의 위치를 알아야 문제에서 주어진 식대로 풀어 낼수있었는데궁수의 위치를 하루종일 고민 해버려서.. 공격범위 파악하는데도 문제가 생겼다..
# 4.deepcopy
#     이 문제의 특성상 기존의 입력 받았던 map을 수정해야 하는 시뮬레이션 문제이기 때문에 maps2 이라는 배열 이름으로 기존의 입력 받았던 map를 deepcopy를 해야 되겠다 라는 생각을 했다.