# 정렬해주기 위한 리스트
ans = []
for _ in range(int(input())):
    # 합
    hap = 0
    k = input()
    for i in k:
        # 만약 그것이 숫자라면
        if i.isdigit():
            # 합산
            hap += int(i)
    # 원래 본 모습과, 합을 넣어줌
    ans.append((k, hap))

# x의 길이, hap이 작은, 사전순으로 정렬
ans.sort(key=lambda x:(len(x[0]), x[1], x))
for i in ans:
    print(i[0])