import sys
def solution(A):
    pr = 0
    ans =0
    for P in range(0,len(A)):
        for Q in range(0,len(A)):
            if P < Q :
                for R in range(len(A)):
                    if Q < R :
                        pr = A[P]*A[Q]*A[R]
                        if ans < pr:
                            ans = pr
    return pr
