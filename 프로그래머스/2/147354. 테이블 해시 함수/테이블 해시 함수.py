def sort_value(data, col):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    return data

def cal_mod(data, n):
    hap = 0
    
    for num in data:
        hap += num % n
    
    return hap

def cal_xor(vals):
    cal = 0
    for num in vals:
        cal ^= num
    return cal

def solution(data, col, row_begin, row_end):
    data = sort_value(data, col)
    answer = []
    for number in range(len(data)):
        if not (row_begin -1 <= number <= row_end -1):
            continue
        answer.append(cal_mod(data[number], number + 1))
    return cal_xor(answer)