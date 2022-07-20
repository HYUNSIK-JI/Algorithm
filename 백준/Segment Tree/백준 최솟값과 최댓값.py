#백준 2357번
import sys
from math import ceil,log
sys.setrecursionlimit(10000)

input=sys.stdin.readline

def mininum(left,right,start,end,node):
    if left>end or right<start: return 1000000000
    if left<=start and right>=end: return graph[node]
    mid=(start+end)//2
    return min(mininum(left,right,start,mid,node*2),mininum(left,right,mid+1,end,node*2+1))

def maxinum(left,right,start,end,node):
    if left>end or right<start: return 0
    if left<=start and right>=end: return graph1[node]
    mid=(start+end)//2
    return max(maxinum(left,right,start,mid,node*2),maxinum(left,right,mid+1,end,node*2+1))

def init(size):
    for i in range(size-1,0,-1):
        graph[i]=min(graph[i*2],graph[2*i+1])
        graph1[i]=max(graph1[i*2],graph1[2*i+1])

n,m=map(int,input().split())

size=2**ceil(log(n,2))
size_max=2*size

graph=[1000000000]*size_max
graph1=[0]*size_max

for i in range(n):
    k=int(input())
    graph[size+i]=k
    graph1[size+i]=k
init(size)

for _ in range(m):
    s,e=map(int,input().split())
    print(mininum(s-1,e-1,0,size-1,1),maxinum(s-1,e-1,0,size-1,1))