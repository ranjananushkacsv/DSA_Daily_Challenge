class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
    
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
    
        return count
'''APPROACH -
We create a sorted version of heights called expected
We then compare each index of heights and expected
If they differ we increment count by 1
Finally we return count
'''
