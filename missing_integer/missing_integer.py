def solution (A):
    lista = set()
    min = 1
    for i,v in enumerate(A,1) :
        lista.add(v)
        if v < 0:
            return 1
    s = list(lista)
    s = sorted(s)
    for i in range(1,len(s)+1):
        if len(s)== len(A):
            return len(s)+1 
        elif len(s) < len(A):
            for i,v in enumerate(s,1):
                if i == v:
                    min += 1
            return min
        else :
            return 1
        

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
