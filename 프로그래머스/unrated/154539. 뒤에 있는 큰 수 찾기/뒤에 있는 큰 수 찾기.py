def solution(numbers):
    stack = []
    ans = [-1] * len(numbers) 
    
    for i, k in enumerate(numbers):
        while stack:
            if stack[-1][1] < k:
                ans[stack[-1][0]] = k
                stack.pop()
            else:
                break
        stack.append((i, k))
    return ans