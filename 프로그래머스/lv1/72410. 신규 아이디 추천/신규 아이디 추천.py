import re

def step_one(data):
    return data.lower()
def step_two(data):
    accecpt_str = ['.', '-', '_']
    ans = []
    for i in data:
        if i.isdigit() or i.isalpha() or i in accecpt_str:
            ans.append(i)
        elif not i in accecpt_str:
            continue
    return "".join(ans)
def step_three(data):
    data = re.sub(r'\.+', '.', data)
    return data

def step_four(data):
    if data[0] == "." and data[-1] != ".":
        data = data[1:]
    elif data[0] != "." and data[-1] == ".":
        data = data[:-1]
    elif data[0] == "." and data[-1] == ".":
        data = data[1:-1]
    return data

def step_five(data):
    if not data:
        data += "a"
    return data
def step_six(data):
    ans = []
    if len(data) >= 16:
        data = data[:15]
    if data[-1] == ".":
        data = data[:-1]
    return data
def step_seven(data):
    while len(data) < 3:
        data += data[-1]
    return data
def solution(new_id):
    answer = step_one(new_id)
    answer = step_two(answer)
    answer = step_three(answer)
    answer = step_four(answer)
    answer = step_five(answer)
    answer = step_six(answer)
    answer = step_seven(answer)
    return answer