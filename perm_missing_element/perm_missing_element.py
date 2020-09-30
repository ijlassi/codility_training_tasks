
def solution(A):
    list = []
     if A == []:
        return 2
    elif len(A) == 1:
      return 2
    elif len(A)== 2:
        return 3
    else :
        for i in range(1,len(A)+1):
            list.append(i)
        A = sorted(A)
        for i in range(1,len(A)) :
            if  A[i]!= list[i]:
                return list[i]