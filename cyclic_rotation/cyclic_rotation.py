def arrRotate(A):
    list1 = A.copy()
    for i in range(1,len(A)):
        A[0] = list1[len(A)-1]
        A[i] = list1[i-1]
def solution(A,K):
    for i in range(K):
        arrRotate(A)
    return A