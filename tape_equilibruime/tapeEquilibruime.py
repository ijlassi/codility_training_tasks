def solution(A):
    answer1= 0
    answer2= 0
    list1= []
    list2= []
    list3= []
    for i in range(0,len(A)-1) :
        answer1 = answer1 + A[i]
        list_1.append(answer1)
    res = A[::-1]
    for i in range(0,len(res)-1):
        answer2 = answer2 + res[i]
        list2.append(answer2)
    list4 = list2[::-1]
    for i,v in zip(list1,list4):
        val = abs(i-v)
        list3.append(val)
    return  min(list3)
