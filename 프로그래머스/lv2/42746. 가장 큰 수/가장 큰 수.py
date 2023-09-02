from functools import cmp_to_key

def custom_compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def solution(numbers):
    nums_str = list(map(str, numbers))
    nums_str.sort(key=cmp_to_key(custom_compare))
    return str(int("".join(nums_str)))