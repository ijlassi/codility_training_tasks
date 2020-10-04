def solution(N, A):
    list = [0]*N
    lista = []
    for i in range(len(A)):
        if A[i] in range(0,N+1):
           list[A[i]-1]+= 1 
        elif A[i]== N+1:
            res = max(list)
            for i,v in enumerate(list):
              list[i]= res
               
            
    return list
print(solution(5,[3, 4, 4, 6, 1, 4, 4]))
print(solution(1, [1]))