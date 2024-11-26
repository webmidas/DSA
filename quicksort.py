#implementation of quicksort in python

def quick_sort(input):
    for i in range(len(input)):
        pivot = input[i]
        left = input[i+1]
        right = input[len(input - 1)]

    pass


input = [5,0, 8,7,9, 3, 6, 11, 99,4]
print(quick_sort(input))