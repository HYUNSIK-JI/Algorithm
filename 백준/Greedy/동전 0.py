import sys

n,k=map(int,sys.stdin.readline().split())
coin=[]
cnt=0

for _ in range(n):
    coin.append(int(input()))

for i in range(n-1,-1,-1):
    if k==0:
        break
    if coin[i]>k:
        continue
    cnt+= k // coin[i]
    k%= coin[i]
print(cnt)