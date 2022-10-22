def solution(num):
    if num > 1:
      solution(num // 2)
      print num % 2
