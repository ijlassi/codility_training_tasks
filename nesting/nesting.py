def solution(S):
    opening = ["("]
    closing = [")"]
    list1 = []
    if len(S) == 0:
        return 1
    for s in S:
        if s in opening:
            list1.append(s)
        elif s in closing:
            if len(list1) < 1:
                return 0
            element = list1.pop()
            if opening.index(element) != closing.index(s):
                return 0
    if len(list1) == 0:
        return 1
    return 0
  
