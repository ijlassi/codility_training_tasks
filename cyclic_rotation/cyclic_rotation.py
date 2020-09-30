def arrRotate(arr):
    list = arr.copy()
    for i in range(1,len(arr)):
        arr[0] = list[len(arr)-1]
        arr[i]= list[i-1]
    
def solution(arr,k):
    for i in range(k):
        arrRotate(arr)
    print(arr)

print(solution([3, 8, 9, 7, 6], 3))
print(solution([1, 2, 3, 4], 4))
print(solution([1,5,7,8,9,6,2,3,6,7],1500))
