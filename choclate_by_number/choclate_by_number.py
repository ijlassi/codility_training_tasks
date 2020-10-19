def solution(N, M):
    X = 0
    count = 1
    result = [0]
    while True:
        X = (X+M) % N
        if X == 0:  
            break  
        else:
            count += 1        
    return count

