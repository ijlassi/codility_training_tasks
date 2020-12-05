def solution(A):
    count = 0
    count1 = 0
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
                count1 = count1 + 1 
            if count1 > (i + 1)//2 and (count - count1) > (len(A) -1 - i) // 2 :
                answer = answer + 1 
    return answer 

