def solution(survey, choices):
    ans = ''
    scores = [0] + [3, 2, 1, 0, 1, 2, 3]
    table = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i, num in zip(survey, choices):
        if num > 4:
            table[i[1]] += scores[num]
        elif num < 4:
            table[i[0]] += scores[num]
    if table['R'] >= table['T']:
        ans += 'R'
    else:
        ans += 'T'
    
    if table['C'] >= table['F']:
        ans += 'C'
    else:
        ans += 'F'
    if table['J'] >= table['M']:
        ans += 'J'
    else:
        ans += 'M'
    if table['A'] >= table['N']:
        ans += 'A'
    else:
        ans += 'N'
    return ans