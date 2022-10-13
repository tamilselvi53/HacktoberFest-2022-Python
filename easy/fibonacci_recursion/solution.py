def solution(*args):
    if len(args)==0:
        return -1
        
    if args[0]<=1:
        return args[0]
    return solution(args[0]-1)+solution(args[0]-2)
