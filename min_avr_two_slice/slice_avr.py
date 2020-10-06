import sys
def solution(A):
    N = len(A)
    minAvg = sys.maxsize 
    sum = 0
    result = 0
    for  i   in range(0,N -1):
        sum = A[i]
        print("A[i] = ", A[i])
        for  j in  range(i+1, N) :
            if j < i+3:
                sum += A[j]
                print("A[j] = :", A[j])
                print("sum = :", sum)
                avg = (sum / (j-i+1))
                print(avg)
                if (avg < minAvg) :
                     minAvg = avg
                     result = i
    return result  
        
           

print(solution([4,2,2,5,1,5,8]))