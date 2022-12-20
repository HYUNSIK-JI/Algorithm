import sys
from heapq import heappush, heappop

INF = sys.maxsize
input = sys.stdin.readline

class Solution():
    def __init__(self):
        self.n, self.m, self.t, self.d = map(int, input().split())
        self.maps = []
        self.row = []
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        self.q = []
    def change(self):
        self.row = list(input().rstrip())
        for i in range(self.m):
            k = ord(self.row[i])
            if k >= 97:
                self.row[i] = k - 71
            else:
                self.row[i] = k - 65
        self.maps.append(self.row)

    def dijstra(self, s_x, s_y):
        queue = []
        heappush(queue, (0, s_x, s_y))

        dis = [[INF] * self.m for _ in range(self.n)]
        dis[s_x][s_y] = 0

        while queue:
            dist, x, y = heappop(queue)

            if dis[x][y] < dist:
                continue
            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]

                if 0 <= nx < self.n and 0 <= ny < self.m:
                    g = self.maps[nx][ny] - self.maps[x][y]

                    if abs(g) <= self.t:
                        if g <= 0:
                            time = 1
                        else:
                            time = g ** 2
                        cost = dist + time
                        if cost < dis[nx][ny]:
                            dis[nx][ny] = cost
                            heappush(queue, (cost, nx, ny))
        return dis
    def cal(self, n, m, lst):
        for i in range(n):
            for j in range(m):
                if lst[i][j] <= self.d:
                    heappush(self.q, (-self.maps[i][j], i, j))
        return self.q
    def ans(self, lst, S):
        while lst:
            dist, x, y = heappop(lst)
            E = self.dijstra(x, y)

            if E[0][0] + S[x][y] <= self.d:
                print(self.maps[x][y])
                break

k = Solution()
for _ in range(k.n):
    k.change()
s = k.dijstra(0, 0)
w = k.cal(k.n, k.m, s)
k.ans(w, s)