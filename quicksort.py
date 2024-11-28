#implementation of quicksort in python

def quick_sort(input):
    for i in range(len(input)):
        pivot = input[i]
        left = input[i+1]
        right = input[len(input - 1)]
        if input[left] >= pivot and input[right] <= pivot:
            input[left], input[right] = input[right], input[left]
        if input[left] < pivot:
            left += 1
        if input[right] > pivot:
            right -= 1

    pass


input = [5,0, 8,7,9, 3, 6, 11, 99,4]
print(quick_sort(input))