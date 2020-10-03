def solution (A):
    lista = set()
    min = 1
    for i,v in enumerate(A,1) :
        lista.add(v)
    s = sorted(list(lista))
    for i in s:
        if i == min:
            min += 1
    return min
    

        

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
