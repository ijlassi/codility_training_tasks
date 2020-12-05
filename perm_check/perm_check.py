def solution(A):
    count = 0
    lista = []
    for i in range(1,len(A)+1):
        lista.append(i)
    A= sorted(A)
    for i in range(len(lista)) :
        if  A[i]== list[i]:
            count = count +1
    if count == len(A):
        return 1
    return 0
