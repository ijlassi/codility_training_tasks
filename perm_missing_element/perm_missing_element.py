def solution(A):
    list = []
    for i in range(1,len(A)+1):
        list.append(i)
   
    A = sorted(A)
    for i in range(1,len(A)) :
        if  A[i]!= list[i]:
            return list[i]