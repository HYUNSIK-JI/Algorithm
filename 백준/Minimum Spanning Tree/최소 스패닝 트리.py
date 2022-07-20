import sys

def find_parent(x):
	if parent[x]!=x:
		parent[x]=find_parent(parent[x])
	return parent[x]
def union_parent(parent,a,b):
	a=find_parent(a)
	b=find_parent(b)
	if a<b:
		parent[b]=a
	else:
		parent[a]=b
v,e=map(int,sys.stdin.readline().split())
parent=[i for i in range(v+1)]
edges=[]
for _ in range(e):
	a,b,cost=map(int,sys.stdin.readline().split())
	edges.append((cost,a,b))
edges.sort()
answer=0
for cost,a,b in edges:
	if find_parent(a)!=find_parent(b):
		union_parent(parent,a,b)
		answer+=cost
print(answer)