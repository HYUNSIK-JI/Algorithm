# 문제 설명
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.
# 입출력 예

# number  k   return
# "1924"  2   "94"
# "1231234"   3   "3234"
# "4177252841"    4   "775841"

def solution(number, k):
    stack = []
    
    for i in range(len(number)):
        # 스택안에 요소가 있고 제거 할 수가 남아 있다면 while문 으로
        while stack and k:
            # 만약 스택의 마지막 요소 가 numbers[i] 요소 보다 작은지 판별 하는 조건문
            if stack[-1] < number[i]:
                # 작다면 스택의 마지막 요소 제거
                stack.pop()
                # 제거했으니 제거 할 수 -1
                k -= 1
            #작지 않다면 break 통해 while 탈출
            else:
                break
        # 스택에 요소들을 게속하여 넣음
        stack.append(number[i])
    # 만약 4321 과 같은 작은수가 존재하지 않는다면 k개는 남아 있으므로 k개 만큼 앞에서 슬라이싱
    if k:
        return str("".join(map(str,stack[:len(number) - k])))
    else:
        return str("".join(map(str, stack)))