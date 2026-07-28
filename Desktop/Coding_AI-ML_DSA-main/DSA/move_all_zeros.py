def move_zeros(arr):
    pos = 0  # keeping next non zero element here
 
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]   # swap
            pos += 1
 
    return arr