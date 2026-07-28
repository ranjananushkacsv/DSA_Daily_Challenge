def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1
    length = 0 
    
    while i >=0 and s[i] == ' ':
        i -=1
        
    while i >=0 and s[i] != ' ':
        length +=1
        i -=1
    return length
    
"""

APPROACH - 

1. initialze a pointter i from the last of the string and a variable length to 0.
2. A loop will start, from the end till i is less than or equal to 0 basically till we reach start.
   and till we reach a blank space.
3. move i to left.
4. another loop will strat from back till front and till no blank space.
5. the count will be stored in the length
6. retun length
"""