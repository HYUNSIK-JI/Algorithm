import sys

p=10**6
prime=[False,False]+[True]*(p-1)
answer=[]
for i in range(2,p+1):
	if prime[i]:
		answer.append(i)
		for j in range(2*i,p+1,i):
			prime[j]=False

n=int(sys.stdin.readline())
check=False

if n<8:
	print(-1)
else:
	if n%2==0:
		ans=[2,2]
		n-=4
		for i in range(len(answer)):
			for j in range(len(answer)):
				sum_num=answer[i]+answer[j]
				if sum_num==n:
					ans.extend([answer[i],answer[j]])
					check=True
					break
			if check:
				break
		print(*ans)
	else:
		ans=[2,3]
		n-=5
		for i in range(len(answer)):
			for j in range(len(answer)):
				sum_num=answer[i]+answer[j]
				if sum_num==n:
					ans.extend([answer[i],answer[j]])
					check=True
					break
			if check:
				break
		print(*ans)