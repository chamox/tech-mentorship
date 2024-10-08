def quick_sort(array, low, high):
    if low < high:
        # Divide and sort pivot
        pi = partition(array, low, high)
    
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    
def partition(array, low, high):  
    # Pivot is the last element
    pivot = array[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            # Increment index of smaller element
            i = i + 1
            # Swap
            (array[i], array[j]) = (array[j], array[i])
    
    # Swap pivot with element at index i + 1
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    
    # Return index of pivot
    return i + 1

arr = [4,6,2,5,8,9,5,10]
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)