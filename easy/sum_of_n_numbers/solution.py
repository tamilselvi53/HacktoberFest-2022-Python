def solution(n):
    sum = 0
    if not str(n).isnumeric():
        sum = -1
        return sum
    else:
        n = int(n)
        for i in range(n):
            i = i + 1
            sum = sum +  i
    return sum