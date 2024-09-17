import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 태풍의 각 방향에 따른 모래 퍼짐 비율
spread_patterns = {
    0: [  # ← (좌)
        (-1, 1, 1), (-1, 0, 7), (-1, -1, 10), (0, -2, 5),
        (1, 1, 1), (1, 0, 7), (1, -1, 10), (2, 0, 2), (-2, 0, 2)
    ],
    1: [  # ↓ (하)
        (-1, -1, 1), (0, -1, 7), (1, -1, 10), (2, 0, 5),
        (-1, 1, 1), (0, 1, 7), (1, 1, 10), (0, 2, 2), (0, -2, 2)
    ],
    2: [  # → (우)
        (-1, -1, 1), (-1, 0, 7), (-1, 1, 10), (0, 2, 5),
        (1, -1, 1), (1, 0, 7), (1, 1, 10), (2, 0, 2), (-2, 0, 2)
    ],
    3: [  # ↑ (상)
        (1, -1, 1), (0, -1, 7), (-1, -1, 10), (-2, 0, 5),
        (1, 1, 1), (0, 1, 7), (-1, 1, 10), (0, 2, 2), (0, -2, 2)
    ]
}

# 모래를 퍼뜨리는 함수
def spread_sand(s, e, d, arr):
    global result

    sand = arr[s][e]
    total_spread = 0
    
    for ds, de, percentage in spread_patterns[d]:
        ns, ne = s + ds, e + de
        spread_amount = int(sand * percentage / 100)

        # 범위를 벗어나는 경우 처리
        if 0 <= ns < N and 0 <= ne < N:
            arr[ns][ne] += spread_amount
        else:
            result += spread_amount
        
        total_spread += spread_amount

    # 나머지 모래 a% 처리
    remain_sand = sand - total_spread
    ns, ne = s + dx[d], e + dy[d]  # 나머지 모래는 태풍 이동 방향에 따라 위치
    if 0 <= ns < N and 0 <= ne < N:
        arr[ns][ne] += remain_sand
    else:
        result += remain_sand
    
    arr[s][e] = 0  # 모래가 모두 퍼지고 나면 원래 위치는 0으로 만듦

# 태풍이 움직이는 함수
def t_moving(k, d, tx, ty, arr):
    step = 1  # 태풍이 이동할 거리
    d = 0  # 시작 방향은 왼쪽(←)

    while tx > 0 or ty > 0:  # 태풍이 (0, 0)까지 이동해야 종료
        for _ in range(2):  # 한 번의 이동 거리마다 두 번 방향 전환
            for _ in range(step):  # 한 방향으로 `step`만큼 이동
                tx += dx[d]
                ty += dy[d]

                # 태풍이 맵 범위를 벗어나지 않는다면
                if 0 <= tx < N and 0 <= ty < N:
                    spread_sand(tx, ty, d, arr)  # 모래 퍼뜨리기

                # 태풍이 (0, 0)에 도착하면 종료
                if not tx and not ty:
                    return
            
            d = (d + 1) % 4  # 방향 전환

        step += 1  # step 증가 (태풍이 나선형으로 점점 더 멀리 이동)

# 입력 처리 및 실행
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
t_moving(1, -1, N // 2, N // 2, arr)

print(result)
