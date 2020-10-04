def solution(S,P,Q):
    ans = []
    for i,j in zip(P, Q):
        if 'A' in S[i:j+1]:
            ans.append(1)
        elif 'C' in S[i:j+1]:
            ans.append(2)
        elif 'G' in S[i:j+1]:
            ans.append(3)
        elif 'T' in S[i:j+1]:
            ans.append(4)
    return ans
           