def solution(A):
    max_sum = A[0]
    count = 0
    for i in range(0,len(A)):
      count = count + A[i]
      if count > max_sum :
          max_sum = count
      if count < 0 :
          count = 0
    return max_sum