def longestMonotonicSubarray(self,nums: List[int])->int:
    if not arr:
        return 0
        
    max_len = 1
    inc_len = 1
    dec_len=1
        
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            inc_len+=1
            dec_len = 1
        elif arr[i]< arr[i-1]:
            dec_len +=1
            inc_len = 1
        else:
            inc_len = 1
            dec_len=1
        
        max_len = max(max_len,inc_len,dec_len)
        
    return max_len

'''APPROACH- 
We are going to first rule out the edge condition where if the arr is empty we return 0. Now we run a loop iterating through each element staring from 1. 

Then we check for conditions if arr[i] >arr[i-1] then we are going to increase the inc_len by one and keep the dec_len 1. similarliy for other way around. 

Once the conditions are checked we will be checking for the max_len. 
'''
                
            
        
        