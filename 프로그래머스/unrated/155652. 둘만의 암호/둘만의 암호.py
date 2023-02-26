def solution(s, skip, index):
    skip_list = set(ord(i) for i in skip)
    ans = []
    
    for word in s:
        cnt = index
        k = ord(word)
        
        while cnt:
            k += 1
            
            if k > 122:
                k -= 26
            if k in skip_list:
                continue
            cnt -= 1
        ans.append(chr(k))
    return "".join(ans)