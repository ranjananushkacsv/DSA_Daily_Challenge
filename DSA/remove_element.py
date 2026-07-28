def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

'''
APPROACH - 

1. Initialize a pointer k and i. Traverse the array using a for loop/
2. If current element is not val then keep it in stratinf (k=0)
3. Increase k by one
4. return k


'''