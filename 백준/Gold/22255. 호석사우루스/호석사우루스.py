import sys
from heapq import heappush, heappop

INF = sys.maxsize
input = sys.stdin.readline

class Solution():
    def __init__(self):
        self.N = list(map(int, input().split()))
        self.position = list(map(int, input().split()))
        self.queue = []
        self.maps = [list(map(int, input().split())) for _ in range(self.N[0])]
        self.dis = [[[INF] * 3 for _ in range(self.N[1])] for _ in range(self.N[0])]
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def cal(self, nx, ny, dist, c):
        if 0 <= nx < self.N[0] and 0 <= ny < self.N[1] and not self.maps[nx][ny] == -1:
            cost = dist + self.maps[nx][ny]

            if cost < self.dis[nx][ny][(c + 1) % 3]:
                self.dis[nx][ny][(c + 1) % 3] = cost
                heappush(self.queue, (cost, c + 1, nx, ny))

    def dijstra(self):
        heappush(self.queue, (0, 1, self.position[0] - 1, self.position[1] - 1))
        self.dis[self.position[0] - 1][self.position[1] - 1][1] = 0

        while self.queue:
            dist, c, x, y = heappop(self.queue)

            if x == (self.position[2] - 1) and y == (self.position[3] - 1):
                return dist

            if not c % 3:
                for i in range(4):
                    nx = x + self.dx[i]
                    ny = y + self.dy[i]

                    self.cal(nx, ny, dist, c)

            elif c % 3 == 1:
                for i in range(2):
                    nx = x + self.dx[i]
                    ny = y + self.dy[i]

                    self.cal(nx, ny, dist, c)
            else:
                for i in range(2, 4):
                    nx = x + self.dx[i]
                    ny = y + self.dy[i]

                    self.cal(nx, ny, dist, c)
        return -1

answer = Solution()
print(answer.dijstra())
