def solution(A): 
    n = len(A)
    max_double_slice_sum = 0
    current_double_slice_sum = 0
    current_left_slice_sum = 0
    for z in range(3, n):
        current_left_slice_sum = max(0, current_left_slice_sum + A[z - 2])
        current_double_slice_sum = max(current_double_slice_sum + A[z - 1],current_left_slice_sum)
        max_double_slice_sum = max(max_double_slice_sum,current_double_slice_sum)
    return max_double_slice_sum

