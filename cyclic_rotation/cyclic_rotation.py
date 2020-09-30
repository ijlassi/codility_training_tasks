def arrRotate(A):
    list = A.copy()
    for i in range(1,len(arr)):
        A[0] = list[len(arr)-1]
        Ai]= list[i-1]
    
def solution(A,K):
    for i in range(K):
        arrRotate(A)
    return A