def solution(S):
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    list_ = []

    if len(S) == 0:
        return 1
    for s in S:
        if s in opening:
            list_.append(s)
        elif s in closing:
            if len(list_) < 1:
                return 0
            element = list_.pop()
            if opening.index(element) != closing.index(s):
                return 0
    if len(list_) == 0:
        return 1
    return 0
          
          
          

