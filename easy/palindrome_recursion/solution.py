from typing import Optional


def solution(number: Optional[int] = None):
    if number is None or number < 0:
        return -1
    current_word = str(number)
    if len(current_word) < 2:
        return 1
    if len(current_word) < 2:
        return 1
    else:
        first_letter = current_word[0]
        last_letter = current_word[len(current_word) - 1]
        if first_letter == last_letter:
            middle_word = current_word[1:len(current_word) - 1]
            if middle_word == '':
                return 1
            return solution(int(middle_word))
        else:
            return 0
