#implementation of selection sort in python

input = [5,0, 8,7,9, 3, 6, 11, 99,4]

def selection_sort(input):
    for i in range(len(input)-1):
        min = i
        for j in range(i+1, len(input)):
            if input[j] < input[min]:
                min = j

        input[i], input[min] = input[min], input[i]


    return input



print(selection_sort(input))