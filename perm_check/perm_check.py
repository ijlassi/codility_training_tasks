def perm(arr):
    list = []
    for i in range(1,len(arr)+1):
        list.append(i)
    arr.sort()
    for i in range(1,len(arr)) :
        if  arr[i]== list[i]:
            return 1
        else:
            return 0

