def solution(N, A):
    list1 = [0]*N
    min_l = 0
    max_l = 0
    for i in A:
        if i in range(0,N+1):
           list1[i-1] = max(list1[i-1],min_l) +1 
           max_l = max(max_l,list1[i-1])
        else :
            min_l = max_l
    for i in range(N):
         list1[i]= max(list1[i],min_l)
    return list1
