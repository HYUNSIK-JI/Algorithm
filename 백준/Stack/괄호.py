import sys

n = int(sys.stdin.readline())
for i in range(n):
    a = sys.stdin.readline().strip()
    cnt=0
    for j in a:
        if j == "(":
            cnt+=1
        elif j == ")":
            cnt-=1

        if cnt==-1:
            answer = "NO"
            break
    if cnt == 0 and a[-1] == ")":
        answer = "YES"
    else:
        answer = "NO"
    print(answer)