import sys
from collections import deque

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def BFS():
	queue=deque()
	queue.append([0,0,1])
	visit=[[[0]*2 for _ in range(m)]for _ in range(n)]
	visit[0][0][1]=1

	while queue:
		a,b,p=queue.popleft()
		if a==n-1 and b==m-1:
			return visit[a][b][p]
		for i in range(4):
			nx=dx[i]+a
			ny=dy[i]+b

			if 0<=nx<n and 0<=ny<m:
				if graph[nx][ny]==1 and p==1:
					visit[nx][ny][0]=visit[a][b][1]+1
					queue.append([nx,ny,0])
				elif graph[nx][ny]==0 and visit[nx][ny][p]==0:
					visit[nx][ny][p]=visit[a][b][p]+1
					queue.append([nx,ny,p])
	return -1

n,m=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

print(BFS())