def binary_search(array, value):
    if len(array) < 1:
        return False

    # If the array size is 4, then midIndex is 2,
    # which is greater than the midpoint.
    # If the array size is 5, then midIndex is 2,
    # which is the midpoint
    midIndex = len(array) // 2

    midValue = array[midIndex]

    if len(array) == 1 and value != midValue:
        return False

    if value < midValue:
        return binary_search(array[:midIndex], value)
    elif value > midValue:
        return binary_search(array[midIndex + 1:], value)
    else:
        return True


