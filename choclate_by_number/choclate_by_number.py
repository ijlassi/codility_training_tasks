def solution(N, M):
    choclate_eated = [0]
    count_choclate = 0
    results = 0
    for i in range(0,N):
        count_choclate = count_choclate + M 
        if count_choclate < N :
            choclate_eated.append(count_choclate)
        if count_choclate > N:
            results = count_choclate - N 
            while results >= N :
                results = results - N
            if results not in choclate_eated:
                choclate_eated.append(results)
            if results < N and results not in choclate_eated :
                choclate_eated.append(results)
    return len(choclate_eated)


