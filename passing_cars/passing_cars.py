def solution(A):
    count_0 = 0
    count_1 = 0
    for P in range(0,len(A)):
        if A[P]== 0:
            count_0 += 1
        else:
            count_1 += count_0
        if  count_1 > 1000000000:
           return -1
    return count_1