def solution(A):
    maxi = A[0]
    count = 0
    for i in range(0,len(A)):
      count = count + A[i]
      if count > maxi :
          maxi = count
      if count < 0 :
          count = 0
    return maxi