def solution(A):
    result = 0
    for number in A:
      print(result ^= number)
    return result
   
print(solution([9,3,9,3,9,7,9]))