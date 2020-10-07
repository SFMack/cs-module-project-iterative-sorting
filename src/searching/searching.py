def linear_search(arr, target):
    # loop through array
    for i in range(arr):
        # if the current item is equal to the target item
        if arr[i] == target:
            # return the item
            return i
    
    # didn't find the item so return -1
    return -1   



# CAUTION!! Data set must sorted and ordered to use BS
def binary_search(arr, target):
    # create the outer bounds
    low = 0
    high = len(arr) - 1
    
    # iterate through array
    while low <= high:
        # get the middle
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        if guess > target:
            high = middle - 1
        else: 
            low = middle + 1


    return -1  # not found