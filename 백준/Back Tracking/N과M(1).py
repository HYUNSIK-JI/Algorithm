import sys

def dfs(depth):

    if len(answer)==m:
        print(" ".join(map(str,answer)))
        return
    for i in range(1,n+1):
        if not i in answer:
            answer.append(i)
            dfs(i)
            answer.pop()
n,m=map(int,sys.stdin.readline().split())
answer=[]
dfs(0)