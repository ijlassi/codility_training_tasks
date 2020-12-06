def solution(N, A):
    list1 = [0]*N
    mini = 0
    maxi = 0
    for i in A:
        if i in range(0,N+1):
           list1[i-1] = max(list1[i-1],mini) +1 
           maxi = max(maxi,list1[i-1])
        else :
            mini = maxi
    for i in range(N):
         list1[i]= max(list1[i],mini)
    return list1
