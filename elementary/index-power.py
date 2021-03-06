def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if n >= len(array):
        return -1
    else:
        return array[n] ** n


if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    assert index_power([96, 92, 94], 3), "Cube"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
