def binary_search(array, value):
    low = 0
    high = len(array)

    while low < high:
        midIndex = low + (high - low) // 2
        midValue = array[midIndex]

        if value < midValue:
            high = midIndex - 1
        elif value > midValue:
            low = midIndex + 1
        else:
            return True

    return False
