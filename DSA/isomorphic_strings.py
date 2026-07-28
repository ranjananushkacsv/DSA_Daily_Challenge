def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    mapping = {}
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        else:
            if char_t in mapping.values():
                return False
            mapping[char_s] = char_t
    return True

'''
APPORACH - 
1. write the edge case if the len is not equal it is false there.
2. create a dictionary calles mapping and start a loop till len(s) and traverse char in s and char in t
3. if the char_s is in mapping return true, if the mapping of char_s is not equal to that of t then false.
4. else if we see that char_t is in mapping vales already return false
5. else if not there then we add mapping[char_s] to char_t
'''