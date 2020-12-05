def solution(H):
    n = len(H)
    count = 1
    stack = [H[0]]
    for i in range(1, n):
        if H[i] == stack[-1]:
            continue
        elif H[i] < stack[-1]:
            while H[i] < stack[-1]:
                stack.pop()
                if (len(stack) == 0) or (H[i] > stack[-1]):
                    stack.append(H[i])
                    count += 1
                    break
                elif stack[-1] == H[i]:
                    break
        else:
            stack.append(H[i])
            count += 1         
    return count

