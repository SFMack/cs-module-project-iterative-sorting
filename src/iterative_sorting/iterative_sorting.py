# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # iterate through node values
        for item_index in range(i+1, len(arr)):
            # if the value of 'smallest_index' is greater than the value of 'current_index'
            if arr[smallest_index] > arr[item_index]:
                # change the value of 'smallest_index' to the value of 'item_index'
                smallest_index = item_index


        # TO-DO: swap
        # swap the nodes
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # get the length of the array
    array_length = len(arr)

    # loop through all array elements
    # using 'array_length - 1' to accomodate zero index
    for item in range(array_length):
        # loop through the remaining elements in array
        for item_x in range(0, array_length-item-1):
            # if the found element is greater than the current element
            if arr[item_x] > arr[item_x+1]:
                # swap the elements
                arr[item_x], arr[item_x+1] = arr[item_x+1], arr[item_x]


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
