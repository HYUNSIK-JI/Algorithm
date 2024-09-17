import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def lattice_rotation(k, arr):
    # 격자의 부분 크기 2^k
    lattice_size = 2 ** k
    N = len(arr)  # 격자의 크기는 2^N x 2^N
    
    # 새로 회전한 격자를 담을 배열
    new_arr = [row[:] for row in arr]  # 깊은 복사
    
    # 2^k 크기 부분 격자들을 순차적으로 회전
    for i in range(0, N, lattice_size):
        for j in range(0, N, lattice_size):
            # 부분 격자 회전
            for x in range(lattice_size):
                for y in range(lattice_size):
                    # 시계방향 회전: (i + x, j + y) -> (i + y, j + lattice_size - 1 - x)
                    new_arr[i + y][j + lattice_size - 1 - x] = arr[i + x][j + y]
    
    return new_arr


def ice_melts(K, arr):
    # 감소할 얼음이 있는 칸을 기록할 리스트
    melt_list = []

    # 각 칸을 순회하면서 얼음이 3개 이상 인접한 칸을 확인
    for i in range(K):
        for j in range(K):
            if arr[i][j] > 0:  # 얼음이 있는 경우만 확인
                adjacent_ice = 0

                for d in range(4):  # 4방향 확인
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0 <= nx < K and 0 <= ny < K and arr[nx][ny] > 0:  # 인접한 곳에 얼음이 있으면
                        adjacent_ice += 1

                # 인접한 얼음이 3개 미만인 경우에 얼음이 줄어듦
                if adjacent_ice < 3:
                    melt_list.append((i, j))

    # melt_list에 기록된 칸들의 얼음 양을 줄임
    for i, j in melt_list:
        arr[i][j] -= 1

def find_answer(N, arr):
    k = 2 ** N
    queue = deque()
    visit = [[False] * k for _ in range(k)]

    total_ice = 0
    largest_chunk = 0
    
    for i in range(k):
        total_ice += sum(arr[i])  # 전체 얼음 양 계산
    
    # 최대 덩어리 크기 계산
    for i in range(k):
        for j in range(k):
            if arr[i][j] > 0 and not visit[i][j]:  # 얼음이 있고 방문하지 않았을 경우
                chunk_size = 1
                queue.append((i, j))
                visit[i][j] = True

                while queue:
                    x, y = queue.popleft()
                    for d in range(4):  # 4방향 탐색
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < k and 0 <= ny < k and arr[nx][ny] > 0 and not visit[nx][ny]:
                            chunk_size += 1
                            visit[nx][ny] = True
                            queue.append((nx, ny))
                
                largest_chunk = max(largest_chunk, chunk_size)  # 가장 큰 덩어리 업데이트
    
    return total_ice, largest_chunk

    
                    
N, Q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(2 ** N)]
L = map(int, input().split())

for i in L:
    arr = lattice_rotation(i, arr)
    ice_melts(2 ** N, arr)

ans, ans1 = find_answer(N, arr)
print(ans, ans1, sep="\n")