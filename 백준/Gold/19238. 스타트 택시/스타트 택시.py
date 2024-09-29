import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우 이동 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

is_exit = 0

# 최단 거리 찾기 (BFS 사용)
def find_shortest_distance(a, b):
    visit = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((a, b))
    visit[a][b] = 0  # 시작 지점은 거리가 0
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny] and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
    return visit

# 택시 이동 로직
def move_taxi(t_x, t_y, ans):
    global is_exit, customers
    while customers:
        if is_exit:
            break

        # 고객들을 정렬하기 전에 거리를 추가
        customers = update_customers_with_distance(t_x, t_y)
        
        dis, a, b, c, d = customers.pop(0)

        # 연료가 부족하거나 손님까지의 거리를 갈 수 없는 경우 종료
        if k <= 0 or dis == -1:
            is_exit = 1
            break
        
        # 손님에게 이동
        t_x, t_y = move_to_customer(a, b, t_x, t_y)
        if is_exit:
            break
        
        # 목적지로 이동
        t_x, t_y, ans = move_to_destination(c, d, t_x, t_y, ans)
        if is_exit:
            break
    
    return ans

# 고객 리스트에 거리 추가 후 정렬
def update_customers_with_distance(t_x, t_y):
    short = find_shortest_distance(t_x, t_y)

    # 고객 배열에 거리 추가
    for i, customer in enumerate(customers):
        if len(customer) == 4:
            c_s_x, c_s_y, c_e_x, c_e_y = customer
        else:
            dis, c_s_x, c_s_y, c_e_x, c_e_y = customer
        dis = short[c_s_x][c_s_y]
        customers[i] = [dis, c_s_x, c_s_y, c_e_x, c_e_y]
    
    # 거리, x좌표, y좌표 순으로 정렬
    customers.sort(key=lambda x: (x[0], x[1], x[2]))
    return customers

# 손님에게 이동
def move_to_customer(a, b, t_x, t_y):
    global k, is_exit
    queue = deque()
    queue.append((t_x, t_y))
    visit = [[-1] * n for _ in range(n)]
    visit[t_x][t_y] = 0

    while queue:
        x, y = queue.popleft()

        if k <= 0:
            is_exit = 1
            break

        if x == a and y == b:
            k -= visit[x][y]  # 손님에게 도착할 때까지 소모한 연료만큼 감소
            return a, b

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny] and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
    
    return t_x, t_y

# 목적지로 이동
def move_to_destination(c, d, t_x, t_y, ans):
    global k, is_exit
    queue = deque()
    queue.append((t_x, t_y))
    visit = [[-1] * n for _ in range(n)]
    visit[t_x][t_y] = 0

    while queue:
        x, y = queue.popleft()

        if x == c and y == d:
            distance = visit[x][y]
            k -= distance  # 이동하는 동안 연료 감소
            if k < 0:
                is_exit = 1
                break
            ans += 1  # 목적지 도착하면 고객 1명 완료
            k += (distance * 2)  # 연료 회복
            return c, d, ans

        if k <= 0:
            is_exit = 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny] and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))

    return t_x, t_y, ans

# 입력 받기
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

t_x, t_y = map(lambda x: x - 1, map(int, input().split()))  # 택시 초기 위치
customers = [list(map(lambda x: x - 1, map(int, input().split()))) for _ in range(m)]  # 손님 리스트
ans = 0

# 택시 이동 시작
ans = move_taxi(t_x, t_y, ans)

if ans == m:
    print(k)
else:
    print(-1)
