import sys

input = sys.stdin.readline
p = 10 ** 6 # 최대숫자가 백만
prime = [False, False] + [True] * (p - 1) # 백만개의 숫자를 소수인지 아닌지 판별하기 위한 불리언 값 설정

for i in range(1, int(p ** 0.5) + 1): # 백만 => 제곱승이 짝수 이므로 10 ** 3 까지만 돌려도 된다.
    if prime[i]: # 만약 소수라면
        for j in range(2 * i, p + 1, i): # 소수의 배수는 소수가 아니다. 에라토스테네스의체
            prime[j] = False # 소수가 아닌걸로 설정
while True:
    n = int(input()) # 짝수 입력
    if not n: # 만약 0이라면 무한 루프 종료
        break

    for i in range(3, n + 1):
        if prime[i] and prime[n - i]: # i가 소수이고 n - i 가 소수라면 골드바흐 추측에 적합한 숫자들이다.
            print(f"{n} = {i} + {n - i}")
            break