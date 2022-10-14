def solution(n):
    if n<1:
        return -1;
    string= ""
    if(n>0):
        for row in range(n):
            for column in range(row+1):
                string+="*"
            if row==n-1:
                break
            string+="\n"
    return string
