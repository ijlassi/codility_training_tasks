def solution(A):
    answer_1 = 0 
    answer_2 = 0
    count = 0
    if len(A) == 0: 
        return 0
    plane_of_discs = list(enumerate(A))
    for disc1, radius1 in plane_of_discs:
        for disc2, radius2 in plane_of_discs[disc1+1:]:
            answer_1 = (disc1 + radius1) 
            answer_2 = (disc2 - radius2)
            if answer_1 >= answer_2 :
                count = count +1 
    return count 
        
                

print(solution([1,5,2,1,4,0]))