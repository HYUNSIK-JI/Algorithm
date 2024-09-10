def solution(code):
    
    result = ''
    mode = 0

    for k, v in enumerate(code):
        if k == len(code):
            continue
        if not mode:
            if v.isdigit():
                mode = not mode
                continue
            else:
                if k % 2:
                    continue
                result += v
        else:
            if v.isdigit():
                mode = not mode
                continue
            else:
                if not k % 2:
                    continue
                result += v
    return result if result else 'EMPTY'