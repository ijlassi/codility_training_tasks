def solution(A, B):
    result_list = []
    remainder = 0
    power = 0
    i = 0 
    a = 0
    b = 1 
    fib_numbers = [0,1]
    while i <= len(A):
        c = a + b 
        a = b 
        b = c
        fib_numbers.append(c)
        i = i + 1
    for i in range(len(B)) :
       power = 2**B[i]
       remainder = fib_numbers[A[i] + 1] % power 
       result_list.append(remainder)
    return result_list

