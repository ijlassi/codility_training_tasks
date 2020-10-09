def solution(A):
   A =sorted(A)
   for i in range (0,len(A)):
       if A[0]*A[1]<0 :
           return A[len(A)-1]*A[len(A)-2]*A[len(A)-3]
       if A[0]*A[1]>= 0 :
           if  A[0]*A[1]*A[len(A)-1]> A[len(A)-1]*A[len(A)-2]*A[len(A)-3]:
               return A[0]*A[1]*A[len(A)-1]
           else :
               return A[len(A)-1]*A[len(A)-2]*A[len(A)-3]

    
