def containsduplicate(nums):
    comp = []
    
    for num in nums:
        if num in comp:
            return True
        comp.append(num)
    return False

'''APPROACH -

1. firstly we are creating an empty list
2. iterate through the list and if the element in num is seen in comp, return true
3. Aooend the num in the empty list(comp)
4. else return false
'''