def solution(A,B,K):
     if A % K != 0:
          return 0
     else:
          return (B//K)-(A//K)+1



