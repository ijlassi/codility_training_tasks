def occur(arr): 
    if (len (A))==1 :
        return A[0]
    A = sorted(A)
    for i in range (0,len(A),2):
        if i+1 == len(A) :
            return A[i]
        elif A[i] != A[i+]:
            return A[i]
    
print(occur([1,1,2,2,3]))
