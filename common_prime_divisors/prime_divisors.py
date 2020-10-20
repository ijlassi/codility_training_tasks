def gcd(a,b):
    if b == 0:
       return a 
    return gcd(b,a % b)
    
def solution(A,B):
    count = 0 
    for i in range(0,len(A)):
       a = A[i]
       b = B[i]
       p = gcd(a,b) 
       while True :
          d = gcd(a,p)
          if d == 1:
             break
          a = a // d 
       while True :
          d = gcd(b,p)
          if d == 1:
             break
          b = b // d 
       if a == 1 and b == 1 :
         count = count + 1
       else :
           0
    return count 
