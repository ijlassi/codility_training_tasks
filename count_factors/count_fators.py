from functools import reduce
def solution(N):
    list1 = set()
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            list1.add(i)
            list1.add(N//i)
    return len(list1)
            