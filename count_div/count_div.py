def solution(A,B,K):
   count = A
   if A > B :
        return 0
   else:
        for i in range(A,B):
            if count % K == 0:
                count = count +1
        return i - count


