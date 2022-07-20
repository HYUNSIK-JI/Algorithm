import sys

n=int(sys.stdin.readline())
sequence=sorted(list(map(int,sys.stdin.readline().split())))

left,right=0,n-1
answer=2e9+1
result=[]

while left<right:
	hap=sequence[left]+sequence[right]

	if abs(hap)<answer:
		answer=abs(hap)
		result=[sequence[left],sequence[right]]

	if hap<0:
		left+=1
	else:
		right-=1
print(result[0],result[1])