def solution(A): 
    if len (A) == 1:
        return A[0]
    A = sorted(A)
    for i in range (0, len(A), 2):
        if i + 1 == len(A):
            return A[i]
        elif A[i] != A[i + 1]:
            return A[i]
    

