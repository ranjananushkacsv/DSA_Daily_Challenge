def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i]==0:
            left_empty = (i==0) or (flowerbed[i-1]==0)
            right_empty = (i==length-1) or (flowerbed[i+1]==0)
            
            if left_empty and right_empty:
                flowerbed[i]=1
                count+=1
            if count>=n:
                return True
            
    return count>=n

'''
APPROACH - 

1. Iterate through each position in flowerbed
2. check if current and right and left spots exists or are equal to 0
3. if all the conditions are satisfied plant the flower and inc the count by 1
4. return true if count>=n
'''
     