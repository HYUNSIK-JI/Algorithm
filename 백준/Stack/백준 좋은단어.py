import sys

input=sys.stdin.readline

#n번 반복
n=int(input())
#좋은 단어를 카운트 하기 위한 변수 선언
cnt=0

for _ in range(n):
    word=input().rstrip()
    # word의 한글자 한글자를 담기 위한 리스트 선언
    stack=[]
    for j in range(len(word)):
        #stack에 담겨져 있고 word[j]의 글자가 stack의 마지막 글자와 동일하면
        if stack and word[j]==stack[-1]:
            #stack의 마지막 요소를 제거
            stack.pop()
        #if절 조건문의 반대라면
        else:
            #stack에 word[j]요소를 추가
            stack.append(word[j])
    #스택이 비어 있다면
    if not stack:
        #좋은 단어 이므로 +1
        cnt+=1
#좋은 단어 갯수 출력
print(cnt)