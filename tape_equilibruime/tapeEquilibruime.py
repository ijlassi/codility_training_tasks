import math
def diff(arr):
    s = 0
    list = []
    l = []
    k = []
    f = 0
    for i in range(0,len(arr)-1) :
        s = s + arr[i]
        list.append(s)
    res = arr[::-1]
    for i in range(0,len(res)-1):
        f = f + res[i]
        l.append(f)
    r = l[::-1]
    for i,v in zip(list,r):
        n = abs(i-v)
        k.append(n)
    return  min(k)


print(diff([3,1,2,4,3]))