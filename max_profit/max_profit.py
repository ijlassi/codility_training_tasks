def solution(A):
    answer = 0
    maxi = 0
    if len(A) < 2 :
        return 0
    max_profit = A[len(A)-1]
    for i in range(len(A)-2, -1, -1):
        maxi = max(maxi, max_profit-A[i])
        max_profit = max(A[i], max_profit)
    return maxi
