import sys

input = sys.stdin.readline

k = 10 ** 7

# 에라토스테네스의 체를 이용한 소수 판별
prime = [False, False] + [True] * (k + 1)

for i in range(2, k + 1):
    if prime[i]:
        for j in range(i * i, k + 1, i):
            prime[j] = False

# 소수 리스트 생성
primes = [i for i, is_prime in enumerate(prime) if is_prime]

# 입력 받기
N = int(input())
number_list = list(map(int, input().split()))

# 소인수 분해 결과를 저장할 리스트
factorizations = []

# 소인수 분해 수행
for number in number_list:
    factors = []
    original_number = number
    for p in primes:
        if p * p > number:
            break
        while not number % p:
            factors.append(p)
            number //= p
    if number > 1:
        factors.append(number)
    factorizations.append(factors)

# 결과 출력
for idx, number in enumerate(number_list):
    print(' '.join(map(str, factorizations[idx])))
