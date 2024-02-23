# Find minimum difference between two elements of Array of Binary Tree 
# arr = [5,32,45,4,12,18,25]

def min_diff_ele(arr):
    arr=sorted(arr)
    size=len(arr)
    min_diff=9999*999       #largest element to compare the diff of elements of array

    for i in range(0,size-1):
        if(arr[i+1]-arr[i] < min_diff):
            min_diff = arr[i+1]-arr[i]
    return min_diff

arr = [5,32,45,3,12,18,25]
print("Minimum difference b/w elements of array is: ", min_diff_ele(arr))


#######################################################################
# Find maximum difference between two elements of Array of Binary Tree 

def max_diff_ele(arr):
    arr=sorted(arr)
    size=len(arr)
    max_diff= -9999*999

    for i in range(0,size-1):
        if(arr[i+1]-arr[i] > max_diff):
            max_diff = arr[i+1]-arr[i]
    return max_diff

arr = [5,32,45,4,12,18,25]
print("Maximum difference b/w elements of array is: ", max_diff_ele(arr))
