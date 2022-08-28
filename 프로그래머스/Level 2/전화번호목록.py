def solution(phone_book):
    answer = True
    phone_book.sort()
    # 이중 포문시 시간초과.
    # 효율성을 위해 sort() 하고 진행
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return answer