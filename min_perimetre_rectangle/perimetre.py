def solution(N):
    list_factors = []
    temp_list = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
           list_factors.append(i)
           list_factors.append(N//i)
           peri = (i + N//i)*2
           temp_list.append(peri)
    return min(temp_list)

