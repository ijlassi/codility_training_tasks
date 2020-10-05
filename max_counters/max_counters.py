def solution(N, A):
    list = [0]*N
    min_l = 0
    max_l = 0
    for i in A:
        if i in range(0,N+1):
           list[i-1] = max(list[i-1],min_l) +1 
           max_l = max(max_l,list[i-1])
        else :
            min_l = max_l
    for i in range(N):
         list[i]= max(list[i],min_l)
    return list
