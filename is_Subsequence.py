""" 
SUBSEQUENCE - A subsequence of a string is a new string that is formed from the original string by deleting some or none characters without disturbing
the relative position of the remaning character
"""

def isSubsequence(self, s: str, t: str) -> bool:
    i, j = 0, 0 
    while i<len(s) and j <len(t):
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==len(s)

"""
APPROACH - 

1. Applying two pointer approach, taking i and j for s and t respectively.
2. a while loop will run till the end of each string s and t.
3. compare elements at i and j.
4. if matched move i by one.
5. Anyways j has to move after every comparision.

"""