def Scoreofstring():
    #s is the string provided in question
    score = 0
    
    for i in range(len(s) - 1):
        curr = ord(s[i])
        
        next = ord(s[i-1])
        difference = abs(curr - next)
        score += difference
        
    return score