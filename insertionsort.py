#implementation of insertion sort in python

def insertion_sort(input):
    for i in range(1, len(input)):
        key = input[i]
        j = i-1

        while j >=0 and key < input[j]:
            input[j+1] = input[j]
            j -=1
        input[j+1] = key

    return input






input = [5,0, 8,7,9, 3, 6, 11, 99,4]
print(insertion_sort(input))