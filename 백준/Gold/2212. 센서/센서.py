import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
sensor=sorted(list(map(int,sys.stdin.readline().split())))

if k>=n:
	print(0)
	sys.exit()
	
distance=[]

for i in range(1,n):
	distance.append(sensor[i]-sensor[i-1])

distance.sort(reverse=True)

for _ in range(k-1):
	distance.pop(0)

print(sum(distance))