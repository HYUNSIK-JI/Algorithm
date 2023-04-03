def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for i in range(len(photo)):
        hap = 0
        for j in photo[i]:
            if not j in name:
                hap += 0
            else:
                hap += dic[j]
        answer.append(hap)
    return answer