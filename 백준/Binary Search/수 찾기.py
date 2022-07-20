def binary_search(target,start,end,data):
    if start>end:
        return None
    mid=(start+end)//2

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid -1

    return binary_search(target,start,end,data)
n=int(input())
n_list=sorted(list(map(int,input().split())))
m=int(input())
m_list=list(map(int,input().split()))

for i in range(len(m_list)):
    if binary_search(m_list[i],0,len(n_list)-1,n_list)!=None:
        print(1)
    else:
        print(0)