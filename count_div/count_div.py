def solution(A,B,K):
     if A % K != 0:
          return (B//K)-(A//K)
     else:
          return (B//K)-(A//K)+1

