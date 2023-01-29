import sys
n=int(sys.stdin.readline())
dp=[]

for i in range(n):
	dp.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,len(dp)):
	dp[i][0]=dp[i][0]+min(dp[i-1][1],dp[i-1][2])
	dp[i][1]=dp[i][1]+min(dp[i-1][0],dp[i-1][2])
	dp[i][2]=dp[i][2]+min(dp[i-1][0],dp[i-1][1])
print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))