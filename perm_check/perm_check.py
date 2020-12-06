def solution(A):
    count = 0
    list1 = []
    for i in range(1, len(A) + 1):
        list1.append(i)
    A= sorted(A)
    for i in range(len(list1)) :
        if  A[i] == list1[i]:
            count = count + 1
    if count == len(A):
        return 1
    return 0
