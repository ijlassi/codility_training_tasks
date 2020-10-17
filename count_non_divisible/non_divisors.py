def solution(A):
    count = 0
    list_non_divisors = []
    if len(A) <= 1:
        return 0 
    for i in range(0,len(A)):
       for j in range(0, len(A)):
           if A[i]% A[j] != 0 :
               count = count +1 
       list_non_divisors.append(count)
       count = 0
    return list_non_divisors


