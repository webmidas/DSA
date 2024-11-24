# implementation of binary search using recursion in python

def bin_search(search, target):
    left = 0
    right = len(target) - 1
    result = search_now(search, target, left , right)
    return result

def search_now(search, target, left , right):
    mid_position = (left + right) // 2
    mid_value = target[mid_position]

    if left > right:
        return -1
    if search == mid_value:
        return mid_position
    elif search > mid_value:
        left = mid_position + 1
        return search_now(search, target, left , right)
    else:
        right = mid_position - 1
        return search_now(search, target, left, right)

target = [1,2,4,5,6,8,9,11,12,15,17,18,19]
search = 115

print(bin_search(search, target))