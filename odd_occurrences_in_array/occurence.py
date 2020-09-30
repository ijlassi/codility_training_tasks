def occur(arr):
    
    for i in arr:
        if arr.count(i)  == 1 :
           print(i)
    
print(occur([1,1,2,2,3]))