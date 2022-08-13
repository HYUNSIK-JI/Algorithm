def solution(clothes):
    # 종류 별 개수 파악을 위한 딕셔너리
    dic = {}

    for k, v in clothes:
        # 옷 종류별 개수 파악
        dic[v] = dic.get(v, 0) + 1
    answer = 1
    # 경우의수!
    for i in dic.values():
        answer *= (i + 1)
    # 마지막 마이너스는 아예 아무것도 입지 않는 경우의 수 빼기
    return answer - 1