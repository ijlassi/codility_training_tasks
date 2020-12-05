def solution(X,A):
    lista = set()
    for i,v in enumerate(A):
        if v <= X:
            lista.add(v)
            if len(lista)==X:
                return i
    return -1

  
