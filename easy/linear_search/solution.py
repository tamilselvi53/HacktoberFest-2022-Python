def solution(array = [], item = -1):
    if type(array) != list:
        return -1
    for index, value in enumerate(array):
        if value == item:
            return index
    return -1
