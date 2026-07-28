def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern,words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        
        else:
            if word in word_to_char:
                return False
            
            char_to_word[char] = word
            word_to_char[word] = char
            
        return True
    
'''APPROACH- 
we start of by splitting s into words, then check lengths match if the length doesn't match then return false,
now we have created 2 dictionaries, one for letter -> word and other for word -> letter
now for each  latter and word we run a loop - if letter already mapped then it must match same word, if letter is new then word must not be already mapped to another letter.

If all of this is satisfied return true, else false.


'''