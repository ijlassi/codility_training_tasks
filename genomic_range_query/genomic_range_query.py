def solution(S,P,Q):
    items = []
    for i,j in zip(P, Q):
        if 'A' in S[i:j+1]:
            items.append(1)
        elif 'C' in S[i:j+1]:
            items.append(2)
        elif 'G' in S[i:j+1]:
            items.append(3)
        elif 'T' in S[i:j+1]:
            items.append(4)
    return items
           