def solution (A):
    list1 = set()
    min = 1
    for i,v in enumerate(A,1) :
        list1.add(v)
    list2 = sorted(list(list1))
    for i in list2 :
        if i == min:
            min += 1
    return min
    
