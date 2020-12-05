def solution(S,P,Q):
    answer = []
    for i,j in zip(P, Q):
        if 'A' in S[i:j+1]:
            answer.append(1)
        elif 'C' in S[i:j+1]:
            answer.append(2)
        elif 'G' in S[i:j+1]:
            answer.append(3)
        elif 'T' in S[i:j+1]:
            answer.append(4)
    return answer
           