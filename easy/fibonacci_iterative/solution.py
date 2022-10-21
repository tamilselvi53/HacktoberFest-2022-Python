def solution(n = -1):
    n1 = 1
    n2 = 1
    if n == 0: return 0
    if n < 0: return -1
    if n == None: return -1
    for i in range (1,n-1):
        n1 += n2
        n2 = n1 - n2
    return n1


    pass
