import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
maps=[]

r_x,r_y=0,0
b_x,b_y=0,0
for i in range(n):
    a=list(input().rstrip())
    for j in range(m):
        #빨간 구슬 위치
        if a[j]=="R":
            r_x,r_y=i,j
        #파란 구슬 위치
        elif a[j]=="B":
            b_x,b_y=i,j
    maps.append(a)
#상,하,좌,우
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(a,b,c,d):
    queue=deque()
    queue.append((a,b,c,d))

    visit=[] #방문여부를 판단하기 위한 리스트
    visit.append((a,b,c,d))
    count=0
    while queue:
        for _ in range(len(queue)):
            r_x,r_y,b_x,b_y=queue.popleft()

            #움직인 횟수가 10이상 이면 -1 출력
            if count>10:
                print(-1)
                return
            # 현재 빨간 구슬의 위치가 구멍이라면 count 출력
            if maps[r_x][r_y]=="O":
                print(count)
                return
            #4방향 탐색을 위한 반복문
            for i in range(4):
                n_rx,n_ry=r_x,r_y
                # 벽 "#"일때 까지 혹은 구멍일 때까지 움직임
                while True:
                    n_rx+=dx[i]
                    n_ry+=dy[i]
                    # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                    if maps[n_rx][n_ry]=="#":
                        n_rx-=dx[i]
                        n_ry-=dy[i]
                        break
                    if maps[n_rx][n_ry]=="O":
                        break
                n_bx,n_by=b_x,b_y
                # #일 때 까지 혹은 구멍일 때 까지 움직임
                while True:
                    n_bx+=dx[i]
                    n_by+=dy[i]
                    # 벽인 경우 왔던 방향 그대로 한칸 뒤로 이동
                    if maps[n_bx][n_by]=="#":
                        n_bx-=dx[i]
                        n_by-=dy[i]
                        break
                    if maps[n_bx][n_by]=="O":
                        break
                # 파란 구슬이 먼저 구멍에 들어 가거나 동시에 들어가면 안됨 따라서 이 경우 무시
                if maps[n_bx][n_by]=="O":
                    continue
                # 두 구슬의 위치가 같다면
                if n_rx==n_bx and n_ry==n_by:
                    # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                    if abs(n_rx-r_x) + abs(n_ry-r_y)>abs(n_bx-b_x)+abs(n_by-b_y):
                        n_rx-=dx[i]
                        n_ry-=dy[i]
                    else:
                        n_bx-=dx[i]
                        n_by-=dy[i]
                # 방문 해본적이 없는 위치라면 새로 큐에 추가후 방문처리
                if (n_rx,n_ry,n_bx,n_by) not in visit:
                    queue.append((n_rx,n_ry,n_bx,n_by))
                    visit.append((n_rx,n_ry,n_bx,n_by))
        count+=1
    #10회가 초과하지 않았지만 10회내에도 구멍에 들어 가지 못한 경우
    print(-1)
bfs(r_x,r_y,b_x,b_y)