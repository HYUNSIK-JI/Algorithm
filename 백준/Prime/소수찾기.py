import sys

p=1000 # N의 수 범위가 1~1000 이므로 1000으로 설정
prime=[False,False]+[True]*(p-1) #에라토스테네스의 체 활용하기 위한 리스트

for i in range(2,p+1): # 2~1001 까지 반복문
	if prime[i]: # 만약 우리 찾던 소수 라면
		for j in range(2*i,p+1,i): # 소수의 배수는 소수가 아니다 (에라토스테네스 체 논리)
			prime[j]=False # 소수가 아니므로 False처리
### n개 만큼 매번 소수가 맞는지 아닌지 시간초과를 줄이기 위해 n값을 받기전에 N의 수 범위 만큼 미리 소수판정
n=int(sys.stdin.readline()) #몇개 의 숫자를 판정 할것인지 위한 값 선언 
lst=list(map(int,sys.stdin.readline().split())) # n개의 자연수를 리스트에 선언
cnt=0 # 소수가 몇개 인지 카운트 하기 위한 변수

for i in lst: # lst안에 있는 숫자를 순서대로 i에 대입하여 나오게하는 반복문
	if prime[i]: # 그것이 소수라면
		cnt+=1 # 카운트
print(cnt) # 소수의 갯수