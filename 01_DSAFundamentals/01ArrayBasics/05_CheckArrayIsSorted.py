def checkArraySorted(arr):
    if len(arr) <= 1:
        return "Sorted"
    
    isAscending = True
    isDescending = True

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            isDescending = False
        if arr[i] > arr[i+1]:
            isAscending = False
    
    if isAscending and isDescending:
        return "Constant (All elements are equal)"
    elif isAscending:
        return "Sorted Forward (Ascending)"
    elif isDescending:
        return "Sorted Backward (Descending)"
    
    return "Not Sorted"

print(checkArraySorted([2, 3, 4, 5, 6]))