from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(i,j):
	global px,py
	queue=deque()
	queue.append((i,j))
	visit[i][j]=True
	while queue:
		x,y=queue.popleft()
		px,py=x,y
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<n:
				if not visit[nx][ny] and maps[nx][ny]!=0:
					visit[nx][ny]=True
					queue.append((nx,ny))
for test_case in range(1,int(input())+1):
	n=int(input())
	maps=[list(map(int,input().split())) for _ in range(n)]
	position=[]
	visit=[[False]*n for _ in range(n)]
	cnt=0
	s_x,s_y,f_x,f_y=0,0,0,0
	answer=[]
	for i in range(n):
		for j in range(n):
			if not visit[i][j] and maps[i][j]!=0:
				answer.append((i,j))
				bfs(i,j)
				cnt+=1
				answer.append((px,py))
	for i in range(0,len(answer),2):
		x1=(answer[i+1][0]-answer[i][0])+1
		y1=(answer[i+1][1]-answer[i][1])+1
		position.append((x1,y1,x1*y1))
	print(f"#{test_case}",end=" ")
	print(cnt,end=" ")
	position.sort(key=lambda x:(x[2],x[0]))
	for i in position:
		print(i[0],i[1],end=" ")
	print()