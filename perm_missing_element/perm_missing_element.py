def solution(A):
    count = 1
    A = sorted(A)
    for i in range(0, len(A)):
        if  A[i] != count :
            return count
        count += 1
    return count