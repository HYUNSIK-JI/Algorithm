
def solution(num_list):
    count_list = {}
    def cal(n):
        copy_n = n
        count = 0
        while not n == 1:
            if count_list.get(n):
                count_list[copy_n] = count_list.get(n) + count
                return
            if not n % 2:
                n //= 2
                count += 1
            else:
                n = (n - 1) // 2
                count += 1
        count_list[copy_n] = count
        return
    for num in range(1, 31):
        cal(num)
    answer = 0
    for num in num_list:
        answer += count_list.get(num)
    return answer