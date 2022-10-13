def answer(n):
    if n<=1:
        return n
    else:
        return answer(n-1)+answer(n-2)
n=int(input())
print(answer(n))
