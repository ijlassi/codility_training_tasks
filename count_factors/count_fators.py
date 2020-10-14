from functools import reduce
def solution(N):
    return len(set(reduce(list.__add__, 
                ([i, N//i] for i in range(1, int(N**0.5) + 1) if N % i == 0))))
