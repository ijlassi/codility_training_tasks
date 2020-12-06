def solution(A):
    answer1 = 0 
    answer2 = 0
    count = 0
    if len(A) == 0: 
        return 0
    plane_of_discs = list(enumerate(A))
    for disc1, radius1 in plane_of_discs:
        for disc2, radius2 in plane_of_discs[disc1+1:]:
            answer1 = (disc1 + radius1) 
            answer2 = (disc2 - radius2)
            if answer1 >= answer2 :
                count = count +1 
    return count 
        
                
