import sys

def dfs(start,hap):
	global answer

	if start>=n:
		return
	hap+=sequence[start]

	if hap==s:
		answer+=1
	dfs(start+1,hap)
	dfs(start+1,hap-sequence[start])

n,s=map(int,sys.stdin.readline().split())
sequence=list(map(int,sys.stdin.readline().split()))
answer=0
dfs(0,0)
print(answer)