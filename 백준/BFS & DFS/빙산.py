import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
maps=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]###빙산

dx,dy=[0,0,-1,1],[1,-1,0,0] #4방탐색

year,cnt,check=0,0,0

q=deque()

def BFS(x,y):
	q.append((x,y))

	while q:
		x,y=q.popleft()
		visit[x][y]=1

		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]

			if 0<=nx<n and 0<=ny<m:
				if maps[nx][ny]!=0 and visit[nx][ny]==0: ###한번도 방문하지 않았으며 얼음이 녹지않은곳
					visit[nx][ny]=1#방문처리
					q.append((nx,ny))
				elif maps[nx][ny]==0:
					count[x][y]+=1 #4방탐색을통해 얼음근처의 바닷물이 맞닿는곳이 있다면 +1
	return 1
while True:
	visit=[[0]*m for _ in range(n)] ### 얼음근처 맞닿는 바다의 수만큼 차감해주고 나서 0이 되는곳이 있기 때문에 게속하여 방문초기화
	count=[[0]*m for _ in range(n)] ### 위와 동일
	result=[]

	for i in range(n):
		for j in range(m):
			if maps[i][j]!=0 and visit[i][j]==0:
				result.append(BFS(i,j)) ### 얼음이 몇덩이로 있는지 체크하기 위한 result

	for i in range(n):
		for j in range(m):
			maps[i][j]-=count[i][j] ###1년마다 바다가 맞닿는곳만큼 얼음을 녹임!
			if maps[i][j]<0: ##단 얼음이 음수로 됫을때
				maps[i][j]=0 ## 0으로 처리

	if len(result)==0: ### 빙산이 다 녹아없어졌으면 break
		break
	elif len(result)>=2:## 빙산이 2덩이 이상 살아있을시 
		check=1 ## 체크 True
		break
	year+=1

if check: ##빙산이 2덩이 이상살아있을시
	print(year) ## 몇년걸렸는지 체크
else:
	print(0)##그게아니라면 0출력 