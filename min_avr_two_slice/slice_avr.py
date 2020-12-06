import sys
def solution(A):
    N = len(A)
    minAvg = sys.maxsize 
    sum = 0
    result = 0
    for  i   in range(0, N - 1):
        sum = A[i]
        for  j in  range(i+1, N) :
            if j < i+3:
                sum += A[j]
                avg = (sum / (j-i+1))
                if (avg < minAvg) :
                     minAvg = avg
                     result = i
    return result