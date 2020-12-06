def solution(X,A):
    list1 = set()
    for i,v in enumerate(A):
        if v <= X:
            list1.add(v)
            if len(list1)==X:
                return i
    return -1

  
