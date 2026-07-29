def check(arr):
    n = len(arr)
    expected = n * (n + 1) // 2
    curr_sum = sum(arr)
    missing = expected - curr_sum
    return missing