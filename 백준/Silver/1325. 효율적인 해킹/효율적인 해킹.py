import sys
from collections import deque

def BFS(v):
	cnt=0
	queue=deque()
	queue.append(v)

	visit=[False]*(n+1)
	visit[v]=True

	while queue:
		x=queue.popleft()
		cnt+=1
		for i in graph[x]:
			if visit[i]==False:
				visit[i]=True
				queue.append(i)
	return cnt
n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]

for i in range(m):
	a,b=map(int,sys.stdin.readline().split())
	graph[b].append(a)

mx=0
answer=[]

for i in range(1,n+1):
	if graph[i]:
		value=BFS(i)
		if mx<=value:
			if mx<value:
				answer=[]
			mx=value
			answer.append(i)
print(*answer)