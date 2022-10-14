
def solution(n):
    if  not str(n).isnumeric():
        return -1
    
    if int(n) == 0:
        return 0
        
    if int(n)<0:
        return -1

    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   



