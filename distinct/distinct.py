def solution(A):
    A = sorted(A)
    list1 = set()
    for  item in A :
            list1.add(item)
    return len(list1)
    
