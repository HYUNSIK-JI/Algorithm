
def solution(today, terms, privacies):
    alpha = {}
    for i in range(len(terms)):
        alpha[terms[i][0]] = alpha.get(terms[i][0], 0) + int(terms[i][2:])
    
    ans = []
    
    todays = today.split(".")
    a = int(todays[0]) * 12 * 28 + int(todays[1]) * 28 + int(todays[2])
    for i in range(len(privacies)):
        datas = privacies[i].split(" ")
        dates = datas[0].split(".")
        
        year = dates[0]
        month = dates[1]
        day = dates[2]
        
        num = alpha[datas[1]]
        
        b = int(year) * 12 * 28 + int(month) * 28 + int(num) * 28 + int(day)
        
        if a >= b:
            ans.append(i + 1)
    return ans
        