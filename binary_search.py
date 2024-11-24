# implementing binary search in python
# time complexity best case O(1)
#space complexity

def binary_search(search, target):
    left = 0
    right = len(target) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = target[mid]
        print(mid, left, right)

        if mid_value == search:
            return mid
        elif search < mid_value:
            right = mid - 1
        else:
            left = mid + 1


    return -1


search = 133
target = [1, 2, 3, 5,7, 8 ,9, 11,13,17]

print(binary_search(search,target))