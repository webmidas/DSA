# implementing linear search through python
#time complexity best O(1), Worst O(n)
#Space Complexity O(1)

def linear_search(search, target):
    for i in range(len(target)):
        if search == target[i]:
            return i

    return False

search = 5
target = [1, 3, 6, 5, 8, 9, 11]

print(linear_search(search, target))
