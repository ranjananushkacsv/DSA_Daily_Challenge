def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return " "
    
    prefix = ""
    for i in range(len(strs[0])):
        char = str[0][i]
        
        for word in strs:
            if i >=len(word) or word[i] != char:
                return prefix
        prefix += char
    
    return prefix

'''
APPROACH - 

1. If no words are there in trs we return empty string this is our edge case.
2. make a variable named prefix and initialsise it to an empty string
3. loop thrugh the first word from index 0 and then keep track of current char
4. then an inner loop for word in strs, where if the len of word is smaller than our char or char doesn't match
5. return prefix
6. if all matched add to prefix

'''