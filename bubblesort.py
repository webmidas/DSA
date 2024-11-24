#implementing bubblesort in python
#complexity

def bubble_sort(input):
    for i in range(len(input) - 1):
        for j in range(0, len(input)-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]

    return input


input = [5,9,3,5,15, 7, 11,2]

print(bubble_sort(input))

