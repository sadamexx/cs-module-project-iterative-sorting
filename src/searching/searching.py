array1 = [3, 4, 6, 16, 26, 28, 52, 55]

def linear_search(array, target):
    for i in array:
        if array[i] == target:
            return i
        else:
            return -1  # not found

print(linear_search(array1, 4))
# Write an iterative implementation of Binary Search
# takes a sorted array and a target as input
# returns the index of the target in the array if exists
# returns -1 if not found
def binary_search(arr, target):
    # find the midpoint element
    # length /2
    left = 0
    right = len(arr)

    # keep iterating while the left is < or equal to right
    while left <= right:
        midpoint = (right + left) // 2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] > target:
            # toss out the left side of array
            # adding one gets rid of the midpoint too, that's its index spot
            right = midpoint - 1
        else:
            # subtracting 1 will take the midpoint out
            left = midpoint + 1
    return -1



print(binary_search(array1, 52))
print(binary_search(array1, 26))
