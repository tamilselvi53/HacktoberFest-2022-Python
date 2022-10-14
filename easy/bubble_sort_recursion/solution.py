def solution(list_of_nums = []):
    return bubble_sort(list_of_nums)

def bubble_sort(list_of_nums):
    # Check if it is a valid input.
    if not list_of_nums or not isinstance(list_of_nums, list):
        # If not a valid input return empty list.
        return []

    # Return bubble sort recursive solution
    return recursive_sort(list_of_nums, len(list_of_nums))

def recursive_sort(list_of_nums, len):
    # Basic case.
    if len == 1:
        return list_of_nums

    # Order sublist.
    for i in range(len-1):
        if list_of_nums[i] > list_of_nums[i+1]:
            list_of_nums[i], list_of_nums[i+1] = list_of_nums[i+1], list_of_nums[i]

    return recursive_sort(list_of_nums, len-1)
