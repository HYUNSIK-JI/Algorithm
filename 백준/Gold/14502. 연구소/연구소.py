import sys
import copy

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def selecet_wall(start, count):
	global Max_count
	if count == 3:
		second_Map=copy.deepcopy(Map)
		for i in range(len(virus)):
			r, c = virus[i]
			spread_virus(r, c, second_Map)
		safe_area=sum(i.count(0) for i in second_Map)
		Max_count=max(safe_area, Max_count)
		return True
	else:
		for i in range(start, n * m):
			r = i // m
			c = i % m
			if not Map[r][c]:
				Map[r][c] = 1
				selecet_wall(start, count + 1)
				Map[r][c] = 0
def spread_virus(r,c,second_Map):
	if second_Map[r][c] == 2:
		for i in range(4):
			nr = r + dx[i]
			nc = c + dy[i]
			if 0<= nr < n and 0 <= nc < m and not second_Map[nr][nc]:
				second_Map[nr][nc] = 2
				spread_virus(nr, nc, second_Map)
n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
virus = []
Max_count = 0

for i in range(n):
	for j in range(m):
		if Map[i][j] == 2:
			virus.append((i, j))
selecet_wall(0, 0)
print(Max_count)