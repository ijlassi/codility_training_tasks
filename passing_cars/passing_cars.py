def solution(A):
    count0 = 0
    count1 = 0
    for P in range(0, len(A)):
        if A[P]== 0:
            count0 += 1
        else:
            count1 += count0
        if  count1 > 1000000000:
           return -1
    return count1