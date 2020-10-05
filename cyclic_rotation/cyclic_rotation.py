def arrRotate(A):
    list = A.copy()
    for i in range(1,len(A)):
        A[0] = list[len(A)-1]
        A[i]= list[i-1]
    
def solution(A,K):
    for i in range(K):
        arrRotate(A)
    return A