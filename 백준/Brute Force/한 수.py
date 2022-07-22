#n 값 입력
n = int(input())

# 한 수의 갯수 위한 변수 와 한 수를 판별 하기 위한 변수
cnt,count = 0, 0

#1~n까지
for a in range(1, n + 1):
    a = str(a)

    # 길이가 2이하인 수들은 한 수
    if len(a) <= 2:
        # 한 수의 갯수 +1
        cnt += 1
    # 길이가 2초과인 수들은 한수 인지 아닌지 판별해야한다.
    elif len(a) > 2:
        # 등차수열의 일정한 공차를 확인하기 위한 작업
        data = int(a[0]) - int(a[1])

        # a라는 숫자가 일정한 등차 수열인지 판별하기 위한 반복문
        for i in range(len(a)):

            # a 라는 숫자에 마지막 숫자는 그 뒤에 판별한 숫자가 없으므로 len(a) -1 까지만 판별을 위한 조건문
            if i != len(a) - 1:
                # 만약 a[i] 과 a[i+1]차이가 data와 같은지 판별을 위한 조건문
                if (int(a[i]) - int(a[i + 1])) == data:
                    # 같으면 count += 1
                    count += 1
        #만약 일정한 차이가 있으면 더했던 count 가 len(a) - 1 와 동일하면 그수는 한수이다.
        if count == len(a) - 1:
            # 한수 갯수 +1
            cnt += 1
            # 판별을 위했던 count 초기화
            count = 0
        else:
            count = 0
# 한수의 갯수 출력
print(cnt)