def solution(n=-1):
    if n==-1:
        return -1
    if n<1:
        return -1
    string= ""
    if(n>0):
        for row in range(n):
            for column in range(n-row):
                string+=str(column+1)
            if row==n-1:
                break
            string+="\n"
    return string