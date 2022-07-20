from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(a,b):
	global x1,y1
	queue=deque()
	queue.append((a,b))
	visit[a][b]=True

	while queue:
		x,y=queue.popleft()
		x1,y1=x,y
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and maps[nx][ny]=="#":
				visit[nx][ny]=True
				queue.append((nx,ny))
for test_case in range(1,int(input())+1):
	n=int(input())
	maps=[]
	x1,y1=0,0
	p=0
	position=[]
	visit=[[False]*n for _ in range(n)]

	for i in range(n):
		a=list(input())
		for j in range(len(a)):
			if a[j]=="#":
				p+=1
		maps.append(a)
	for i in range(n):
		for j in range(n):
			if maps[i][j]=="#" and not visit[i][j]:
				position.append((i,j))
				bfs(i,j)
				position.append((x1,y1))
	k=len(position)
	position=sorted(list(set(position)))
	x,y=((position[-1][0]-position[0][0])+1),((position[-1][1]-position[0][1])+1)

	if x==y and k==2 and x*y==p:
		print(f"#{test_case} {'yes'}")
	else:
		print(f"#{test_case} {'no'}")