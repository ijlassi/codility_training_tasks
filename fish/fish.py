def solution(A,B):
    count = 0
    upst = []
    downst = []
    for i in range(len(A)):
        if B[i]== 0:
             upst.append(A[i])
        elif B[i]== 1:
            downst.append(A[i])
        if len(upst) > 0 and len(downst) == 0:
            count += len(upst)
            upst.clear()
        while len(downst) > 0 and len(upst) > 0:
            if downst[-1] > upst[-1]:
                upst.pop()
            elif upst[-1] > downst[-1]:
                downst.pop()
    return len(downst) + len(upst) + count
