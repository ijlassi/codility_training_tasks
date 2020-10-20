def solution(A,B):
    count = 0 
    for i in range(0,len(A)):)
       mod = max(A[i],B[i]) % min(A[i],B[i]) 
       if mod == 0:
           while ( math.gcd(A[i], p) != 1):
                A[i]= A[i]// math.gcd(A[i], p)
           while (math.gcd(B[i], p) != 1):
                B[i] = B[i] // math.gcd(B[i], p)
           if ( A[i] == 1 and B[i] == 1) :
                count = count + 1
    return count 
