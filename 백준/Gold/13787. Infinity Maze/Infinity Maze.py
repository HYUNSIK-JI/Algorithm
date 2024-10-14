import sys; input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def get_direction(c):
    return {
        'N': 0,
        'E': 1,
        'S': 2,
        'W': 3
    }.get(c, -1)

directions = ['N', 'E', 'S', 'W']

while True:
    h, w, moves = map(int, input().split())
    if not (h + w):
        break

    arr = []
    
    sx, sy, sd = 0, 0, 0  # 시작 좌표 및 방향

    for i in range(h):
        temp = list(input().strip())
        for j in range(w):
            d = get_direction(temp[j])
            if d >= 0:
                sx, sy, sd = j, i, d  # 시작 좌표와 방향 저장
        arr.append(temp)
    
    visit = [[[0 for _ in range(4)] for _ in range(w)] for _ in range(h)]
    loop = []


    while moves > 0:
        visit[sy][sx][sd] += 1

        if visit[sy][sx][sd] == 2:
            loop.append((sy, sx, sd))
        
        elif visit[sy][sx][sd] == 3:
            moves %= len(loop)
            sy, sx, sd = loop[moves]
            break

        moved = False  # 이동 여부 체크용 변수

        for i in range(4):
            nd = (sd + i) % 4
            nx = sx + dx[nd]
            ny = sy + dy[nd]

            if 0 <= nx < w and 0 <= ny < h and arr[ny][nx] != "#":
                sx = nx
                sy = ny
                sd = nd  # 방향을 현재 방향으로 설정
                moves -= 1
                moved = True  # 이동했음을 표시
                break

        if not moved:
            sd = (sd + 1) % 4  # 이동하지 못했다면 방향을 90도 회전

    print(sy + 1, sx + 1, directions[sd])