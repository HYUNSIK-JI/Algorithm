import sys
import math

prime_result=[]
def prime(n):
	if n<2:
		return 0
	else:
		for i in range(2,int(math.sqrt(n))+1):
			if n%i==0:
				return 0
	return prime_result.append(n)

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

for i in range(n,m+1):
	prime(i)
	
if len(prime_result)!=0:
	print(sum(prime_result))
	print(min(prime_result))
else:
	print(-1)