def solution(A):
    ans_1= 0
    ans_2 =0
    list_1 = []
    list_2 = []
    list_3 = []
    for i in range(0,len(A)-1) :
        ans_1 = ans_1 + A[i]
        list_1.append(ans_1)
    res = A[::-1]
    for i in range(0,len(res)-1):
        ans_2 = ans_2 + res[i]
        list_2.append(ans_2)
    list_4 = list_2[::-1]
    for i,v in zip(list_1,list_4):
        val = abs(i-v)
        list_3.append(val)
    return  min(list_3)
