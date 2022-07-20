import sys

n,m=map(int,sys.stdin.readline().split())
sequence=list(map(int,sys.stdin.readline().split()))

left,right=0,1
cnt=0

while right<=n and left<=right:
	hap=sequence[left:right]
	answer=sum(hap)

	if answer==m:
		cnt+=1
		right+=1

	elif answer<m:
		right+=1
	else:
		left+=1
print(cnt)