n_list = []


def self_num(n):
    n, hap = str(n), 0

    if len(n) == 1:
        hap += int(n) + int(n[0])
        n_list.append(hap)
    else:
        for i in range(len(n)):
            hap += int(n[i])
        hap += int(n)
        n_list.append(hap)
    return n_list


for i in range(1, 10001):
    self_num(i)
    if i not in n_list:
        print(i)