def solution(S):
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    list1 = []
    if len(S) == 0:
        return 1
    for item in S:
        if item in opening:
            list1.append(item)
        elif item in closing:
            if len(list1) < 1:
                return 0
            element = list1.pop()
            if opening.index(element) != closing.index(item):
                return 0
    if len(list1) == 0:
        return 1
    return 0
          
          
          

