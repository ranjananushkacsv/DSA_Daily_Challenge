def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    max_count = 0
    curr_count = 0
    
    for num in nums:
        if num == 1:
            curr_count += 1
        else:
            max_count = max(max_count, curr_count)
            curr_count = 0
    max_count = max(max_count, curr_count)
    
    return max_count

'''
APPROACH - 

1. 2 variables max_count and curr_count are made.
2. A for loop is strated for tracing each element in nums array. Check if num == 1, then we update the current count.
3. If not then max count is updated with the max of (max_count, curr_count)
4. After the loop, update max_count one more time (in case the array ends with 1's)

'''