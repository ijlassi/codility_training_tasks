def solution(A):
   count = 0
   number = 0
   res = 0
   half = len(A)//2 
   if len(A) == 0:
       return -1
   for i in A :
       res = A.count(i)
       if res > count :
           count = res
           number = A.index(i)
           if count > (len(A) // 2):
               return number
   return -1

