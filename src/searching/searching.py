def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr) -1

    while left <= right:
        #midpoint
        mid = (left + right) // 2
        #if mid is target you are done
        if arr[mid] == target:
            return mid
        #But if the number you are searching for is less than the middle number we go left
        if arr[mid] < target:
            left = mid + 1
        #And if the target is greater than the middle number we head right
        else:
            right = mid -1


    return -1  # not found
