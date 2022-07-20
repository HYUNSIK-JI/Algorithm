import sys
import heapq
input=sys.stdin.readline
p=5000000

prime=[False,False]+[True]*(p-1)
for i in range(2,p+1):
    if prime[i]:
        for j in range(2*i,p+1,i):
            prime[j]=False
n=int(input())
god,master=[],[]
god_score,master_score=0,0
check=[]
for i in range(n):
    a,b=map(int,input().split())
    if prime[a]:
        if a in check:
            god_score-=1000
        else:
            check.append(a)
            heapq.heappush(god,(-a,a))
    else:
        if len(master)<3:
            master_score+=1000
        else:
            n_list=[]
            for _ in range(3):
                n_list.append(heapq.heappop(master))
            master_score+=n_list[2][1]
            for k,w in n_list:
                heapq.heappush(master,(k,w))
    if prime[b]:
        if b in check:
            master_score-=1000
        else:
            check.append(b)
            heapq.heappush(master,(-b,b))
    else:
        if len(god)<3:
            god_score+=1000
        else:
            n_list = []
            for _ in range(3):
                n_list.append(heapq.heappop(god))
            god_score += n_list[2][1]
            for k, w in n_list:
                heapq.heappush(god, (k, w))
if god_score>master_score:
    print("소수의 신 갓대웅")
elif god_score<master_score:
    print("소수 마스터 갓규성")
else:
    print("우열을 가릴 수 없음")