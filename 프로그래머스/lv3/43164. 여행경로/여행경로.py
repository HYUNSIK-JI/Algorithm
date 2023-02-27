def solution(tickets):
    ans = ["ICN"]
    tickets.sort(key=lambda x:(x[0], x[1]))
    
    def dfs(tickets, ans):
        if not len(tickets):
            return ans
        k = 0
        while k < len(tickets) and tickets[k][0] != ans[-1]: 
            k += 1
        if k == len(tickets):
            return []
        
        while tickets[k][0] == ans[-1]:
            res = dfs(tickets[:k] + tickets[k + 1:], ans + [tickets[k][1]])
            if res != []: 
                return res
            k += 1
        return res
    answer = dfs(tickets, ans)
    return answer