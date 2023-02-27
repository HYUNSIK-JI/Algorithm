def solution(numbers, target):
    res = [0]
    def dfs(start, n, lst):
        if start == len(lst):
            if n == target:
                res[0] += 1
            return
        v = lst[start] 
        dfs(start + 1, n + v, lst)
        dfs(start + 1, n - v, lst)

    dfs(0, 0, numbers)

    return res[0]