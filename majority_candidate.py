def majorityElement(self, nums: List[int]) -> int:
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate
'''APPROACH -
1. initially we will have a count and candidate variable
2. we will traverse array num, if we see the count is zero we add that num to candidate
3. else if we already have it as candidate then we increment the count by 1
'''