def solution(A):
    list_indexes = []
    found_cnt = 0
    if len(A) < 3 :
        return 0
    for v in range(1,len(A)-1):
       if A[v] > A[v + 1] and A[v] > A[v - 1]:
           list_indexes.append(v)
    for i in range(len(list_indexes),0,-1):
        res = len(A)% i
        if res == 0 :
            block_size = len(A) // i
            found = [False] * i
            for peak in list_indexes:
                block = peak//block_size
                if found[block] == False:
                    found[block] = True
                    found_cnt += 1
            if found_cnt == i:
                return i
    return 0
   
            

   
        
