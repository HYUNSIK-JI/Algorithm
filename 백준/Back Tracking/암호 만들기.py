import sys

input = sys.stdin.readline

def back(start):
    # 암호문의 길이 l초과 시 return
    if len(ciphertext) > l:
        return
    # 암호문의 길이 l 일때 문제에서 요구 하는 암호문이 맞는지 파악
    if len(ciphertext) == l:
        # l의 길이를 가진 암호문 set화
        k = set(ciphertext)

        # 암호문에 있는 모음들을 제거 자음만 남음
        cip = k - vowel
        # 자음의 길이 2이상이고 암호문의 길이에서 자음의 길이를 빼면 모음이므로 모음이 1개 이상일때 찾기위한 조건문
        if len(cip) >= 2 and l - len(cip) >= 1:
            #출력
            print("".join(ciphertext))
        return
    #combination 이므로 start로 for 시작지점 지정
    for i in range(start,c):
        #같은 알파벳이 들어가지 않도록 하기 위해 중복 제거 조건문
        if character[i] not in ciphertext:
            ciphertext.append(character[i])
            # for문 start 지점을 지정하기 위한 i 값으로 함수시작
            back(i)
            ciphertext.pop()

# 암호문의 길이 와 알파벳 의 개수
l, c = map(int, input().split())

# 알파벳들
character = sorted(list(input().rstrip().split()))

# 모음
vowel = set("aeiou")

# 암호문을 넣을 리스트
ciphertext = []

# combination
back(0)