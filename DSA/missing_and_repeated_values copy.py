def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    n = len(grid)
    total = n*n #because these many numbers has to be there in the matrix
    
    count = [0] * (total + 1) 
    for row in grid:
        for num in row:
            count[num] += 1
            
    repeat= missing = 0
    
    for num in range(1, total + 1):
        if count[num]==2:
            repeat = num
        elif count[num] ==0:
            missing = num
    return [repeat, missing]

'''APPROACH - 
1. Traverse the entire matrix and find out frequency count of every number.
2. from 1 to n^2 we will run a loop and find out frequency 2 = a and frequency 0 = b
3. return the repeat and missing value array.

'''