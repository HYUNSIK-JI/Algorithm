import sys
from collections import deque

dx=[0,0,0,1,-1,1,-1,-1,1]
dy=[0,1,-1,0,0,1,1,-1,-1]

maps=[]
walls=[]
for i in range(8):
	a=list(input())
	for j in range(8):
		if a[j]=="#":
			walls.append((i,j))
	maps.append(a)
queue=deque()
queue.append((7,0))
visit=[[False]*8 for _ in range(8)]
answer=0
while queue:
	for _ in range(len(queue)):
		x,y=queue.popleft()
		if (x,y) in walls:
			continue
		if x==0 and y==7:
			answer=1
			break
		for i in range(9):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<8 and 0<=ny<8 and not visit[nx][ny] and not (nx,ny) in walls:
				visit[nx][ny]=True
				queue.append((nx,ny))
	if walls:
		visit=[[False]*8 for _ in range(8)]
	next_walls=[]
	for x,y in walls:
		if 0<=x<7:
			next_walls.append((x+1,y))
	walls=next_walls
print(answer)