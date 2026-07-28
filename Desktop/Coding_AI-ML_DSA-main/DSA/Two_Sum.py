def twoSum(self,nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return[i,j]
            
""" 
APPROCH - 

1. taking 2 pointers i and j, i will start formn and j from i+1 till n.
2. for i check all possible j vales.
3. main condition, if nums[i] + nums[j] == target if it's satisfies return i and j
4. assuming array is sorted!
"""