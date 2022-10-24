def solution(X, Y):
    answer = ''
    check = set(X) & set(Y)
    if not check:
        return "-1"
    else:
        check = list(check)
        check.sort(reverse=True)
        for i in check:
            a = X.count(i)
            b = Y.count(i)
            if a > b:
                answer += str(i * b)
            elif a < b:
                answer += str(i * a)
            else:
                if a == 1:
                    answer += str(i)
                else:
                    answer += str(i * a)
        if answer[0] == "0":
            return "0"
        else:
            return answer