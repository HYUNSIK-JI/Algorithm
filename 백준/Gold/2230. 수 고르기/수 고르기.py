import sys

n,m=map(int,sys.stdin.readline().split())
lst=[]
for _ in range(n):
	lst.append(int(sys.stdin.readline()))
lst.sort()
left,right=0,0
p=2e9

while left<n and right<n:
	hap=lst[right]-lst[left]

	if hap<m:
		right+=1
	else:
		if p>hap:
			p=hap
		left+=1
print(p)