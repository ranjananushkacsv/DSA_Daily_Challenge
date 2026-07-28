class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = list(zip(heights, names))
        pair.sort(reverse=True)
        return [names for height, name in pair]
    
    
'''APPROACH -
1. pair each height with corresponding names
2. sort the names based on descending height
3. extract only names from mapped values

'''
        
        