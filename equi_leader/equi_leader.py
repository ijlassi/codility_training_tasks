def solution(A):
    count = 0
    count_1 = 0
    number = 0
    answer = 0
    for i in A:
        if count == 0 :
            number = i
        if number == i:
            count = count + 1
        else : 
            count = count - 1 
    count = A.count(number)
    if count > len(A)//2:
        for i in range(len(A)):
            if A[i] == number :
                count_1 = count_1 + 1 
            if count_1 > (i + 1)//2 and (count - count_1) > (len(A) -1 - i) // 2 :
                answer = answer + 1 
    return answer 

