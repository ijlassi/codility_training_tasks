def solution(A):
    count = 0
    for P in range(0,len(A)):
        if A[P]== 0:
            for Q in range(0,len(A)):
                if P < Q and A[P] != A[Q] :
                    count += 1
    return count 