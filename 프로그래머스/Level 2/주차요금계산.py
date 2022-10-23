def solution(fees, records):
    dic = {}
    answer = {}
    result = []
    for info in records:
        info = info.split()
        if info[2] == "IN":
            dic[info[1]] = info[0]
        else:
            k = dic[info[1]]

            h1, m1 = k.split(":")
            h2, m2 = info[0].split(":")
            answer[info[1]] = answer.get(info[1], 0) + (int(h2) - int(h1)) * 60 + int(m2) - int(m1)
            dic.pop(info[1])
    for i in dic:
        k = dic[i]
        h1, m1 = k.split(":")
        answer[i] = answer.get(i, 0) + (23 - int(h1)) * 60 + 59 - int(m1)
    answer = sorted([(k, v) for k, v in answer.items()])
    for i in answer:
        hap = 0
        k = i[1]
        if not k:
            result.append(hap)
        else:
            if k >= fees[0]:
                hap += fees[1]
                k -= fees[0]
                if k <= 0:
                    result.append(hap)
                else:
                    p1 = k / fees[2]
                    p2 = k // fees[2]
                    if p1 == p2:
                        hap += p2 * fees[3]
                        result.append(hap)
                    else:
                        hap += (p2 + 1) * fees[3]
                        result.append(hap)
            else:
                hap += fees[1]
                k -= fees[0]
                result.append(hap)
    return result