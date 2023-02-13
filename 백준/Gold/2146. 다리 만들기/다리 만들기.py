import sys
from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(a,b):
	global cnt
	queue=deque()
	queue.append((a,b))
	Map[a][b]=cnt
	while queue:
		x,y=queue.popleft()

		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<n and visit[nx][ny]==False and Map[nx][ny]==1:
				visit[nx][ny]=True
				Map[nx][ny]=cnt
				queue.append((nx,ny))
def bfs2(k):
	global answer
	distance=[[-1]*n for _ in range(n)]
	queue=deque()

	for i in range(n):
		for j in range(n):
			if Map[i][j]==k:
				queue.append((i,j))
				distance[i][j]=0
	while queue:
		x,y=queue.popleft()
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<n:
				if Map[nx][ny]>0 and Map[nx][ny]!=k:
					answer=min(answer,distance[x][y])
				elif Map[nx][ny]==0 and distance[nx][ny]==-1:
					distance[nx][ny]=distance[x][y]+1
					queue.append((nx,ny))
n=int(sys.stdin.readline())
Map=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit=[[False for _ in range(n)] for _ in range(n)]
cnt=1
answer=1e9
for i in range(n):
	for j in range(n):
		if Map[i][j]==1 and visit[i][j]==False:
			visit[i][j]=True
			bfs(i,j)
			cnt+=1
for i in range(1,cnt):
	bfs2(i)
print(answer)