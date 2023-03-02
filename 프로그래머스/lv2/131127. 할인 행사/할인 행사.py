import copy

def solution(want, number, discount):
    dic = {}
    ans = 0
    for i in range(len(want)):
        dic[want[i]] = dic.get(want[i], 0) + number[i]
    wantSet = set(dic)

    for i in range(10):
        if discount[i] in dic.keys():
            dic[discount[i]] -= 1
            if not dic[discount[i]]:
                wantSet.remove(discount[i])
    if not len(wantSet):
        ans += 1        
    for j in range(10, len(discount)):

        if discount[j] in dic.keys():
            dic[discount[j]] -= 1
            if not dic[discount[j]]:
                wantSet.remove(discount[j])


        if discount[j - 10] in dic.keys():
            dic[discount[j - 10]] += 1
            if dic[discount[j - 10]] == 1:
                wantSet.add(discount[j - 10])

        if not len(wantSet):
            ans += 1 

    return ans