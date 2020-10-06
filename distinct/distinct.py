def solution(A):
    A= sorted(A)
    list = set()
    for  item in A :
            list.add(item)
    return len(list)
    
