def countOccurrence(arr, target):
    count = 0
    for num in arr:
        if target == num:
            count += 1
    return count

print(countOccurrence([1, 2, 3, 4, 3, 2, 3, 1, 3, 5, 3, 7, 2], 3))