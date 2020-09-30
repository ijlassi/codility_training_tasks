def pos(x,y,d): 
   distance = y -x 
   if  distance % d == 0:
       return distance // d

   else :
       return distance // d +1 

print(pos(10,85,30))
