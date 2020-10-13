def solution(A):
    answer = 0
    maxi = 0
    for i in range(len(A)):
        for j in range (i+1,len(A)):
            if i <= j :
                answer = A[j] - A[i]
                if answer > maxi:
                    maxi = answer
                    
            
    return maxi