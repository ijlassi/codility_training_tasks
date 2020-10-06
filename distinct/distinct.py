def solution(A):
    A= sorted(A)
    list = []
    for  item in A :
       if item not in list :
            list.append(item)
    return list
    
