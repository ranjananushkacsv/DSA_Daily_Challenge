from collections import counter 

def word_counter(text):
    words = text.lower().split() 
    return counter(words)


