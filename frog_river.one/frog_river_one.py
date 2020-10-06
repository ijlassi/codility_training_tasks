def solution(X,A):
    lista = set()
    for i,v in enumerate(A):
        print(i,v)
        if v <= X:
            lista.add(v)
            print(lista)
            if len(lista)==X:
                return i
      
    
    return -1

  
