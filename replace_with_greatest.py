def replaceElements(arr):
    n = len(arr)
    if n == 0:
        return arr
    
    # Start from the end and work backwards
    max_so_far = -1
    
    for i in range(n - 1, -1, -1):
        current = arr[i]
        arr[i] = max_so_far
        max_so_far = max(max_so_far, current)
    
    return arr