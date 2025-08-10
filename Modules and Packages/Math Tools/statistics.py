def mean(data):
    """Return the mean (average) of a list of numbers."""
    if not data:
        raise ValueError("Data list cannot be empty.")
    return sum(data) / len(data)


def median(data):
    """Return the median of a list of numbers."""
    if not data:
        raise ValueError("Data list cannot be empty.")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        # Odd number of elements → middle value
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
# ALSO NEEDED TO ADD PROBABLITY PACKAGE LIKE COMBINATIONS , PERMUTATIONS ETC.......