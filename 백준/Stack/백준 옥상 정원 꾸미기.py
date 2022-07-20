import sys

n=int(sys.stdin.readline())
num=[int(sys.stdin.readline()) for _ in range(n)]
answer=0
stack=[]


for i in range(n):
    while stack and stack[-1]<=num[i]: #stack이 빈공간이 아니고 마지막에 들어갔던 숫자가 num[i]번째 숫자보다 작으면
        stack.pop()#stack의 마지막에 들어왔던 변수를 pop()
    stack.append(num[i])
    answer+=len(stack)-1 ##자기자신을 제외한 길이 만큼 +1
print(answer)