import sys
from collections import deque

# 4방향 탐색을 위한 변수선언
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x,y):
  # 큐 선언
  queue = deque()

  # 스타트할 곳을 x,y 선언
  queue.append((x,y))

  # 첫 방문 1번 지나간곳이기에 1로 선언 및 다시 방문 하지 않기 위함
  visit[x][y] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      # 4방향 탐색을 위한 변수들 선언
      nx = x + dx[i]
      ny = y + dy[i]

      # 리스트의 범위를 넘지 않기 위함
      if 0<= nx < n and 0<= ny < m:
        # 지나가는곳이 이동할수 있는 곳 ("1")인지 그리고 방문 하지 않은곳인지 판별
        if maps[nx][ny] == "1" and visit[nx][ny] == 0:
          # 지나 갈수 있는 곳이고 전에 방문했던것 보다 한칸더 간것이기에 + 1
          visit[nx][ny] = visit[x][y] + 1
          #지나 갈수 있는 곳이 도착지라면
          if nx == n - 1 and ny == m -1:
            # 몇번만에 방문했는지 리턴
            return visit[nx][ny]
          queue.append((nx,ny))

input = sys.stdin.readline

#세로 가로 길이를 나타내는 n, m 값 선언
n, m = map(int, input().split())

#미로
maps = [list(input().rstrip()) for _ in range(n)]

#방문한 곳은 다시 들리지 않기 위한 것과 몇번만에 도착지에 가는지 위한 리스트 선언
visit = [[0] * m for _ in range(n)]

#정답
print(bfs(0, 0))