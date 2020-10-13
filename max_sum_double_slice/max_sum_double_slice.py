def solution(A): 
    maxi = 0
    answer_1 = 0
    answer_2 = 0
    answer = 0 
    j = 0
    k = 0 
    for i in range(len(A)):
        for j in range(i+1,len(A)-1):
            for k in range(j+1,len(A)):
                if j - i == 1 or k - j == 1:
                     answer = answer + 0
                if j - i >= 2 :
                    for v in range(i+1, j):
                        answer_1 = answer_1 + A[v]
                if k - j >= 2:
                    for w in range(j+1, k):
                        answer_2 = answer_2 + A[w]
                answer = answer_1 + answer_2
                answer_1 = 0
                answer_2 = 0

                if answer > maxi :
                    maxi = answer
                    answer = 0
    return maxi
