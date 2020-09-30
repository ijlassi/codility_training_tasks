def solution(N): 
    if (N == 0 or (N & (N - 1)) == 0): 
        return 0
    bit = 1
    prev = 0
    i = 1
    while(i < 33): 
        prev += 1
        if ((N & bit) == bit): 
            bit = bit << 1
            break
        bit = bit << 1
    max = -10**9
    cur = prev 
    for j in range(i + 1, 33): 
        cur += 1
        if ((N & bit) == bit): 
            if (max < (cur - prev - 1)): 
                max = cur - prev - 1
            prev = cur 
        bit = bit << 1
    return max 