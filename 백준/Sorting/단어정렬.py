import sys

#입력 시간을 줄이기 위한 것
input = sys.stdin.readline

#단어의 수
n = int(input())

#단어 와 단어의 길이를 받을 리스트
words = []

for _ in range(n):
    #단어 입력
    word = input().rstrip()
    #단어의 길이
    word_len = len(word)

    #단어 와 단어의 길이 추가
    words.append((word,word_len))
#단어 중복 제거
words=list(set(words))

#람다식을 이용해 단어의 길이로 오름차순 정리 후 길이가 같은것은 사전 순으로 정리
words.sort(key=lambda x:(x[1],x[0]))

#words안에 있는 요소 꺼내기
for word in words:
    #요소 보여주기
    print(word[0])