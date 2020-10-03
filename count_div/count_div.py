def solution(A,B,K):
     count =0
     for i in range(A,B):
          if count % K == 0:
                count = count +1
        return count


