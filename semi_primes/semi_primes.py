def solution(N, P, Q):
    results = []
    semi_primes = [0] * (N+1)
    flags = [0] * (N+1)
    for i in range(2, N+1):
        for j in range(i, int(N/i)+1):
            num1 = semi_primes[i]
            num2 = semi_primes[j]
            if num1==0 and num2==0:
                semi_primes[i*j]+=1
            elif num1==0 or num2==0:
                semi_primes[i*j]+=2
    flags[0] = semi_primes[0]
    for idx, semi in enumerate(semi_primes[1:]):
        print(idx,semi)
        if semi==1:
            flags[idx+1] = flags[idx] + 1
            print(flags)
        else:
            flags[idx+1] = flags[idx]
            print(flags)
    for p, q in zip(P, Q):
        results.append(flags[q] - flags[p-1])
    return results
print(solution(26,[1,4,16],[26,10,20]))