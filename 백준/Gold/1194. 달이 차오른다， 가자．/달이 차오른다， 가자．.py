import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_exit():
    visit = [[[-1] * (1 << 6) for _ in range(m)] for _ in range(n)]
    start_key_state = 0
    visit[sx][sy][start_key_state] = 0
    queue = deque([(sx, sy, start_key_state)])

    while queue:
        x, y, key_state = queue.popleft()

        if (x, y) in exit_postion:
            return visit[x][y][key_state]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == "#":
                continue

            new_key_state = key_state

            # 키를 얻는 경우
            if arr[nx][ny] in key_type:
                key_index = ord(arr[nx][ny]) - ord('a')
                new_key_state |= (1 << key_index)  # 해당 키 획득

            # 문을 통과하는 경우
            if arr[nx][ny] in door_type:
                door_index = ord(arr[nx][ny]) - ord('A')
                if not (new_key_state & (1 << door_index)):  # 필요한 키가 없는 경우
                    continue

            # 이미 방문한 곳이고, 동일한 키 상태라면 건너뛰기
            if visit[nx][ny][new_key_state] != -1:
                continue
            
            # 새롭게 방문 처리
            visit[nx][ny][new_key_state] = visit[x][y][key_state] + 1
            queue.append((nx, ny, new_key_state))

    return -1

n, m = map(int, input().split())

key_type = ['a', 'b', 'c', 'd', 'e', 'f']
door_type = ['A', 'B', 'C', 'D', 'E', 'F']

arr = []
sx, sy = 0, 0
exit_postion = []

for i in range(n):
    temp = list(input().rstrip())
    for j in range(m):
        if temp[j] == "0":
            sx, sy = i, j
        elif temp[j] == "1":
            exit_postion.append((i, j))
    arr.append(temp)

ans = find_exit()

print(ans)
