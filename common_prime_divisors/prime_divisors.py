def solution(A,B):
    count = 0 
    for i in range(0,len(A)):
       div = max(A[i],B[i]) // min(A[i],B[i])
       mod = max(A[i],B[i]) % min(A[i],B[i]) 
       if mod == 0:
           if min(A[i],B[i]) % div == 0:
               count = count + 1
    return count 
